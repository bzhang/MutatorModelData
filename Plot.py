#!/usr/bin/env python
# encoding: utf-8
"""
Plot.py

Created by Bingjun Zhang on 2012-08-09.
Copyright (c) 2012 Bingjun Zhang. All rights reserved.
"""

import sys
import os
import glob
from util import *
from matplotlib.pyplot import *
from matplotlib.axes import *

def main():
	data_path = "/Volumes/BigTwins/MutatorModelData/"
	os.chdir(data_path)
	files = glob.glob("*test_MutE03.txt")
	n_gen = 4000
	fig_title = "test_MutE03_AntiMutE03"
	print "# of files = " + str(len(files))
	print "# of generations = " + str(n_gen)

	fitness_pop = map(list,[[]]*n_gen)
	mutator_strength_pop = map(list,[[]]*n_gen)
	n_dele_pop = map(list,[[]]*n_gen)
	n_bene_pop = map(list,[[]]*n_gen)
	
	for file_name in files:
		print file_name
		file = open(file_name, "r")
		file.readline()
		records = [record for record in file.read().split('\n') if record]
		for i in range(0, n_gen):
			# print i
			record = records[i].split()
			fitness_pop[i].append(record[0])
			mutator_strength_pop[i].append(record[1])
			n_dele_pop[i].append(record[2])
			n_bene_pop[i].append(record[3])
		file.close()

	fitness_pop = string_to_float(fitness_pop)
	mutator_strength_pop = string_to_float(mutator_strength_pop)
	n_dele_pop = string_to_float(n_dele_pop)
	n_bene_pop = string_to_float(n_bene_pop)
	
	# print fitness_pop

	fitness_mean, fitness_CI = list_mean_CI(fitness_pop)
	mutator_strength_mean, mutator_strength_CI = list_mean_CI(mutator_strength_pop)
	n_dele_mean, n_dele_CI = list_mean_CI(n_dele_pop)
	n_bene_mean, n_bene_CI = list_mean_CI(n_bene_pop)

	fig = figure(figsize=(10,8))
	matplotlib.rcParams.update({'font.size': 18})
	errorbar(range(1,n_gen+1),fitness_mean,fitness_CI,color='r',capsize=0,ecolor='gray')
	# yscale('log')
	xlabel("Generation", fontsize=20)
	ylabel("Fitness", fontsize=20)
	fig.savefig("fitness_" + fig_title + ".png")

	fig = figure(figsize=(10,8))
	matplotlib.rcParams.update({'font.size': 18})
	errorbar(range(1,n_gen+1),mutator_strength_mean,mutator_strength_CI,fmt='r',ecolor='gray',capsize=0)
#	 yscale('log')
	xlabel("Generation", fontsize=20)
	ylabel("Mutator Strength", fontsize=20)
	fig.savefig("Mut_" + fig_title + ".png")

	fig = figure(figsize=(10,8))
	matplotlib.rcParams.update({'font.size': 18})
	errorbar(range(1,n_gen+1),n_dele_mean,n_dele_CI,fmt='r',ecolor='gray',capsize=0)
	xlabel("Generation", fontsize=20)
	ylabel("# of Deleterious mutations", fontsize=20)
	fig.savefig("Dele_" + fig_title + ".png")

	fig = figure(figsize=(10,8))
	matplotlib.rcParams.update({'font.size': 18})
	errorbar(range(1,n_gen+1),n_bene_mean,n_bene_CI,fmt='r',ecolor='gray',capsize=0)
	xlabel("Generation", fontsize=20)
	ylabel("# of Beneficial mutations", fontsize=20)
	fig.savefig("Bene_" + fig_title + ".png")

	fig, ax1 = subplots(figsize=(10,8))
	ax2 = ax1.twinx()
	matplotlib.rcParams.update({'font.size': 18})
	ax1.plot(range(1,n_gen+1),fitness_mean,'b-')
	# ax1.set_yscale('log')
	ax1.set_xlabel("Generation", fontsize=20)
	ax1.set_ylabel("Fitness", fontsize=20)
	ax2.plot(range(1,n_gen+1),mutator_strength_mean,'r-')
	# ax2.set_yscale('log')
	ax2.set_ylabel("Mutator Strength", fontsize=20)
	# Change the axis colors...
	ax1.tick_params(axis='y', labelcolor='blue')
	ax1.yaxis.label.set_color('blue')
	ax2.tick_params(axis='y', labelcolor='red', color='red')
	ax2.yaxis.label.set_color('red')

	fig.savefig("FitMut_" + fig_title + ".png")
		

if __name__ == '__main__':
	main()

