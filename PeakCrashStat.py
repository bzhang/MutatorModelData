import glob
import os
import re
from matplotlib.pyplot import hist
from util import *
import matplotlib.pylab as plt

__author__ = 'bingjun'

data_path = "/Volumes/BigTwins/MutatorModelData/"
os.chdir(data_path)
dirs = glob.glob("py_N1000_G600k/")
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
#    n_gen = int(nG.group('nG'))
	n_gen = 600000
	gen_counts = [i * 1000 for i in range(1,n_gen+1)]
	print(n_gen)
	files = glob.glob("*.txt")
	gen_peak = []
	gen_crash = []
	mutator_peak = []
	mutator_crash = []
	fitness_peak = []

	file_id = 0
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
					mutator_strength.append(line[2])
				else:
					mutator_crash.append(line[2])
					gen_crash.append(line[0])
					break
		m = max(fitness)
		fitness_peak.append(m)
		position = fitness.index(m)
		gen_peak.append(position)
		mutator_peak.append(mutator_strength[position])
		if not (mutator_crash[file_id:file_id+1]):
			mutator_crash.append(mutator_strength[-1])
		if not (gen_crash[file_id:file_id+1]):
			gen_crash.append(gen_counts[-1])
		file_id += 1
#		print file_id

	print gen_crash
	save_peak_crash(gen_peak, gen_crash, mutator_peak, mutator_crash, fitness_peak)
	print "Done saving."
#    fig = plt.figure(figsize=(20, 18))
#    plt.subplot(221)
#    hist(gen_peak)

