import glob
import os
import matplotlib.pylab as plt
from util import string_to_float_list
import numpy as np

data_path = '/Volumes/BigTwins/MutatorModelData/M0.0_R0.0_G500000_N1000_BeneMR3.0E-5_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR1.0E-4_AntiMutMR1.0E-5_MutaE0.3_AntiMutE0.3_EvlFrom1/'
os.chdir(data_path)
files = glob.glob("*_Fixed_Mut.txt")

bene_muts = []
dele_muts = []

for file_name in files:
    file = open(file_name, 'rb')
    print(file_name)
    records = [record for record in file.read().split('\n') if record]
    for i in range(0, len(records)):
        record = records[i].split()
        if float(record[1]) > 1:
            bene_muts.append(record[2])
        else:
            dele_muts.append(record[2])
    file.close()

bene_muts = string_to_float_list(bene_muts)
dele_muts = string_to_float_list(dele_muts)

bene = np.asarray(bene_muts)
dele = np.asarray(dele_muts)

fig = plt.figure(figsize=(15, 25))
plt.matplotlib.rcParams.update({'font.size': 18})

plt.subplot(211)
plt.hist(bene, weights=np.zeros_like(bene) + 1. / bene.size, bins=50)
plt.xlabel('Mutator Strength', fontsize=20)
plt.ylabel('Frequency')
plt.ylim(0, 0.16)
plt.title('Beneficial Mutations Fixed at 500,000 Generation, # = ' + str(bene.size))

plt.subplot(212)
plt.hist(dele, weights=np.zeros_like(dele) + 1. / dele.size, bins=50)
plt.xlabel('Mutator Strength', fontsize=20)
plt.ylabel('Frequency')
plt.ylim(0, 0.16)
plt.title('Deleterious Mutations Fixed at 500,000 Generation, # = ' + str(dele.size))

fig.savefig('Mutator_Strength_Distribution.png')
