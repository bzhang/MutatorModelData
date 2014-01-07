#! /usr/local/bin/python
__author__ = 'bingjun'
import os
import glob
import re
from matplotlib.pyplot import *
from matplotlib.axes import *
from util import *
import matplotlib.pylab as plt

data_path = "/Volumes/BigTwins/MutatorModelData/"
os.chdir(data_path)
print os.getcwd()
dir1 = "M0.0_R0.0_G50000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE0.3_AntiMutE0.3_EvlFrom1"
dir2 = "M0.0_R0.0_G70000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE0.2_AntiMutE0.2_EvlFrom1_Period1000"
dir3 = "M0.0_R0.0_G60000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE0.1_AntiMutE0.1_EvlFrom1"
dir4 = "M0.0_R0.0_G60000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE0.05_AntiMutE0.05_EvlFrom1"
dir5 = "M0.0_R0.0_G600000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE0.01_AntiMutE0.01_EvlFrom1_Period1000"
dir6 = "M0.0_R0.0_G70000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE0.4_AntiMutE0.4_EvlFrom1_Period1000"
dir7 = "M0.0_R0.0_G70000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE0.5_AntiMutE0.5_EvlFrom1_Period1000"
dir8 = "M0.0_R0.0_G70000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE0.15_AntiMutE0.15_EvlFrom1_Period1000"
dir9 = "M0.0_R0.0_G60000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE0.01_AntiMutE0.01_EvlFrom1"

fitness_mean_data  = map(list, [[]] * 9)
mut_rate_mean_data = map(list, [[]] * 9)
# fitness_CI_data    = map(list, [[]] * 5)
# mut_rate_CI_data   = map(list, [[]] * 5)

dir_counter = 0
for dir_name in [dir1, dir2, dir3, dir4, dir5, dir6, dir7, dir8]:
	os.chdir(dir_name)
	fitness_mean, fitness_CI, mutator_strength_mean, mutator_strength_CI, \
    n_dele_mean, n_dele_CI, n_bene_mean, n_bene_CI, \
    dele_fitness_effect_mean, dele_fitness_effect_ci, \
    bene_fitness_effect_mean, bene_fitness_effect_ci = restore_mean_CI()
	fitness_mean_data[dir_counter] = fitness_mean
	mut_rate_mean_data[dir_counter] = mutator_strength_mean
	# fitness_CI_data[dir_counter].append(fitness_CI)
	# mut_rate_CI_data[dir_counter].append(mutator_strength_CI)
	dir_counter += 1
	os.chdir("..")

# print fitness_mean_data
fitness_mean_data  = string_to_float(fitness_mean_data)
# fitness_CI_data    = string_to_float(fitness_CI_data)
mut_rate_mean_data = string_to_float(mut_rate_mean_data)
# mut_rate_CI_data   = string_to_float(mut_rate_CI_data)

fitness_temp = []
mut_temp = []
for i in range(0, (len(fitness_mean_data[3])/10)):
	j = i * 10
 	fitness_temp.append(fitness_mean_data[3][j])
	mut_temp.append (mut_rate_mean_data[3][j])
fitness_mean_data[3] = fitness_temp
mut_rate_mean_data[3] = mut_temp


fig = plt.figure(figsize=(45, 30))
matplotlib.rcParams.update({'font.size': 18})
gen_counts = [i * 1000 for i in range(0, len(fitness_mean_data[0]))]
ax1 = plt.subplot(343)
ax2 = ax1.twinx()
ax1.plot(gen_counts, fitness_mean_data[0], 'b-')
ax1.set_yscale('log')
ax1.set_xlabel("Generations", fontsize=20)
ax1.set_ylabel("Fitness", fontsize=20)
ax2.plot(gen_counts, mut_rate_mean_data[0], 'r-')
ax2.set_ylabel("Relative Mutation Rate", fontsize=20)
ax1.tick_params(axis='y', labelcolor='blue')
ax1.yaxis.label.set_color('blue')
ax2.tick_params(axis='y', labelcolor='red', color='red')
ax2.yaxis.label.set_color('red')
title('Mean Mutator Effect = 0.3')

gen_counts = [i * 1000 for i in range(0, len(fitness_mean_data[1]))]
ax1 = plt.subplot(344)
ax2 = ax1.twinx()
ax1.plot(gen_counts, fitness_mean_data[1], 'b-')
ax1.set_yscale('log')
# ax1.xlim((0, 60000))
ax1.set_xlabel("Generations", fontsize=20)
ax1.set_ylabel("Fitness", fontsize=20)
ax2.plot(gen_counts, mut_rate_mean_data[1], 'r-')
ax2.set_ylabel("Relative Mutation Rate", fontsize=20)
ax1.tick_params(axis='y', labelcolor='blue')
ax1.yaxis.label.set_color('blue')
ax2.tick_params(axis='y', labelcolor='red', color='red')
ax2.yaxis.label.set_color('red')
title('Mean Mutator Effect = 0.2')

gen_counts = [i * 1000 for i in range(0, len(fitness_mean_data[2]))]
ax1 = plt.subplot(346)
ax2 = ax1.twinx()
ax1.plot(gen_counts, fitness_mean_data[2], 'b-')
ax1.set_yscale('log')
ax1.set_xlabel("Generations", fontsize=20)
ax1.set_ylabel("Fitness", fontsize=20)
ax2.plot(gen_counts, mut_rate_mean_data[2], 'r-')
ax2.set_ylabel("Relative Mutation Rate", fontsize=20)
ax1.tick_params(axis='y', labelcolor='blue')
ax1.yaxis.label.set_color('blue')
ax2.tick_params(axis='y', labelcolor='red', color='red')
ax2.yaxis.label.set_color('red')
title('Mean Mutator Effect = 0.1')

gen_counts = [i * 1000 for i in range(0, len(fitness_mean_data[7]))]
ax1 = plt.subplot(345)
ax2 = ax1.twinx()
ax1.plot(gen_counts, fitness_mean_data[7], 'b-')
ax1.set_yscale('log')
ax1.set_xlabel("Generations", fontsize=20)
ax1.set_ylabel("Fitness", fontsize=20)
ax2.plot(gen_counts, mut_rate_mean_data[7], 'r-')
ax2.set_ylabel("Relative Mutation Rate", fontsize=20)
ax1.tick_params(axis='y', labelcolor='blue')
ax1.yaxis.label.set_color('blue')
ax2.tick_params(axis='y', labelcolor='red', color='red')
ax2.yaxis.label.set_color('red')
title('Mean Mutator Effect = 0.15')

gen_counts = [i * 1000 for i in range(0, len(fitness_mean_data[3]))]
ax1 = plt.subplot(347)
ax2 = ax1.twinx()
ax1.plot(gen_counts, fitness_mean_data[3], 'b-')
ax1.set_yscale('log')
ax1.set_xlabel("Generations", fontsize=20)
ax1.set_ylabel("Fitness", fontsize=20)
ax2.plot(gen_counts, mut_rate_mean_data[3], 'r-')
ax2.set_ylabel("Relative Mutation Rate", fontsize=20)
ax1.tick_params(axis='y', labelcolor='blue')
ax1.yaxis.label.set_color('blue')
ax2.tick_params(axis='y', labelcolor='red', color='red')
ax2.yaxis.label.set_color('red')
title('Mean Mutator Effect = 0.05')

gen_counts = [i * 1000 for i in range(0, len(fitness_mean_data[4]))]
ax1 = plt.subplot(348)
ax2 = ax1.twinx()
ax1.plot(gen_counts, fitness_mean_data[4], 'b-')
ax1.set_yscale('log')
ax1.set_xlabel("Generations", fontsize=20)
ax1.set_ylabel("Fitness", fontsize=20)
ax2.plot(gen_counts, mut_rate_mean_data[4], 'r-')
ax2.set_ylabel("Relative Mutation Rate", fontsize=20)
ax1.tick_params(axis='y', labelcolor='blue')
ax1.yaxis.label.set_color('blue')
ax2.tick_params(axis='y', labelcolor='red', color='red')
ax2.yaxis.label.set_color('red')
title('Mean Mutator Effect = 0.01')

gen_counts = [i * 1000 for i in range(0, len(fitness_mean_data[5]))]
ax1 = plt.subplot(342)
ax2 = ax1.twinx()
ax1.plot(gen_counts, fitness_mean_data[5], 'b-')
ax1.set_yscale('log')
ax1.set_xlabel("Generations", fontsize=20)
ax1.set_ylabel("Fitness", fontsize=20)
ax2.plot(gen_counts, mut_rate_mean_data[5], 'r-')
ax2.set_ylabel("Relative Mutation Rate", fontsize=20)
ax1.tick_params(axis='y', labelcolor='blue')
ax1.yaxis.label.set_color('blue')
ax2.tick_params(axis='y', labelcolor='red', color='red')
ax2.yaxis.label.set_color('red')
title('Mean Mutator Effect = 0.4')

gen_counts = [i * 1000 for i in range(0, len(fitness_mean_data[6]))]
ax1 = plt.subplot(341)
ax2 = ax1.twinx()
ax1.plot(gen_counts, fitness_mean_data[6], 'b-')
ax1.set_yscale('log')
ax1.set_xlabel("Generations", fontsize=20)
ax1.set_ylabel("Fitness", fontsize=20)
ax2.plot(gen_counts, mut_rate_mean_data[6], 'r-')
ax2.set_ylabel("Relative Mutation Rate", fontsize=20)
ax1.tick_params(axis='y', labelcolor='blue')
ax1.yaxis.label.set_color('blue')
ax2.tick_params(axis='y', labelcolor='red', color='red')
ax2.yaxis.label.set_color('red')
title('Mean Mutator Effect = 0.5')

plt.subplot(349)
for index in range(0, 8):
	gen_counts = [i * 1000 for i in range(0, len(fitness_mean_data[index]))]
	plot(gen_counts, fitness_mean_data[index])
	yscale('log')
xlabel("Generations", fontsize=20)
ylabel("Fitness", fontsize=20)
title('Fitness for Various Mutator Effects')
legend(["0.3", "0.2", "0.1", "0.05", "0.4", "0.5", "0.15", "0.01"], loc=2)

plt.subplot(3, 4, 10)
for index in [0, 1, 2, 3, 5, 6, 7, 8]:
	gen_counts = [i * 1000 for i in range(0, len(fitness_mean_data[index]))]
	plot(gen_counts, fitness_mean_data[index])
	yscale('log')
xlabel("Generations", fontsize=20)
ylabel("Fitness", fontsize=20)
title('Fitness for Various Mutator Effects')
legend(["0.3", "0.2", "0.1", "0.05", "0.01", "0.4", "0.5", "0.15"], loc=2)

plt.subplot(3, 4, 11)
for index in range(0, 8):
	gen_counts = [i * 1000 for i in range(0, len(mut_rate_mean_data[index]))]
	plot(gen_counts, mut_rate_mean_data[index])
xlabel("Generations", fontsize=20)
ylabel("Relative Mutation Rates", fontsize=20)
title('Relative Mutation Rates for Various Mutator Effects')
legend(["0.3", "0.2", "0.1", "0.05", "0.01", "0.4", "0.5", "0.15"], loc=2)

plt.subplot(3, 4, 12)
for index in [0, 1, 2, 3, 5, 6, 7, 8]: 
	gen_counts = [i * 1000 for i in range(0, len(mut_rate_mean_data[index]))]
	plot(gen_counts, mut_rate_mean_data[index])
xlabel("Generations", fontsize=20)
ylabel("Relative Mutation Rates", fontsize=20)
title('Relative Mutation Rates for Various Mutator Effects')
legend(["0.3", "0.2", "0.1", "0.05", "0.4", "0.5", "0.15", "0.01"], loc=2)

fig.savefig('Mutator_Effects_11.png')
