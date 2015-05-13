from euler import *
from numpy import logspace
import matplotlib.pyplot as plt

if __name__ == '__main__':
    v = 1.
    x = 0.
    h = .05
    t = 12 * pi
    
    tlist, xlist, vlist = explicit_euler(v, x, h, t)
    elist = [xlist[i] ** 2 + vlist[i] ** 2 for i in xrange(len(xlist))]
    
    plt.plot(tlist, elist)
    plt.xlabel('Time (t)')
    plt.ylabel('Energy')
    plt.show()
