import logging
import sys
import os
import json

#JSON
# data = {"name": "james", "age": 15, "city": None, "alive": True}
# x = json.dumps(data) #dict to string
# print(type(x))
# print(x)
# new_data = json.loads(x) #string to dict
# print(new_data)
# print(type(new_data))
# print(new_data["alive"])
###########################


# print(sys.argv)
# print(os.environ)

# d = {"a": "b"}
# value = d.get("a")
# print(value)
# log_level = os.environ.get("LOGLEVEL", "DEBUG")
# print(log_level)
##############

# logging.Handler
# logging.Formatter


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log = {"time": record.created, "module": record.module}
        return json.dumps(log)

logger = logging.getLogger("yovel")
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JsonFormatter)
logger.addHandler(handler)


log_format = "%(asctime)s:%(name)s:%(levelname)s:%(module)s:%(lineno)s:%(funcname)s:%(message)s"
logging.basicConfig(filename='myapp.log', format=log_format ,level=logging.ERROR)
log_level = os.environ.get("LOGLEVEL", "DEBUG")

logger.info("this is info")
logger.error("this is error")
logger.warning("this is warning")
logger.debug("this is debug")
