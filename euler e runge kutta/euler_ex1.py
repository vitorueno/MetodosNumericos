# y'=x

from math import *


def diffq(a):
    ypr = a
    return ypr


def ivp(inix, iniy):
    c = iniy - float(inix**2)/2
    return c


def solde(a):
    y = float(a**2)/2 + ivp(inix, iniy)
    return y


def error(ex, app):
    err = abs(ex-app) / (ex) * 100
    return err


inix = float(input('Initial value for x?: '))
iniy = float(input('Initial value for y?: '))
it = int(input('How many iterations?: '))
ss = float(input('Which step size?: '))
print('')

step = 0
xn = inix
yn = iniy

print('Iteration 0: y_0 =', yn)
print('Exact Value: y_0 =', solde(xn))
print('Error: ', error(solde(xn), yn), '%')
print('')

while step < it:

    yn1 = yn + diffq(xn)*ss
    xn = xn + ss

    string = 'y_'+str(step+1)
    print('Iteration', step+1, ': ', string, '=', yn1)
    print('Exact Value: ', string, '=', solde(xn))
    print('Error: ', error(solde(xn), yn1), '%')
    print('')

    yn = yn1
    step = step + 1
