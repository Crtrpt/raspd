from socket import *

from threading import Thread
from time import sleep
import logging;
import sys

# logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s  -%(process)s -%(thread)s - %(levelname)s - %(message)s ')

logger = logging.getLogger(__name__)


class discovery:
    # 是否开启广播
    isOpen = True;
    id = 0x01;
    maginxCode = bytes([
        0x80, 0x08
    ])
    version = 0x01;
    client = socket(AF_INET, SOCK_DGRAM)

    def __init__(self):
        self.client.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    def broadcast(self):
        if self.isOpen:

            self.id = (self.id + 1)
            if self.id > 255:
                self.id = 0
            logger.info("find me")
            buffer = bytes();
            payload = (65535).to_bytes(2, byteorder='big')
            fiexed = bytes([
                self.version,
                len(payload),
                self.id,
            ]);
            buffer += bytearray(self.maginxCode);
            buffer += bytearray(fiexed);
            buffer += bytearray(payload);
            buffer += bytearray(bytes([
                0xff,
                0xfe
            ]));
            logger.info(buffer)
            self.client.sendto(buffer, ('255.255.255.255', 50000))
        else:
            pass


if __name__ == '__main__':
    d = discovery();
    d.broadcast();
