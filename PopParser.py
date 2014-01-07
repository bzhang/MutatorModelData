import glob
import os
import re
from matplotlib.pyplot import figure, ylabel, xlabel, title, plot, yscale
from util import *
import matplotlib.pylab as plt
from matplotlib_2_ggplot import *

__author__ = 'bingjun'

data_path = "/Volumes/BigTwins/MutatorModelData/ScanMutEAntiMutE/"
#data_path = "/Users/bingjun/Documents/MutatorModel/"
os.chdir(data_path)
dirs = glob.glob("M0.0_R0.0_G60000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE10.05_AntiMutE0.05_EvlFrom1")
print(os.getcwd())
print(len(dirs))

nG_exp   = re.compile(r"_G(?P<nG>\d+)_")
mu_exp   = re.compile(r"DeleMR(?P<mu>[\d\.E-]+)_")
evol_exp = re.compile(r"StartEvol(?P<evol>\d+)_")

for dir_name in dirs:
    os.chdir(dir_name)
    print(dir_name)
    nG = nG_exp.search(dir_name)
    # n_gen = int(nG.group('nG'))
    mu = mu_exp.search(dir_name)
    base_mu = float(mu.group('mu'))
    n_gen = 70001
    period = 1
    print(n_gen)
    gen_counts = [i * period for i in range(0, n_gen)]
    # print gen_counts
    # gen_counts = range(0,n_gen)    

    files               = glob.glob("*_Pop.txt")
    typical_pop = "7363326780440510_Pop.txt"

    n_pop               = len(files)
    fitness             = map(list, [[]] * n_pop)
    mut_rate            = map(list, [[]] * n_pop)
    n_dele              = map(list, [[]] * n_pop)
    n_bene              = map(list, [[]] * n_pop)
    dele_fitness_effect = map(list, [[]] * n_pop)
    bene_fitness_effect = map(list, [[]] * n_pop)

    # n_mutator   = map(list, [[]] * n_pop)
    # n_antimut   = map(list, [[]] * n_pop)
    # pop_size    = map(list, [[]] * n_pop)
    pop_counter = 0
    for file_name in files:
        print(file_name)
        file = csv.reader(open(file_name, 'rb'), delimiter="\t", skipinitialspace=True)
        file.next()
        for line in file:
            if line:
                fitness[pop_counter].append(line[1])
                mut_rate[pop_counter].append(float(line[2]) * base_mu)
                n_dele[pop_counter].append(line[3])
                n_bene[pop_counter].append(line[4])
                dele_fitness_effect[pop_counter].append(line[5])
                bene_fitness_effect[pop_counter].append(line[6])
        if pop_counter >= 30: 
            break
        pop_counter = pop_counter + 1

    typical_fitness = []
    typical_mut_rate = []
    typical_file = csv.reader(open(file_name, 'rb'), delimiter="\t", skipinitialspace=True)
    typical_file.next()
    for line in typical_file:
        if line:
            typical_fitness.append(line[1])
            typical_mut_rate.append(float(line[2]) * base_mu)
#    print(fitness)
    fitness             = string_to_float(fitness)
    mut_rate            = string_to_float(mut_rate)
    n_dele              = string_to_float(n_dele)
    n_bene              = string_to_float(n_bene)
    dele_fitness_effect = string_to_float(dele_fitness_effect)
    bene_fitness_effect = string_to_float(bene_fitness_effect)

    # Uncomment below for python code
    # n_mutator = string_to_float(n_mutator)
    # n_antimut = string_to_float(n_antimut)
#   pop_size = string_to_float(pop_size)

    font_size = 30
    label_size = 35

    # fig = plt.figure(figsize=(48, 20))    
    fig, ax = plt.subplots(figsize=(10, 10))
    # ax.yaxis.set_ticks_position('right')
    matplotlib.rcParams.update({'font.size': font_size})

    # ax1 = plt.subplot(241)
    # # ax1.spines['right'].set_visible(False)
    # ax1.spines['top'].set_visible(False)
    # ax1.xaxis.set_ticks_position('bottom')
    # ax1.yaxis.set_ticks_position('left')
    # ax2 = ax1.twinx()
    # print "len(fitness[pop_counter-1]) = ", len(fitness[pop_counter-1])
    # ax1.plot(range(0, len(fitness[pop_counter - 1])), fitness[pop_counter - 1], 'b-', linewidth=3)
    # ax1.set_yscale('log')
    # ax1.set_xlabel("Generations", fontsize=25)
    # ax1.set_ylabel("Fitness", fontsize=25)
    # ax2.plot(range(0, len(fitness[pop_counter - 1])), mut_rate[pop_counter - 1], 'r-', linewidth=3)
    # ax2.set_ylabel("Relative Mutation Rate", fontsize=font_size)
    # # Change the axis colors...
    # ax1.tick_params(axis='y', labelcolor='blue')
    # ax1.yaxis.label.set_color('blue')
    # ax2.tick_params(axis='y', labelcolor='red', color='red')
    # ax2.yaxis.label.set_color('red')

    # fig, ax = plt.subplots(figsize=(12, 10))
    # ax.yaxis.set_ticks_position('right')
    # matplotlib.rcParams.update({'font.size': font_size})
    # fig = plt.figure(figsize=(50, 20))
    # ax = plt.subplot(241)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    for fitness_data in fitness:
        fitness_data.insert(0, 1.0)
        gen_counts = [i * period for i in range(0, len(fitness_data))]
        # print len(fitness_data)
        # print len(gen_counts)
        plot(gen_counts, fitness_data, linewidth=2, color='0.75')        
        yscale('log')
    # title('Mean Fitness')
    gen_counts = [i * period for i in range(0, len(typical_fitness))]
    plot(gen_counts, typical_fitness, linewidth=2, color='0')
    yscale('log')
    xlabel("Generations", fontsize=label_size)
    ylabel("Fitness", fontsize=label_size)
    fig.savefig('Fitness_pops_ME005.png')
    # fig, ax = plt.subplots(figsize=(12, 10))
    # matplotlib.rcParams.update({'font.size': font_size})

    fig, ax = plt.subplots(figsize=(10, 10))
    # ax = plt.subplot(242)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    for mut_data in mut_rate:
        mut_data.insert(0, base_mu)
        gen_counts = [i * period for i in range(0, len(mut_data))]
        plot(gen_counts, mut_data, linewidth=2, color='0.75')
    # plt.ylim((0.995, 1.005))
    gen_counts = [i * period for i in range(0, len(typical_mut_rate))]
    plot(gen_counts, typical_mut_rate, linewidth=2, color='0')
    xlabel("Generations", fontsize=label_size)
    ylabel("Genomic Deleterious Mutation Rate", fontsize=label_size)
    fig.savefig('Mut_pops_ME005.png')
    
    # ax = plt.subplot(243)
    # ax.spines['right'].set_visible(False)
    # ax.spines['top'].set_visible(False)
    # ax.xaxis.set_ticks_position('bottom')
    # ax.yaxis.set_ticks_position('left')
    # for dele_data in n_dele:
    #     gen_counts = [i * period for i in range(0, len(dele_data))]
    #     plot(gen_counts, dele_data[0:], linewidth=2)
    # xlabel("Generations", fontsize=label_size)
    # ylabel("# of Deleterious mutations", fontsize=label_size)
    # # title('Mean # of Deleterious Mutations/Individual')

    # ax = plt.subplot(244)
    # ax.spines['right'].set_visible(False)
    # ax.spines['top'].set_visible(False)
    # ax.xaxis.set_ticks_position('bottom')
    # ax.yaxis.set_ticks_position('left')
    # for bene_data in n_bene:
    #     gen_counts = [i * period for i in range(0, len(bene_data))]
    #     plot(gen_counts, bene_data[0:], linewidth=2)
    # xlabel("Generations", fontsize=label_size)
    # ylabel("# of Beneficial mutations", fontsize=label_size)
    # # title('Mean # of Beneficial Mutations/Individual')

    # ax = plt.subplot(245)
    # ax.spines['right'].set_visible(False)
    # ax.spines['top'].set_visible(False)
    # ax.xaxis.set_ticks_position('bottom')
    # ax.yaxis.set_ticks_position('left')
    # for dele_fitness_effect_data in dele_fitness_effect:
    #     gen_counts = [i * period for i in range(0, len(dele_fitness_effect_data))]
    #     plot(gen_counts, dele_fitness_effect_data[0:], linewidth=2)
    # xlabel("Generations", fontsize=label_size)
    # ylabel("Deleterious Fitness Effect", fontsize=label_size)
    # # title('Mean # Deleterious Fitness Effect/Individual')

    # ax = plt.subplot(246)
    # ax.spines['right'].set_visible(False)
    # ax.spines['top'].set_visible(False)
    # ax.xaxis.set_ticks_position('bottom')
    # ax.yaxis.set_ticks_position('left')
    # for bene_fitness_effect_data in bene_fitness_effect:
    #     gen_counts = [i * period for i in range(0, len(bene_fitness_effect_data))]
    #     plot(gen_counts, bene_fitness_effect_data[0:], linewidth=2)
    # xlabel("Generations", fontsize=label_size)
    # ylabel("Beneficial Fitness Effect", fontsize=label_size)
    # title('Mean # Beneficial Fitness Effect/Individual')

    # plt.subplot(235)
    # for mutator_data in n_mutator:
    #     plot(gen_counts, mutator_data[0: ])
    # xlabel("50k Generations", fontsize=20)
    # ylabel("# of Mutators", fontsize=20)
    # title('Mean # of Mutators/Individual')

    # plt.subplot(236)
    # for antimut_data in n_antimut:
    #     plot(gen_counts, antimut_data[0: ])
    # xlabel("50k Generations", fontsize=20)
    # ylabel("# of Anti-mutators", fontsize=20)
    # title('Mean # of Anti-mutators/Individual')

    # plt.subplot(337)
    # for pop_size_data in pop_size:
    #     plot(gen_counts, pop_size_data[0: ])
    # xlabel("Generation", fontsize=20)
    # ylabel("Population Size", fontsize=20)
    # title('Population Size')

    fig.savefig(dir_name + '.png')

    os.chdir("..")
