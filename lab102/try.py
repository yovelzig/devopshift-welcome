# my_dict={"name": "Yovel", "age": 26 , "city": "Netanya"}
# print(my_dict)
# my_dict["height"]= 1.85
# print(my_dict)
# # print(my_dict["age"])
# from pydantic import BaseModel, ValidationError
# class Server(BaseModel):
#     name: str
#     online: bool
#     cpus: int
#     ram: int
# Mylist : list[Server] = []
# Mylist.append(Server(name="Yovel", online=True, cpus=6, ram=10))
# print(Mylist)
# # Mylist["height"]= 1.85
# for key in Mylist:
#     print(key.name)
 
from pydantic import BaseModel, ValidationError
import json
from fastapi import FastAPI


app = FastAPI()
class ServerStatusResponse(BaseModel):
    server_name: str
    server_status: str | bool


class Server(BaseModel):
    name: str
    online: bool
    cpus: int
    ram: int

def read_server_list() -> list[Server]:
    with open("C:\\Users\\User\\Desktop\\python\\python_study\\devopshift-welcome\\lab3\\servers.txt", "r") as f:
        servers: list[Server] = []
        for line in f.readlines():
            if line.strip():
                json_object = json.loads(line)
                try:
                    new_server = Server(**json_object)
                except ValidationError:
                    pass
                else:
                    servers.append(new_server)
    return servers


def add_new_server(new_server: Server):
    with open("C:\\Users\\User\\Desktop\\python\\python_study\\devopshift-welcome\\lab3\\servers.txt", "a") as f:
        f.write("\n")
        f.write(new_server.model_dump_json())
           
@app.get("/server")
def get_server(server_name: str) -> ServerStatusResponse:
    servers = read_server_list()
    # server_status = servers.get(server_name, "Does not exist")
    for server in servers:
        if server.name == server_name:
            server_status = server.online
            break
        return ServerStatusResponse(server_name=server_name, server_status=server_status)
    return ServerStatusResponse(server_name=server_name, server_status="Did not find server")

#my update
@app.post("/server")
def create_server(server_name: str, online: bool, cpus: int, ram: int) -> ServerStatusResponse:
    new_server = Server(name=server_name, online=online, cpus=cpus, ram=ram)
    add_new_server(new_server)
    return ServerStatusResponse(server_name=server_name, server_status="Created")