import glob
import os
import re
from util import string_to_float_list, save_mut_props
import csv

data_path = '/Volumes/BigTwins/MutatorModelData/' + 'M0.0_R0.0_G50000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE0.3_AntiMutE0.3_EvlFrom1'
os.chdir(data_path)
genID = '50000'
fixed_files = glob.glob('new' + genID + "*_Fixed_Mut.txt")
fileID_exp     = re.compile(r"_(?P<fileID>\d+)_")

fixed_bene_fitness_effect = []
fixed_bene_fitness_zscore  = []
fixed_bene_mut_strength   = []
fixed_dele_fitness_effect = []
fixed_dele_fitness_zscore  = []
fixed_dele_mut_strength   = []

lost_bene_fitness_effect = []
lost_bene_fitness_zscore  = []
lost_bene_mut_strength   = []
lost_dele_fitness_effect = []
lost_dele_fitness_zscore  = []
lost_dele_mut_strength   = []

for i in range(0, len(fixed_files)):
    fixed_file_name = fixed_files[i]
    fileID = fileID_exp.search(fixed_file_name)
    fileID = int(fileID.group('fileID'))
    lost_file_name = 'new' + str(fileID) + '_Lost_Mut.txt'
    print fixed_file_name, lost_file_name
    # MutationId    FitnessEffect   IndividualFitness MutatorStregnth Generation    Locus
    file = csv.reader(open(fixed_file_name, 'rb'), delimiter="\t", skipinitialspace=True)
    file.next()
    for line in file:
        if line:
            if 20000 <= int(line[5]) <= 30000:
                if float(line[1]) > 1:
                    fixed_bene_fitness_effect.append(line[1])
                    fixed_bene_fitness_zscore.append(line[3])
                    fixed_bene_mut_strength.append(line[4])
                else:
                    fixed_dele_fitness_effect.append(line[1])
                    fixed_dele_fitness_zscore.append(line[3])
                    fixed_dele_mut_strength.append(line[4])
    if i <= 5:
        file = csv.reader(open(lost_file_name, 'rb'), delimiter="\t", skipinitialspace=True)
        file.next()
        for line in file:
            if line:
                if 20000 <= int(line[5]) <= 30000:
                    if float(line[1]) > 1:
                        lost_bene_fitness_effect.append(line[1])
                        lost_bene_fitness_zscore.append(line[3])
                        lost_bene_mut_strength.append(line[4])
                    else:
                        lost_dele_fitness_effect.append(line[1])
                        lost_dele_fitness_zscore.append(line[3])
                        lost_dele_mut_strength.append(line[4])

fixed_bene_fitness_effect = string_to_float_list(fixed_bene_fitness_effect)
fixed_bene_fitness_zscore  = string_to_float_list(fixed_bene_fitness_zscore)
fixed_bene_mut_strength   = string_to_float_list(fixed_bene_mut_strength)
fixed_dele_fitness_effect = string_to_float_list(fixed_dele_fitness_effect)
fixed_dele_fitness_zscore  = string_to_float_list(fixed_dele_fitness_zscore)
fixed_dele_mut_strength   = string_to_float_list(fixed_dele_mut_strength)
lost_bene_fitness_effect = string_to_float_list(lost_bene_fitness_effect)
lost_bene_fitness_zscore  = string_to_float_list(lost_bene_fitness_zscore)
lost_bene_mut_strength   = string_to_float_list(lost_bene_mut_strength)
lost_dele_fitness_effect = string_to_float_list(lost_dele_fitness_effect)
lost_dele_fitness_zscore  = string_to_float_list(lost_dele_fitness_zscore)
lost_dele_mut_strength   = string_to_float_list(lost_dele_mut_strength)

save_file_name = '20000_30000_mut_props'
save_mut_props(fixed_bene_fitness_effect, fixed_bene_fitness_zscore, fixed_bene_mut_strength, fixed_dele_fitness_effect, fixed_dele_fitness_zscore, fixed_dele_mut_strength, lost_bene_fitness_effect, lost_bene_fitness_zscore, lost_bene_mut_strength, lost_dele_fitness_effect, lost_dele_fitness_zscore, lost_dele_mut_strength, save_file_name)

print "Done saving."


