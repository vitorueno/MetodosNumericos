import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn

v0 = 0 
a = -9.81

def yLinha(t, y):
    return a*t + v0 

def yReal(t, y):
    return (a * (1/2) * t**2) + (v0 * t) + r0(0, 0) 

def r0(t0, y0):
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


def imprimirGraficoEuler(x0, y0, xn, h):
    x, y = euler(x0, y0, xn, h)

    yReais = []
    for i in range(len(x)):
        yReais.append(yReal(x[i], y[i]))

    seaborn.set(style='ticks')
    fig, ax = plt.subplots()
    ax.plot(x, y, label='euler', color='red')
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

    imprimirTabelaEuler(t0, y0, xn, hs)
    imprimirGraficoEuler(t0, y0, xn, h)
