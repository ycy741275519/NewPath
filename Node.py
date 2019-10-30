# -*- coding: utf-8 -*-
# @File  : Node.py
# @Author: ycy
# @Date  : 2019/10/28
# @Desc  :传感器节点类

class Node(object):
    a=4.32*1e-4
    b=0.2316
    def __init__(self,x,y):
        self.x = x               # 节点位置
        self.y = y
        self.active = True      # 存活标记
        self.energy = 1          # 初始能量
        self.Eth = 0.7           # 能量阈值
        self.Ect = 0.01          # 能量消耗率

    def decreaseEnergy(self,t):   # 随时间能量减少
        self.energy -= t*self.Ect
        if(self.energy<=0):
            self.active = False

    def increaseEnergy(self,t,d):  # 充电增加能量
       self.energy += Node.a/(d+Node.b)^2





if __name__ == '__main__':
    node1 = Node(1,2)
    node2 = Node(2, 3)
