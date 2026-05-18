import logging

"""
To generate logs, I am going to create 2 directories. 
A. Utilities: To write code for generating logs.
B. Logs: To store log msgs.
"""

# logging.basicConfig(filename="..\\Logs\\logfile.log",
#                     format="%(asctime)s: %(levelname)s: %(message)s",
#                     datefmt="%d/%m/%Y %I:%M:%S %p",
#                     level=logging.INFO)
#
# log = logging.getLogger()
#
# log.info("This is our first log")

def log():
    logging.basicConfig(filename="..\\Logs\\logfile.log",
                        format="%(asctime)s: %(levelname)s: %(message)s",
                        datefmt="%d/%m/%Y %I:%M:%S %p",
                        level=logging.INFO)

    logger = logging.getLogger()
    return logger

logger = log()
logger.info("This is a new log msg")
logger.error("This is an error msg")
logger.warning("This is an warning msg")
logger.debug("This is a debug msg")

