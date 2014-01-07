import glob
import linecache
import os
import re
import csv

data_path = '/Volumes/BigTwins/MutatorModelData/' + 'M0.0_R0.0_G50000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE0.3_AntiMutE0.3_EvlFrom1'
os.chdir(data_path)
fixed_files = glob.glob("*_Fixed_Mut.txt")
fileID_exp  = re.compile(r"_(?P<fileID>\d+)_")

for i in range(0, len(fixed_files)):
    fixed_file_name = fixed_files[i]
    fileID = fileID_exp.search(fixed_file_name)
    fileID = int(fileID.group('fileID'))
    # if fileID > 6315387282538294:
    lost_file_name      = str(fileID) + '_Lost_Mut.txt'
    pop_file_name       = str(fileID) + '_Pop.txt'
    new_fixed_file_name = 'new' + fixed_file_name
    new_lost_file_name  = 'new' + lost_file_name
    print fixed_file_name, lost_file_name, pop_file_name
    
    file = csv.reader(open(fixed_file_name, 'rb'), delimiter="\t", skipinitialspace=True)
    new_fixed_file = open(new_fixed_file_name, 'w')
    new_fixed_file.write("MutationID\tFitnessEffec\tIndividualFitness\tFitnessZScore\tMutatorStrength\tGeneration\tLocus\n")
    for line in file:
        if line:
            genID         = int(line[4])
            indiv_fitness = float(line[2])
            records       = linecache.getline(pop_file_name, genID + 1).split('\t')
            fitness_mean  = float(records[1])
            fitness_sd    = float(records[7])
            z_score       = (indiv_fitness - fitness_mean) / fitness_sd
            write_str = line[0] + "\t" + line[1] + "\t" + line[2] + "\t" + str(z_score)+ "\t" + line[3] + "\t" + line[4] + "\t" + line[5] + "\n"
            new_fixed_file.write(write_str)
    new_fixed_file.close()

    file = csv.reader(open(lost_file_name, 'rb'), delimiter="\t", skipinitialspace=True)
    file.next()
    new_lost_file = open(new_lost_file_name, 'w')
    new_lost_file.write("MutationID\tFitnessEffec\tIndividualFitness\tFitnessZScore\tMutatorStrength\tGeneration\tLocus\n")
    for line in file:
        if line:
            genID         = int(line[4])
            indiv_fitness = float(line[2])
            records       = linecache.getline(pop_file_name, genID + 1).split('\t')
            fitness_mean  = float(records[1])
            fitness_sd    = float(records[7])
            z_score       = (indiv_fitness - fitness_mean) / fitness_sd
            write_str = line[0] + "\t" + line[1] + "\t" + line[2] + "\t" + str(z_score)+ "\t" + line[3] + "\t" + line[4] + "\t" + line[5] + "\n"
            new_lost_file.write(write_str)
    new_lost_file.close()    
    linecache.clearcache()



