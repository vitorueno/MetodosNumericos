# y'=x

from math import *
import matplotlib.pyplot as plt
import numpy as np
import seaborn


def f(x, y):
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


def show_from_list(xList, yList, xList2, yList2):
    for i in range(len(xList)):
        xn = xList[i]
        yn = yList[i]
        xn2 = xList2[i]
        yn2 = yList2[i]
        expect = expectedSolution(xn)

        print(f'STEP {i}')
        print(f'Expected Value :  y_{i} = {expect}')
        print(f'Runge Kutta : y_{i} = {yn2}')
        print(f'Euler : y_{i} = {yn}')
        print(f'Error Runge Kutta: {calculateErrorPercentage(expect, yn2)} %\n')
        print(f'Error Euler: {calculateErrorPercentage(expect, yn)} %')


def euler(xn, yn, numberOfIterations, stepSize):
    x = [xn]
    y = [yn]
    for step in range(numberOfIterations):
        yn1 = yn + f(xn, yn) * stepSize
        xn += stepSize
        x.append(xn)
        y.append(yn1)

        yn = yn1

    return (x, y)

def runge_kutta(xn, yn, numberOfIterations, stepSize):
    x = [xn] 
    y = [yn]
    for step in range(numberOfIterations):
        k1 = f(xn, yn)
        k2 = f(xn + (stepSize/2), yn + (stepSize/2) * k1)
        k3 = f(xn + (stepSize/2), yn + (stepSize/2) * k2)
        k4 = f(xn+stepSize, yn + stepSize*k3)
        yn1 = yn + (1/6) * (k1 + 2*k2 + 2*k3 + k4) 
        xn += stepSize
        x.append(xn)
        y.append(yn1)

        yn = yn1
    
    return (x,y)


def plotar(x, y, x2, y2):
    ex_y = []
    for i in range(len(x)):
        ex_y.append(expectedSolution(x[i]))

    seaborn.set(style='ticks')
    fig, ax = plt.subplots()
    ax.plot(x, y, label='euler', color='red')
    ax.plot(x, ex_y, label='esperada', color='blue')
    ax.plot(x2, y2, label='runge kutta', color='green')
    ax.set_aspect('auto')
    ax.grid(True, which='both')
    seaborn.despine(ax=ax, offset=0)
    ax.legend()

    plt.show()

x0 = 1
y0 = 1
numberOfIterations = 10
stepSize = 1


x, y = euler(x0, y0, numberOfIterations, stepSize)
x2, y2 = runge_kutta(x0, y0, numberOfIterations, stepSize)

show_from_list(x, y, x2, y2)
plotar(x, y, x2, y2)
