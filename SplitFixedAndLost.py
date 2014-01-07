import glob
import os
import re

data_path = '/Volumes/BigTwins/MutatorModelData/' + 'M0.0_R0.0_G450000_N1000_BeneMR3.0E-5_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR1.0E-4_AntiMutMR1.0E-5_MutaE0.3_AntiMutE0.03_EvlFrom1'
os.chdir(data_path)
mut_prop_files = glob.glob("*_MutMap.txt")
fileID_exp     = re.compile(r"^(?P<fileID>\d+)_")
genID = '450000'

for i in range(0, len(mut_prop_files)):
    mutMap_file_name = mut_prop_files[i]
    print mutMap_file_name
    fileID = fileID_exp.search(mutMap_file_name)
    fileID = int(fileID.group('fileID'))
    fixed_file_name = genID + '_' + str(fileID) + '_Fixed_Mut.txt'
    lost_file_name = str(fileID) + '_Lost_Mut.txt'
    print fixed_file_name, lost_file_name
    # cmd = 'comm -23 ' + mutMap_file_name + ' ' + fixed_file_name + ' > ' + lost_file_name
    cmd = 'grep -Fxv -f ' + fixed_file_name + ' ' + mutMap_file_name + ' > ' + lost_file_name
    os.system(cmd)
