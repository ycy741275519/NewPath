# -*- coding: utf-8 -*-
# @File  : main.py
# @Author: ycy
# @Date  : 2019/10/28
# @Desc  : 主过程
import numpy as np
import matplotlib.pyplot as plt
from Node import *
from Charger import *
import math
from matplotlib.pyplot import MultipleLocator




NUMBER=100    # 节点数量


def createNode(num):  # 创建节点
    np.random.seed(20)
    row = np.random.rand(num)*100
    np.random.seed(5)
    col = np.random.rand(num)*100
    return row,col


def createSpath(L,d):   # 创建三角停留点
    row = []
    x = []
    y = []
    for i in range(L//d-1):
        k=0
        print(len(row))
        for j in range(L//(2*d)):
            row.append((k*d,(i+1)*d))
            row.append((2*d*j+d/2,(i+1)*d-(d*math.sqrt(3)/2)))
            row.append(((k+1)*d,(i+1)*d))
            row.append((2*d*j+d+d/2,(i+1)*d+(d*math.sqrt(3)/2)))
            k+=2
        row.append((k * d, (i + 1) * d))
    for i in range(len(row)):
        if i%2 !=0:
            t=row[41*i:41*(i+1)]
            l=t[::-1]
            row[41 * i:41 * (i + 1)]=l
    for p in row:
        x.append(p[0])
        y.append(p[1])
    plt.figure(1)
    plt.plot(x,y,'og')
    plt.plot(x,y,'r')
    plt.show()


def createHpath(L,d):       # 创建H停留点
    pass










if __name__ == '__main__':
    createSpath(100,5)
    plt.show()
    # 初始化传感器节点
    # x,y=createNode(NUMBER)
    # node = []
    # for i in range(NUMBER):
    #     node.append(Node(x[i],y[i]))
    # # print(len(node))
    # # for n in node:
    # #     plt.scatter(n.x,n.y,c='b',marker='o')
    # # plt.show()
    #
    # #  初始化充电器
    # charger = Charger(0,0,1,5,5)  # 坐标，速度，覆盖范围，停留时间
    #
    #
    # #  三角路径计算停留点和长度