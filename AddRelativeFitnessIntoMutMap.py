import glob
import linecache
import os
import re
import csv

data_path = '/Volumes/BigTwins/MutatorModelData/' + 'M0.0_R0.0_G50000_N1000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE0.3_AntiMutE0.3_EvlFrom1'
os.chdir(data_path)
mut_files = glob.glob("*_MutMap.txt")
fileID_exp  = re.compile(r"^(?P<fileID>\d+)_")

for i in range(0, len(mut_files)):
    mut_file_name     = mut_files[i]
    print mut_file_name
    fileID            = fileID_exp.search(mut_file_name)
    new_mut_file_name = 'new_' + mut_file_name
    fileID            = int(fileID.group('fileID'))
    pop_file_name     = str(fileID) + '_Pop.txt'
    print mut_file_name, pop_file_name
    
    file = csv.reader(open(mut_file_name, 'rb'), delimiter="\t", skipinitialspace=True)
    file.next()
    new_mut_file = open(new_mut_file_name, 'w')
    new_mut_file.write("MutationID\tFitnessEffec\tIndividualFitness\tFitnessZScore\tMutatorStrength\tGeneration\tLocus\n")
    for line in file:
        if line:
            genID         = int(line[4])
            indiv_fitness = float(line[2])
            records       = linecache.getline(pop_file_name, genID + 1).split('\t')
            fitness_mean  = float(records[1])
            fitness_sd    = float(records[7])
            z_score       = (indiv_fitness - fitness_mean) / fitness_sd
            write_str     = line[0] + "\t" + line[1] + "\t" + line[2] + "\t" + str(z_score)+ "\t" + line[3] + "\t" + line[4] + "\t" + line[5] + "\n"
            new_mut_file.write(write_str)
    new_mut_file.close()
    linecache.clearcache()
    cmd = 'rm -fr ' + mut_file_name
    os.system(cmd)
    print mut_file_name + 'deleted.'


