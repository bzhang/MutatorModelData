import glob
import os
import re
from util import *
from matplotlib.pyplot import *
from matplotlib.axes import *
import matplotlib.pylab as plt
import numpy as np

__author__ = 'bingjun'

data_path = "/Volumes/BigTwins/MutatorModelData/FixedMutationRates/"
os.chdir(data_path)
file_name = "AdaptationRates_MeanSquaredErrors.txt"
mu_exp = re.compile(r"DeleMR(?P<mu>[\d\.E-]+)_")

u_rates = []
means = []
cis = []

file = csv.reader(open(file_name, 'rb'), delimiter="\t", skipinitialspace=True)
for line in file:
    mu = mu_exp.search(line[0])
    u = float(mu.group('mu'))
    if u >= 1e-4 and u <= 1:
        u_rates.append(u)
        data = string_to_float_list(line[1:-1])
        mean, ci = mean_95CI(data)
        means.append(mean)
        cis.append(ci)

print u_rates

font_size = 20
label_size = 25
fig, ax = plt.subplots(figsize=(14, 10))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
matplotlib.rcParams.update({'font.size': font_size})
u_rates, means, cis = zip(*sorted(zip(u_rates, means, cis)))
errorbar(u_rates, means, cis, fmt='o-', ecolor='gray', capsize=0, markersize=5)
# p = np.poly1d(np.polyfit(u_rates, means, deg=9))
# xp = np.linspace(0.0001, 0.6, 500)
# print p
# ax.plot(xp, p(xp), '-', linewidth=2)
# axhline(y=0, color='black', linewidth=3)
xlabel("Mutation Rates", fontsize=label_size)
ylabel("Mean Squared Residuals", fontsize=label_size)
xscale('log')
# ylim(-0.002, 0.001)
xlim(3e-4, 1)
handles, labels = ax.get_legend_handles_labels()

fig.savefig('Fixed_Asexual_MSE_sorted.png')
