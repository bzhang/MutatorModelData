import glob
import os
import re
from util import *
import matplotlib.pylab as plt
from matplotlib.pyplot import *
from subprocess import check_output 
import numpy as np

__author__ = 'bingjun'

data_path = "/Volumes/BigTwins/MutatorModelData/N1000/Sexual/"
# data_path = "/Volumes/BigTwins/MutatorModelData/ScanMutEAntiMutE/"
# data_path = "/Volumes/BigTwins/MutatorModelData/ScanMutMRAntiMutMR/"
os.chdir(data_path)
print os.getcwd()
# dirs = glob.glob("M0.0_R0.0_G70000_N10000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_*")
# dirs = glob.glob("M0.0_R0.0_*MutMR0.0010*")
# dirs = glob.glob("M0.0_R0.0_*MutaE10.05_*")
dirs = glob.glob("M0.0_R1.0_*_G70000_N1000_BeneMR1.0E-4_DeleMR0.05_BeneE0.03_DeleE0.03_MutStr2_MutMR0.0010_AntiMutMR1.0E-5_MutaE10.1_MutaE20.3_Prob2MutaE11.0_AntiMutE0.1_EvlFrom1_Period1000")
print dirs
extinction_data_1 = []
# extinction_data_6 = []
# extinction_data_10 = []
r_data_1 = []
# r_data_6 = []
# r_data_10 = []
# n_mutator_data = []
# mut_e_data = []
# anti_mut_e_data = []
# mut_r_data = []
# anti_mut_r_data = []
# extinction_data = []
r_exp = re.compile(r"R1.0_(?P<r>[\d\.E-]+)_")
# n_mutator_exp = re.compile(r"NMutator(?P<n_mutator>[\d]+)_")
# mut_r_exp = re.compile(r"_MutMR(?P<mut_r>[\d\.E-]+)_")
# anti_mut_r_exp = re.compile(r"_AntiMutMR(?P<anti_mut_r>[\d\.E-]+)_")
# mut_e1_exp = re.compile(r"_MutaE1(?P<mut_e>[\d\.E-]+)_")
# anti_mut_e_exp = re.compile(r"_AntiMutE(?P<anti_mut_e>[\d\.E-]+)_")

for dir_name in dirs:
    os.chdir(dir_name)
    print "dir_name = ", dir_name
    r_results = r_exp.search(dir_name)
    r = float(r_results.group('r'))
    print r
    # n_mutator_results = n_mutator_exp.search(dir_name)
    # mut_r_results = mut_r_exp.search(dir_name)
    # anti_mut_r_results = anti_mut_r_exp.search(dir_name)
    # mut_e_results = mut_e1_exp.search(dir_name)
    # anti_mut_e_results = anti_mut_e_exp.search(dir_name)
    # print n_mutator_results
    # print re.match(n_mutator_exp, dir_name)
    # if n_mutator_results:
    #     print 'Matched!'
    #     n_mutator = int(n_mutator_results.group('n_mutator'))      
    # else:
    #     n_mutator = 1
    r_data_1.append(r)
    # n_mutator_data.append(n_mutator)
    # print "r = ", r
    # print "n_mutator = ", n_mutator
    # mut_r = float(mut_r_results.group('mut_r'))
    # anti_mut_r = float(anti_mut_r_results.group('anti_mut_r'))
    # mut_e = float(mut_e_results.group('mut_e'))
    # anti_mut_e = float(anti_mut_e_results.group('anti_mut_e'))
    # mut_r_data.append(mut_r)
    # anti_mut_r_data.append(anti_mut_r)
    # mut_e_data.append(mut_e)
    # anti_mut_e_data.append(anti_mut_e)
    # print "mut_r = ", mut_r
    # print "anti_mut_r = ", anti_mut_r
    # print "anti_mut_e = ", anti_mut_e

    files = glob.glob("*_Pop.txt")
    extinction_counter = 0.0
    survive_counter = 0.0
    for file_name in files:        
        # print(file_name)
        n_line = check_output(["tail", "-1", file_name])
        # print "n_line = ", n_line
        # print int(n_line.split()[0])        
        if int(n_line.split()[0]) < 70000 and float(n_line.split()[1]) < 0:
            print float(n_line.split()[1])
            extinction_counter = extinction_counter + 1.0
        elif float(n_line.split()[1]) < 1e-1:
            print float(n_line.split()[1])
            extinction_counter = extinction_counter + 1.0
        elif float(n_line.split()[1]) > 1e5:
            print float(n_line.split()[1])
            survive_counter = survive_counter + 1.0
    # print extinction_counter
    # print len(files)    
    extinction_p = extinction_counter/(extinction_counter + survive_counter)
    # if n_mutator == 1:
    #     r_data_1.append(r)
    #     extinction_data_1.append(extinction_p)
    # elif n_mutator == 6:
    #     r_data_6.append(r)
    #     extinction_data_6.append(extinction_p)
    # elif n_mutator == 10:
    #     r_data_10.append(r)
    #     extinction_data_10.append(extinction_p)
    extinction_data_1.append(extinction_p)
    print "extinction_counter = ", extinction_counter
    print "survive_counter = ", survive_counter
    print "extinction_p = ", extinction_p
    os.chdir(data_path)
# mut_e_data = np.array(mut_e_data)
# anti_mut_e_data = np.array(anti_mut_e_data)
# extinction_data = np.array(extinction_data)
# mut_r_data = np.array(mut_r_data)
# anti_mut_r_data = np.array(anti_mut_r_data)
# extinction_data = np.array(extinction_data)

# print mut_r_data
# print anti_mut_r_data
# print anti_mut_e_data
print r_data_1
print extinction_data_1


# anti_mut_r_data, extinction_data = zip(*sorted(zip(anti_mut_r_data, extinction_data)))
# anti_mut_e_data, extinction_data = zip(*sorted(zip(anti_mut_e_data, extinction_data)))
r_data_1, extinction_data_1 = zip(*sorted(zip(r_data_1, extinction_data_1)))
print r_data_1
print extinction_data_1
# mut_e_1 = []
# anti_mut_e_1 = []
# extinction_1 = []
# mut_e_2 = []
# anti_mut_e_2 = []
# extinction_2 = []
# mut_e_3 = []
# anti_mut_e_3 = []
# extinction_3 = []
# mut_e_4 = []
# anti_mut_e_4 = []
# extinction_4 = []
# mut_r = map(list, [[]]*3)
# anti_mut_r = map(list, [[]]*3)
# extinction = map(list, [[]]*3)

# for i in range(0, len(mut_e_data)):
#     if mut_e_data[i] == 0.05:
#         mut_e_1.append(mut_e_data[i])
#         anti_mut_e_1.append(anti_mut_e_data[i])
#         extinction_1.append(extinction_data[i])
#     elif mut_e_data[i] == 0.1:
#         mut_e_2.append(mut_e_data[i])
#         anti_mut_e_2.append(anti_mut_e_data[i])
#         extinction_2.append(extinction_data[i])
#     elif mut_e_data[i] == 0.2:
#         mut_e_3.append(mut_e_data[i])
#         anti_mut_e_3.append(anti_mut_e_data[i])
#         extinction_3.append(extinction_data[i])
#     elif mut_e_data[i] == 0.3:
#         mut_e_4.append(mut_e_data[i])
#         anti_mut_e_4.append(anti_mut_e_data[i])
#         extinction_4.append(extinction_data[i])

# for i in range(0, len(mut_r_data)):
#     if mut_r_data[i] == 0.0005:
#         mut_r[0].append(mut_r_data[i])
#         anti_mut_r[0].append(anti_mut_r_data[i])
#         extinction[0].append(extinction_data[i])
#     elif mut_r_data[i] == 0.001:
#         mut_r[1].append(mut_r_data[i])
#         anti_mut_r[1].append(anti_mut_r_data[i])
#         extinction[1].append(extinction_data[i])
#     elif mut_r_data[i] == 0.005:
#         mut_r[2].append(mut_r_data[i])
#         anti_mut_r[2].append(anti_mut_r_data[i])
#         extinction[2].append(extinction_data[i])

# for i in range(0, len(anti_mut_r_data)):
#     if anti_mut_r_data[i] == 1e-5:
#         mut_r_1.append(mut_r_data[i])
#         anti_mut_r_1.append(anti_mut_r_data[i])
#         extinction_1.append(extinction_data[i])
#     elif anti_mut_r_data[i] == 5e-5:
#         mut_r_2.append(mut_r_data[i])
#         anti_mut_r_2.append(anti_mut_r_data[i])
#         extinction_2.append(extinction_data[i])
#     elif anti_mut_r_data[i] == 1e-4:
#         mut_r_3.append(mut_r_data[i])
#         anti_mut_r_3.append(anti_mut_r_data[i])
#         extinction_3.append(extinction_data[i])
#     elif anti_mut_r_data[i] == 5e-4:
#         mut_r_4.append(mut_r_data[i])
#         anti_mut_r_4.append(anti_mut_r_data[i])
#         extinction_4.append(extinction_data[i])
#     elif anti_mut_r_data[i] == 1e-3:
#         mut_r_5.append(mut_r_data[i])
#         anti_mut_r_5.append(anti_mut_r_data[i])
#         extinction_5.append(extinction_data[i])
# print mut_e_1
# print anti_mut_e_1
# print extinction_1
# print mut_e_2
# print anti_mut_e_2
# print extinction_2
# print mut_e_3
# print anti_mut_e_3
# print extinction_3
# print mut_e_4
# print anti_mut_e_4
# print extinction_4
# print mut_r
# print anti_mut_r
# print extinction


font_size = 20
label_size = 25

fig, ax = plt.subplots(figsize=(12, 10))
# fig = plt.figure(figsize=(12, 10))
# ax = Axes3D(fig)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
matplotlib.rcParams.update({'font.size': font_size})
# plt.plot(anti_mut_e_1, extinction_1, 'o-', linewidth=3)
# plt.plot(anti_mut_e_2, extinction_2, 'o-', linewidth=3)
# plt.plot(anti_mut_e_3, extinction_3, 'o-', linewidth=3)
# plt.plot(anti_mut_e_4, extinction_4, 'o-', linewidth=3)
# for i in range(0, 3):
#     plt.plot(anti_mut_r[i], extinction[i], 'o', linewidth=3)
# plt.plot(anti_mut_r_data, extinction_data, 'o-', linewidth=3)
# plt.plot(anti_mut_e_data, extinction_data, 'o-', linewidth=3)
# plt.ylim(-0.1, 1.1)
# p = np.poly1d(np.polyfit(anti_mut_r_data, extinction_data, deg=5))
# xp = np.linspace(min(anti_mut_r_data), 2e-4, 500)
# plt.plot(xp, p(xp), '-', linewidth=2)

plot(r_data_1, extinction_data_1, 'o-', linewidth=3, markersize=10)
yticks, yticklabels = plt.yticks()
ymin = (3*yticks[0] - yticks[1])/2.
ymax = (3*yticks[-1] - yticks[-2])/2.
plt.ylim(ymin, ymax)
plt.yticks(yticks)
# plot(r_data_6, extinction_data_6, 'gs-', linewidth=3, markersize=10)
# plot(r_data_10, extinction_data_10, 'r>-', linewidth=3, markersize=10)
# ax.plot_surface(X=mut_r_data, Y=anti_mut_r_data, Z=extinction_data)
# ax.plot_wireframe(X=mut_r_data, Y=anti_mut_r_data, Z=extinction_data)
# ax.scatter(xs=mut_r_data, ys=anti_mut_r_data, zs=extinction_data)
xscale('log')
# yscale('log')
xlabel("Recombination Rates", fontsize=label_size)
# ylabel("Extinction Percentage", fontsize=label_size)
# xlabel("Mutator Mutation Rate")
# ylabel("AntiMutator Mutation Rate")
# xlabel("AntiMutator Mutation Rate")
# xlabel("AntiMutator Effects")
ylabel("Extinction Percentage", fontsize=label_size)
# title("N = 1000, Sexual")
# legend_label = [0.0005, 0.001, 0.005]
# lg = legend(legend_label, loc=1)
# lg.draw_frame(False)
# # Shink current axis's height by 10% on the bottom
# box = ax.get_position()
# ax.set_position([box.x0, box.y0 + box.height * 0.2, 
#                  box.width, box.height * 0.8])
# # Put a legend below current axis
# ax.legend(legend_label, loc='upper center', bbox_to_anchor=(0.5, -0.1), 
#           ncol=4)
# fig.savefig('Scan_MutE_AntiMutE_Extinction_Percentage.png')
fig.savefig('N1000_Sexual_ScanR_Extinction_Percentage.png')
# plt.show()
