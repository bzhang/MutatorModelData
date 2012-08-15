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
dirs = glob.glob("Core_Expo_M0.0_R0.0_G400000_N1000_BeneMR3.0E-5_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR1.0E-4_AntiMutMR1.0E-5_MutaE0.3")
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
	n_gen = 4000
	print(n_gen)
	mu = mu_exp.search(dir_name)
	base_mu = float(mu.group('mu'))

	files = glob.glob("*_Pop.txt")
	n_pop = len(files)
	fitness = map(list,[[]] * n_pop)
	mut_rate = map(list,[[]] * n_pop)
	n_dele = map(list,[[]] * n_pop)
	n_bene = map(list,[[]] * n_pop)
	pop_counter = 0
	for file_name in files:
		print(file_name)
		fitness[pop_counter] = get_column(file_name, "\t", 1)
#		 print(len(fitness[pop_counter]))
		mut_rate[pop_counter] = get_column(file_name, "\t", 3)
		n_dele[pop_counter] = get_column(file_name, "\t", 5)
		n_bene[pop_counter] = get_column(file_name, "\t", 7)
		pop_counter += 1
#		 break

#	 print(fitness)
	fitness = string_to_float(fitness)
	mut_rate = string_to_float(mut_rate)
	n_dele = string_to_float(n_dele)
	n_bene = string_to_float(n_bene)
 
	fig = figure(figsize=(10,8))
	matplotlib.rcParams.update({'font.size': 18})
	for fitness_data in fitness:
#		 print(fitness_data)
		plot(range(0, n_gen), fitness_data[0 : n_gen-1])
		# yscale('log')
	title("DeleMu = " + str(base_mu))
	xlabel("Generation", fontsize=20)
	ylabel("Fitness", fontsize=20)
	fig.savefig("g4000_fitness_Pop_" + dir_name + ".png")

	fig = figure(figsize=(10,8))
	matplotlib.rcParams.update({'font.size': 18})
	for mut_data in mut_rate:
		plot(range(0, n_gen), mut_data[0 : n_gen-1])
	xlabel("Generation", fontsize=20)
	ylabel("Mutator Strength", fontsize=20)
	fig.savefig("g4000_Mut_Pop_" + dir_name + ".png")
	   
	fig = figure(figsize=(10,8))
	matplotlib.rcParams.update({'font.size': 18})
	for dele_data in n_dele:
		plot(range(0, n_gen), dele_data[0 : n_gen-1])
	xlabel("Generation", fontsize=20)
	ylabel("# of Deleterious mutations", fontsize=20)
	fig.savefig("g4000_Dele_Pop_" + dir_name + ".png")
	   
	fig = figure(figsize=(10,8))
	matplotlib.rcParams.update({'font.size': 18})
	for bene_data in n_bene:
		plot(range(0, n_gen), bene_data[0 : n_gen-1])
	xlabel("Generation", fontsize=20)
	ylabel("# of Beneficial mutations", fontsize=20)
	fig.savefig("g4000_Bene_Pop_" + dir_name + ".png")
 
	os.chdir("..")