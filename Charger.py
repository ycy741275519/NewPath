# -*- coding: utf-8 -*-
# @File  : Charger.py
# @Author: ycy
# @Date  : 2019/10/28
# @Desc  :充电器节点
import math

class Charger(object):

    def __init__(self,x,y,speed,range,stopTime):
        self.x = x                              # 充电器的位置
        self.y = y
        self.speed = speed                      # 移动速度m/s
        self.range = range                      # 充电范围
        self.stopTime = stopTime                # 停留时间

    def move(self,x,y):                         # 移动
        self.x = x
        self.y = y

    def chargeEnergy(self,node):                     # 充电
        d=math.sqrt((self.x-node.x)^2+(self.y-node.y)^2)
        if(d<=self.range):
            node.increaseEnergy(self.stopTime,d)

if __name__ == '__main__':
    pass