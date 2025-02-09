# Create subnet inside the VPC
resource "aws_subnet" "public_subnet" {
 count = var.subnet_count
 vpc_id            = aws_vpc.custom_vpc.id
 cidr_block        = var.subnet_cidrs[count.index]
 map_public_ip_on_launch = true

 tags = {
   Name = "yovelPublic-subnet-${count.index + 1}"
 }
}
resource "aws_subnet" "private_subnet" {
  vpc_id     = aws_vpc.custom_vpc.id
  cidr_block = "10.0.2.0/24"

  tags = {
    Name = "yovelPrivate-subnet"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.custom_vpc.id

  tags = {
    Name = "yovel-gateway"
  }
}
# Create VPC only if enabled
resource "aws_vpc" "custom_vpc" {

 cidr_block           = var.vpc_cidr
 enable_dns_support   = true
 enable_dns_hostnames = true

 tags = {
   Name = "yovel-vpc"
 }
}



resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.custom_vpc.id

  # Route to direct all traffic to the Internet Gateway
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "yovel-rt"
  }
}
resource "aws_route_table_association" "public_rt_assoc" {
  count          = var.subnet_count
  subnet_id      = aws_subnet.public_subnet[count.index].id
  route_table_id = aws_route_table.public_rt.id
}
resource "aws_route_table" "private" {
  vpc_id = aws_vpc.custom_vpc.id

  tags = {
    Name = "private-route-table"
  }
}

resource "aws_route_table_association" "private" {
  subnet_id      = aws_subnet.private_subnet.id
  route_table_id = aws_route_table.private.id
}
resource "aws_security_group" "instance_sg" {
  name        = "instance-sg"
  description = "Allow SSH and HTTP"
  vpc_id      = aws_vpc.custom_vpc.id

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "instance-sg"
  }
}

variable "key_pairs" {
  description = "key_pairs"
  type = list(object({
    key_name   = string
    public_key = string
  }))
  default = [
    {
      key_name   = "yovelkey1"
      public_key = "./modules/Mykey1.pub"
    }, 
    {
      key_name   = "yovelkey2"
      public_key = "./modules/Mykey2.pub"
    },
    {
      key_name   = "yovelkey3"
      public_key = "./modules/Mykey3.pub"
    }
  ]
}
resource "aws_key_pair" "my_key_pair" {
  count = var.subnet_count
  key_name   = var.key_pairs[count.index].key_name
  public_key = file(var.key_pairs[count.index].public_key)
}

resource "aws_instance" "ubuntu_instance" {
  count = var.subnet_count
  ami                    = "ami-0c02fb55956c7d316"
  instance_type          = var.instance_type
  subnet_id              = aws_subnet.public_subnet[count.index].id
  vpc_security_group_ids = [aws_security_group.instance_sg.id]
  associate_public_ip_address = var.associate_public_ip_address
  key_name               = aws_key_pair.my_key_pair[count.index].key_name
  tags = {
    Name = "Yovel-Machine-${count.index + 1}"
  }
}
output "vm_public_ip" {
  
  value       = aws_instance.ubuntu_instance[*].public_ip
  description = "Public IP address of the VM"
}