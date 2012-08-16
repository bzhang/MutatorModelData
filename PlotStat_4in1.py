import glob
import os
import re
from util import *
import matplotlib.pylab as plt

__author__ = 'bingjun'

data_path = "/Volumes/BigTwins/MutatorModelData/"
os.chdir(data_path)
dirs = glob.glob("Core_Expo_M0.0_R0.0_G600000_N1000_BeneMR3.0E-5_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR1.0E-4_AntiMutMR1.0E-5_MutaE0.03")
print(os.getcwd())
print(len(dirs))

nG_exp=re.compile(r"_G(?P<nG>\d+)_")
mu_exp=re.compile(r"DeleMR(?P<mu>[\d\.E-]+)_")
evol_exp=re.compile(r"StartEvol(?P<evol>\d+)_")

for dir_name in dirs:
    os.chdir(dir_name)
    print(dir_name)
    nG = nG_exp.search(dir_name)
#    n_gen = int(nG.group('nG'))
    n_gen = 600
    gen_counts = [i * 1000 for i in range(1,n_gen+1)]
    print(n_gen)
    files = glob.glob("1000_*_Pop.txt")
    for file_name in files:
        fitness = []
        mutator_strength = []
        n_dele = []
        n_bene = []
        # if n_file > 0:
        print(file_name)
        file = csv.reader(open(file_name, 'rb'), delimiter="\t", skipinitialspace=True)
        file.next()
        for line in file:
            if line:
                fitness.append(line[1])
                mutator_strength.append(line[3])
                n_dele.append(line[5])
                n_bene.append(line[7])

#        print n_bene
        fitness = string_to_float_list(fitness)
        mutator_strength = string_to_float_list(mutator_strength)
        n_dele = string_to_float_list(n_dele)
        n_bene = string_to_float_list(n_bene)

#        print n_bene


        fig = plt.figure(figsize=(20, 18))
        plt.subplot(221)
        plt.plot(gen_counts, fitness)
        plt.xlabel("Generation", fontsize=20)
        plt.ylabel("Fitness", fontsize=20)

        plt.subplot(222)
        plt.plot(gen_counts, mutator_strength)
        plt.xlabel("Generation", fontsize=20)
        plt.ylabel("Mutator Strength", fontsize=20)

        plt.subplot(223)
        plt.plot(gen_counts, n_bene)
        plt.xlabel("Generation", fontsize=20)
        plt.ylabel("# of Beneficial Mutations", fontsize=20)

        plt.subplot(224)
        plt.plot(gen_counts, n_dele)
        plt.xlabel("Generation", fontsize=20)
        plt.ylabel("# of Deleterious Mutations", fontsize=20)

        fig.savefig(file_name + ".png")
