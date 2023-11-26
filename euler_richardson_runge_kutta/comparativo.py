from metodo import Euler, Richardson, RungeKutta
import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn
from prettytable import PrettyTable

C = 20

def f(x, y):
    return -y


def real(x, y):
    return math.exp(-x)


def calcularErro(x, y, aproximacao):
    return real(x, y) - aproximacao

def calcularErroRelativo(x, y, aproximacao):
    try:
        return calcularErro(x, y, aproximacao) / real(x,y)
    except:
        return 0


def imprimirTabelaComparativa(x0, y0, xn, h):
    euler = Euler(x0, y0, h, f)
    richardson = Richardson(x0, y0, h, f)
    runge = RungeKutta(x0, y0, h, f) 

    table = PrettyTable(['h', 'x', 'y real', 'y euler', 'y richardson', 'y runge kutta (4)', 'erro euler', 'erro richardson', 'erro runge kutta'])

    table.add_row([h, x0, y0, y0, y0, y0, 0, 0, 0])
    xr = np.arange(x0+h, xn+h, h).round(2)
    y = real(x0+h, y0)
    for x in xr:
        y = real(x, y)

        _, passo_euler = euler.next_step()
        _, passo_richar = richardson.next_step() 
        _, passo_runge = runge.next_step()

        erro_euler = calcularErro(x, y, passo_euler)
        erro_richar = calcularErro(x, y, passo_richar)
        erro_runge = calcularErro(x,y, passo_runge)

        if (int(x) == x):
            table.add_row([h, x, y, passo_euler, passo_richar, passo_runge, erro_euler, erro_richar, erro_runge])
    
    print(table)

def imprimirGraficoComparativo(x0, y0, xn, h):
    euler = Euler(x0, y0, h, f)
    richardson = Richardson(x0, y0, h, f)
    runge = RungeKutta(x0, y0, h, f)
     

    xEuler, yEuler = euler.range_respostas(xn)
    xRichar, yRichar = richardson.range_respostas(xn)
    xRunge, yRunge = runge.range_respostas(xn)
    
    yReais = []
    y = y0 
    for i in range(len(xEuler)):
        y = real(xEuler[i], y)
        yReais.append(y)


    seaborn.set(style='ticks')
    fig, ax = plt.subplots()
    ax.plot(xEuler, yEuler, label='Euler', color='red')
    ax.plot(xRichar, yRichar, label='Richardson', color='blue')
    ax.plot(xRunge, yRunge, label='Runge Kutta (4)', color='orange')
    ax.plot(xEuler, yReais, label='Real', color='green')
    ax.set_aspect('auto')
    ax.grid(True, which='both')
    seaborn.despine(ax=ax, offset=0)
    ax.legend()

    plt.show()

       

if __name__ == '__main__':
    x0 = 0
    y0 = 1 
    xn = 10
    h = 0.1 

    imprimirTabelaComparativa(x0, y0, xn, h)
    imprimirGraficoComparativo(x0, y0, xn, h)



