import glob
import linecache
import os
import re
import sys
from util import pairwise

data_path = '/Volumes/BigTwins/MutatorModelData/' + 'M0.0_R0.0_G450000_N1000_BeneMR3.0E-5_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR1.0E-4_AntiMutMR1.0E-5_MutaE0.03_AntiMutE0.03_EvlFrom1'
os.chdir(data_path)
mut_prop_files = glob.glob("*_MutMap.txt")
mut_structure_files = glob.glob("*_MutStructure.txt")
fileID_exp = re.compile(r"^(?P<fileID>\d+)_")

for i in range(0, len(mut_prop_files)):
    fileID_mut_prop      = fileID_exp.search(mut_prop_files[i])
    fileID_mut_structure = fileID_exp.search(mut_structure_files[i])
    fileID_mut_prop      = int(fileID_mut_prop.group('fileID'))
    fileID_mut_structure = int(fileID_mut_structure.group('fileID'))
#	pairs = []
    if fileID_mut_prop == fileID_mut_structure:
#		fixed_mutID = []
        mut_structure_file = open(mut_structure_files[i], 'rb')
        print(mut_structure_files[i])
        mut_structure_file.readline()
        records = [record for record in mut_structure_file.read().split('\n') if record]
        for j in range(0, len(records)):
            mutIDs = records[j].split('\t')
            genID = mutIDs[0]
            output_file_name = str(genID) + '_' + str(fileID_mut_structure) + '_Fixed_Mut.txt'
            output_file = open(output_file_name, 'w')
            for pair in pairwise(mutIDs[1:]):
                if int(pair[1]) == 1000:
                    output_file.write(linecache.getline(mut_prop_files[i], int(pair[0]) + 1))
            output_file.close()

        linecache.clearcache()
        mut_structure_file.close()

    else:
        sys.exit('Can not pair up MutMap and MutStructure files!')
