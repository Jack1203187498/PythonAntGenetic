import math
import random

import matplotlib.pyplot as plt
import numpy as np
from numpy import cumsum


def initpop(popsize, chromlength):
    tmp = np.zeros((popsize, chromlength)).tolist()
    for i in range(popsize):
        for j in range(chromlength):
            tmp[i][j] = round(random.random())
    return tmp

def binary2decimal(pop):
    tmp = np.zeros((len(pop), 1))
    for i in range(len(pop)):
        num = ''.join(str(int(_)) for _ in pop[i])
        num = int(num, 2)
        tmp[i] = num * 10.0 / 1023
    return tmp


def cal_objvalue(pop):
    x = binary2decimal(pop)
    for i in range(len(x)):
        tmp = x[i]
        x[i] = 10 * math.sin(5 * tmp) + 7 * abs(tmp - 5) + 10
    return x

def selection(pop, fitvalue):
    px = len(pop)
    py = len(pop[0])
    totalfit = sum(fitvalue)
    p_fitvalue = fitvalue / totalfit
    p_fitvalue = cumsum(p_fitvalue)
    newpop = np.zeros((px, py)).tolist()
    ms = []
    for i in range(px):
        ms.append(random.random())
    ms = sorted(ms)
    fitin = 0
    newin = 0
    while newin <= px and fitin < px and newin < px:
        if ms[newin] < p_fitvalue[fitin]:
            newpop[newin][:] = pop[fitin][:]
            newin += 1
        else:
            fitin += 1
    return newpop

def crossover(pop, pc):
    px = len(pop)
    py = len(pop[0])
    newpop = []
    for i in range(0, px-1, 2):
        if random.random() < pc:
            cpoint = round(random.random() * py)
            if cpoint == py:
                cpoint -= 1
            newpop.append(pop[i][0:cpoint] + pop[i+1][cpoint:py])
            newpop.append(pop[i+1][0:cpoint] + pop[i][cpoint:py])
        else:
            newpop.append(pop[i])
            newpop.append(pop[i+1])
    return newpop

def mutation(pop, pm):
    px = len(pop)
    py = len(pop[0])
    newpop = np.ones((px, py))
    for i in range(px):
        if(random.random() < pm):
            mpoint = round(random.random() * py)
            if mpoint == py:
                mpoint -= 1
            newpop[i] = pop[i]
            if newpop[i][mpoint] == 1:
                newpop[i][mpoint] = 0
            else:
                newpop[i][mpoint] = 1

        else:
            newpop[i] = pop[i]
    return newpop.tolist()

def cal_function(min, max, step):
    x = np.arange(min, max, step)
    y = np.arange(min, max, step)
    for i in range(len(x)):
        tmp = x[i]
        y[i] = 10 * math.sin(5 * tmp) + 7 * abs(tmp - 5) + 10
    return x, y

def best(pop, fitvalue):
    px = len(pop)
    py = len(pop[0])

    bestindividual = pop[0]
    bestfit = fitvalue[0][0]
    for i in range(px):
        if fitvalue[i][0] > bestfit:
            bestindividual = pop[i]
            bestfit = fitvalue[i][0]
    return [bestindividual, bestfit]

def main():
    popsize = 1000
    chromlength = 10
    pc = 0.6
    pm = 0.01
    pop = initpop(popsize, chromlength)
    x2 = 0
    bestfit = 0
    for i in range(500):
        objvalue = cal_objvalue(pop)
        fitvalue = objvalue
        newpop = selection(pop, fitvalue)
        newpop = crossover(newpop, pc)
        newpop = mutation(newpop, pm)
        pop = newpop
        [bestindividual, bestfit] = best(pop, fitvalue)
        x2 = binary2decimal([bestindividual])[0][0]
        x1 = binary2decimal(pop)
        y1 = cal_objvalue(pop)
        if i % 499 == 0 and i != 0:
            xbase, ybase = cal_function(0, 10, 0.001)
            plt.plot(xbase, ybase)
            plt.plot(x1, y1, '.')
            plt.plot(x2, bestfit, '*')


    print("The best X is --->>", str(x2))
    print("The best Y is --->>", str(bestfit))
    plt.show()

main()