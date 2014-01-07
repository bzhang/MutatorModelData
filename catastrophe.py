# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np

# <codecell>

u = np.logspace(-1, .14, 51)
w = np.logspace(0, 11, 51)
t = np.arange(51)

# <codecell>

def set_up_axes(ax, xmin, xmax, xstep, ymin, ymax, ystep, \
    xlabel='', ylabel=''):
    for loc, spine in ax.spines.items():
        if loc in ['left','bottom']:
            spine.set_position(('outward',10)) # outward by 10 points
        elif loc in ['right','top']:
            spine.set_color('none') # don't draw spine
        else:
            raise ValueError('unknown spine location: %s'%loc)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    xticks = np.arange(xmin, xmax + xstep, xstep)
    yticks = np.arange(ymin, ymax + ystep, ystep)
    ax.set_xlim(xmin, xmax)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticks, fontsize=14)
    ax.set_xlabel(xlabel, fontsize=14)
    ax.xaxis.set_ticks_position('bottom')
    ax.set_ylim(ymin, ymax)
    ax.set_yticks(yticks)
    ax.set_yticklabels(yticks, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    ax.yaxis.set_ticks_position('left')

# <codecell>

fig = plt.figure(1, figsize=(8.6, 4))
ax1 = fig.add_axes([0.09, 0.16, 0.37, 0.8])
ax2 = fig.add_axes([0.61, 0.16, 0.37, 0.8])
set_up_axes(ax1, 0, 50, 10, 0, 1.5, .5, \
    'Time (thousands of generations)', 'Deleterious mutation rate')
set_up_axes(ax2, 0, 50, 10, 10, 100, 10, \
    'Time (thousands of generations)', 'Mean fitness')
ax1.plot(t, u, 'k')
ax2.semilogy(t, w, 'k')
yticks = [1e-3, 1, 1e3, 1e6, 1e9, 1e12]
ax2.set_yticks(yticks)
ax2.set_yticklabels(np.logspace(-3, 12, 6), fontsize=14)
ax2.yaxis.set_major_formatter(matplotlib.ticker.LogFormatterMathtext())
ax2.tick_params(axis='y', which='minor', left='off')
ax1.text(2.5, 1.495,  'A', size=24, fontweight='bold', \
    ha='center', va='center')
ax2.text(2.5, 9e11, 'B', size=24, fontweight='bold', \
    ha='center', va='center')
plt.savefig('/Users/rbazev/Desktop/test.pdf')
!open /Users/rbazev/Desktop/test.pdf

# <codecell>

!ipython nbconvert --to latex --template article catastrophe.ipynb
!open catastrophe.tex

# <codecell>


