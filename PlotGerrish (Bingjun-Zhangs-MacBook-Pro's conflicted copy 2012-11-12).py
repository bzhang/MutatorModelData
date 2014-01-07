import os
import csv
import matplotlib.pylab as plt
from matplotlib.pyplot import *
from matplotlib.axes import *

data_path = '/Volumes/BigTwins/MutatorModelData/'
file_name = 'cat_0_default.out'
os.chdir(data_path)
file = csv.reader(open(file_name, 'rb'), delimiter=',', skipinitialspace=True)
fitness_data = []
mut_data     = []
n_gen = 0
for line in file:
    if line:
        n_gen += 1
        fitness_data.append(line[2])
        mut_data.append(line[3])
# file.close()

print 'Done reading.'

gen_counts = [i * 100 for i in range(1, n_gen + 1)]

fig = plt.figure(figsize=(10, 10))
ax1 = plt.subplot(111)

title('Fitness and Mutator Strength')
ax2 = ax1.twinx()
ax1.plot(gen_counts, fitness_data, 'b-')
ax1.set_yscale('log')
ax1.set_xlabel("Generation", fontsize=20)
ax1.set_ylabel("Fitness", fontsize=20)
ax2.plot(gen_counts, mut_data, 'r-')
ax2.set_ylabel("Mutator Strength", fontsize=20)
ax1.tick_params(axis='y', labelcolor='blue')
ax1.yaxis.label.set_color('blue')
ax2.tick_params(axis='y', labelcolor='red', color='red')
ax2.yaxis.label.set_color('red')
fig.savefig('Gerrish_0_default_log' + ".png")
