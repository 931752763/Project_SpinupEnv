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

file_2_GE_12 = open("GE_s=2_v=0.12.txt", 'r')
v_2_GE_12 = get_v(file_2_GE_12)
file_2_DRL_12 = open("DRL_s=2_v=0.12.txt", 'r')
v_2_DRL_12 = get_v(file_2_DRL_12)

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
          }
plt.rcParams.update(params)


def plot_ax1ax2():
    x = np.arange(16, 24, 0.04)
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    fig.subplots_adjust(hspace=0.3, wspace=0.1)
    ax1.plot(x, v_0_GE[400: 600], label="GE0")
    ax1.plot(x, v_0_DRL[400: 600], label="DRL0")
    ax1.set_title("joint elasticity=0Nm/rad, v=0.12m/s")
    # ax1.legend(fontsize=12, loc=1)
    ax2.plot(x, v_2_GE[400: 600], label="GE2")
    ax2.plot(x, v_2_DRL[400: 600], label="DRL2")
    ax2.set_title("joint elasticity=2Nm/rad, v=0.20m/s")
    # ax2.legend(fontsize=12, loc=1)
    lines, labels = fig.axes[-1].get_legend_handles_labels()
    # fig.legend(lines, labels, loc = 'center', fontsize=12, ncol=2, bbox_to_anchor=(0.5, 1))
    fig.text(0.5, 0, 'Time (s)', ha='center', fontsize=15, size='large', weight='heavy')
    fig.text(-.01, 0.5, 'Velocity (m/s)', va='center', rotation='vertical', fontsize=15, size='large', weight='heavy')
    fig.legend(lines, labels, loc='center', fontsize=12, ncol=4, bbox_to_anchor=(0.5, 1))

# plot_ax1ax2()


x = np.arange(16, 24, 0.04)

# plt.plot(x, v_0_GE[400: 600], label="GE0")
# plt.plot(x, v_0_DRL[400: 600], label="DRL0")

# plt.plot(x, v_2_GE[400: 600], label="GE2")
# plt.plot(x, v_2_DRL[400: 600], label="DRL2")

# plt.plot(x, v_2_GE_12[400: 600], label="GE2")
# plt.plot(x, v_2_DRL_12[400: 600], label="DRL2")

# plt.plot(x, v_0_GE[400: 600], label="GE0", color="skyblue")
plt.plot(x, v_2_GE_12[400: 600], label="GE2", color="darkblue")

# plt.plot(x, v_0_DRL[400: 600], label="DRL0", color="gold")
plt.plot(x, v_2_DRL_12[400: 600], label="DRL2", color="darkorange")

plt.xlabel('Time (s)', size='large', weight='heavy')
plt.ylabel('Velocity (m/s)', size='large', weight='heavy')
plt.legend(fontsize=12, loc=1)
# plt.savefig("../pic/s=2_v.pdf", bbox_inches="tight")
plt.show()

