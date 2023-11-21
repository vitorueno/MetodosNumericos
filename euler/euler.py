import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn
from prettytable import PrettyTable


def yLinha(x, y):
    return 2*x


def yReal(x, y):
    return x**2

def calcularErro(xi, yi, aproximado):
    return yReal(xi, yi) - aproximado


def calcularErroRelativo(xi, yi, aproximado):
    try:
        return calcularErro(xi, yi, aproximado) / yReal(xi, yi) 
    except: 
        return 0


def imprimirTabelaEuler(x0, y0, xn, hs):
    for h in hs:
        x, y = euler(x0, y0, xn, h)

        table = PrettyTable(['h', 'xi', 'aproximado', 'real', 'erro', 'erro relativo'])
        # print(f'h\tXi\tAPROXIMADO\tREAL\t\tERRO\t\tERRO RELATIVO')
        # print(h, end='\t')

        for xi, yi in zip(x, y):
            real = yReal(xi, yi)
            erro = calcularErro(xi, yi, yi)
            relativo = calcularErroRelativo(xi, yi, yi)
            table.add_row([h, xi, yi, real, erro, relativo])
            # end = '\n\t' if xi != x[-1] else '\n'
            # print(
            #     f'{xi}\t{yi:.5f}\t\t{real:.5f}\t\t{erro:.5f}\t\t{relativo:.5f}', end=end)
        print(table)
            

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
    x0 = 0
    y0 = 0
    xn = 5
    h = 0.1
    hs = [0.2, 0.1]

    imprimirTabelaEuler(x0, y0, xn, hs)
    imprimirGraficoEuler(x0, y0, xn, h)
