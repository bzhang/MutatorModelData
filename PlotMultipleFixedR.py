import glob
import os
import re
from util import *
from matplotlib.pyplot import *
from matplotlib.axes import *
import matplotlib.pylab as plt
import numpy as np

__author__ = 'bingjun'

data_path = "/Volumes/BigTwins/MutatorModelData/N1000/Sexual/"
asexual_file_name = "/Volumes/BigTwins/MutatorModelData/N1000/FixedMutationRates/AdaptationRates_LogFit_NoSeg.txt"
os.chdir(data_path)
file_name = "AdaptationRates_LogFit_NoSeg.txt"
mu_exp = re.compile(r"DeleMR(?P<mu>[\d\.E-]+)_")
r_exp = re.compile(r"FixedR(?P<r>[\d\.E-]+)")
dirs = glob.glob("FixedR*")

u_rates = map(list, [[]] * 5)
r_rates = []
means = map(list, [[]] * 5)
cis = map(list, [[]] * 5)
color = ['r', 'b', 'g', 'Orange']

dir_count = 0
asexual_file = csv.reader(open(asexual_file_name, 'rb'), delimiter="\t", skipinitialspace=True)
r_rates.append(0)
for line in asexual_file:
    mu = mu_exp.search(line[0])
    u = float(mu.group('mu'))
    if u >= 1e-3 and u <= 1:
        u_rates[dir_count].append(u)
        # print u
        data = string_to_float_list(line[1:-1])
        mean, ci = mean_95CI(data)
        means[dir_count].append(mean)
        cis[dir_count].append(ci)
dir_count = dir_count + 1

for dir_name in dirs:
    os.chdir(dir_name)
    r_results = r_exp.search(dir_name)
    r = float(r_results.group('r'))
    r_rates.append(r)
    sexual_file = csv.reader(open(file_name, 'rb'), delimiter="\t", skipinitialspace=True)
    for line in sexual_file:
        mu = mu_exp.search(line[0])
        u = float(mu.group('mu'))
        if u >= 1e-3 and u <= 1:
            u_rates[dir_count].append(u)
            # print u
            data = string_to_float_list(line[1:-1])
            mean, ci = mean_95CI(data)
            means[dir_count].append(mean)
            cis[dir_count].append(ci)
    dir_count = dir_count + 1
    os.chdir(data_path)

print u_rates
print r_rates

font_size = 20
label_size = 25
fig, ax = plt.subplots(figsize=(12, 10))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
matplotlib.rcParams.update({'font.size': font_size})
# legends = []
# for r_count in range(0, len(r_rates)):
for r_count in range(0, 1):
    print r_count
    # for u_data in u_rates:
    #     print u_data
    errorbar(u_rates[r_count], means[r_count], cis[r_count], fmt='o', ecolor='gray', capsize=0, markersize=5)
    p = np.poly1d(np.polyfit(u_rates[r_count], means[r_count], deg=7))
    xp = np.linspace(0.001, 1.0, 500)
    print r_rates[r_count]
    # ax.add_artist(plot(xp, p(xp), '-', linewidth=2))
    ax.plot(xp, p(xp), '-', linewidth=2, label="r = " + str(r_rates[r_count]))
axhline(y=0, color='black', linewidth=3)
xlabel("Mutation Rates", fontsize=label_size)
ylabel("Adaptation Rates", fontsize=label_size)
# title("N = 1000, r = 0, 0.25, 0.5, 0.75, 1")
xscale('log')
ylim(-0.4, 0.2)
xlim(1e-3, 4e-1)
handles, labels = ax.get_legend_handles_labels()
# display = (1, 3, 5, 7, 9, 0,2,4,6,8)
# lg = ax.legend([handle for i, handle in enumerate(handles) if i in display], [label for i, label in enumerate(labels) if i in display], loc=3, numpoints=1)
# lg = ax.legend(handles, labels, loc=3)
# lg.draw_frame(False)
# fig.savefig('Fixed_R_AdaptationRates_LogFit.png')
fig.savefig('Fixed_R_Asexual_AdaptationRates_LogFit.png')
