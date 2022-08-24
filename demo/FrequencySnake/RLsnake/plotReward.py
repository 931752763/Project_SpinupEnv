import matplotlib.pyplot as plt
import numpy as np

file = open("/home/zheng/spinningup/data/paper_10.11/water/z2021-12-21_11:00:53_m_gear=0.1_a=0.01_d=0.01_s=0_/progress.txt","r")
file_noc = open("/home/zheng/spinningup/data/paper_10.11/water/2022-02-07_19:34:32nocurriculum_s=0_/progress.txt","r")
list = file.readlines()
AverageEpRet = []
for i in range(1, len(list), 1):
    line = list[i]
    a = line.split(" ")
    b = line.split("\t")
    AverageEpRet.append(float(b[1]))

list_noc = file_noc.readlines()
AverageEpRet_noc = []
for i in range(1, len(list_noc), 1):
    line = list_noc[i]
    a = line.split(" ")
    b = line.split("\t")
    AverageEpRet_noc.append(float(b[1]))

plt.figure(0)
params = {
    'font.family': 'DeJavu Serif',
    'font.serif': 'Times New Roman',
    # 'font.style': 'italic',
    'font.weight': 'bold',  # or 'bold'
    'font.size': 15,  # or large,small
    'axes.labelweight' : 'bold',
    'axes.titleweight' : 'bold',
    'axes.titlesize' : 12,
    'xtick.labelsize' : 12,
    'ytick.labelsize' : 12,
    'pdf.fonttype': 42,
    'ps.fonttype': 42
}
plt.rcParams.update(params)

plt.xlabel('Training iterations', size='large', weight='heavy')
plt.ylabel('Rewards', size='large', weight='heavy')

print(len(AverageEpRet_noc))
plt.plot(np.arange(0, len(AverageEpRet_noc), 100), AverageEpRet_noc[0: len(AverageEpRet_noc): 100]
         , label="no curriculum, target=0.1m/s", linestyle="--", linewidth=3)
plt.plot(np.arange(0, 2000), AverageEpRet[0: 2000], label="curriculum, easy task", linewidth=3)
for i in range(0,7):
    plt.plot(range(i*1000+2000, i*1000+3000), AverageEpRet[i*1000+2000: i*1000+3000],
                label="curriculum, target=" + str((7-i) * 0.02) + "m/s", linewidth=3)

# plt.scatter(range(len(AverageEpRet)), AverageEpRet, label="simple to complex, target velocity=" + str((7-i) * 0.02) + "m/s")
# plt.scatter(range(len(AverageEpRet_xv)), AverageEpRet_xv, label="direct complex, target velocity=0.1m/s")
plt.legend(fontsize=11)
plt.savefig("../pic/reward.jpg", dpi=300, bbox_inches="tight")
plt.show()
