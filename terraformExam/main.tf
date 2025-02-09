# provider "aws" {
#   region = "us-east-1"  
# }

# resource "aws_security_group" "sg" {
#   name        = "allow_ssh_http"
#   description = "Allow SSH and HTTP traffic"

#   ingress {
#     from_port   = 22
#     to_port     = 22
#     protocol    = "tcp"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

#   ingress {
#     from_port   = 80
#     to_port     = 80
#     protocol    = "tcp"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

#   egress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }
# }

# resource "aws_instance" "ubuntu_instance" {
#   ami           = "ami-0c02fb55956c7d316"
#   instance_type = "t2.micro"

#   associate_public_ip_address = true

#   security_groups = [aws_security_group.sg.name]

#   tags = {
#     Name = "ubuntu-instance"
#   }
# }

# output "public_ip" {
#   value = aws_instance.ubuntu_instance.public_ip
# }

provider "aws" {
  region = "us-east-1"
}

module "vpc_ec2" {
  source = "./modules/ec2_instance"
  vpc_cidr             = "10.0.0.0/16"
  instance_type        = "t2.micro"
  subnet_count  = 2
  associate_public_ip_address = true
  subnet_cidrs = ["10.0.1.0/24", "10.0.3.0/24"]
}