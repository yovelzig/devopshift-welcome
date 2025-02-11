from log import setup_logging

logger = setup_logging()
servers = {"ngnix": True, "docker": False}

def get_status(server_name: str) -> bool:
    lowercase_servers = {key.strip().lower(): value for key, value in servers.items()}
    if server_name in servers:
         return servers[server_name]
    else:
        logger.error("The server name does not exist")
        return False

def get_status2(server_name: str) -> bool:
    lowercase_servers = {key.strip().lower(): value for key, value in servers.items()}
    try:
         return servers[server_name]
    except KeyError:
        logger.error("The server name does not exist")
    return servers[server_name]

def kaki():
    while True:
        server_name = input("Enter server name : ").strip().lower()
        status = get_status(server_name)
        logger.info(f"Server {server_name} status is :  {status}")
        # logger.info("Server status is : "+str(status))