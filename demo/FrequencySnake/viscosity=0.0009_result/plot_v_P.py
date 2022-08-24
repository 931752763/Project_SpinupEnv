import matplotlib.pyplot as plt
import numpy as np

def get_v(file):
    list = file.readlines()
    output = []
    for fields in list:
        fields = fields.strip()
        fields = fields.strip("[]")
        fields = fields.split(",")
        output.append(fields)
    v = [float(x) for x in output[0]]
    return v

file_0_GE = open("80.0_0.2_20.0_0.2_s=0_v=0.117.txt", 'r')
v_0_GE = get_v(file_0_GE)
file_0_DRL = open("DRL_s=0_v=0.124.txt", 'r')
v_0_DRL = get_v(file_0_DRL)
file_2_GE = open("150.0_0.5_30.0_1.0_s=2_v=0.201.txt", 'r')
v_2_GE = get_v(file_2_GE)
file_2_DRL = open("DRL_s=2_v=0.199.txt", 'r')
v_2_DRL = get_v(file_2_DRL)

p_0_GE = [0.01227246, 0.02953293, 0.04960382, 0.0658519, 0.07883105, 0.0953582]
p_0_DRL = [0.05658921, 0.05661467, 0.059972, 0.06164008, 0.04148059, 0.03349776]
p_2_GE = [0.11299039, 0.10300982, 0.14242584, 0.17851861, 0.17307953, 0.14627116]
p_2_DRL = [0.03583858, 0.10524179, 0.17197304, 0.06944944, 0.04635233, 0.02576122]

p_GE2_spring = [3.14369175, 2.69052683, 3.55082828, 4.70762122, 4.9825541, 4.28145535]
p_DRL2_spring = [3.18477493, 4.30882873, 5.15427154, 4.60399627, 5.52944167, 4.0563301]

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

fig, (ax1, ax2) = plt.subplots(2, 1)
fig.subplots_adjust(hspace=0.5, wspace=0.1)

# x1 = np.arange(16, 24, 0.04)
# ax1.plot(x1, v_0_GE[400: 600], label="GE0")
# ax1.plot(x1, v_0_DRL[400: 600], label="DRL0")
# # ax1.legend(fontsize=12)
# ax1.set_xlabel('Time (s)', fontsize=15, weight='heavy')
# ax1.set_ylabel('Velocity (m/s)', fontsize=15, weight='heavy')
#
# bar_width = 0.3  # 设置柱状图的宽度
# tick_label = np.arange(1, 7)
# x2 = np.arange(1, 7)  # 柱状图在横坐标上的位置
# ax2.bar(x2, p_0_GE, bar_width, label="GE0")
# ax2.bar(x2 + 1 * bar_width, p_0_DRL, bar_width, label="DRL0")
# plt.xticks(x2 + bar_width * .5, tick_label)
# # ax2.legend(fontsize=12)
# ax2.set_xlabel('Motor index', fontsize=15, weight='heavy')
# ax2.set_ylabel('Average Power (W)', fontsize=15, weight='heavy')


x1 = np.arange(16, 24, 0.04)
ax1.plot(x1, v_2_GE[400: 600], label="GE2")
ax1.plot(x1, v_2_DRL[400: 600], label="DRL2")
# ax1.legend(fontsize=12)
ax1.set_xlabel('Time (s)', fontsize=15, weight='heavy')
ax1.set_ylabel('Velocity (m/s)', fontsize=15, weight='heavy')

bar_width = 0.3  # 设置柱状图的宽度
tick_label = np.arange(1, 7)
x2 = np.arange(1, 7)  # 柱状图在横坐标上的位置
ax2.bar(x2, p_2_GE, bar_width, label="GE2")
ax2.bar(x2 + 1 * bar_width, p_2_DRL, bar_width, label="DRL2")
# ax2.bar(x2 + 2 * bar_width, p_GE2_spring, bar_width, label="GE2_spring")
# ax2.bar(x2 + 3 * bar_width, p_DRL2_spring, bar_width, label="DRL2_spring")
plt.xticks(x2 + bar_width * .5, tick_label)
# ax2.legend(fontsize=12)
ax2.set_xlabel('Motor index', fontsize=15, weight='heavy')
ax2.set_ylabel('Average Power (W)', fontsize=15, weight='heavy')

lines, labels = [], []
for ax in fig.axes:
    axLine, axLabel = ax.get_legend_handles_labels()
    lines.extend(axLine)
    labels.extend(axLabel)
fig.legend(lines, labels, loc = 'center', fontsize=12, ncol=4, bbox_to_anchor=(0.5, 0.95))

# fig.text(0.5, 0, 'Time (s)', ha='center', fontsize=15, size='large', weight='heavy')
# fig.text(-.01, 0.5, 'Velocity (m/s)', va='center', rotation='vertical', fontsize=15, size='large', weight='heavy')
# fig.legend(lines, labels, loc = 'center', fontsize=12, ncol=4, bbox_to_anchor=(0.5, 1))
plt.savefig("../pic/vp2.eps", bbox_inches="tight")
plt.show()

