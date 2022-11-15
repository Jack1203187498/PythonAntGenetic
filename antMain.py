import random
import copy

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator


def functionG2D(G):
    l = len(G[0])
    D = np.zeros((l, l, l, l))
    for i in range(l):
        for j in range(l):
            if(G[i][j] == 0):
                for m in range(l):
                    for n in range(l):
                        if(G[m][n] == 0):
                            im = abs(i - m)
                            jn = abs(j - n)
                            if im + jn == 1 or (im == 1 and jn == 1):
                                D[i][j][m][n] = np.sqrt(im + jn)
    return D

def main():
    # figure1: 绘制最优路径更新情况
    # figure2: 绘制蚂蚁最优路径
    # figure3: 绘制每次迭代中的蚂蚁最优路径
    figure1 = 1
    figure2 = 1
    figure3 = 1

    # G 地形图为01矩阵，1表示障碍物
    G = [[0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],]
    G = list(zip(*G[::-1]))

    MM = len(G[0])
    # Tau 初始化信息素矩阵
    Tau = np.ones((MM, MM, MM, MM))
    Tau = 8.0 * Tau
    # 迭代次数（蚂蚁出动多少波）
    K = 100
    # 蚂蚁个数
    M = 50
    # 最短路径起始点
    S = [0, MM-1]
    # 最短路径目的点
    E = [MM-1, 0]
    # Alpha 表征信息素重要程度的参数
    Alpha = 1
    # Beta 表征启发式因子重要程度的参数
    Beta = 7
    # Rho 信息素蒸发系数
    Rho = 0.3
    # Q 信息素增加强度系数
    Q = 1

    mink = 0
    minl = 0
    minkl = float("inf")

    D = functionG2D(G)
    # N 问题的规模（像素个数）
    N = len(D[0])
    # 小方格像素的边长
    a = 1
    # 起始点横纵坐标
    Sx = S[0] + 0.5
    Sy = S[1] + 0.5
    # 终止点横坐标
    Ex = E[0] + 0.5
    # 终止点纵坐标
    Ey = E[1] + 0.5
    # 启发式信息，取为至目标点的直线距离的倒数
    Eta = np.zeros((MM, MM))
    # 以下启发式信息矩阵
    for i in range(MM):
        for j in range(MM):
            ix = i + 0.5
            iy = j + 0.5
            if ix != Ex or iy != Ey:
                Eta[i][j] = 1.0 / np.sqrt(np.square(ix - Ex) + np.square(iy - Ey))
            else:
                Eta[i][j] = 100

    ROUTES = []
    for i in range(K):
        tmp = []
        for j in range(M):
            tmp.append([])
        ROUTES.append(tmp)
    PL = np.zeros((K, M))

    for k in range(K):
        print("round:" + str(k))
        for m in range(M):
            W = S
            Path = [S]
            PLkm = 0
            TABUkm = np.ones((MM, MM))
            TABUkm[S[0]][S[1]] = 0
            DD = copy.deepcopy(D)
            #下一步可以前往的结点
            DW = DD[W[0]][W[1]]
            DW1 = np.nonzero(DW)
            for j in range(len(DW1[0])):
                if TABUkm[DW1[0][j]][DW1[1][j]] == 0:
                    DW[DW1[0][j]][DW1[1][j]] = 0
            LJD = np.nonzero(DW)
            LenLJD = len(LJD[0])
            # 蚂蚁遇到食物或者陷入死胡同则觅食停止
            while W != E and LenLJD >= 1:
                PP = np.zeros(LenLJD)
                for i in range(LenLJD):
                    PP[i] = (Tau[W[0]][W[1]][LJD[0][i]][LJD[1][i]] ** Alpha) * (Eta[LJD[0][i]][LJD[1][i]] ** Beta)
                sumpp = PP.sum()
                PP = PP / sumpp
                Pcum = np.zeros(LenLJD)
                Pcum[0] = PP[0]
                for i in range(1, LenLJD):
                    Pcum[i] = Pcum[i-1] + PP[i]
                Select = -1

                p = random.random()
                for i in range(len(Pcum)):
                    if Pcum[i] >= p:
                        Select = i
                        break
                to_visit = [LJD[0][Select], LJD[1][Select]]

                Path.append(to_visit)
                PLkm += DD[W[0]][W[1]][to_visit[0]][to_visit[1]]
                W = to_visit
                for kk in range(N):
                    for kkk in range(N):
                        if TABUkm[kk][kkk] == 0:
                            DD[W[0]][W[1]][kk][kkk] = 0
                            DD[kk][kkk][W[0]][W[1]] = 0
                TABUkm[W[0]][W[1]] = 0
                DW = DD[W[0]][W[1]]
                DW1 = np.nonzero(DW)
                for j in range(len(DW1[0])):
                    if TABUkm[DW1[0][j]][DW1[1][j]] == 0:
                        DW[DW1[0][j]][DW1[1][j]] = 0
                LJD = np.nonzero(DW)
                LenLJD = len(LJD[0])
            ROUTES[k][m] = Path
            if Path[-1] == E:
                PL[k][m] = PLkm
                if PLkm < minkl:
                    mink = k
                    minl = m
                    minkl = PLkm
            else:
                PL[k][m] = 0
        Delta_Tau = np.zeros((N, N, N, N))
        for m in range(M):
            if PL[k][m]:
                ROUT = ROUTES[k][m]
                TS = len(ROUT) - 1
                PL_km = PL[k][m]
                for s in range(TS):
                    x = ROUT[s]
                    y = ROUT[s + 1]
                    Delta_Tau[x[0]][x[1]][y[0]][y[1]] = Delta_Tau[x[0]][x[1]][y[0]][y[1]] + Q / PL_km
                    Delta_Tau[y[0]][y[1]][x[0]][x[1]] = Delta_Tau[y[0]][y[1]][x[0]][x[1]] + Q / PL_km
        Tau = (1.0 - Rho) * Tau + Delta_Tau
    if figure1 == 1:
        minPL = []
        for i in range(K):
            PLK = PL[i]
            notZero = np.nonzero(PLK)
            if len(notZero) == 0:
                continue
            PLKPLK = []
            for j in range(len(notZero[0])):
                PLKPLK.append(PLK[notZero[0][j]])
            if len(PLKPLK) == 0:
                continue
            minPL.append(min(PLKPLK))
        plt.figure(figsize=(5, 5))
        plt.grid(True)
        # x_major_locator = MultipleLocator(1)
        # y_major_locator = MultipleLocator(1)
        # ax = plt.gca()
        # ax.xaxis.set_major_locator(x_major_locator)
        # ax.yaxis.set_major_locator(y_major_locator)
        plt.plot(minPL)
    # 绘制蚂蚁爬行路径
    if figure2 == 1:
        plt.figure(figsize=(5, 5))
        plt.grid(True)
        x_major_locator = MultipleLocator(1)
        y_major_locator = MultipleLocator(1)
        ax = plt.gca()
        ax.xaxis.set_major_locator(x_major_locator)
        ax.yaxis.set_major_locator(y_major_locator)
        plt.xlim(0, 20)
        plt.ylim(0, 20)
        for i in range(MM):
            for j in range(MM):
                x1 = i
                y1 = j
                x2 = i
                y2 = j + 1
                x3 = i + 1
                y3 = j + 1
                x4 = i + 1
                y4 = j
                if G[i][j] == 1:
                    plt.fill([x1, x2, x3, x4], [y1, y2, y3, y4], "gray")
                else:
                    plt.fill([x1, x2, x3, x4], [y1, y2, y3, y4], "white")

        ROUT = ROUTES[mink][minl]
        LENROUT = len(ROUT)
        Rx = []
        Ry = []
        for ii in range(LENROUT):
            Rx.append(ROUT[ii][0] + 0.5)
            Ry.append(ROUT[ii][1] + 0.5)
        plt.plot(Rx, Ry)
    # 绘制各代蚂蚁的爬行图
    if figure3 == 1:
        plt.figure(figsize=(5, 5))
        plt.grid(True)
        x_major_locator = MultipleLocator(1)
        y_major_locator = MultipleLocator(1)
        ax = plt.gca()
        ax.xaxis.set_major_locator(x_major_locator)
        ax.yaxis.set_major_locator(y_major_locator)
        plt.xlim(0, 20)
        plt.ylim(0, 20)
        for i in range(MM):
            for j in range(MM):
                x1 = i
                y1 = j
                x2 = i
                y2 = j + 1
                x3 = i + 1
                y3 = j + 1
                x4 = i + 1
                y4 = j
                if G[i][j] == 1:
                    plt.fill([x1, x2, x3, x4], [y1, y2, y3, y4], "gray")
                else:
                    plt.fill([x1, x2, x3, x4], [y1, y2, y3, y4], "white")
        for k in range(K):
            PLK = PL[k]
            choose = 0
            notZero = np.nonzero(PLK)
            if len(notZero[0]) != 0:
                minklTmp = float('inf')
                for kk in notZero[0]:
                    if PLK[kk] < minklTmp:
                        minklTmp = PLK[kk]
                        choose = kk
            else:
                continue
            ROUT = ROUTES[k][choose]
            LENROUT = len(ROUT)
            Rx = []
            Ry = []
            for ii in range(LENROUT):
                Rx.append(ROUT[ii][0] + 0.5)
                Ry.append(ROUT[ii][1] + 0.5)
            plt.plot(Rx, Ry)
    if figure1 + figure2 + figure3 >= 1:
        plt.show()










main()
