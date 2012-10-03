import os
from util import get_column
import matplotlib.pylab as plt
import numpy as np

__author__ = 'bingjun'

x = np.random.randn(1000)

fig = plt.figure()
ax = fig.add_subplot(111)
n, bins, rectangles = ax.hist(x, 50, normed=True)
fig.canvas.draw()
plt.show()