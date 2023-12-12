import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn
from prettytable import PrettyTable

def yLinha(t, y):
    return y

def yReal(t, y):
    return math.exp(t)


def calcularErro(ti, yi, aproximado):
    return yReal(ti, yi) - aproximado


def calcularErroRelativo(ti, yi, aproximado):
    try:
        return calcularErro(ti, yi, aproximado) / yReal(ti, yi)
    except:
        return 0


def imprimirTabelaEulerRichardson(t0, y0, tn, h):
    for h in hs:
        x, y = euler(t0, y0, tn, h)
        x2h, y2h = euler(t0, y0, tn, 2*h)

        table = PrettyTable(['h', 'x', 'y real', 'y euler', 'aproximacao', 'ERRO EULER', 'estimativa erro'])

        for xi, yi in zip(x, y):
            real = yReal(xi, yi)
            erro = calcularErro(xi, yi, yi)
            
            erro_rirchardson = 0
            aprox_rirchardson = 0
            if (int(xi) == xi): 
                j = x2h.index(xi)
                erro_rirchardson = yi - y2h[j]
                relativo_richardson = calcularErroRelativo(xi, yi, erro_rirchardson)
                aprox_rirchardson = 2*yi - y2h[j]
                relativo = calcularErroRelativo(xi, yi, yi)
                richardson_real = yReal(xi, yi) - aprox_rirchardson 

                table.add_row([h, xi, real, yi, aprox_rirchardson, erro, erro_rirchardson])


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

def euler_step(x0, y0, xn, h):
    return y0 + h * yLinha(x0, y0)

def imprimirGraficoEulerRirchardson(x0, y0, xn, h):
    x, y = euler(x0, y0, xn, h)
    x2h, y2h = euler(x0, y0, xn, 2*h)
    
    yReais = []
    for i in range(len(x)):
        yReais.append(yReal(x[i], y[i]))

    y_richardson = []
    for i in range(len(x)):
        for j in range(len(x2h)):
            if x[i] == x2h[j]:
                y_richardson.append(2*y[i] - y2h[j])


    seaborn.set(style='ticks')
    fig, ax = plt.subplots()
    ax.plot(x, y, label='euler', color='red')
    ax.plot(x, yReais, label='esperada', color='blue')
    ax.plot(x2h, y_richardson, label='Aproximação de Richardson', color='green')
    ax.set_aspect('auto')
    ax.grid(True, which='both')
    seaborn.despine(ax=ax, offset=0)
    ax.legend()

    plt.show()

if __name__ == '__main__':
    x0 = 0
    y0 = 1
    xn = 5
    h = 0.1
    hs = [0.1, 0.05]

    y1 = y0
    x1 = x0
    y2 = y0 
    x2 = x0
    h1 = h 
    h2 = h/2

    table = PrettyTable(['x1', 'x2', 'real', 'y1 (euler)', 'y2', 'richardson' ])
    for i in range(int(xn/h)):
        x1 = round(x1+h1, 2)
        y1 = y1 + h1*yLinha(x1, y1)

        x2 = round(x2+h2, 2)
        y2 = y2 + h2*yLinha(x2, y2)
        x2 = round(x2+h2, 2)
        y2 = y2 + h2*yLinha(x2, y2)

        richardson = 2* y2 - y1

        if (int(x1) == x1):
            real = yReal(x1, y1)
            table.add_row([x1, x2, real, y1, y2, richardson ])
    print(table)

    imprimirTabelaEulerRichardson(x0, y0, xn, hs)
    imprimirGraficoEulerRirchardson(x0, y0, xn, h)
