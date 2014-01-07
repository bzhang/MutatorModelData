import glob
import os
import re
from util import *
import matplotlib.pylab as plt

__author__ = 'bingjun'

data_path = "/Volumes/BigTwins/MutatorModelData/"
os.chdir(data_path)
dirs = glob.glob("M0.0_R0.0_G500000_N1000_BeneMR3.0E-5_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR1.0E-4_AntiMutMR1.0E-5_MutaE0.3_AntiMutE0.3_EvlFrom1")
print(os.getcwd())
print(len(dirs))
fitness_cutoff = 1e-3

nG_exp   = re.compile(r"_G(?P<nG>\d+)_")
mu_exp   = re.compile(r"DeleMR(?P<mu>[\d\.E-]+)_")
evol_exp = re.compile(r"StartEvol(?P<evol>\d+)_")

for dir_name in dirs:
    os.chdir(dir_name)
    print(dir_name)
    nG = nG_exp.search(dir_name)
#    n_gen = int(nG.group('nG'))
    n_gen = 500
    gen_counts = [i * 1000 for i in range(1, n_gen + 1)]
    print(n_gen)
    files = glob.glob("1000_*.txt")
    for file_name in files:
        fitness          = []
        mutator_strength = []
        n_dele           = []
        n_bene           = []
        n_mutator        = []
        n_antimut        = []
        pop_size         = []
        # if n_file > 0:
        print(file_name)
        file = csv.reader(open(file_name, 'rb'), delimiter="\t", skipinitialspace=True)
        file.next()
        for line in file:
            if line:
                curr_fitness = float(line[1])
                if curr_fitness >= fitness_cutoff:
                    fitness.append(line[1])
                    mutator_strength.append(line[2])
                    n_dele.append(line[3])
                    n_bene.append(line[4])
                    # Uncomment below for python code
#					n_mutator.append(line[5])
#					n_antimut.append(line[6])
#					pop_size.append(line[13])
                else:
                    break

        fitness          = string_to_float_list(fitness)
        mutator_strength = string_to_float_list(mutator_strength)
        n_dele           = string_to_float_list(n_dele)
        n_bene           = string_to_float_list(n_bene)

        # Uncomment below for python code
        n_mutator = string_to_float_list(n_mutator)
        n_antimut = string_to_float_list(n_antimut)
        pop_size = string_to_float_list(pop_size)

#        print n_bene

        x_ax = [i * 1000 for i in range(1, len(fitness) + 1)]
#        print x_ax, len(fitness)
#        print fitness, fitness_cutoff
#        exit(0)
#		fig = plt.figure(figsize=(30, 25))
        fig = plt.figure(figsize=(50, 25))
        plt.matplotlib.rcParams.update({'font.size': 18})

        plt.subplot(231)
        plt.plot(x_ax, fitness)
        plt.xlabel("Generation", fontsize=20)
        plt.ylabel("Fitness", fontsize=20)
        plt.title('Mean Fitness')

        plt.subplot(232)
        plt.plot(x_ax, mutator_strength)
        plt.xlabel("Generation", fontsize=20)
        plt.ylabel("Mutator Strength", fontsize=20)
        plt.title('Mean Mutator Strength')

        plt.subplot(233)
        plt.plot(x_ax, n_dele)
        plt.xlabel("Generation", fontsize=20)
        plt.ylabel("# of Deleterious Mutations", fontsize=20)
        plt.title('Mean # of Deleterious Mutations/Individual')

        plt.subplot(234)
        plt.plot(x_ax, n_bene)
        plt.xlabel("Generation", fontsize=20)
        plt.ylabel("# of Beneficial Mutations", fontsize=20)
        plt.title('Mean # of Beneficial Mutations/Individual')

#		plt.subplot(335)
#		plt.plot(x_ax, n_mutator)
#		plt.xlabel("Generation", fontsize=20)
#		plt.ylabel("# of Mutators", fontsize=20)
#		plt.title('Mean # of Mutators/Individual')
#
#		plt.subplot(336)
#		plt.plot(x_ax, n_antimut)
#		plt.xlabel("Generation", fontsize=20)
#		plt.ylabel("# of Anti-mutators", fontsize=20)
#		plt.title('Mean # of Anti-mutators/Individual')
#
#		plt.subplot(337)
#		plt.plot(x_ax, pop_size)
#		plt.xlabel("Generation", fontsize=20)
#		plt.ylabel("Population Size", fontsize=20)
#		plt.title('Population Size')

        fig.savefig(file_name + ".png")
