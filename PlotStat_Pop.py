__author__ = 'bingjun'
#! /usr/local/bin/python
import os, glob, pylab
import re
from matplotlib.pyplot import *
from matplotlib.axes import *
from util import *

data_path = "/Volumes/BigTwins/MutatorModelData/"
#output_path = "/Volumes/BigTwins/Dropbox/MutatorModel/Results/"
#data_path = "/Volumes/BigTwins/Project/mutator-model/out/"
#data_path = "/Volumes/BigTwins/Project/mutator-model/out/"
# data_path = "/Users/bingjun/Documents/MutatorModel/"
# output_path = "/Users/bingjun/Dropbox/MutatorModel/Results/"
os.chdir(data_path)
dirs = glob.glob("Core_M0.0_R0.0_G300000_N1000_BeneMR4.5E-5_DeleMR0.075_BeneE0.03_DeleE0.03_MutStr2_MutMR1.0E-4_AntiMutMR1.0E-5_MutaE0.03_EvlFrom600000")
# dirs = glob.glob("MutCount_M0.0_R0.0_G5000_N500_BeneMR1.0E-4_DeleMR0.01_BeneE1.01_DeleE0.99_MutStr2_InitMutaMR0.0_EvolMutaMR0.01_StartEvol2500_Prob2M0.5_MutaE2")
# MutCount_M0.0_R1.0_G5000_N500_BeneMR1.0E-4_DeleMR0.01_BeneE1.01_DeleE0.99_MutStr2_MutaMR0.01_Prob2M0.5_MutaE2
# dirs=glob.glob("MutCount*_R0.0_*_MutaMR0.0_*")
print(os.getcwd())
print(len(dirs))

nG_exp=re.compile(r"_G(?P<nG>\d+)_")
mu_exp=re.compile(r"DeleMR(?P<mu>[\d\.E-]+)_")
evol_exp=re.compile(r"StartEvol(?P<evol>\d+)_")

for dir_name in dirs:
	nG = nG_exp.search(dir_name)
	mu = mu_exp.search(dir_name)
	base_mu = float(mu.group('mu'))
	# n_gen = int(nG.group('nG'))
	n_gen = 300
	print(base_mu)
	print(n_gen)
#	if evol_exp.search(dir_name):
#		evol = evol_exp.search(dir_name)
#		start = int(evol.group('evol'))
#	else:
#		start = 1
	os.chdir(dir_name)

	fitness_mean, fitness_CI, mutator_strength_mean, mutator_strength_CI, n_dele_mean, n_dele_CI, n_bene_mean, n_bene_CI = restore_mean_CI()
	# fitness_mean, mutator_strength_mean, n_dele_mean, n_bene_mean = restore_mean()

#	fitness_mean[4000:] = []
#	fitness_CI[4000:] = []
#	mutator_strength_mean[4000:] = []
#	mutator_strength_CI[4000:] = []
#	n_dele_mean[4000:] = []
#	n_dele_CI[4000:] = []
#	n_bene_mean[4000:] = []
#	n_bene_CI[4000:] = []

	print(len(fitness_mean))

	fig = figure(figsize=(10,8))
	matplotlib.rcParams.update({'font.size': 18})
	errorbar(range(1,n_gen+1),fitness_mean,fitness_CI,color='r',capsize=0,ecolor='gray')
	# yscale('log')
#	title("DeleMu = " + str(base_mu))
	xlabel("Generation", fontsize=20)
	ylabel("Fitness", fontsize=20)
#	axvline(x=start,color='g')
	fig.savefig("Fitness_" + dir_name + ".png")
	# fig.savefig("93_fitness_log_" + dir_name + ".png")

	fig = figure(figsize=(10,8))
	matplotlib.rcParams.update({'font.size': 18})
	errorbar(range(1,n_gen+1),mutator_strength_mean,mutator_strength_CI,fmt='r',ecolor='gray',capsize=0)
#	 yscale('log',basey=2)
#	 yscale('log')
	# title("Asexual Populations")
	# title("DeleMu = " + str(base_mu))
	xlabel("Generation", fontsize=20)
	ylabel("Mutator Strength", fontsize=20)
#	axvline(x=start,color='g')
#	 fig.savefig("Log2_Mut_" + dir_name + ".png")
	fig.savefig("Mut_" + dir_name + ".png")

	fig = figure(figsize=(10,8))
	matplotlib.rcParams.update({'font.size': 18})
	errorbar(range(1,n_gen+1),n_dele_mean,n_dele_CI,fmt='r',ecolor='gray',capsize=0)
	# title("DeleMu = " + str(base_mu))
	# title("Asexual Populations")
	xlabel("Generation", fontsize=20)
	ylabel("# of Deleterious mutations", fontsize=20)
#	 pylab.ylim([0,25])
#	axvline(x=start,color='g')
	fig.savefig("Dele_" + dir_name + ".png")
	# fig.savefig("93_Dele_" + dir_name + ".png")

	fig = figure(figsize=(10,8))
	matplotlib.rcParams.update({'font.size': 18})
	errorbar(range(1,n_gen+1),n_bene_mean,n_bene_CI,fmt='r',ecolor='gray',capsize=0)
	# title("Asexual Populations")
	# title("DeleMu = " + str(base_mu))
	xlabel("Generation", fontsize=20)
	ylabel("# of Beneficial mutations", fontsize=20)
#	 pylab.ylim([0,25])
#	axvline(x=start,color='g')
	fig.savefig("Bene_" + dir_name + ".png")
	# fig.savefig("93_Bene_" + dir_name + ".png")

	fig, ax1 = subplots(figsize=(10,8))
	ax2 = ax1.twinx()
	matplotlib.rcParams.update({'font.size': 18})
	ax1.plot(range(1,n_gen+1),fitness_mean,'b-')
	# title("93 Populations")
	# ax1.set_yscale('log')
#	 ylim(0.9,1.02) # StartEvol2500/3500
#	 ax1.set_yticks([0.975,0.990,1.005,1.020,1.035])
	# ylim(0.990,1.006) # StartEvol1
	# ax1.set_yticks([0.990,0.994,0.998,1.002,1.006])
	ax1.set_xlabel("Generation", fontsize=20)
	ax1.set_ylabel("Fitness", fontsize=20)
	ax2.plot(range(1,n_gen+1),mutator_strength_mean,'r-')
#	 ax2.set_yscale('log',basey=2)
	# ax2.set_yscale('log')
	ax2.set_ylabel("Mutator Strength", fontsize=20)
#	 ylim(2**-22,2**1)
#	 ax2.set_yticks([2**-16,2**-12,2**-8,2**-4,2**0])
	# ylim(2**-16,2**1) # StartEvol1
	# ax2.set_yticks([2**-16,2**-12,2**-8,2**-4,2**0])
	# ax2.set_yticklabels([2**-16,2**-12,2**-8,2**-4,2**0])
	# ylim([2^-16,2^1])
	# ax2.set_yticks([2^-16,2^-12,2^-8,2^-4,2^1])
	# ax2.set_yticklabels([2^-16,2^-12,2^-8,2^-4,2^1])
	# pylab.yticks(arrange(4))

	# ax2.yaxis.tick_right()
	# Change the axis colors...
	ax1.tick_params(axis='y', labelcolor='blue')
	ax1.yaxis.label.set_color('blue')
	ax2.tick_params(axis='y', labelcolor='red', color='red')
	ax2.yaxis.label.set_color('red')
#	axvline(x=start,color='g')
	# title("Asexual Populations")

	fig.savefig("FitMut_" + dir_name + ".png")
 
#	  fig = figure(figsize=(10,8))
#	  matplotlib.rcParams.update({'font.size': 18})
#	  plot(range(1,n_gen+1),fitness_mean,color='r')
#	  # yscale('log')
#	  title("DeleMu = " + str(base_mu))
#	  xlabel("Generation", fontsize=20)
#	  ylabel("Fitness", fontsize=20)
#	  axvline(x=start,color='g')
# #	   fig.savefig("fitness_" + dir_name + ".png")
#	  fig.savefig("fitness_mean_" + dir_name + ".png")
# 
#	  fig = figure(figsize=(10,8))
#	  matplotlib.rcParams.update({'font.size': 18})
#	  plot(range(1,n_gen+1),mutator_strength_mean,color='r')
# #	   yscale('log',basey=2)
# #	   yscale('log')
#	  # title("Asexual Populations")
#	  # title("DeleMu = " + str(base_mu))
#	  xlabel("Generation", fontsize=20)
#	  ylabel("Mutator Strength", fontsize=20)
#	  axvline(x=start,color='g')
# #	   fig.savefig("Log2_Mut_" + dir_name + ".png")
#	  fig.savefig("Mut_mean_" + dir_name + ".png")

#	  fig = figure(figsize=(10,8))
#	  matplotlib.rcParams.update({'font.size': 18})
#	  plot(range(1,n_gen+1),n_dele_mean,color='r')
#	  title("1000_300649921759_Dele")
#	  # title("DeleMu = " + str(base_mu))
#	  # title("Asexual Populations")
#	  xlabel("Generation", fontsize=20)
#	  ylabel("# of Deleterious mutations", fontsize=20)
# #	   pylab.ylim([0,25])
#	  axvline(x=start,color='g')
# #	   fig.savefig("Dele_" + dir_name + ".png")
#	  fig.savefig("1000_300649921759_Dele_mean_" + dir_name + ".png")
# 
#	  fig = figure(figsize=(10,8))
#	  matplotlib.rcParams.update({'font.size': 18})
#	  plot(range(1,n_gen+1),n_bene_mean,color='r')
#	  title("1000_300649921759_Bene")
#	  # title("Asexual Populations")
#	  # title("DeleMu = " + str(base_mu))
#	  xlabel("Generation", fontsize=20)
#	  ylabel("# of Beneficial mutations", fontsize=20)
# #	   pylab.ylim([0,25])
#	  axvline(x=start,color='g')
# #	   fig.savefig("Bene_" + dir_name + ".png")
#	  fig.savefig("1000_300649921759_Bene_mean_" + dir_name + ".png")


	os.chdir("..")