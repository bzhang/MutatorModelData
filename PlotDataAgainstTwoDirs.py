#! /usr/local/bin/python
__author__ = 'bingjun'
import os
import glob
import re
from matplotlib.pyplot import *
from matplotlib.axes import *
from util import *
import matplotlib.pylab as plt

data_path = "/Volumes/BigTwins/MutatorModelData/ScanMutEAntiMutE/"
os.chdir(data_path)
print os.getcwd()

dir1 = "M0.0_R0.0_G70000_N10000_BeneMR4.0E-4_DeleMR0.2_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE10.3_AntiMutE0.3_EvlFrom1_Period1000"
dir2 = "M0.0_R0.0_G50000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE10.3_AntiMutE0.3_EvlFrom1/1000pops"

fitness_mean_data  = map(list, [[]] * 2)
mut_rate_mean_data = map(list, [[]] * 2)
fitness_CI_data  = map(list, [[]] * 2)
mut_rate_CI_data  = map(list, [[]] * 2)
actual_mut_rate_mean_data = map(list, [[]] * 2)
actual_mut_rate_CI_data = map(list, [[]] * 2)

dir_counter = 0
for dir_name in [dir1, dir2]:
    os.chdir(dir_name)
    fitness_mean, fitness_CI, mutator_strength_mean, mutator_strength_CI, \
    n_dele_mean, n_dele_CI, n_bene_mean, n_bene_CI, \
    dele_fitness_effect_mean, dele_fitness_effect_ci, \
    bene_fitness_effect_mean, bene_fitness_effect_ci = restore_mean_CI()
    fitness_mean_data[dir_counter] = fitness_mean
    mut_rate_mean_data[dir_counter] = mutator_strength_mean
    fitness_CI_data[dir_counter] = fitness_CI
    mut_rate_CI_data[dir_counter] = mutator_strength_CI
    dir_counter += 1
    os.chdir("..")

# print fitness_mean_data
fitness_mean_data  = string_to_float(fitness_mean_data)
fitness_CI_data    = string_to_float(fitness_CI_data)
mut_rate_mean_data = string_to_float(mut_rate_mean_data)
mut_rate_CI_data   = string_to_float(mut_rate_CI_data)

# Add the first generation data for dir2 since it's missing that in the original data
fitness_mean_data[1].insert(0, 1)
mut_rate_mean_data[1].insert(0, 1)
fitness_CI_data[1].insert(0, 0)
mut_rate_CI_data[1].insert(0, 0)
# Convert to actual mutation rates by multiplying the starting dele_mut_rate
actual_mut_rate_mean_data[0] = [i * 0.2 for i in mut_rate_mean_data[0]]
actual_mut_rate_mean_data[1] = [i * 0.05 for i in mut_rate_mean_data[1]]
actual_mut_rate_CI_data[0] = [i * 0.2 for i in mut_rate_CI_data[0]]
actual_mut_rate_CI_data[1] = [i * 0.05 for i in mut_rate_CI_data[1]]

gen_counts = [i * 1000 for i in range(0, len(fitness_mean_data[1]))]

font_size = 20
label_size = 25

fig, ax = plt.subplots(figsize=(12, 10))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
matplotlib.rcParams.update({'font.size': font_size})
plt.subplot(111)
# fig = plt.figure(figsize=(25, 10))

# plt.subplot(121)

# errorbar(gen_counts, fitness_mean_data[0][0:len(gen_counts)], fitness_CI_data[0][0:len(gen_counts)], fmt='b', ecolor='gray', capsize=0, linewidth=3)
# errorbar(gen_counts, fitness_mean_data[1], fitness_CI_data[1], fmt='r', ecolor='gray', capsize=0, linewidth=3)
# # plot(gen_counts, fitness_mean_data[0][0:len(gen_counts)], 'b-')
# # plot(gen_counts, fitness_mean_data[1], 'r-')
# yscale('log')
# xlabel("Generations", fontsize=label_size)
# ylabel("Fitness", fontsize=label_size)

# plt.subplot(122)
errorbar(gen_counts, actual_mut_rate_mean_data[0][0:len(gen_counts)], actual_mut_rate_CI_data[0][0:len(gen_counts)], fmt='b', ecolor='gray', capsize=0, linewidth=3)
errorbar(gen_counts, actual_mut_rate_mean_data[1], actual_mut_rate_CI_data[1], fmt='r', ecolor='gray', capsize=0, linewidth=3)
# axhline(y=0.097, color='g', linewidth=3)
xlabel("Generations", fontsize=label_size)
ylabel("Genomic Mutation Rates", fontsize=label_size)

fig.savefig('MutR_Compare_Two_Starting_Mut_Rates.pdf')
