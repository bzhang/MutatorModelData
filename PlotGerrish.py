import os
import csv
import matplotlib.pylab as plt
from matplotlib.pyplot import *
from matplotlib.axes import *
import glob
from util import *

data_path = '/Volumes/BigTwins/MutatorModelData/mu_evol/'
os.chdir(data_path)
files = glob.glob("*.out")
n_gen = 600
fitness_pop          = map(list, [[]] * n_gen)
mutator_strength_pop = map(list, [[]] * n_gen)

for file_name in files:
    # print file_name
    file = csv.reader(open(file_name, 'rb'), delimiter=',', skipinitialspace=True)
    i = 0
    for line in file:
        i += 1
        if line:
            fitness_pop[i].append(line[2])
            mutator_strength_pop[i].append(line[3])

print 'Done reading.'

gen_counts = [i * 100 for i in range(0, n_gen)]

fitness_pop          = string_to_float(fitness_pop)
mutator_strength_pop = string_to_float(mutator_strength_pop)
fitness_mean, fitness_CI                   = list_mean_CI(fitness_pop)
mutator_strength_mean, mutator_strength_CI = list_mean_CI(mutator_strength_pop)

fig = plt.figure(figsize=(35, 10))

ax1 = plt.subplot(131)
title('Fitness and Mutator Strength')
ax2 = ax1.twinx()
ax1.plot(gen_counts, fitness_mean, 'b-')
ax1.set_yscale('log')
ax1.set_xlabel("Generation", fontsize=20)
ax1.set_ylabel("Fitness", fontsize=20)
ax2.plot(gen_counts, mutator_strength_mean, 'r-')
ax2.set_ylabel("Mutator Strength", fontsize=20)
ax1.tick_params(axis='y', labelcolor='blue')
ax1.yaxis.label.set_color('blue')
ax2.tick_params(axis='y', labelcolor='red', color='red')
ax2.yaxis.label.set_color('red')

plt.subplot(132)
errorbar(gen_counts, fitness_mean, fitness_CI, color='r', capsize=0, ecolor='gray')
yscale('log')
title('Mean Fitness')
xlabel('Generation', fontsize=20)
ylabel('Fitness', fontsize=20)

plt.subplot(133)
errorbar(gen_counts, mutator_strength_mean, mutator_strength_CI, fmt='r', ecolor='gray', capsize=0)
title('Mean Mutator Strength')
xlabel("Generation", fontsize=20)
ylabel("Mutator Strength", fontsize=20)

fig.savefig('Gerrish_0_default_log' + ".png")
