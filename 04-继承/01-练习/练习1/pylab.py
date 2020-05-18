import matplotlib.pylab as mp
import numpy.random as nr

x=nr.randn(10000)
y=nr.randn(10000)
mp.hexbin(x,y)
mp.show()