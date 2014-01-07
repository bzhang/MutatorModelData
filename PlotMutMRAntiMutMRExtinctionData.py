import matplotlib.pylab as plt
from matplotlib.pyplot import *
import os

data_path = "/Volumes/BigTwins/MutatorModelData/ScanMutMRAntiMutMR/"
os.chdir(data_path)
# anti_mut_r_1 = [1.0000000000000001e-05, 5.0000000000000002e-05, 0.00050000000000000001, 0.0001, 0.001]
# extinction_1 = [1.0, 0.52000000000000002, 0.0, 0.0, 0.0]
# anti_mut_r_2 = [0.001, 0.00050000000000000001, 0.0001, 5.0000000000000002e-05, 1.0000000000000001e-05]
# extinction_2 = [0.0, 0.0, 1.0, 0.90000000000000002, 0.34000000000000002]
# anti_mut_r_3 = [0.001, 0.00050000000000000001, 0.0001, 5.0000000000000002e-05, 1.0000000000000001e-05]
# extinction_3 = [0.0, 1.0, 0.26000000000000001, 0.16, 0.20000000000000001]
# anti_mut_r_4 = [0.00050000000000000001, 0.0001, 5.0000000000000002e-05, 1.0000000000000001e-05]
# extinction_4 = [0.69999999999999996, 0.0, 0.0, 0.21359223300970873]

anti_mut_r_1 = [1.0000000000000001e-05, 5.0000000000000002e-05, 0.0001, 0.00050000000000000001, 0.001]
extinction_1 = [1.0, 0.66000000000000003, 0.51000000000000001, 0.0, 0.0]
anti_mut_r_2 = [1.0000000000000001e-05, 5.0000000000000002e-05, 0.0001, 0.00050000000000000001, 0.001]
extinction_2 = [1.0, 1.0, 1.0, 0.11320754716981132, 0.0]
anti_mut_r_3 = [1.0000000000000001e-05, 5.0000000000000002e-05, 0.0001, 0.00050000000000000001, 0.001]
extinction_3 = [1.0, 1.0, 1.0, 1.0, 0.28000000000000003]
anti_mut_r_4 = [1.0000000000000001e-05, 0.00050000000000000001]
extinction_4 = [1.0, 1.0]


fig, ax = plt.subplots(figsize=(12, 10))
font_size = 20
label_size = 25
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
matplotlib.rcParams.update({'font.size': font_size})
plot(anti_mut_r_1, extinction_1, 'o-', linewidth=3, markersize=10)
plot(anti_mut_r_2, extinction_2, 'o-', linewidth=3, markersize=10)
plot(anti_mut_r_3, extinction_3, 'o-', linewidth=3, markersize=10)
plot(anti_mut_r_4, extinction_4, 'o-', linewidth=3, markersize=10)
xscale('log')
xlabel("AntiMutator Mutation Rate")
ylabel("Extinction Percentage")
# title("N = 1000, Sexual")
legend_label = [1e-3, 5e-3, 1e-2, 5e-2]
# lg = legend(legend_label, loc=1)
# lg.draw_frame(False)
# Shink current axis's height by 10% on the bottom
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.2, 
                 box.width, box.height * 0.8])
# Put a legend below current axis
ax.legend(legend_label, loc='upper center', bbox_to_anchor=(0.5, -0.1), 
          ncol=4)
fig.savefig('Extinction_Percentage_1.pdf')