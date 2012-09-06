import csv

__author__ = 'bingjun'
#! /usr/local/bin/python
import pickle
from math import *

def save_data(fitness_pop, mutator_strength_pop, n_dele_pop, n_bene_pop):
    file = open("state",'w')
    data = {'fitness_pop':fitness_pop,
            'mutator_strength_pop':mutator_strength_pop,
            'n_dele_pop':n_dele_pop,
            'n_bene_pop':n_bene_pop}
    pickle.dump(data, file)
    file.close()

def save_mean_CI(fitness_mean, fitness_CI, mutator_strength_mean,
                 mutator_strength_CI,n_dele_mean, n_dele_CI, n_bene_mean, n_bene_CI):
    file = open("state_mean_CI",'w')
    data = {'fitness_mean':fitness_mean,
            'mutator_strength_mean':mutator_strength_mean,
            'n_dele_mean':n_dele_mean,
            'n_bene_mean':n_bene_mean,
            'fitness_CI':fitness_CI,
            'mutator_strength_CI':mutator_strength_CI,
            'n_dele_CI':n_dele_CI,
            'n_bene_CI':n_bene_CI}
    pickle.dump(data, file)
    file.close()

def save_python_data(fitness_pop, mutator_strength_pop, n_dele_pop, n_bene_pop, n_mutator_pop, n_antimut_pop, pop_size):
    file = open("python_state", 'w')
    data = {'fitness_pop':fitness_pop,
            'mutator_strength_pop':mutator_strength_pop,
            'n_dele_pop':n_dele_pop,
            'n_bene_pop':n_bene_pop,
            'n_mutator_pop':n_mutator_pop,
            'n_antimut_pop':n_antimut_pop,
            'pop_size':pop_size}
    pickle.dump(data, file)
    file.close()

def save_python_mean_CI(fitness_mean, fitness_CI, mutator_strength_mean, mutator_strength_CI,
                        n_dele_mean, n_dele_CI, n_bene_mean, n_bene_CI,
                        n_mutator_mean, n_mutator_CI, n_antimut_mean, n_antimut_CI,
                        pop_size_mean, pop_size_CI):
    file = open("python_state_mean_CI", 'w')
    data = {'fitness_mean':fitness_mean,
            'mutator_strength_mean':mutator_strength_mean,
            'n_dele_mean':n_dele_mean,
            'n_bene_mean':n_bene_mean,
            'fitness_CI':fitness_CI,
            'mutator_strength_CI':mutator_strength_CI,
            'n_dele_CI':n_dele_CI,
            'n_bene_CI':n_bene_CI,
            'n_mutator_mean':n_mutator_mean,
            'n_mutator_CI':n_mutator_CI,
            'n_antimut_mean':n_antimut_mean,
            'n_antimut_CI':n_antimut_CI,
            'pop_size_mean':pop_size_mean,
            'pop_size_CI':pop_size_CI}
    pickle.dump(data, file)
    file.close()

def restore_python_data():
#    global fitness_pop, mutator_strength_pop, n_dele_pop, n_bene_pop, n_mutator_pop, n_antimut_pop, pop_size
    file = open("python_state",'r')
    data = pickle.load(file)
    file.close()
    fitness_pop = data['fitness_pop']
    mutator_strength_pop = data['mutator_strength_pop']
    n_dele_pop = data['n_dele_pop']
    n_bene_pop = data['n_bene_pop']
    n_mutator_pop = data['n_mutator_pop']
    n_antimut_pop = data['n_antimut_pop']
    pop_size = data['pop_size']
    return fitness_pop, mutator_strength_pop, n_dele_pop, n_bene_pop, n_mutator_pop, n_antimut_pop, pop_size

def restore_python_mean_CI():
#    global fitness_mean, fitness_CI, mutator_strength_mean, mutator_strength_CI
#    global n_dele_mean, n_dele_CI, n_bene_mean, n_bene_CI
    file = open("python_state_mean_CI",'r')
    data = pickle.load(file)
    file.close()
    fitness_mean = data['fitness_mean']
    mutator_strength_mean = data['mutator_strength_mean']
    n_dele_mean = data['n_dele_mean']
    n_bene_mean = data['n_bene_mean']
    fitness_CI = data['fitness_CI']
    mutator_strength_CI = data['mutator_strength_CI']
    n_dele_CI = data['n_dele_CI']
    n_bene_CI = data['n_bene_CI']
    n_mutator_mean = data['n_mutator_mean']
    n_mutator_CI = data['n_mutator_CI']
    n_antimut_mean = data['n_antimut_mean']
    n_antimut_CI = data['n_antimut_CI']
    pop_size_mean = data['pop_size_mean']
    pop_size_CI = data['pop_size_CI']
    return fitness_mean, fitness_CI, mutator_strength_mean, mutator_strength_CI, \
           n_dele_mean, n_dele_CI, n_bene_mean, n_bene_CI, \
           n_mutator_mean, n_mutator_CI, n_antimut_mean, n_antimut_CI, pop_size_mean, pop_size_CI




def restore_peak_crash():
    global gen_peak, gen_crash, mutator_peak, mutator_crash, fitness_peak
    file = open("state_peak_crash",'r')
    data = pickle.load(file)
    file.close()
    gen_peak = data['gen_peak']
    gen_crash = data['gen_crash']
    mutator_peak = data['mutator_peak']
    mutator_crash = data['mutator_crash']
    fitness_peak = data['fitness_peak']
    return gen_peak, gen_crash, mutator_peak, mutator_crash, fitness_peak


def save_peak_crash(gen_peak, gen_crash, mutator_peak, mutator_crash, fitness_peak):
    file = open("state_peak_crash", 'w')
    data = {'gen_peak':gen_peak,
            'gen_crash':gen_crash,
            'mutator_peak':mutator_peak,
            'mutator_crash':mutator_crash,
            'fitness_peak':fitness_peak
    }
    pickle.dump(data, file)
    file.close()


def save_mean(fitness_mean, mutator_strength_mean,
              n_dele_mean, n_bene_mean):
    file = open("state_mean",'w')
    data = {'fitness_mean':fitness_mean,
            'mutator_strength_mean':mutator_strength_mean,
            'n_dele_mean':n_dele_mean,
            'n_bene_mean':n_bene_mean,
    }
    pickle.dump(data, file)
    file.close()


def restore_mean_CI():
    global fitness_mean, fitness_CI, mutator_strength_mean, mutator_strength_CI
    global n_dele_mean, n_dele_CI, n_bene_mean, n_bene_CI
    file = open("state_mean_CI",'r')
    data = pickle.load(file)
    file.close()
    fitness_mean = data['fitness_mean']
    mutator_strength_mean = data['mutator_strength_mean']
    n_dele_mean = data['n_dele_mean']
    n_bene_mean = data['n_bene_mean']
    fitness_CI = data['fitness_CI']
    mutator_strength_CI = data['mutator_strength_CI']
    n_dele_CI = data['n_dele_CI']
    n_bene_CI = data['n_bene_CI']
    return fitness_mean, fitness_CI, mutator_strength_mean, mutator_strength_CI, n_dele_mean, n_dele_CI, n_bene_mean, n_bene_CI


def restore_mean():
    global fitness_mean, mutator_strength_mean
    global n_dele_mean, n_bene_mean
    file = open("state_mean",'r')
    data = pickle.load(file)
    file.close()
    fitness_mean = data['fitness_mean']
    mutator_strength_mean = data['mutator_strength_mean']
    n_dele_mean = data['n_dele_mean']
    n_bene_mean = data['n_bene_mean']
    return fitness_mean, mutator_strength_mean, n_dele_mean, n_bene_mean


def save_sex():
    global fitness_2000_sex, mutator_strength_2000_sex, n_dele_2000_sex, n_bene_2000_sex
    global fitness_3000_sex, mutator_strength_3000_sex, n_dele_3000_sex, n_bene_3000_sex
    global fitness_4000_sex, mutator_strength_4000_sex, n_dele_4000_sex, n_bene_4000_sex
    global fitness_5000_sex, mutator_strength_5000_sex, n_dele_5000_sex, n_bene_5000_sex
    global base_mu
    file = open("state_sex",'w')
    data = {'fitness_2000_sex':fitness_2000_sex,
            'fitness_3000_sex':fitness_3000_sex,
            'fitness_4000_sex':fitness_4000_sex,
            'fitness_5000_sex':fitness_5000_sex,
            'mutator_strength_2000_sex':mutator_strength_2000_sex,
            'mutator_strength_3000_sex':mutator_strength_3000_sex,
            'mutator_strength_4000_sex':mutator_strength_4000_sex,
            'mutator_strength_5000_sex':mutator_strength_5000_sex,
            'n_dele_2000_sex':n_dele_2000_sex,
            'n_dele_3000_sex':n_dele_3000_sex,
            'n_dele_4000_sex':n_dele_4000_sex,
            'n_dele_5000_sex':n_dele_5000_sex,
            'n_bene_2000_sex':n_bene_2000_sex,
            'n_bene_3000_sex':n_bene_3000_sex,
            'n_bene_4000_sex':n_bene_4000_sex,
            'n_bene_5000_sex':n_bene_5000_sex,
            'base_mu':base_mu
    }
    pickle.dump(data, file)
    file.close()

def restore_sex():
    global fitness_2000_sex, mutator_strength_2000_sex, n_dele_2000_sex, n_bene_2000_sex
    global fitness_3000_sex, mutator_strength_3000_sex, n_dele_3000_sex, n_bene_3000_sex
    global fitness_4000_sex, mutator_strength_4000_sex, n_dele_4000_sex, n_bene_4000_sex
    global fitness_5000_sex, mutator_strength_5000_sex, n_dele_5000_sex, n_bene_5000_sex
    global base_mu
    file = open("state_sex",'r')
    data = pickle.load(file)
    file.close()
    fitness_2000_sex = data['fitness_2000_sex']
    fitness_3000_sex = data['fitness_3000_sex']
    fitness_4000_sex = data['fitness_4000_sex']
    fitness_5000_sex = data['fitness_5000_sex']
    base_mu = data['base_mu']
    return fitness_2000_sex,fitness_3000_sex,fitness_4000_sex,fitness_5000_sex,base_mu


def restore_asex():
    global fitness_2000_asex, mutator_strength_2000_asex, n_dele_2000_asex, n_bene_2000_asex
    global fitness_3000_asex, mutator_strength_3000_asex, n_dele_3000_asex, n_bene_3000_asex
    global fitness_4000_asex, mutator_strength_4000_asex, n_dele_4000_asex, n_bene_4000_asex
    global fitness_5000_asex, mutator_strength_5000_asex, n_dele_5000_asex, n_bene_5000_asex
    global base_mu
    file = open("state_asex",'r')
    data = pickle.load(file)
    file.close()
    fitness_2000_asex = data['fitness_2000_asex']
    fitness_3000_asex = data['fitness_3000_asex']
    fitness_4000_asex = data['fitness_4000_asex']
    fitness_5000_asex = data['fitness_5000_asex']
    base_mu = data['base_mu']
    return fitness_2000_asex,fitness_3000_asex,fitness_4000_asex,fitness_5000_asex,base_mu


def restore_data():
    global fitness_pop, mutator_strength_pop, n_dele_pop, n_bene_pop
    file = open("state",'r')
    data = pickle.load(file)
    file.close()
    fitness_pop = data['fitness_pop']
    mutator_strength_pop = data['mutator_strength_pop']
    n_dele_pop = data['n_dele_pop']
    n_bene_pop = data['n_bene_pop']
    return fitness_pop, mutator_strength_pop, n_dele_pop, n_bene_pop

def string_to_float(nested_list):
    result = map(list,[[]]*len(nested_list))
    for i in range(0,len(nested_list)):
#        print(nested_list[i])
        for j in range(0,len(nested_list[i])):
#            print(nested_list[i][j])
            result[i].append(float(nested_list[i][j]))
    return result

def string_to_float_list(list):
    result = []
    for i in range(0,len(list)):
        result.append(float(list[i]))
    return result


def mean_95CI(list):
    n, mean, std, se, ci = len(list), 0, 0, 0, 0
    mean = get_mean(list)
    for i in list:
        std += (i - mean) ** 2
    std = sqrt(std / float(n-1))
    se = std / sqrt(float(n-1))
    ci = 1.96 * se
    return mean, ci

def get_mean(list):
    n, mean = len(list), 0
    for i in list:
        mean += i
    mean /= float(n)
    return mean

def get_mean_std(list):
    n, mean, std = len(list), 0, 0
    for i in list:
        mean += i
    mean /= float(n)
    for i in list:
        std += (i - mean) ** 2
    std = sqrt(std / float(n-1))
    return mean, std

def list_mean_CI(nested_list):
    mean_list, CI_list = [], []
    for i in nested_list:
        mean, ci = mean_95CI(i)
        mean_list.append(mean)
        CI_list.append(ci)
    return mean_list, CI_list

def list_mean(nested_list):
    mean_list = []
    for i in nested_list:
        mean = get_mean(i)
        mean_list.append(mean)
    return mean_list


def list_mean_CI_nonNest(list):
    mean_list, CI_list = [], []
    mean, ci = mean_95CI(list)
    mean_list.append(mean)
    CI_list.append(ci)
    return mean_list, CI_list

def log_list(list, base):
    result = []
    for i in list:
        result.append(log(i,base))
    return result

def get_column(file_name, separator, column):
    file = csv.reader(open(file_name, 'rb'), delimiter=separator, skipinitialspace=True)
    file.next()
    data = []
    for line in file:
        if line:
            data.append(line[column])
    file.close()
    return data
