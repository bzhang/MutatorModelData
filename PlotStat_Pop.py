__author__ = 'bingjun'
#! /usr/local/bin/python
import os
import glob
import re
from matplotlib.pyplot import *
from matplotlib.axes import *
from util import *
import matplotlib.pylab as plt

data_path = "/Volumes/BigTwins/MutatorModelData/ScanMutEAntiMutE/"
#output_path = "/Volumes/BigTwins/Dropbox/MutatorModel/Results/"
#data_path = "/Volumes/BigTwins/Project/mutator-model/out/"
#data_path = "/Volumes/BigTwins/Project/mutator-model/out/"
# data_path = "/Users/bingjun/Documents/MutatorModel/"
# output_path = "/Users/bingjun/Dropbox/MutatorModel/Results/"
os.chdir(data_path)
dirs = glob.glob("M0.0_R0.0_G50000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE10.3_AntiMutE0.3_EvlFrom1")
# dirs = glob.glob("MutCount_M0.0_R0.0_G5000_N500_BeneMR1.0E-4_DeleMR0.01_BeneE1.01_DeleE0.99_MutStr2_InitMutaMR0.0_EvolMutaMR0.01_StartEvol2500_Prob2M0.5_MutaE2")
# MutCount_M0.0_R1.0_G5000_N500_BeneMR1.0E-4_DeleMR0.01_BeneE1.01_DeleE0.99_MutStr2_MutaMR0.01_Prob2M0.5_MutaE2
# dirs=glob.glob("MutCount*_R0.0_*_MutaMR0.0_*")
print(os.getcwd())
print(len(dirs))

nG_exp   = re.compile(r"_G(?P<nG>\d+)_")
mu_exp   = re.compile(r"DeleMR(?P<mu>[\d\.E-]+)_")
evol_exp = re.compile(r"StartEvol(?P<evol>\d+)_")

for dir_name in dirs:
    nG = nG_exp.search(dir_name)
    mu = mu_exp.search(dir_name)
    base_mu = float(mu.group('mu'))
    # n_gen = int(nG.group('nG'))
    n_gen = 70001
    period = 1
    gen_counts = [i * period for i in range(0, n_gen)]
#    print(base_mu)
    print 'n_gen = ', n_gen
#   if evol_exp.search(dir_name):
#       evol = evol_exp.search(dir_name)
#       start = int(evol.group('evol'))
#   else:
#       start = 1
    os.chdir(dir_name)
    # os.chdir("1000pops")

    # fitness_mean, fitness_CI, mutator_strength_mean, mutator_strength_CI, \
    # n_dele_mean, n_dele_CI, n_bene_mean, n_bene_CI, \
    # n_mutator_mean, n_mutator_CI, n_antimut_mean, n_antimut_CI = restore_python_mean_CI()
# , pop_size_mean, pop_size_CI
#    fitness_mean, mutator_strength_mean, n_dele_mean, n_bene_mean = restore_mean()
    print os.getcwd()
    fitness_mean, fitness_CI, mutator_strength_mean, mutator_strength_CI, \
    n_dele_mean, n_dele_CI, n_bene_mean, n_bene_CI, \
    dele_fitness_effect_mean, dele_fitness_effect_ci, \
    bene_fitness_effect_mean, bene_fitness_effect_ci = restore_mean_CI()
    # mutator_strength_mean = [i * base_mu for i in mutator_strength_mean]

#   fitness_mean[4000:] = []
#   fitness_CI[4000:] = []
#   mutator_strength_mean[4000:] = []
#   mutator_strength_CI[4000:] = []
#   n_dele_mean[4000:] = []
#   n_dele_CI[4000:] = []
#   n_bene_mean[4000:] = []
#   n_bene_CI[4000:] = []
    # os.chdir("..")
    print 'fitness_mean = ', len(fitness_mean)

    # fig = plt.figure(figsize=(47, 20))
    # fig = plt.figure(figsize=(120, 18))
    # fig = plt.subplots(nrows=2, ncols=4)
    # plt.tight_layout()

    font_size = 30
    label_size = 35

    fig = plt.figure(1, figsize=(8.6, 4))
    ax1 = fig.add_axes([0.09, 0.16, 0.37, 0.8])
    ax2 = fig.add_axes([0.61, 0.16, 0.37, 0.8])
    # fig = plt.figure(figsize=(48, 20))
    # fig, ax = plt.subplots(figsize=(12, 10))
    set_up_axes()
    # fitness_mean.insert(0, 1)
    # fitness_CI.insert(0, 0)
    print 'gen_counts = ', len(gen_counts)
    errorbar(gen_counts, fitness_mean, fitness_CI, color='r', capsize=0, ecolor='gray', linewidth=3)
    yscale('log')
    xlabel('Generations', fontsize=label_size)
    ylabel('Fitness', fontsize=label_size)
    # plt.ylim([1, 10e15])
#   axvline(x=start,color='g')

    ax = plt.subplot(242)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
#     mutator_strength_mean.insert(0, 1)
#     mutator_strength_CI.insert(0, 0)
#     mutator_strength_mean = [x * 0.05 for x in mutator_strength_mean]
#     mutator_strength_CI = [x * 0.05 for x in mutator_strength_CI]

    errorbar(gen_counts, mutator_strength_mean, mutator_strength_CI, fmt='r', ecolor='gray', capsize=0, linewidth=3)
#    yscale('log',basey=2)
#    yscale('log')
    xlabel("Generations", fontsize=label_size)
    ylabel("Genomic Deleterious Mutation Rate", fontsize=label_size)
#     plt.ylim([0.04, 0.22])
# #   axvline(x=start,color='g')

    ax = plt.subplot(243)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    errorbar(gen_counts, n_dele_mean, n_dele_CI, fmt='r', ecolor='gray', capsize=0, linewidth=3)
    # title('Mean # of Deleterious Mutations/Individual')
    xlabel("Generations", fontsize=label_size)
    ylabel("# of Deleterious mutations", fontsize=label_size)
# #    pylab.ylim([0,25])
# #   axvline(x=start,color='g')

    ax = plt.subplot(244)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    errorbar(gen_counts, n_bene_mean, n_bene_CI, fmt='r', ecolor='gray', capsize=0, linewidth=3)
    # title('Mean # of Beneficial Mutations/Individual')
    xlabel("Generations", fontsize=label_size)
    ylabel("# of Beneficial mutations", fontsize=label_size)
# #    pylab.ylim([0,25])
# #   axvline(x=start,color='g')

#     # Uncomment for python code
#     # plt.subplot(245)
#     # errorbar(gen_counts,n_mutator_mean,n_mutator_CI,fmt='r',ecolor='gray',capsize=0)
#     # title('Mean # of Mutator/Individual')
#     # xlabel("60k Generations", fontsize=20)
#     # ylabel("# of Mutator", fontsize=20)

#     # plt.subplot(246)
#     # errorbar(gen_counts,n_antimut_mean,n_antimut_CI,fmt='r',ecolor='gray',capsize=0)
#     # title('Mean # of Anti-mutator/Individual')
#     # xlabel("60 Generations", fontsize=20)
#     # ylabel("# of Anti-mutator", fontsize=20)
# #
# #   plt.subplot(337)
# #   errorbar(range(0,n_gen),pop_size_mean,pop_size_CI,fmt='r',ecolor='gray',capsize=0)
# #   title('Mean Population Size')
# #   xlabel("Generation", fontsize=20)
# #   ylabel("Population Size", fontsize=20)
# #   plt.ylim(950,1050)

# #   ax1 = plt.subplot(338)
    ax1 = plt.subplot(247)
    # ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.xaxis.set_ticks_position('bottom')
    ax1.yaxis.set_ticks_position('left')   
    # title('Fitness and Relative Mutation Rate')
    ax2 = ax1.twinx()
    # ax1.plot(gen_counts, fitness_mean, 'b-', linewidth=3)
    ax1.errorbar(gen_counts, mutator_strength_mean, mutator_strength_CI, color='b', capsize=0, ecolor='0.85', linewidth=3)
#     # title("93 Populations")
    
#     #    ylim(0.9,1.02) # StartEvol2500/3500
#     #    ax1.set_yticks([0.975,0.990,1.005,1.020,1.035])
#     # ylim(0.990,1.006) # StartEvol1
#     # ax1.set_yticks([0.990,0.994,0.998,1.002,1.006])
    ax1.set_xlabel("Generations", fontsize=label_size)
    ax1.set_ylabel("Deleterious Mutation Rate", fontsize=label_size)
    # ax2.plot(gen_counts, mutator_strength_mean, 'r-', linewidth=3)
    ax2.errorbar(gen_counts, fitness_mean, fitness_CI, fmt='r', ecolor='0.75', capsize=0, linewidth=3)    
#     #    ax2.set_yscale('log',basey=2)
    ax2.set_yscale('log')
    ax2.set_ylabel("Fitness", fontsize=label_size)
    xlim(0, 50000)
#     #    ylim(2**-22,2**1)
#     #    ax2.set_yticks([2**-16,2**-12,2**-8,2**-4,2**0])
#     # ylim(2**-16,2**1) # StartEvol1
#     # ax2.set_yticks([2**-16,2**-12,2**-8,2**-4,2**0])
#     # ax2.set_yticklabels([2**-16,2**-12,2**-8,2**-4,2**0])
#     # ylim([2^-16,2^1])
#     # ax2.set_yticks([2^-16,2^-12,2^-8,2^-4,2^1])
#     # ax2.set_yticklabels([2^-16,2^-12,2^-8,2^-4,2^1])
#     # pylab.yticks(arrange(4))

#     # ax2.yaxis.tick_right()
    # Change the axis colors...
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.yaxis.label.set_color('blue')
    ax2.tick_params(axis='y', labelcolor='red', color='red')
    ax2.yaxis.label.set_color('red')
#     #   axvline(x=start,color='g')
#     # title("Asexual Populations")

    ax = plt.subplot(245)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    errorbar(gen_counts, dele_fitness_effect_mean, dele_fitness_effect_ci, \
            fmt='r', ecolor='gray', capsize=0, linewidth=3)
    # title('Mean Deleterious Fitness Effect/Individual')
    xlabel("Generations", fontsize=label_size)
    ylabel("Mean Deleterious Fitness Effect", fontsize=label_size)

    ax = plt.subplot(246)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    errorbar(gen_counts, bene_fitness_effect_mean, bene_fitness_effect_ci, \
            fmt='r', ecolor='gray', capsize=0, linewidth=3)
    # title('Mean Beneficial Fitness Effect/Individual')
    xlabel("Generations", fontsize=label_size)
    ylabel("Mean Beneficial Fitness Effect", fontsize=label_size)

#     # fig.savefig("log" + dir_name + ".png")
    fig.savefig(dir_name + ".png")
    # fig.savefig("Fitness_" + dir_name + ".pdf")
# , bbox_inches='tight' # add into savefig() to remove margin outside plots
#     fig = figure(figsize=(10,8))
#     matplotlib.rcParams.update({'font.size': 18})
#     plot(range(1,n_gen+1),fitness_mean,color='r')
#     # yscale('log')
#     title("DeleMu = " + str(base_mu))
#     xlabel("Generation", fontsize=20)
#     ylabel("Fitness", fontsize=20)
#     axvline(x=start,color='g')
# #    fig.savefig("fitness_" + dir_name + ".png")
#     fig.savefig("fitness_mean_" + dir_name + ".png")
#
#     fig = figure(figsize=(10,8))
#     matplotlib.rcParams.update({'font.size': 18})
#     plot(range(1,n_gen+1),mutator_strength_mean,color='r')
# #    yscale('log',basey=2)
# #    yscale('log')
#     # title("Asexual Populations")
#     # title("DeleMu = " + str(base_mu))
#     xlabel("Generation", fontsize=20)
#     ylabel("Mutator Strength", fontsize=20)
#     axvline(x=start,color='g')
# #    fig.savefig("Log2_Mut_" + dir_name + ".png")
#     fig.savefig("Mut_mean_" + dir_name + ".png")

#     fig = figure(figsize=(10,8))
#     matplotlib.rcParams.update({'font.size': 18})
#     plot(range(1,n_gen+1),n_dele_mean,color='r')
#     title("1000_300649921759_Dele")
#     # title("DeleMu = " + str(base_mu))
#     # title("Asexual Populations")
#     xlabel("Generation", fontsize=20)
#     ylabel("# of Deleterious mutations", fontsize=20)
# #    pylab.ylim([0,25])
#     axvline(x=start,color='g')
# #    fig.savefig("Dele_" + dir_name + ".png")
#     fig.savefig("1000_300649921759_Dele_mean_" + dir_name + ".png")
# 
#     fig = figure(figsize=(10,8))
#     matplotlib.rcParams.update({'font.size': 18})
#     plot(range(1,n_gen+1),n_bene_mean,color='r')
#     title("1000_300649921759_Bene")
#     # title("Asexual Populations")
#     # title("DeleMu = " + str(base_mu))
#     xlabel("Generation", fontsize=20)
#     ylabel("# of Beneficial mutations", fontsize=20)
# #    pylab.ylim([0,25])
#     axvline(x=start,color='g')
# #    fig.savefig("Bene_" + dir_name + ".png")
#     fig.savefig("1000_300649921759_Bene_mean_" + dir_name + ".png")


    os.chdir("..")