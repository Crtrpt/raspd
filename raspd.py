#!/usr/bin/python3                                                              
# -*- coding: utf-8 -*-
import sys;
import time;
import logging


logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class raspd:
    def signup(self):
        logger.info("注册设备")

    def init(self):
        logger.info("链接服务器")

    def run(self):
        logger.info("开始运行")
        self.init();
        self.signup();

if __name__ == '__main__':
    device = raspd();
    device.run();