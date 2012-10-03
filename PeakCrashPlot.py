from matplotlib.pyplot import hist, axvline

__author__ = 'bingjun'
#! /usr/local/bin/python
import os, glob
import re
import matplotlib.pylab as plt
from util import *

data_path = "/Volumes/BigTwins/MutatorModelData/"
os.chdir(data_path)
dirs = glob.glob("py_N1000_G600k")
print(os.getcwd())
print(len(dirs))

nG_exp=re.compile(r"_G(?P<nG>\d+)_")
mu_exp=re.compile(r"DeleMR(?P<mu>[\d\.E-]+)_")
evol_exp=re.compile(r"StartEvol(?P<evol>\d+)_")

for dir_name in dirs:
    nG = nG_exp.search(dir_name)
    mu = mu_exp.search(dir_name)
#    base_mu = float(mu.group('mu'))
#    n_gen = int(nG.group('nG'))
    n_gen = 600
#    print(base_mu)
    print(n_gen)
    os.chdir(dir_name)

    gen_peak, gen_crash, mutator_peak, mutator_crash, fitness_peak = restore_peak_crash()
    gen_peak = string_to_float_list(gen_peak)
    gen_crash = string_to_float_list(gen_crash)
    mutator_peak = string_to_float_list(mutator_peak)
    mutator_crash = string_to_float_list(mutator_crash)
    fitness_peak = string_to_float_list(fitness_peak)

    print gen_crash
#    exit(0)

    mean_gen_peak, std_gen_peak = get_mean_std(gen_peak)
    mean_gen_crash, std_gen_crash = get_mean_std(gen_crash)
    mean_mutator_peak, std_mutator_peak = get_mean_std(mutator_peak)
    mean_mutator_crash, std_mutator_crash = get_mean_std(mutator_crash)
    mean_fitness_peak, std_fitness_peak = get_mean_std(fitness_peak)

    fig = plt.figure(figsize=(30, 18))
    plt.subplot(231)
    hist(fitness_peak, 20, histtype='bar', color='0.75')
    axvline(x=mean_fitness_peak, linewidth=2, color='r')
    axvline(x=mean_fitness_peak-std_fitness_peak, linewidth=1, color='b')
    axvline(x=mean_fitness_peak+std_fitness_peak, linewidth=1, color='b')
    plt.title("mean = " + str(mean_fitness_peak) + ", std = " + str(std_fitness_peak))
    plt.xlabel("Fitness at peak", fontsize=20)

    plt.subplot(232)
    hist(gen_peak, 20, histtype='bar', color='0.75')
    axvline(x=mean_gen_peak, linewidth=2, color='r')
    axvline(x=mean_gen_peak-std_gen_peak, linewidth=1, color='b')
    axvline(x=mean_gen_peak+std_gen_peak, linewidth=1, color='b')
    plt.title("mean = " + str(mean_gen_peak) + ", std = " + str(std_gen_peak))
    plt.xlabel("Time at fitness peak (generations)", fontsize=20)

    plt.subplot(233)
    hist(mutator_peak, 20, histtype='bar', color='0.75')
    axvline(x=mean_mutator_peak, linewidth=2, color='r')
    axvline(x=mean_mutator_peak-std_mutator_peak, linewidth=1, color='b')
    axvline(x=mean_mutator_peak+std_mutator_peak, linewidth=1, color='b')
    plt.title("mean = " + str(mean_mutator_peak) + ", std = " + str(std_mutator_peak))
    plt.xlabel("Mutator strength at fitness peak", fontsize=20)

    plt.subplot(234)
    hist(mutator_crash, 20, histtype='bar', color='0.75')
    axvline(x=mean_mutator_crash, linewidth=2, color='r')
    axvline(x=mean_mutator_crash-std_mutator_crash, linewidth=1, color='b')
    axvline(x=mean_mutator_crash+std_mutator_crash, linewidth=1, color='b')
    plt.title("mean = " + str(mean_mutator_crash) + ", std = " + str(std_mutator_crash))
    plt.xlabel("Mutator strength at extinction (fitness < 10^-3)", fontsize=20)

    plt.subplot(235)
    hist(gen_crash, 20, histtype='bar', color='0.75')
    axvline(x=mean_gen_crash, linewidth=2, color='r')
    axvline(x=mean_gen_crash-std_gen_crash, linewidth=1, color='b')
    axvline(x=mean_gen_crash+std_gen_crash, linewidth=1, color='b')
    plt.title("mean = " +  str(mean_gen_crash) + ", std = " + str(std_gen_crash))
    plt.xlabel("Time at extinction (fitness < 10^-3)", fontsize=20)

    fig.savefig("DateSummary" + ".png")