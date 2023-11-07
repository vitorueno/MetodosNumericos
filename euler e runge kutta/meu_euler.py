# y'=x

from math import *
import matplotlib.pyplot as plt
import numpy as np
import seaborn


def f(x):
    ypr = x
    return ypr


def initialValueProblem(initialX, initialY):
    c = initialY - float(initialX**2)/2
    return c


def expectedSolution(a):
    y = float(a**2)/2 + initialValueProblem(x0, y0)
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
        yn1 = yn + f(xn) * stepSize
        xn += stepSize
        x.append(xn)
        y.append(yn1)

        yn = yn1

    return (x, y)


def plotar(x, y):
    ex_y = []
    for i in range(len(x)):
        ex_y.append(expectedSolution(x[i]))

    seaborn.set(style='ticks')
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.plot(x, ex_y)
    ax.set_aspect('auto')
    ax.grid(True, which='both')
    seaborn.despine(ax=ax, offset=0)

    plt.show()

x0 = 1
y0 = 1
numberOfIterations = 10
stepSize = 1


x, y = euler(x0, y0, numberOfIterations, stepSize)


show_from_list(x, y)
plotar(x, y)
