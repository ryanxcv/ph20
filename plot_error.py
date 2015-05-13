from euler import *
from numpy import logspace
import matplotlib.pyplot as plt

if __name__ == '__main__':
    v = 1.
    x = 0.
    t = 12 * pi
    
    hlist = logspace(-1, -3, num=20)
    print hlist
    errlist = []
    for h in hlist:
        tlist, xlist, vlist = explicit_euler(v, x, h, t)
        errlist.append(max(xlist - analytic(v, x, tlist)[0]))
    
    plt.plot(hlist, errlist)
    plt.xlabel('Timestep (h)')
    plt.ylabel('Maximum positional error')
    plt.savefig('img/truncation.pdf', bbox_inches='tight')
