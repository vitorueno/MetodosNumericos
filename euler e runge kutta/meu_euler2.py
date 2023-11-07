# y'= -1.2 * y + 7 * e^(-0.3*x)

from math import *
import matplotlib.pyplot as plt
import numpy as np
import seaborn


def differentialEquation(x, y):
    ypr = -1.2*y + 7 * (exp((-0.3)*x))
    return ypr


def initialValueProblem(initialX, initialY):
    c = initialY - float(initialX**2)/2
    return c


def expectedSolution(x):
    y = (70/9) * exp((-0.3)*x) - (43/9) * exp((-1.2) * x)
    return y


def calculateErrorPercentage(expected, approximation):
    error = abs(expected-approximation) / expected * 100
    return error


def show_from_list(xList, yList):
    for i in range(len(xList)):
        xn = xList[i]
        yn = yList[i]
        expect = expectedSolution(xn)

        print(f'Iteration {i} : y_{i} = {yn}')
        print(f'Expected Value :  y_{i} = {expect}')
        print(f'Error: {calculateErrorPercentage(expect, yn)} %\n')


def euler(xn, yn, numberOfIterations, stepSize):
    x = [xn]
    y = [yn]
    for step in range(numberOfIterations):
        yn1 = yn + differentialEquation(xn, yn) * stepSize

        xn += stepSize
        yn = yn1
        x.append(xn)
        y.append(yn1)

    return (x, y)


def plotar(x, y):
    ex_y = []
    for i in range(len(x)):
        ex_y.append(expectedSolution(x[i]))

    seaborn.set(style='ticks')
    fig, ax = plt.subplots()
    ax.plot(x, y, label='aproximada', color='orange')
    ax.plot(x, ex_y, label='esperada', color='green')
    ax.set_aspect('auto')
    ax.grid(True, which='both')
    ax.legend()
    seaborn.despine(ax=ax, offset=0)

    plt.show()

x0 = 0
y0 = 3
numberOfIterations = 40
stepSize = 0.1


x, y = euler(x0, y0, numberOfIterations, stepSize)


show_from_list(x, y)
plotar(x, y)
