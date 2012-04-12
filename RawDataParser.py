import glob
import os
from util import *

__author__ = 'bingjun'

# data_path = "/Volumes/BigTwins/MutatorModelData/"
output_path = "/Volumes/BigTwins/Dropbox/MutatorModel/Results/"
data_path = "/Volumes/BigTwins/Project/mutator-model/out/"
# data_path = "/Users/bingjun/Documents/MutatorModel/"
# output_path = "/Users/bingjun/Dropbox/MutatorModel/Results/"
os.chdir(data_path)
dirs = glob.glob("Expo_M0.0_R0.0_G50000_N1000_BeneMR3.0E-5_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_InitMutaMR0.0_EvolMutaMR1.0E-4_StartEvol1_Prob2M0.9_MutaE0.03")
print(os.getcwd())
print(len(dirs))

n_gen = 50000
# counter = len(dirs)
for dir_name in dirs:
# if counter > 0:
	os.chdir(dir_name)
	print(dir_name)
	files = glob.glob("*_Pop.txt")
	# n_file = len(files)
	fitness_pop = map(list,[[]]*n_gen)
	mutator_strength_pop = map(list,[[]]*n_gen)
	n_dele_pop = map(list,[[]]*n_gen)
	n_bene_pop = map(list,[[]]*n_gen)
	for file_name in files:
	# if n_file > 0:
		file = open(file_name,'rb')
		print(file_name)
		file.readline()
		records = [record for record in file.read().split('\n') if record]
		for i in range(0,n_gen):
			# print(fitness_pop[i])
			record = records[i].split()
			fitness_pop[i].append(record[1])
			mutator_strength_pop[i].append(record[3])
			n_dele_pop[i].append(record[5])
			n_bene_pop[i].append(record[7])
		file.close()
	# print(fitness_pop)
	# n_file -= 1
	# counter -= 1
	# else:
	# 	break

	fitness_pop = string_to_float(fitness_pop)
	mutator_strength_pop = string_to_float(mutator_strength_pop)
	n_dele_pop = string_to_float(n_dele_pop)
	n_bene_pop = string_to_float(n_bene_pop)
	save_data(fitness_pop, mutator_strength_pop, n_dele_pop, n_bene_pop)

	fitness_mean, fitness_CI = list_mean_CI(fitness_pop)
	mutator_strength_mean, mutator_strength_CI = list_mean_CI(mutator_strength_pop)
	n_dele_mean, n_dele_CI = list_mean_CI(n_dele_pop)
	n_bene_mean, n_bene_CI = list_mean_CI(n_bene_pop)
	save_mean_CI(fitness_mean, fitness_CI, mutator_strength_mean,
				 mutator_strength_CI,n_dele_mean, n_dele_CI, n_bene_mean, n_bene_CI)

	os.chdir("..")

