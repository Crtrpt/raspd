from socket import *

from threading import Thread
from time import sleep
import logging;
import sys

# logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s  -%(process)s -%(thread)s - %(levelname)s - %(message)s ')

logger = logging.getLogger(__name__)
class discovery:
    # 是否开启广播
    isOpen=True;
    client=socket(AF_INET,SOCK_DGRAM)
    def broadcast(self):
        logger.info("find me")
        data="find me".encode()
        self.client.sendto(data,('',50000))