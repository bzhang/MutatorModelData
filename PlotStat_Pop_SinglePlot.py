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
os.chdir(data_path)
dirs = glob.glob("M0.0_R0.0_G50000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE10.3_AntiMutE0.3_EvlFrom1")
print(os.getcwd())
print(len(dirs))

nG_exp   = re.compile(r"_G(?P<nG>\d+)_")
mu_exp   = re.compile(r"DeleMR(?P<mu>[\d\.E-]+)_")
evol_exp = re.compile(r"StartEvol(?P<evol>\d+)_")

for dir_name in dirs:
    nG = nG_exp.search(dir_name)
    mu = mu_exp.search(dir_name)
    base_mu = float(mu.group('mu'))
    n_gen = 70001
    period = 1
    gen_counts = [i * period for i in range(0, n_gen)]
    print 'n_gen = ', n_gen
    os.chdir(dir_name)
    # os.chdir("1000pops")
    print os.getcwd()
    fitness_mean, fitness_CI, mutator_strength_mean, mutator_strength_CI, \
    n_dele_mean, n_dele_CI, n_bene_mean, n_bene_CI, \
    dele_fitness_effect_mean, dele_fitness_effect_ci, \
    bene_fitness_effect_mean, bene_fitness_effect_ci = restore_mean_CI()
    print 'fitness_mean = ', len(fitness_mean)

    font_size = 30
    label_size = 35

    fig, ax = plt.subplots(figsize=(14, 10))
    matplotlib.rcParams.update({'font.size': font_size})
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    print 'gen_counts = ', len(gen_counts)
    errorbar(gen_counts, fitness_mean, fitness_CI, color='r', capsize=0, ecolor='gray', linewidth=3)
    yscale('log')
    xlabel('Generations', fontsize=label_size)
    ylabel('Fitness', fontsize=label_size)
    fig.savefig("Fitness_" + dir_name + ".png")

    fig, ax = plt.subplots(figsize=(14, 10))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    errorbar(gen_counts, mutator_strength_mean, mutator_strength_CI, fmt='r', ecolor='gray', capsize=0, linewidth=3)
    xlabel("Generations", fontsize=label_size)
    ylabel("Genomic Deleterious Mutation Rate", fontsize=label_size)
    fig.savefig("DelMR_" + dir_name + ".png") 

    fig, ax = plt.subplots(figsize=(14, 10))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    errorbar(gen_counts, n_dele_mean, n_dele_CI, fmt='r', ecolor='gray', capsize=0, linewidth=3)
    # title('Mean # of Deleterious Mutations/Individual')
    xlabel("Generations", fontsize=label_size)
    ylabel("# of Deleterious mutations", fontsize=label_size)
    fig.savefig("DelNum_" + dir_name + ".png")

    fig, ax = plt.subplots(figsize=(14, 10))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    errorbar(gen_counts, n_bene_mean, n_bene_CI, fmt='r', ecolor='gray', capsize=0, linewidth=3)
    xlabel("Generations", fontsize=label_size)
    ylabel("# of Beneficial mutations", fontsize=label_size)


    fig, ax1 = plt.subplots(figsize=(14, 10))
    ax1.spines['top'].set_visible(False)
    ax1.xaxis.set_ticks_position('bottom')
    ax1.yaxis.set_ticks_position('left')   
    ax2 = ax1.twinx()
    ax1.errorbar(gen_counts, mutator_strength_mean, mutator_strength_CI, color='b', capsize=0, ecolor='0.85', linewidth=3)
    ax1.set_xlabel("Generations", fontsize=label_size)
    ax1.set_ylabel("Deleterious Mutation Rate", fontsize=label_size)
    ax2.errorbar(gen_counts, fitness_mean, fitness_CI, fmt='r', ecolor='0.75', capsize=0, linewidth=3)    
    ax2.set_yscale('log')
    ax2.set_ylabel("Fitness", fontsize=label_size)
    xlim(0, 50000)
    # Change the axis colors...
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.yaxis.label.set_color('blue')
    ax2.tick_params(axis='y', labelcolor='red', color='red')
    ax2.yaxis.label.set_color('red')
    fig.savefig("FitnessMut_" + dir_name + ".png")

    fig, ax = plt.subplots(figsize=(14, 10))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    errorbar(gen_counts, dele_fitness_effect_mean, dele_fitness_effect_ci, \
            fmt='r', ecolor='gray', capsize=0, linewidth=3)
    xlabel("Generations", fontsize=label_size)
    ylabel("Mean Deleterious Fitness Effect", fontsize=label_size)
    fig.savefig("DelFitnessEffect_" + dir_name + ".png")

    fig, ax = plt.subplots(figsize=(14, 10))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    errorbar(gen_counts, bene_fitness_effect_mean, bene_fitness_effect_ci, \
            fmt='r', ecolor='gray', capsize=0, linewidth=3)
    xlabel("Generations", fontsize=label_size)
    ylabel("Mean Beneficial Fitness Effect", fontsize=label_size)
    fig.savefig("BeneFitnessEffect_" + dir_name + ".png")

    os.chdir(data_path)