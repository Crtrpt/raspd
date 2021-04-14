#!/usr/bin/python3                                                              
# -*- coding: utf-8 -*-
import os;
import sys;
import time;
import logging;
import uuid;
import paho.mqtt.client as mqtt;
import web;
import config as cfg;
import find as finder;
import json

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s  -%(process)s -%(thread)s - %(levelname)s - %(message)s ')
logger = logging.getLogger(__name__)

class raspd:
    
    client = mqtt.Client()
    clientId = ""
    topic= ""
    
    def signup(self):
        topic=self.topic+"/signup"
        payload=json.dumps(cfg.capability)
        logger.info("注册设备 %s %s",topic,payload)
        self.client.publish(topic,payload);

    def on_connect(self,client, userdata, flags, rc):
        logger.info("连接成功")
        self.signup()
        logger.info("订阅 "+self.topic)
        self.client.subscribe(self.topic, qos=1)


    def on_message(self,client, userdata, msg):
        logger.info("收到消息 %s",msg.payload.decode())
        
    def initMqtt(self):        
        address = hex(uuid.getnode())[2:];
        self.clientId='-'.join(address[i:i+2] for i in range(0, len(address), 2));
        self.topic="/default/raspd/"+self.clientId;
        logger.info("clientId: "+self.clientId)
        client = mqtt.Client(self.clientId);
        self.client.on_connect = self.on_connect;
        self.client.on_message = self.on_message;
        logger.info("connect to  %s %s %s ",cfg.mqtt.broker,cfg.mqtt.port,cfg.mqtt.timeout)
        self.client.connect(cfg.mqtt.broker,cfg.mqtt.port,cfg.mqtt.timeout);
        self.client.loop_forever();

    def init(self):
        logger.info("链接mqtt服务器")
        self.initMqtt();

    def run(self):
        logger.info("开始运行")
        self.init();
    

if __name__ == '__main__':
    finder=finder.discovery();
    pid = os.fork();
    if pid :
        pid1=os.fork();
        if pid1 :
            logger.info("父进程进入睡眠状态"+str(pid))
            while True :   
                finder.broadcast();
                time.sleep(60)
        else:
            #pass
            web.app.run(host="0.0.0.0", debug=True,threaded=True)
    else:
        device = raspd();
        device.run();