from metodo import Euler, Richardson, RungeKutta, EulerMelhorado, Nystrom, Heun
import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn
from prettytable import PrettyTable


def f(x, y):
    return math.cos(x)


def real(x, y):
    return math.sin(x)


def calcularErro(x, y, aproximacao):
    return real(x, y) - aproximacao


def calcularErroRelativo(x, y, aproximacao):
    try:
        return calcularErro(x, y, aproximacao) / real(x, y)
    except:
        return 0


def calcularPorcentagemErro(x, y, aproximacao):
    try:
        return 100 * calcularErro(x, y, aproximacao) / real(x, y)
    except:
        return 0


def imprimirTabelaComparativa(x0, y0, xn, h):
    euler = Euler(x0, y0, h, f)
    richardson = Richardson(x0, y0, h, f)
    runge = RungeKutta(x0, y0, h, f)
    eulerMelhorado = EulerMelhorado(x0, y0, h, f)
    heun = Heun(x0, y0, h, f)
    nystrom = Nystrom(x0, y0, h, f)

    table = PrettyTable(['h', 'x', 'y real', 'y euler (1)', 'y richar (1)', 'y euler melhorado (2)', 'y heun (3)', 'y nystrom (3)',
                        'y r. kutta (4)', 'erro r. euler', 'erro r. richard', 'erro r. euler m.', 'erro r. heunn', 'erro r. nystrom', 'erro r. r. kutta'])

    table.add_row([h, x0, y0, y0, y0, y0, y0, y0, y0, 0, 0, 0, 0, 0, 0])
    xr = np.arange(x0+h, xn+h, h).round(2)
    y = real(x0+h, y0)
    for x in xr:
        y = real(x, y)

        _, passo_euler = euler.next_step()
        _, passo_richar = richardson.next_step()
        _, passo_euler_melhorado = eulerMelhorado.next_step()
        _, passo_heun = heun.next_step()
        _, passo_nystrom = nystrom.next_step()
        _, passo_runge = runge.next_step()

        erro_euler = calcularErroRelativo(x, y, passo_euler)
        erro_richar = calcularErroRelativo(x, y, passo_richar)
        erro_euler_melhorado = calcularErroRelativo(
            x, y, passo_euler_melhorado)
        erro_heun = calcularErroRelativo(x, y, passo_heun)
        erro_nystrom = calcularErroRelativo(x, y, passo_nystrom)
        erro_runge = calcularErroRelativo(x, y, passo_runge)

        # if (int(x) == x):
        table.add_row([h, x, y, passo_euler, passo_richar, passo_euler_melhorado, passo_heun, passo_nystrom,
                      passo_runge, erro_euler, erro_richar, erro_euler_melhorado, erro_heun, erro_nystrom, erro_runge])

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
    ax.plot(xEuler, yEuler, label='Euler (1)', color='red')
    ax.plot(xRichar, yRichar, label='Richardson (1)', color='blue')
    ax.plot(xMelhorado, yMelhorado, label='Euler Melhorado (2)', color='purple')
    ax.plot(xHeun, yHeun, label='Heun (3)', color='yellow')
    ax.plot(xNystrom, yNystrom, label='Nystrom (3)', color='black')
    ax.plot(xRunge, yRunge, label='Runge Kutta (4)', color='orange')
    ax.plot(xEuler, yReais, label='Real', color='green')
    ax.set_aspect('auto')
    ax.grid(True, which='both')
    seaborn.despine(ax=ax, offset=0)
    ax.legend()

    plt.show()


if __name__ == '__main__':
    x0 = 0
    y0 = 0
    xn = 2*math.pi
    h = 0.1


    imprimirTabelaComparativa(x0, y0, xn, h)
    imprimirGraficoComparativo(x0, y0, xn, h)
