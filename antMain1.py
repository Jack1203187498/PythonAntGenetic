# -*- coding: utf-8 -*-
# 使用mode参数决定是否将每一步显示
#   mode 1 : 显示蚂蚁的爬行过程，运行很慢
#   mode 2 : 显示最终蚂蚁运行结果

import math
import random

import matplotlib.pyplot as plt
import numpy as np
from numpy import meshgrid


def functionF(x, y):
    f = -(x ** 2 + 3 * y ** 4 - 0.2 * math.cos(3.0 * math.pi * x) - 0.4 * math.cos(4 * math.pi * y) + 0.6)
    return f

def functionf(x, y):
    f = -(x**2+3*y**4-0.2*math.cos(3*math.pi*x)-0.4*math.cos(4*math.pi*y)+0.6)
    return f


def functionff(xx, yy):
    ff = -(xx**2+3*yy**4-0.2*math.cos(3*math.pi*xx)-0.4*math.cos(4*math.pi*yy)+0.6)
    return ff

def main1():
    Ant = 300
    Times = 80
    Rou = 0.9
    P0 = 0.2
    Lower_1 = -1
    Upper_1 = 1
    Lower_2 = -1
    Upper_2 = 1

    mode = 2
    # mode 1 : 显示蚂蚁的爬行过程，运行很慢
    # mode 2 : 显示最终蚂蚁运行结果

    X = [[0.0, 0.0] for _ in range(Ant)]
    Tau = [0.0 for _ in range(Ant)]
    for i in range(Ant):
        X[i][0] = (Lower_1 + (Upper_1 - Lower_1) * random.random())
        X[i][1] = (Lower_1 + (Upper_1 - Lower_1) * random.random())
        Tau[i] = functionF(X[i][0], X[i][1])
    step = 0.05

    [x, y] = meshgrid(np.arange(Lower_1, Upper_1 + step, step), np.arange(Lower_2, Upper_2 + step, step))
    z = np.zeros((len(x), len(y)))
    ffz = np.zeros(len(X))
    for i in range(len(x)):
        for j in range(len(x[i])):
            z[i][j] = functionf(x[i][j], y[i][j])

    fig = plt.figure(1)
    ax = fig.add_subplot(121, projection='3d')
    ax.plot_surface(x, y, z, cmap=plt.get_cmap('rainbow'), alpha=0.3)
    ax.scatter([i[0] for i in X], [i[1] for i in X], Tau, marker="x", color="black")

    for T in range(Times):
        for i in range(Ant):
            temp1 = X[i][0] + (2 * random.random() - 1) * 0.05
            temp2 = X[i][1] + (2 * random.random() - 1) * 0.05
            if temp1 < Lower_1:
                temp1 = Lower_1
            if temp1 > Upper_1:
                temp1 = Upper_1
            if temp2 < Lower_2:
                temp2 = Lower_2
            if temp2 > Upper_2:
                temp2 = Upper_2

            if functionF(temp1, temp2) > functionF(X[i][0], X[i][1]):
                X[i][0] = temp1
                X[i][1] = temp2
        for i in range(Ant):
            Tau[i] = (1 - Rou) * Tau[i] + functionF(X[i][0], X[i][1])
        if mode == 1:
            ax2 = fig.add_subplot(122, projection='3d')
            ax2.plot_surface(x, y, z, cmap=plt.get_cmap('rainbow'), alpha=0.3)

            for i in range(len(X)):
                ffz[i] = functionff(X[i][0], X[i][1])

            ax2.scatter([i[0] for i in X], [i[1] for i in X], ffz, marker="x", color="black")
            plt.pause(0.05)
    if mode == 2:
        ax2 = fig.add_subplot(122, projection='3d')
        ax2.plot_surface(x, y, z, cmap=plt.get_cmap('rainbow'), alpha=0.3)

        for i in range(len(X)):
            ffz[i] = functionff(X[i][0], X[i][1])

        ax2.scatter([i[0] for i in X], [i[1] for i in X], ffz, marker="x", color="black")


    index = np.argmax(ffz)
    posX = X[index][0]
    posY = X[index][1]
    print(posX, posY, ffz[index])

    plt.show()


main1()