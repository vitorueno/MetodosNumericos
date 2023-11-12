import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn

v0 = 0 
r0 = 0
a = -9.81

def yLinha(t, y):
    return a 

def yReal(t, y):
    return (a * (1/2) * t**2) + (v0 * t) + pvi(0, 0) 

def pvi(t0, y0):
    p0 = y0 - (v0 * t0) - (a * (1/2) * t0**2)
    return p0

def calcularErro(ti, yi, aproximado):
    return yReal(ti, yi) - aproximado


def calcularErroRelativo(ti, yi, aproximado):
    try:
        return calcularErro(ti, yi, aproximado) / yReal(ti, yi) 
    except: 
        return 0


def imprimirTabelaEuler(x0, y0, xn, hs):
    for h in hs:
        x, y = euler(x0, y0, xn, h)

        print(f'h\tXi\tAPROXIMADO\tREAL\t\tERRO\t\tERRO RELATIVO')
        print(h, end='\t')

        for xi, yi in zip(x, y):
            real = yReal(xi, yi)
            erro = calcularErro(xi, yi, yi)
            relativo = calcularErroRelativo(xi, yi, yi)
            end = '\n\t' if xi != x[-1] else '\n'
            print(
                f'{xi}\t{yi:.5f}\t\t{real:.5f}\t\t{erro:.5f}\t\t{relativo:.5f}', end=end)
            

def euler(x0, y0, xn, h):
    n = int((xn / h))
    
    x = [x0]
    y = [y0]
    for i in range(n):
        x0 = round(x0 + h, 2)
        y0 = y0 + h * (yLinha(x0, y0))

        x.append(x0)
        y.append(y0)

    return x, y

def eulerDuplo(x0, y0, r0, xn, h):
    n = int((xn / h))
    
    x = [x0]
    y = [y0]
    r = [r0]
    for i in range(n):
        x0 = round(x0 + h, 2)
        y0 = y0 + h * (yLinha(x0, y0))
        r0 = r0 + h * y0

        x.append(x0)
        y.append(y0)
        r.append(r0)

    return x, y, r



def imprimirGraficoEuler(x0, y0, xn, h):
    x, y = euler(x0, y0, xn, h)
    x2, y2 = euler(x0, y0, xn, h*2) 
    x3, y3 = euler(x0, y0, xn, h*4) 

    yReais = []
    for i in range(len(x)):
        yReais.append(yReal(x[i], y[i]))

    seaborn.set(style='ticks')
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f'euler h = {h}', color='red')
    ax.plot(x2, y2, label=f'euler h = {h*2}', color='green')
    ax.plot(x3, y3, label=f'euler h = {h*4}', color='purple')
    ax.plot(x, yReais, label='esperada', color='blue')
    ax.set_aspect('auto')
    ax.grid(True, which='both')
    seaborn.despine(ax=ax, offset=0)
    ax.legend()

    plt.show()

def imprimirGraficoEuler2(x0, y0, r0, xn, h):
    x, y, r = eulerDuplo(x0, y0, r0, xn, h)

    yReais = []
    for i in range(len(x)):
        yReais.append(yReal(x[i], y[i]))

    seaborn.set(style='ticks')
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f'euler V = {h}', color='red')
    ax.plot(x, r, label=f'euler R = {h}', color='green')
    ax.plot(x, yReais, label='esperada', color='blue')
    ax.set_aspect('auto')
    ax.grid(True, which='both')
    seaborn.despine(ax=ax, offset=0)
    ax.legend()

    plt.show()

if __name__ == '__main__':
    t0 = 0
    y0 = 0
    xn = 10
    h = 0.1
    hs = [0.2, 0.1, 0.05]

    x, v, r = eulerDuplo(t0, y0, r0, xn, h)
    imprimirGraficoEuler2(t0, y0, r0, xn, h)

    # print(f'X = {x[20]}; V = {v[20]}; R={r[20]}') 
    # imprimirTabelaEuler(t0, y0, xn, hs)
    # imprimirGraficoEuler(t0, y0, xn, h)
