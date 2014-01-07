import glob
import os
import re
from util import *
from matplotlib.pyplot import *
from matplotlib.axes import *
import matplotlib.pylab as plt
import numpy as np

__author__ = 'bingjun'

data_path = "/Volumes/BigTwins/MutatorModelData/N1000/Sexual/FixedR0.75/"
os.chdir(data_path)
file_name = "AdaptationRates_LogFit_NoSeg.txt"
mu_exp = re.compile(r"DeleMR(?P<mu>[\d\.E-]+)_")
# r_exp = re.compile(r"R1.0_(?P<r>[\d\.E-]+)_")
file = csv.reader(open(file_name, 'rb'), delimiter="\t", skipinitialspace=True)

u_rates = []
r_rates = []
means = []
cis = []

for line in file:
    mu = mu_exp.search(line[0])
    u = float(mu.group('mu'))
    # r_results = r_exp.search(line[0])
    # r = float(r_results.group('r'))
    if u >= 1e-4 and u <= 1:
    # if r >= 1e-3 and r <= 1:
        u_rates.append(u)
        # r_rates.append(r)
        print u
        # print r
        data = string_to_float_list(line[1:-1])
        mean, ci = mean_95CI(data)
        means.append(mean)
        cis.append(ci)

font_size = 20
label_size = 25
fig, ax = plt.subplots(figsize=(12, 10))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
matplotlib.rcParams.update({'font.size': font_size})
errorbar(u_rates, means, cis, fmt='ro', ecolor='gray', capsize=0, markersize=10)
# errorbar(r_rates, means, cis, fmt='ro-', ecolor='gray', capsize=0, markersize=10)
axhline(y=0, color="b", linewidth=3)
xlabel("Mutation Rates", fontsize=label_size)
# xlabel("Recombination Rates", fontsize=label_size)
ylabel("Adaptation Rates", fontsize=label_size)
# title("N = 1000, Sexual, Ud = 0.05, Ub = 1e-4")
title("N = 1000, Sexual, r = 0.75")
# xlim((0.1, 0.8))
xscale('log')
# yscale('log')
p = np.poly1d(np.polyfit(u_rates, means, deg=3))
# p = np.poly1d(np.polyfit(r_rates, means, deg=3))
print u_rates
# print r_rates
print means
xp = np.linspace(0.001, 1.0, 500)
plot(xp, p(xp), '-', color='g', linewidth=2)
fig.savefig('AdaptationRates_LogFit.pdf')
