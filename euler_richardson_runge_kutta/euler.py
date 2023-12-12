from metodo import Euler, Richardson, RungeKutta, EulerMelhorado, Nystrom, Heun
import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn
from prettytable import PrettyTable


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

def calcularPorcentagemErro(x, y, aproximacao):
    try:
        return 100 * calcularErro(x, y, aproximacao) / real(x,y)
    except:
        return 0

def imprimirTabelaComparativa(x0, y0, xn, h):
    euler = Euler(x0, y0, h, f)
    euler1h = Euler(x0, y0, h, f)
    euler2h = Euler(x0, y0, 2*h, f)
    richardson = Richardson(x0, y0, h, f)
    runge = RungeKutta(x0, y0, h, f) 
    eulerMelhorado = EulerMelhorado(x0, y0, h, f)
    heun = Heun(x0, y0, h, f)
    nystrom = Nystrom(x0, y0, h, f)

    # table = PrettyTable(['h', 'x', 'y real', 'y euler (1)', 'y richar (1)', 'y euler melhorado (2)', 'y heun (3)', 'y nystrom (3)', 'y r. kutta (4)', 'erro r. euler', 'erro r. richard', 'erro r. euler m.', 'erro r. heunn', 'erro r. nystrom', 'erro r. r. kutta'])
    # table = PrettyTable(['h', 'x', 'y real', 'y euler', 'y richardson', 'y runge kutta 4', 'erro relativo euler', 'erro relativ richardson', 'errro relativo runge kutta 4'])
    table = PrettyTable(['h', 'x', 'y real', 'y euler', 'erro absoluto','erro relativo', 'estimativa de erro', 'erro relativo da estimativa'])

    table.add_row([h, x0, y0, y0, 0, 0, 0, 0])
    xr = np.arange(x0+h, xn+h, h).round(2)
    y = real(x0+h, y0)
    for x in xr:
        y = real(x, y)

        _, passo_euler = euler.next_step()

        _, passo_2euler = euler1h.next_step()
        _, passo_2euler = euler1h.next_step()

        _, passo_euler2h = euler2h.next_step()

        _, passo_richar = richardson.next_step()
        _, passo_euler_melhorado = eulerMelhorado.next_step()
        _, passo_heun = heun.next_step()
        _, passo_nystrom = nystrom.next_step()
        _, passo_runge = runge.next_step()

        erro_euler = calcularErro(x, y, passo_euler)
        erro_relat_euler = calcularErroRelativo(x, y, passo_euler)
        estimativa = passo_2euler - passo_euler2h
        erro_relat_estimativa = calcularErroRelativo(x,y, estimativa)


        erro_richar = calcularErroRelativo(x, y, passo_richar)
        erro_euler_melhorado = calcularErroRelativo(x,y, passo_euler_melhorado)
        erro_heun = calcularErroRelativo(x,y, passo_heun)
        erro_nystrom = calcularErroRelativo(x,y, passo_nystrom)
        erro_runge = calcularErroRelativo(x,y, passo_runge)

        if (int(x) == x):
            table.add_row([h, x, y, passo_euler, erro_euler, erro_relat_euler, estimativa, erro_relat_estimativa])
            # table.add_row([h, x, y, passo_euler, erro_euler, erro_relat_euler])
    
    print(table)

def imprimirGraficoComparativo(x0, y0, xn, h):
    euler = Euler(x0, y0, h, f)
    richardson = Richardson(x0, y0, h, f)
    runge = RungeKutta(x0, y0, h, f)
    melhorado = EulerMelhorado(x0, y0, h, f)
    heun = Heun(x0, y0, h, f)
    nystrom = Nystrom(x0, y0, h, f)
     

    xEuler, yEuler = euler.range_respostas(xn)
    xRichar, yRichar = richardson.range_respostas(xn)
    xRunge, yRunge = runge.range_respostas(xn)
    xMelhorado, yMelhorado = melhorado.range_respostas(xn)
    xHeun, yHeun = heun.range_respostas(xn)
    xNystrom, yNystrom = nystrom.range_respostas(xn)
    
    yReais = []
    y = y0 
    for i in range(len(xEuler)):
        y = real(xEuler[i], y)
        yReais.append(y)


    seaborn.set(style='ticks')
    fig, ax = plt.subplots()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    # ax.plot(xEuler, yEuler, label='Euler', color='red')
    # ax.plot(xMelhorado, yMelhorado, label='Euler Melhorado', color='purple')
    # ax.plot(xRichar, yRichar, label='Richardson', color='blue')
    # ax.plot(xHeun, yHeun, label='Heun', color='yellow')
    # ax.plot(xNystrom, yNystrom, label='Nystrom', color='black')
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
    xn = 5
    h = 0.05

    imprimirTabelaComparativa(x0, y0, xn, h)
    imprimirTabelaComparativa(x0, y0, xn, 2*h)
    # imprimirGraficoComparativo(x0, y0, xn, h)


