import matplotlib.pyplot as plt
import numpy as np

p_0_GE = [0.01227246, 0.02953293, 0.04960382, 0.0658519, 0.07883105, 0.0953582] #v=0.117 p=0.332

p_0_DRL = [0.05658921, 0.05661467, 0.059972, 0.06164008, 0.04148059, 0.03349776] #v=0.124 p=0.309

p_2_GE = [0.11299039, 0.10300982, 0.14242584, 0.17851861, 0.17307953, 0.14627116] #v=0.201 p=0.856

p_2_DRL = [0.03583858, 0.10524179, 0.17197304, 0.06944944, 0.04635233, 0.02576122] #v=0.199 p=0.455

p_2_GE_12 = [0.02590069, 0.02925444, 0.04655662, 0.05484117, 0.05154812, 0.04691202] #v=0.124 p=0.255

p_2_DRL_12 = [0.01511133, 0.025327, 0.08470376, 0.02176908, 0.00724812, 0.00300211] #v=0.120 p=0.155

params = {
    'font.family': 'DeJavu Serif',
    'font.serif': 'Times New Roman',
    # 'font.style': 'italic',
    'font.weight': 'bold',  # or 'bold'
    'font.size': 15,  # or large,small
    'axes.labelweight': 'bold',
    'axes.titleweight': 'bold',
    'axes.titlesize': 12,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
}
plt.rcParams.update(params)

# bar_width = 0.3  # 设置柱状图的宽度
# tick_label = np.arange(1, 7)
# x = np.arange(1, 7)  # 柱状图在横坐标上的位置

# plt.bar(x + 0 * bar_width, p_0_GE, bar_width, label="GE, joint elasticity=0Nm/rad, v=0.117m/s")
# plt.bar(x + 1 * bar_width, p_0_DRL, bar_width, label="DRL, joint elasticity=0Nm/rad, v=0.124m/s")
# plt.bar(x + 2 * bar_width, p_2_GE, bar_width, label="GE, joint elasticity=2Nm/rad, v=0.201m/s")
# plt.bar(x + 3 * bar_width, p_2_DRL, bar_width, label="DRL, joint elasticity=2Nm/rad, v=0.199m/s")
#
# plt.xticks(x + bar_width * 1.5, tick_label)
# plt.xlabel('Motor (left: head, right: tail)', size='large', weight='heavy')
# plt.ylabel('Velocity (m/s)', size='large', weight='heavy')
# plt.legend(fontsize=12)
# plt.show()

def plot_ax1ax2():
    bar_width = 0.3  # 设置柱状图的宽度
    tick_label = np.arange(1, 7)
    x = np.arange(1, 7)  # 柱状图在横坐标上的位置
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    fig.subplots_adjust(hspace=0.3, wspace=0.1)
    ax1.bar(x, p_0_GE, bar_width, label="GE")
    ax1.bar(x + 1 * bar_width, p_0_DRL, bar_width, label="DRL")
    ax1.set_title("joint elasticity=0Nm/rad, v=0.12m/s")
    plt.xticks(x + bar_width * .5, tick_label)
    ax2.bar(x, p_2_GE, bar_width, label="GE")
    ax2.bar(x + 1 * bar_width, p_2_DRL, bar_width, label="DRL")
    ax2.set_title("joint elasticity=2Nm/rad, v=0.20m/s")
    plt.xticks(x + bar_width * .5, tick_label)
    lines, labels = fig.axes[-1].get_legend_handles_labels()
    # fig.legend(lines, labels, loc = 'center', fontsize=12, ncol=2, bbox_to_anchor=(0.5, 1))
    fig.text(0.5, 0, 'Motor index', ha='center', fontsize=15, size='large', weight='heavy')
    fig.text(-.01, 0.5, 'Average Power (W)', va='center', rotation='vertical', fontsize=15, size='large',
             weight='heavy')
    fig.legend(lines, labels, loc='center', fontsize=12, ncol=2, bbox_to_anchor=(0.5, 1))

# plot_ax1ax2()

bar_width = 0.3  # 设置柱状图的宽度
tick_label = np.arange(1, 7)
x = np.arange(1, 7)  # 柱状图在横坐标上的位置

# plt.bar(x, p_0_GE, bar_width, label="GE0")
# plt.bar(x + 1 * bar_width, p_0_DRL, bar_width, label="DRL0")

# plt.bar(x, p_2_GE, bar_width, label="GE2")
# plt.bar(x + 1 * bar_width, p_2_DRL, bar_width, label="DRL2")

# plt.bar(x, p_2_GE_12, bar_width, label="GE2")
# plt.bar(x + 1 * bar_width, p_2_DRL_12, bar_width, label="DRL2")

# colored
# plt.bar(x - 0.5 * bar_width, p_0_GE, bar_width, label="GE0", color="skyblue")
plt.bar(x - 0.5 * bar_width, p_2_GE_12, bar_width, label="GE2", color="darkblue")

# plt.bar(x + 0.5 * bar_width, p_0_DRL, bar_width, label="DRL0", color="gold")
plt.bar(x + 0.5 * bar_width, p_2_DRL_12, bar_width, label="DRL2", color="darkorange")

# bar_width = 0.2
# plt.bar(x - 1.5 * bar_width, p_0_GE, bar_width, label="GE0", color="skyblue")
# plt.bar(x - 0.5 * bar_width, p_2_GE_12, bar_width, label="GE2", color="darkblue")
# plt.bar(x + 0.5 * bar_width, p_0_DRL, bar_width, label="DRL0", color="gold")
# plt.bar(x + 1.5 * bar_width, p_2_DRL_12, bar_width, label="DRL2", color="darkorange")

plt.xlabel('Motor index', size='large', weight='heavy')
plt.ylabel('Average Power (W)', size='large', weight='heavy')
plt.legend(fontsize=12)
plt.savefig("../pic/s=2_p.pdf", bbox_inches="tight")
plt.show()
