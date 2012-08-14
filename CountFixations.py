import glob
import os
import re

__author__ = 'bingjun'

data_path = "/Volumes/BigTwins/MutatorModelData/"
os.chdir(data_path)
dirs = glob.glob("Expo_M0.0_R0.0_G60000_N1000_BeneMR3.0E-5_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR1.0E-4_AntiMutMR1.0E-5_MutaE0.03")
print(os.getcwd())
print(len(dirs))

nG_exp=re.compile(r"_G(?P<nG>\d+)_")
mu_exp=re.compile(r"DeleMR(?P<mu>[\d\.E-]+)_")
evol_exp=re.compile(r"StartEvol(?P<evol>\d+)_")
fileID_exp=re.compile(r"^(?P<fileID>\d+)_")

# counter = len(dirs)
for dir_name in dirs:
# if counter > 0:
    os.chdir(dir_name)
    print(dir_name)
    nG = nG_exp.search(dir_name)
    n_gen = int(nG.group('nG'))
    files = glob.glob("*_MutMap.txt")
    bene_mut_acquired = map(list, [[0]] * n_gen)
    dele_mut_acquired = map(list, [[0]] * n_gen)
    file_counter = 0
    for file_name in files:
        file = open(file_name,'rb')
        print(file_name)
        file.readline()
        records = [record for record in file.read().split('\n') if record]
        for i in range(0,n_gen):
            record = records[i].split()
            if record[1] > 1:
                bene_mut_acquired[i][file_counter] += 1
            else:
                dele_mut_acquired[i][file_counter] += 1
        file.close()
        file_counter += 1

    files = glob.glob("*_MutStructure.txt")
    bene_fixed = map(list, [[0]] * n_gen)
    dele_fixed = map(list, [[0]] * n_gen)
    file_counter = 0
    for file_name in files:
        file = open(file_name, 'rb')
        print(file_name)
        fileID = fileID_exp.search(file_name)
        file_ID = int(fileID.group('fileID'))
        records = [record for record in file.read().split('\n') if record]


