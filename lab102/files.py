# f = open("servers.txt", "r")  
# try:
#     servers = [server.strip() for server in f.readlines()] 
#     print(servers) 
# finally:
#     f.close()
    
# with open("servers.txt", "r") as f:
#     servers = [server.strip() for server in f.readlines()] 
#     print(servers)
    
# print("File already closed")
###################
import json
from dataclasses import dataclass
from pydantic import BaseModel, ValidationError

@dataclass
class Server:
    name: str
    online: bool
    cpu: int
    ram: int
    
class BetterServer(BaseModel):
    name: str
    online: bool
    cpu: int
    ram: int
 
with open("servers.txt", "r") as f:
    servers = [json.loads(server) for server in f.readlines() if server.strip()]   

def read_servers():
    with open("servers.txt", "w") as f:
        servers = []
        for line in f.readlines():
            if line.strip() :
                json_object = json.loads(line)
                try:
                    new_server = Server(**json_object)
                except ValidationError :
                    pass
            else:      
                servers.append(new_server)
        return servers
        
    # new_server = Server( name ="nginx", status = True ,cpu =6 , ram=4)
    # server_str = json.dumps(new_server)
    # f.write("\n")
    # f.write(server_str)
    # f.write("\n")

# with open("servers.txt", "r") as f:
#     servers = [json.loads(server) for server in f.readlines() if server.strip()]
    
#     print(servers)
#     print(servers[0]["name"])
    
# with open("servers.txt", "w") as f:
#     new_server = {"name": "nginx", "status": True , "ram": 4}
#     server_str = json.dumps(new_server)
#     f.write("\n")
#     f.write(server_str)
#     f.write("\n")