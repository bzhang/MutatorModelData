import os
from util import get_column
import matplotlib.pylab as plt
import numpy as np
from pylab import hist, show, xticks

__author__ = 'bingjun'

x = range(-6,6)
hist(x, bins=np.mgrid[-6:6:20j])
show()

