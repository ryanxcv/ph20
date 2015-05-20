from math  import pi, tanh
from numpy import cos, sin
import matplotlib.pyplot as plt
import os

''' Calculates the next velocity explicitly based on v, x, and h. '''
def vnext(v, x, h):
    return v - h * x

''' Calculates the next x explicitly based on vnext, x, and h. '''
def xnext(vnext, x, h):
    return x + h * vnext + h * h * x

''' Calculates the next x implicitly based on v, x, and h. '''
def xnexti(v, x, h):
    return (x + h * v) / (h * h + 1)

''' Calculates the next velocity implicitly based on v, xnext, and h. '''
def vnexti(v, xnext, h):
    return v - h * xnext

def explicit_euler(v, x, h, tmax):
    t = 0.
    tlist = [t]
    xlist = [x]
    vlist = [v]
    while t < tmax:
        t += h
        v = vnext(v, x, h)
        x = xnext(v, x, h)
        tlist.append(t)
        xlist.append(x)
        vlist.append(v)
    
    return (tlist, xlist, vlist)

def implicit_euler(v, x, h, tmax):
    t = 0.
    tlist = [t]
    xlist = [x]
    vlist = [v]
    while t < tmax:
        t += h
        x = xnexti(v, x, h)
        v = vnexti(v, x, h)
        tlist.append(t)
        xlist.append(x)
        vlist.append(v)
    
    return (tlist, xlist, vlist)

'''
Finds parameters and calculates a function of the form 
A * sin (x + phi).
'''
def analytic(v, x, tlist):
    phi = pi / 2
    if v != 0:
        phi = tanh(x / v)
    
    if sin(phi) != 0:
        A = x / sin(phi)
    else:
        A = v / cos(phi)
    
    return (A * sin([t + phi for t in tlist]), A * cos([t + phi for t in tlist]))

if __name__ == '__main__':
    v = 1.
    x = 0.
    h = 0.05
    t = 12 * pi
    
    # Check whether the /img directory exists.
    if not os.path.isdir(os.getcwd() + "/img"):
        # If it doesn't, create it.
        os.makedirs(os.getcwd() + "/img")
    
    # Plot explicit euler.
    plt.xlabel('Time (t)')
    tlist, xlist, vlist = explicit_euler(v, x, h, t)
    plt.plot(tlist, xlist)
    plt.plot(tlist, vlist)
    plt.savefig('img/explicit.pdf', bbox_inches='tight')
    
    # Plot explicit euler error.
    plt.clf()
    plt.xlabel('Time (t)')
    plt.plot(tlist, xlist - analytic(v, x, tlist)[0])
    plt.plot(tlist, vlist - analytic(v, x, tlist)[1])
    plt.savefig('img/error.pdf', bbox_inches='tight')
    
    # Plot explicit euler positional difference.
    plt.clf()
    plt.xlabel('Time (t)')
    plt.ylabel('Position (x)')
    plt.plot(tlist, xlist)
    plt.plot(tlist, analytic(v, x, tlist)[0])
    plt.savefig('img/diff.pdf', bbox_inches='tight')
    
    # Plot impicit euler.
    plt.clf()
    plt.xlabel('Time (t)')
    tlist, xlist, vlist = implicit_euler(v, x, h, t)
    plt.plot(tlist, xlist)
    plt.plot(tlist, vlist)
    plt.savefig('img/implicit.pdf', bbox_inches='tight')
