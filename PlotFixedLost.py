import glob
import os
import re
from util import restore_mut_props
import matplotlib.pylab as plt
import numpy as np

data_path = '/Volumes/BigTwins/MutatorModelData/' + 'M0.0_R0.0_G50000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE0.3_AntiMutE0.3_EvlFrom1'
os.chdir(data_path)
mut_file_name = '20000_30000_mut_props'

fixed_bene_fitness_effect, fixed_bene_fitness_zscore, \
fixed_bene_mut_strength, fixed_dele_fitness_effect, \
fixed_dele_fitness_zscore, fixed_dele_mut_strength, \
lost_bene_fitness_effect, lost_bene_fitness_zscore, \
lost_bene_mut_strength, lost_dele_fitness_effect, \
lost_dele_fitness_zscore, lost_dele_mut_strength \
= restore_mut_props(mut_file_name)

print "Done reading."

fixed_bene_fitness_effect = np.asarray(fixed_bene_fitness_effect)
fixed_bene_fitness_zscore = np.asarray(fixed_bene_fitness_zscore)
fixed_bene_mut_strength   = np.asarray(fixed_bene_mut_strength)
fixed_dele_fitness_effect = np.asarray(fixed_dele_fitness_effect)
fixed_dele_fitness_zscore = np.asarray(fixed_dele_fitness_zscore)
fixed_dele_mut_strength   = np.asarray(fixed_dele_mut_strength)
lost_bene_fitness_effect  = np.asarray(lost_bene_fitness_effect)
lost_bene_fitness_zscore  = np.asarray(lost_bene_fitness_zscore)
lost_bene_mut_strength    = np.asarray(lost_bene_mut_strength)
lost_dele_fitness_effect  = np.asarray(lost_dele_fitness_effect)
lost_dele_fitness_zscore  = np.asarray(lost_dele_fitness_zscore)
lost_dele_mut_strength    = np.asarray(lost_dele_mut_strength)

fig = plt.figure(figsize=(25, 30))
plt.matplotlib.rcParams.update({'font.size': 18})

plt.subplot(4, 3, 1)
plt.hist(fixed_bene_fitness_effect, weights=np.zeros_like(fixed_bene_fitness_effect) + 1. / fixed_bene_fitness_effect.size, bins=np.mgrid[0.7:1.3:20j])
plt.xlabel('Fitness Effect', fontsize=20)
plt.ylabel('Frequency')
plt.ylim(0, 0.5)
plt.title('Fixed Beneficial Mutations, # = ' + str(fixed_bene_fitness_effect.size))
print 'Plot 1.'

plt.subplot(4, 3, 2)
plt.hist(fixed_bene_fitness_zscore, weights=np.zeros_like(fixed_bene_fitness_zscore) + 1. / fixed_bene_fitness_zscore.size, bins=np.mgrid[-6:6:20j])
plt.xlabel('Fitness Z Score', fontsize=20)
plt.ylabel('Frequency')
plt.ylim(0, 0.5)
plt.title('Fixed Beneficial Mutations, # = ' + str(fixed_bene_fitness_zscore.size))
print 'Plot 2.'

plt.subplot(4, 3, 3)
plt.hist(fixed_bene_mut_strength, weights=np.zeros_like(fixed_bene_mut_strength) + 1. / fixed_bene_mut_strength.size, bins=np.mgrid[0:10:20j])
plt.xlabel('Mutator Strength', fontsize=20)
plt.ylabel('Frequency')
plt.ylim(0, 0.5)
plt.title('Fixed Beneficial Mutations, # = ' + str(fixed_bene_mut_strength.size))
print 'Plot 3.'

plt.subplot(4, 3, 4)
plt.hist(fixed_dele_fitness_effect, weights=np.zeros_like(fixed_dele_fitness_effect) + 1. / fixed_dele_fitness_effect.size, bins=np.mgrid[0.7:1.3:20j])
plt.xlabel('Fitness Effect', fontsize=20)
plt.ylabel('Frequency')
plt.ylim(0, 0.5)
plt.title('Fixed Deleterious Mutations, # = ' + str(fixed_dele_fitness_effect.size))
print 'Plot 4.'

plt.subplot(4, 3, 5)
plt.hist(fixed_dele_fitness_zscore, weights=np.zeros_like(fixed_dele_fitness_zscore) + 1. / fixed_dele_fitness_zscore.size, bins=np.mgrid[-6:6:20j])
plt.xlabel('Fitness Z Score', fontsize=20)
plt.ylabel('Frequency')
plt.ylim(0, 0.5)
plt.title('Fixed Deleterious Mutations, # = ' + str(fixed_dele_fitness_zscore.size))
print 'Plot 5.'

plt.subplot(4, 3, 6)
plt.hist(fixed_dele_mut_strength, weights=np.zeros_like(fixed_dele_mut_strength) + 1. / fixed_dele_mut_strength.size, bins=np.mgrid[0:10:20j])
plt.xlabel('Mutator Strength', fontsize=20)
plt.ylabel('Frequency')
plt.ylim(0, 0.5)
plt.title('Fixed Deleterious Mutations, # = ' + str(fixed_dele_mut_strength.size))
print 'Plot 6.'

plt.subplot(4, 3, 7)
plt.hist(lost_bene_fitness_effect, weights=np.zeros_like(lost_bene_fitness_effect) + 1. / lost_bene_fitness_effect.size, bins=np.mgrid[0.7:1.3:20j])
plt.xlabel('Fitness Effect', fontsize=20)
plt.ylabel('Frequency')
plt.ylim(0, 0.5)
plt.title('Lost Beneficial Mutations, # = ' + str(lost_bene_fitness_effect.size))
print 'Plot 7.'

plt.subplot(4, 3, 8)
plt.hist(lost_bene_fitness_zscore, weights=np.zeros_like(lost_bene_fitness_zscore) + 1. / lost_bene_fitness_zscore.size, bins=np.mgrid[-6:6:20j])
plt.xlabel('Fitness Z Score', fontsize=20)
plt.ylabel('Frequency')
plt.ylim(0, 0.5)
plt.title('Lost Beneficial Mutations, # = ' + str(lost_bene_fitness_zscore.size))
print 'Plot 8.'

plt.subplot(4, 3, 9)
plt.hist(lost_bene_mut_strength, weights=np.zeros_like(lost_bene_mut_strength) + 1. / lost_bene_mut_strength.size, bins=np.mgrid[0:10:20j])
plt.xlabel('Mutator Strength', fontsize=20)
plt.ylabel('Frequency')
plt.ylim(0, 0.5)
plt.title('Lost Beneficial Mutations, # = ' + str(lost_bene_mut_strength.size))
print 'Plot 9.'

plt.subplot(4, 3, 10)
plt.hist(lost_dele_fitness_effect, weights=np.zeros_like(lost_dele_fitness_effect) + 1. / lost_dele_fitness_effect.size, bins=np.mgrid[0.7:1.3:20j])
plt.xlabel('Fitness Effect', fontsize=20)
plt.ylabel('Frequency')
plt.ylim(0, 0.5)
plt.title('Lost Deleterious Mutations, # = ' + str(lost_dele_fitness_effect.size))
print 'Plot 10.'

plt.subplot(4, 3, 11)
plt.hist(lost_dele_fitness_zscore, weights=np.zeros_like(lost_dele_fitness_zscore) + 1. / lost_dele_fitness_zscore.size, bins=np.mgrid[-6:6:20j])
plt.xlabel('Fitness Z Score', fontsize=20)
plt.ylabel('Frequency')
plt.ylim(0, 0.5)
plt.title('Lost Deleterious Mutations, # = ' + str(lost_dele_fitness_zscore.size))
print 'Plot 11.'

plt.subplot(4, 3, 12)
plt.hist(lost_dele_mut_strength, weights=np.zeros_like(lost_dele_mut_strength) + 1. / lost_dele_mut_strength.size, bins=np.mgrid[0:10:20j])
plt.xlabel('Mutator Strength', fontsize=20)
plt.ylabel('Frequency')
plt.ylim(0, 0.5)
plt.title('Lost Deleterious Mutations, # = ' + str(lost_dele_mut_strength.size))
print 'Plot 12.'

fig.savefig('20000_30000_Mutations_Properties.png')
