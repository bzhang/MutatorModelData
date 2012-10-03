import glob
import os
import re
import matplotlib
from matplotlib.pyplot import figure, ylabel, xlabel, title, plot, yscale
from util import *
import matplotlib.pylab as plt

__author__ = 'bingjun'

data_path = "/Volumes/BigTwins/MutatorModelData/"
#data_path = "/Users/bingjun/Documents/MutatorModel/"
os.chdir(data_path)
dirs = glob.glob("M0.0_R0.0_G500000_N1000_BeneMR3.0E-5_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR1.0E-4_AntiMutMR1.0E-5_MutaE0.3_AntiMutE0.3_EvlFrom1")
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
	n_gen = 500
	print(n_gen)
#    gen_counts = [i * 1000 for i in range(0,n_gen)]
	gen_counts = range(0,n_gen)
	mu = mu_exp.search(dir_name)

	files = glob.glob("1000_*.txt")
	n_pop = len(files)
	fitness = map(list,[[]] * n_pop)
	mut_rate = map(list,[[]] * n_pop)
	n_dele = map(list,[[]] * n_pop)
	n_bene = map(list,[[]] * n_pop)
	n_mutator = map(list,[[]] * n_pop)
	n_antimut = map(list,[[]] * n_pop)
	pop_size = map(list,[[]] * n_pop)
	pop_counter = 0
	for file_name in files:
		print(file_name)
		file = csv.reader(open(file_name, 'rb'), delimiter="\t", skipinitialspace=True)
		file.next()
		for line in file:
			if line:
				fitness[pop_counter].append(line[1])
				mut_rate[pop_counter].append(line[2])
				n_dele[pop_counter].append(line[3])
				n_bene[pop_counter].append(line[4])

				# Uncomment below for python code
#				n_mutator[pop_counter].append(line[5])
#				n_antimut[pop_counter].append(line[6])
#				pop_size[pop_counter].append(line[13])

		pop_counter += 1

#    print(fitness)
	fitness = string_to_float(fitness)
	mut_rate = string_to_float(mut_rate)
	n_dele = string_to_float(n_dele)
	n_bene = string_to_float(n_bene)
	# Uncomment below for python code
#	n_mutator = string_to_float(n_mutator)
#	n_antimut = string_to_float(n_antimut)
#	pop_size = string_to_float(pop_size)

#	fig = plt.figure(figsize=(30, 25))
	fig = plt.figure(figsize=(50, 25))
	matplotlib.rcParams.update({'font.size': 18})
	plt.subplot(231)
	for fitness_data in fitness:
#        print len(fitness_data)
#        print len(range(0,n_gen))
		plot(gen_counts, fitness_data[0 : ])
		# yscale('log')
	title('Mean Fitness')
	xlabel("Generation", fontsize=20)
	ylabel("Fitness", fontsize=20)

	plt.subplot(232)
	for mut_data in mut_rate:
		plot(gen_counts, mut_data[0 : ])
	xlabel("Generation", fontsize=20)
	ylabel("Mean Mutator Strength", fontsize=20)
	title('Mean Mutator Strength')

	plt.subplot(233)
	for dele_data in n_dele:
		plot(gen_counts, dele_data[0 : ])
	xlabel("Generation", fontsize=20)
	ylabel("# of Deleterious mutations", fontsize=20)
	title('Mean # of Deleterious Mutations/Individual')

	plt.subplot(234)
	for bene_data in n_bene:
		plot(gen_counts, bene_data[0 : ])
	xlabel("Generation", fontsize=20)
	ylabel("# of Beneficial mutations", fontsize=20)
	title('Mean # of Beneficial Mutations/Individual')

#	plt.subplot(335)
#	for mutator_data in n_mutator:
#		plot(gen_counts, mutator_data[0 : ])
#	xlabel("Generation", fontsize=20)
#	ylabel("# of Mutators", fontsize=20)
#	title('Mean # of Mutators/Individual')
#
#	plt.subplot(336)
#	for antimut_data in n_antimut:
#		plot(gen_counts, antimut_data[0 : ])
#	xlabel("Generation", fontsize=20)
#	ylabel("# of Anti-mutators", fontsize=20)
#	title('Mean # of Anti-mutators/Individual')
#
#	plt.subplot(337)
#	for pop_size_data in pop_size:
#		plot(gen_counts, pop_size_data[0 : ])
#	xlabel("Generation", fontsize=20)
#	ylabel("Population Size", fontsize=20)
#	title('Population Size')

	fig.savefig('pops_' + dir_name + '.png')

	os.chdir("..")