import glob
import os
import re
import matplotlib
from matplotlib.pyplot import figure, ylabel, xlabel, title, plot, yscale
from util import *


__author__ = 'bingjun'

data_path = "/Volumes/BigTwins/MutatorModelData/"
#data_path = "/Users/bingjun/Documents/MutatorModel/"
os.chdir(data_path)
dirs = glob.glob("Core_M0.0_R0.0_G300000_N1000_BeneMR4.5E-5_DeleMR0.075_BeneE0.03_DeleE0.03_MutStr2_MutMR1.0E-4_AntiMutMR1.0E-5_MutaE0.03_EvlFrom600000")
print(os.getcwd())
print(len(dirs))

nG_exp=re.compile(r"_G(?P<nG>\d+)_")
mu_exp=re.compile(r"DeleMR(?P<mu>[\d\.E-]+)_")
evol_exp=re.compile(r"StartEvol(?P<evol>\d+)_")

for dir_name in dirs:
    os.chdir(dir_name)
    print(dir_name)
    nG = nG_exp.search(dir_name)
    # n_gen = int(nG.group('nG'))
    n_gen = 300
    print(n_gen)
    gen_counts = [i * 1000 for i in range(1,n_gen+1)]
    mu = mu_exp.search(dir_name)
    base_mu = float(mu.group('mu'))

    files = glob.glob("1000_*_Pop.txt")
    n_pop = len(files)
    fitness = map(list,[[]] * n_pop)
    mut_rate = map(list,[[]] * n_pop)
    n_dele = map(list,[[]] * n_pop)
    n_bene = map(list,[[]] * n_pop)
    pop_counter = 0
    for file_name in files:
        print(file_name)
        file = csv.reader(open(file_name, 'rb'), delimiter="\t", skipinitialspace=True)
        file.next()
        for line in file:
            if line:
                fitness[pop_counter].append(line[1])
                mut_rate[pop_counter].append(line[3])
                n_dele[pop_counter].append(line[5])
                n_bene[pop_counter].append(line[7])
        pop_counter += 1

#    print(fitness)
    fitness = string_to_float(fitness)
    mut_rate = string_to_float(mut_rate)
    n_dele = string_to_float(n_dele)
    n_bene = string_to_float(n_bene)

    fig = figure(figsize=(10,8))
    matplotlib.rcParams.update({'font.size': 18})
    for fitness_data in fitness:
#        print len(fitness_data)
#        print len(range(0,n_gen))
        plot(gen_counts, fitness_data[0 : ])
        # yscale('log')
    title("DeleMu = " + str(base_mu))
    xlabel("Generation", fontsize=20)
    ylabel("Fitness", fontsize=20)
    fig.savefig("Fitness_Pop_" + dir_name + ".png")

    fig = figure(figsize=(10,8))
    matplotlib.rcParams.update({'font.size': 18})
    for mut_data in mut_rate:
        plot(gen_counts, mut_data[0 : ])
    xlabel("Generation", fontsize=20)
    ylabel("Mutator Strength", fontsize=20)
    fig.savefig("Mut_Pop_" + dir_name + ".png")

    fig = figure(figsize=(10,8))
    matplotlib.rcParams.update({'font.size': 18})
    for dele_data in n_dele:
        plot(gen_counts, dele_data[0 : ])
    xlabel("Generation", fontsize=20)
    ylabel("# of Deleterious mutations", fontsize=20)
    fig.savefig("Dele_Pop_" + dir_name + ".png")

    fig = figure(figsize=(10,8))
    matplotlib.rcParams.update({'font.size': 18})
    for bene_data in n_bene:
        plot(gen_counts, bene_data[0 : ])
    xlabel("Generation", fontsize=20)
    ylabel("# of Beneficial mutations", fontsize=20)
    fig.savefig("Bene_Pop_" + dir_name + ".png")

    os.chdir("..")