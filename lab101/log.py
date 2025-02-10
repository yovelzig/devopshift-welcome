import logging
import sys
import json
import os


class InvalidServerNameError(Exception):
    pass

class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log = {"time": record.created, "module": record.module, "level": record.levelname, "message": record.getMessage()}
        return json.dumps(log)
def setup_logging():
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG")
    LOG_FORMAT = os.environ.get("LOG_FORMAT", "TEXT")


    logger = logging.getLogger("myapp")
    logger.setLevel(LOG_LEVEL)
    stdout_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.FileHandler("log.txt")
    if LOG_FORMAT == "JSON":
        formatter = JsonFormatter()
        # stdout_handler.setFormatter(JsonFormatter())
    else:
        formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(module)s:%(lineno)s:%(funcName)s:%(message)s")
        # log_format = "%(asctime)s:%(name)s:%(levelname)s:%(module)s:%(lineno)s:%(funcname)s:%(message)s"
        # stdout_handler.setFormatter(logging.Formatter(log_format))
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger 
# logger.info("test info")
# logger.error("test error")


# log_format1 = "%(asctime)s:%(name)s:%(levelname)s:%(module)s:%(lineno)s:%(funcname)s:%(message)s"
# logging.basicConfig(filename='myapp.log', format=log_format ,level=logging.ERROR)



# def check_status(server_name):
#     serverdict = {"ngnix", "docker", "server5"}
#     if server_name in serverdict:
#         logging.info(f"The server : {server_name} is running")
#         return "running"
#     else:
#         raise ValueError ("unsupported server name")
# while(True):
#     try:
#         user_choise = input("enter your server's name : ")
#         if not user_choise.strip():
#             raise InvalidServerNameError("invaliad server name")
#         if not user_choise.isalnum():
#             raise InvalidServerNameError("invaliad server name")
        
#     except InvalidServerNameError as e:
#         logging.error(e)
#         # print(f"invalid input :{e}")  

#     except ValueError as e:
#         logging.error(e)
#         # print(f"invalid serverName :{e}")     
#     try:   
#         status = check_status(user_choise)
#         logging.info(status)
#     except ValueError as e:
#         logging.error(e)