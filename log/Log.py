import logging
import os
import time
from logging import handlers

class Logger(object):
    def __init__(self,logname):
        self.logger = logging.getLogger(logname)
        self.logger.setLevel(logging.DEBUG)
        formatter= logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # rq = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
        # cp = os.getcwd()
        # print(cp)
        # dn = os.path.dirname((os.path.dirname("D:\pythonworkspace\SeleniumProject\python\log")))
        # print(dn)
        log_path = os.path.dirname(os.getcwd())+"\SeleniumProject\data"
        # pp = os.path.dirname(os.getcwd())
        # print(pp)
        # print(log_path)
        log_title = os.path.join(log_path,logname)+'.txt'
        # print(log_title)
        file = logging.FileHandler(log_title,encoding='utf-8')
        file.setFormatter(formatter)
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(formatter)
        self.logger.addHandler(file)
        self.logger.addHandler(console)
    def getLog(self,msg):
        return  self.logger.info(msg)
    def getErrorLog(self,msg):
        return self.logger.error(msg)
# if __name__ == "__main__":
#     log = Logger("1112221")
#
#     log.getLog("45kkk6")


# logger = logging.getLogger("wudi")
# logger.setLevel(logging.INFO)
# console = logging.StreamHandler()
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# console.setFormatter(formatter)
# console.setLevel(logging.INFO)
# logger.addHandler(console)
# logger.info("widu")

