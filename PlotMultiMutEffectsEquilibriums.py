#! /usr/local/bin/python
__author__ = 'bingjun'
import os
from matplotlib.pyplot import *
from matplotlib.axes import *
from util import *
import matplotlib.pylab as plt

data_path = "/Volumes/BigTwins/MutatorModelData/ScanMutEAntiMutE/"
os.chdir(data_path)
print os.getcwd()
dir0 = "M0.0_R0.0_G70000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE10.15_AntiMutE0.15_EvlFrom1_Period1000"
dir1 = "M0.0_R0.0_G60000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE10.2_AntiMutE0.2_EvlFrom1"
dir2 = "M0.0_R0.0_G50000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE10.3_AntiMutE0.3_EvlFrom1/1000pops"
dir3 = "M0.0_R0.0_G70000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE10.4_AntiMutE0.4_EvlFrom1_Period1000"
dir4 = "M0.0_R0.0_G70000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE10.5_AntiMutE0.5_EvlFrom1_Period1000"



# fitness_mean_data  = map(list, [[]] * 9)
mut_rate_mean_data = map(list, [[]] * 9)
# fitness_CI_data    = map(list, [[]] * 5)
# mut_rate_CI_data   = map(list, [[]] * 5)

dir_counter = 0
for dir_name in [dir0, dir1, dir2, dir3, dir4]:
    os.chdir(dir_name)
    fitness_mean, fitness_CI, mutator_strength_mean, mutator_strength_CI, \
    n_dele_mean, n_dele_CI, n_bene_mean, n_bene_CI, \
    dele_fitness_effect_mean, dele_fitness_effect_ci, \
    bene_fitness_effect_mean, bene_fitness_effect_ci = restore_mean_CI()
    # fitness_mean_data[dir_counter] = fitness_mean
    mutator_strength_mean.insert(0, 0.05)
    mut_rate_mean_data[dir_counter] = mutator_strength_mean
    # fitness_CI_data[dir_counter].append(fitness_CI)
    # mut_rate_CI_data[dir_counter].append(mutator_strength_CI)
    dir_counter += 1
    os.chdir(data_path)

# print fitness_mean_data
# fitness_mean_data = string_to_float(fitness_mean_data)
# fitness_CI_data    = string_to_float(fitness_CI_data)
mut_rate_mean_data = string_to_float(mut_rate_mean_data)
# mut_rate_CI_data   = string_to_float(mut_rate_CI_data)

# fitness_temp = []
# mut_temp = []
# for i in range(0, (len(mut_rate_mean_data[2])/1000)):
#     j = i * 1000
#     # fitness_temp.append(fitness_mean_data[3][j])
#     mut_temp.append(mut_rate_mean_data[2][j])
# # fitness_mean_data[2] = fitness_temp
# mut_rate_mean_data[2] = mut_temp

# mut_rate_mean_data_new = [[x * 0.05 for x in y] for y in mut_rate_mean_data]

font_size = 20
label_size = 25

fig, ax = plt.subplots(figsize=(12, 10))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
matplotlib.rcParams.update({'font.size': font_size})

plt.subplot(1, 1, 1)
for index in range(0, 4):
    gen_counts = [i * 1000 for i in range(0, 50)]
    plot(gen_counts, mut_rate_mean_data[index][0:50], linewidth=3)
xlabel("Generations", fontsize=label_size)
ylabel("Genomic Deleterious Mutation Rates", fontsize=label_size)
# title('Relative Mutation Rates for Various Mutator Effects')

lg = legend(["0.15", "0.2", "0.3", "0.4", "0.5"], loc=2)
lg.draw_frame(False)
fig.savefig('Mutator_Effects_015_05_equilibriums.png')
