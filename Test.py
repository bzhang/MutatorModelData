import os
from util import get_column

__author__ = 'bingjun'

os.chdir("/Volumes/BigTwins/MutatorModelData/Expo_M0.0_R0.0_G1000_N500_BeneMR3.0E-5_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR1.0E-4_AntiMutMR0.0_MutaE0.03")
print(get_column('37930029619894_Pop.txt', "\t", 1))