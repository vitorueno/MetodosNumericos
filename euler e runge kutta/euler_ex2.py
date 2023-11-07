import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn
# y '+ 2y = 2-e ^ -4x


def f(x, y):
    ypr = 2 - float(math.exp((-4) * x)) - 2 * y
    return ypr


def initialValueProblem(initialX, initialY):
    c = initialY + float(math.exp(-2 * initialX)) / 2 - \
        float(math.exp((-4) * initialX)) / 2
    return c


def expectedSolution(x):
    y = initialValueProblem(x0, y0) + \
        float(math.exp((-4) * x)) / 2 - (float(math.exp((-2) * x)) / 2)
    return y


def calculateErrorPercentage(expected, approximation):
    error = abs(expected - approximation) / expected * 100
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
        yn1 = yn + f(xn, yn) * stepSize
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
numberOfIterations = 12
stepSize = 1


x, y = euler(x0, y0, numberOfIterations, stepSize)

show_from_list(x, y)
plotar(x, y)

# step = 0
# xn = x0
# yn = y0

# print('Iteration 0: y_0 =', yn)
# print('Exact Value: y_0 =', expectedSolution(xn))
# print('Error: ', calculateErrorPercentage(expectedSolution(xn), yn), '%')
# print('')

# while step < numberOfIterations:
#     yn1 = yn + f(xn, yn) * stepSize
#     xn = xn + stepSize

#     string = 'y_' + str(step + 1)
#     print('Iteration', step + 1, ': ', string, '=', yn1)
#     print('Exact Value: ', string, '=', expectedSolution(xn))
#     print('Error: ', calculateErrorPercentage(expectedSolution(xn), yn1), '%')
#     print('')

#     yn = yn1

#     step = step + 1
