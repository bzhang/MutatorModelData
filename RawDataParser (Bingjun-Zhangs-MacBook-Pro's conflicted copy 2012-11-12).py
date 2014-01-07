import glob
import os
import re
from util import *

__author__ = 'bingjun'

#data_path = "/Volumes/BigTwins/MutatorModelData/"
#output_path = "/Volumes/BigTwins/Dropbox/MutatorModel/Results/"
#data_path = "/Volumes/BigTwins/Project/mutator-model/out/"
data_path = "/Volumes/BigTwins/MutatorModelData/"
#data_path = "/Users/bingjun/Documents/MutatorModel/"
# output_path = "/Users/bingjun/Dropbox/MutatorModel/Results/"
os.chdir(data_path)
dirs = glob.glob("M0.0_R0.0_G450000_N1000_BeneMR3.0E-5_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR1.0E-4_AntiMutMR1.0E-5_MutaE0.03_AntiMutE0.03_EvlFrom1")
print(os.getcwd())
print(len(dirs))

nG_exp   = re.compile(r"_G(?P<nG>\d+)_")
mu_exp   = re.compile(r"DeleMR(?P<mu>[\d\.E-]+)_")
evol_exp = re.compile(r"StartEvol(?P<evol>\d+)_")

# counter = len(dirs)
for dir_name in dirs:
# if counter > 0:
    os.chdir(dir_name)
    print(dir_name)
    nG = nG_exp.search(dir_name)
#   n_gen = int(nG.group('nG'))
    n_gen = 450
    print(n_gen)
    files = glob.glob("1000_*.txt")
    # n_file = len(files)
    fitness_pop          = map(list, [[]] * n_gen)
    mutator_strength_pop = map(list, [[]] * n_gen)
    n_dele_pop           = map(list, [[]] * n_gen)
    n_bene_pop           = map(list, [[]] * n_gen)

    # Uncomment below for python code
#   n_mutator_pop = map(list,[[]]*n_gen)
#   n_antimut_pop = map(list,[[]]*n_gen)
#   pop_size_pop = map(list,[[]]*n_gen)

    for file_name in files:
    # if n_file > 0:
        file = open(file_name, 'rb')
        print(file_name)
        file.readline()
        records = [record for record in file.read().split('\n') if record]
#        print(records[0])
        for i in range(0, n_gen):
#           print i
#            print records[i]
            record = records[i].split()
#            print(record)
            fitness_pop[i].append(record[1])
            mutator_strength_pop[i].append(record[2])
            n_dele_pop[i].append(record[3])
            n_bene_pop[i].append(record[4])

#            # Uncomment below for python code
#            n_mutator_pop[i].append(record[5])
#            n_antimut_pop[i].append(record[6])
#            pop_size_pop[i].append(record[13])

        file.close()
    # print(fitness_pop)
    # n_file -= 1
    # counter -= 1
    # else:
    #   break

#    print(fitness_pop)
    fitness_pop = string_to_float(fitness_pop)
    mutator_strength_pop = string_to_float(mutator_strength_pop)
    n_dele_pop = string_to_float(n_dele_pop)
    n_bene_pop = string_to_float(n_bene_pop)

#    # Uncomment below for python code
#    n_mutator_pop = string_to_float(n_mutator_pop)
#    n_antimut_pop = string_to_float(n_antimut_pop)
#    pop_size_pop = string_to_float(pop_size_pop)
    save_data(fitness_pop, mutator_strength_pop, n_dele_pop, n_bene_pop)
#    save_python_data(fitness_pop, mutator_strength_pop, n_dele_pop, n_bene_pop, n_mutator_pop, n_antimut_pop, pop_size_pop)

    fitness_mean, fitness_CI = list_mean_CI(fitness_pop)
    mutator_strength_mean, mutator_strength_CI = list_mean_CI(mutator_strength_pop)
    n_dele_mean, n_dele_CI = list_mean_CI(n_dele_pop)
    n_bene_mean, n_bene_CI = list_mean_CI(n_bene_pop)
#    # Uncomment below for python code
#    n_mutator_mean, n_mutator_CI = list_mean_CI(n_mutator_pop)
#    n_antimut_mean, n_antimut_CI = list_mean_CI(n_antimut_pop)
#    pop_size_mean, pop_size_CI = list_mean_CI(pop_size_pop)

    save_mean_CI(fitness_mean, fitness_CI, mutator_strength_mean,
        mutator_strength_CI, n_dele_mean, n_dele_CI, n_bene_mean, n_bene_CI)

    # Uncomment below for python code
    #    save_python_mean_CI(fitness_mean, fitness_CI, mutator_strength_mean, mutator_strength_CI,
#                        n_dele_mean, n_dele_CI, n_bene_mean, n_bene_CI,
#                        n_mutator_mean, n_mutator_CI, n_antimut_mean, n_antimut_CI,
#                        pop_size_mean, pop_size_CI)

    # fitness_mean = list_mean(fitness_pop)
    # mutator_strength_mean = list_mean(mutator_strength_pop)
    # n_dele_mean = list_mean(n_dele_pop)
    # n_bene_mean = list_mean(n_bene_pop)
    # save_mean(fitness_mean, mutator_strength_mean,
    #           n_dele_mean, n_bene_mean)
    print("Done saving.")

    os.chdir("..")
