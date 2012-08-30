import glob
import os
import re
from matplotlib.pyplot import hist
from util import *
import matplotlib.pylab as plt

__author__ = 'bingjun'

data_path = "/Volumes/BigTwins/MutatorModelData/"
os.chdir(data_path)
dirs = glob.glob("Core_Expo_M0.0_R0.0_G600000_N1000_BeneMR3.0E-5_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR1.0E-4_AntiMutMR1.0E-5_MutaE0.03")
print(os.getcwd())
print(len(dirs))
fitness_cutoff = 1e-3

nG_exp=re.compile(r"_G(?P<nG>\d+)_")
mu_exp=re.compile(r"DeleMR(?P<mu>[\d\.E-]+)_")
evol_exp=re.compile(r"StartEvol(?P<evol>\d+)_")

for dir_name in dirs:
    os.chdir(dir_name)
    print(dir_name)
    nG = nG_exp.search(dir_name)
    n_gen = int(nG.group('nG'))
#    n_gen = 400
    gen_counts = [i * 1000 for i in range(1,n_gen+1)]
    print(n_gen)
    files = glob.glob("*_Pop.txt")
    gen_peak = []
    gen_crash = []
    mutator_peak = []
    mutator_crash = []
    fitness_peak = []

    for file_name in files:
        fitness = []
        mutator_strength = []
        print(file_name)
        file = csv.reader(open(file_name, 'rb'), delimiter="\t", skipinitialspace=True)
        file.next()
        for line in file:
            if line:
                curr_fitness = float(line[1])
                if curr_fitness >= fitness_cutoff:
                    fitness.append(line[1])
                    mutator_strength.append(line[3])
                else:
                    mutator_crash.append(line[3])
                    gen_crash.append(line[0])
                    break
        m = max(fitness)
        fitness_peak.append(m)
        position = fitness.index(m)
        gen_peak.append(position)
        mutator_peak.append(mutator_strength[position])


    save_peak_crash(gen_peak, gen_crash, mutator_peak, mutator_crash, fitness_peak)
    print "Done saving."
#    fig = plt.figure(figsize=(20, 18))
#    plt.subplot(221)
#    hist(gen_peak)

