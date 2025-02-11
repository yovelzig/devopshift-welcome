from dataclasses import dataclass
from datetime import datetime
from fastapi import FastAPI
import httpx
from tools import get_status2

@dataclass
class ServerStatus:
    server_name: str
    status: bool | str 
    

def add_server(server_name: str, is_running: bool) -> bool:
    try:
        if(server_name not in servers):
            servers[server_name] = is_running
            return True
    except KeyError:
        print("The server name is invalid")
    return False

def check_status(server_name: str) -> bool:
    if server_name in servers:
         return servers[server_name]
    return False
    
app = FastAPI()
servers = {"ngnix": True, "docker": False}



@dataclass
class User:
    name: str
    email: str
    d: datetime = datetime.now()


@app.get("/servers")
def get_servers(server_name: str):
    servers.get(server_name, "Server not found")
    status = get_status2(server_name)
    if (status):
        return {"status": f"{server_name} is running and {status}"}
    else:
        return {"status": f"{server_name} is not running and {status}"}
   
@app.post('/server')
def post_server(server_name: str, is_running: bool):
    "POST request to check if the server is running or not running "
    # return add_server(server_name, is_running);
    status = add_server(server_name, is_running)
    if(status):
        return {"server":server_name, "status":is_running}
    else:
        return {"server":server_name, "status":is_running}  

@app.get("/")
def hello_world():
    "This is our main function"
    return {"result": ["Hello World", 1, 2, True, None], "error": False}

@app.get("/error")
def error():
    raise ValueError("This is an ERROR")



@app.get("/users")
def get_users() -> list[User]:
    response = httpx.get("https://jsonplaceholder.typicode.com/users")
    users = response.json()
    return users


@app.post("/users")
def create_user(new_user: User) -> bool:
    return True














#Best solution
# from dataclasses import dataclass
# from fastapi import FastAPI

# app = FastAPI()

# servers = {"nginx": True, "docker": False}


# @dataclass
# class ServerStatusResponse:
#     server_name: str
#     server_status: str | bool


# @app.get("/server")
# def get_server(server_name: str) -> ServerStatusResponse:
#     server_status = servers.get(server_name, "Does not exist")
#     return ServerStatusResponse(server_name, server_status)


# @app.post("/server")
# def create_server(server_name: str) -> ServerStatusResponse:
#     if server_name in servers:
#         return ServerStatusResponse(server_name, "Name already exists")
#     else:
#         servers[server_name] = True
#         return ServerStatusResponse(server_name, "Created")