import matplotlib.pyplot as plt
import matplotlib.font_manager
import numpy as np
from matplotlib import font_manager

markers = ['.', '+', 'x', '1', 'v', '*', 'h', 'H', 'd', 'P', 'D', 'X']
colors = ['black', 'rosybrown', 'lawngreen', 'sienna', 'orange', 'darkgoldenrod',
          'olive', 'steelblue', 'purple', 'lightseagreen', 'grey', 'darkgreen']
# colors = ['#1f77b4', '#ff7f0e']
# x16 = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'];


def get_scatter(file):
    list = file.readlines()
    output = []
    for fields in list:
        fields = fields.strip()
        fields = fields.strip("[]")
        fields = fields.split(",")
        output.append(fields)
    v_sin = [float(x) for x in output[0]]
    p_sin = [float(x) for x in output[1]]
    A_sin = [float(x) for x in output[2]]
    O_sin = [float(x) for x in output[3]]
    L_sin = [float(x) for x in output[4]]
    y_sin = [float(x) for x in output[5]]
    return v_sin, p_sin, A_sin, O_sin, L_sin, y_sin


def get_edge(v_sin, p_sin, A_sin, O_sin, L_sin, y_sin):
    select_v = []
    select_p = []
    # y = k x + b
    list = np.append(np.arange(0, 30, 0.1), [100])
    for k in list:
        b = 100
        index = -1
        for i in range(len(v_sin)):
            if (p_sin[i] - k * v_sin[i] < b):
                b = p_sin[i] - k * v_sin[i]
                index = i
        if index != -1:
            select_v.append(v_sin[index])
            select_p.append(p_sin[index])
            print(v_sin[index], p_sin[index], A_sin[index], O_sin[index], L_sin[index], y_sin[index])
    return select_v, select_p


def print_points(v_sin, p_sin, A_sin, O_sin, L_sin, y_sin):
    edge_v = [0]
    edge_p = [0]
    for sample_v in np.arange(0, 0.3, 0.001):
        index = 0
        min = 1000
        for i in range(len(v_sin)):
            # temp = 0.1 * (v_sin[i] - sample_v)**2 + p_sin[i]**2
            # temp = (1 - abs(v_sin[i] - sample_v) / 0.2)**3 * (1 - p_sin[i] / 5)**2
            if (abs(v_sin[i] - sample_v) <= 0.05 and p_sin[i] < min):
                index = i
                min = p_sin[i]
        if v_sin[index] > 0.01:
            edge_v.append(v_sin[index])
            edge_p.append(p_sin[index])
            print(v_sin[index], p_sin[index], A_sin[index], O_sin[index], L_sin[index], y_sin[index])
    return edge_v, edge_p

def plt_DRL_result(v, p):
    i = 0
    for key in v:
        v[key] = v[key][1:]
        p[key] = p[key][1:]

        plt.plot(v[key], p[key], color=colors[i], linewidth = 3)
        plt.scatter(v[key], p[key], s=100, marker=markers[i], label="DRL " + key + " Nm/rad", color=colors[i], linewidth = 3)
        # plt.scatter(v[key], p[key], s=100, marker=markers[i], label="DRL")#, color="#ff7f0e")
        i+=1
    plt.xlabel('Velocity (m/s)', size='large', weight='heavy')
    plt.ylabel('Average Power (W)', size='large', weight='heavy')
    plt.legend(fontsize=12)

def plt_equation_result(files):
    count = 0
    for key in files:
        v_sin, p_sin, A_sin, O_sin, L_sin, y_sin = get_scatter(files[key])

        # v_edge, p_edge = get_edge(v_sin, p_sin, A_sin, O_sin, L_sin, y_sin)

        v_edge, p_edge = print_points(v_sin, p_sin, A_sin, O_sin, L_sin, y_sin)
        plt.plot(v_edge, p_edge, label="GE " + key + " Nm/rad", linewidth = 2, color=colors[count])

        # plt.scatter(v_edge, p_edge, s=50, marker=markers[count])#, color=colors[count])

        # plt.scatter(v_sin, p_sin, alpha=0.5, s=30, label='GE')#, color=colors[count])#)
        # plt.plot(v_edge, p_edge, linewidth = 3, label="Contour line", color="r")

        # print_points(v_sin, p_sin, A_sin, O_sin, L_sin, y_sin)

        plt.xlabel('Velocity (m/s)', size='large', weight='heavy')
        plt.ylabel('Average Power (W)', size='large', weight='heavy')
        plt.legend(fontsize=12)
        count+=1

        # select_v, select_p = get_edge(v_sin, p_sin, A_sin, O_sin, L_sin, y_sin)
        # polynomial_model = np.polyfit(v_print, p_print, 2)
        # polynomial_model_fn = np.poly1d(polynomial_model)
        # x_s = np.arange(0, v_print[len(v_print) - 1], 0.01)
        # plt.plot(x_s, polynomial_model_fn(x_s), linewidth=3, label='stiffness=' + '%.1f'%i)

def plt_compare(v, p, files, x, y):
    fig, axes = plt.subplots(x, y, sharex=True, sharey=True)

    fig.subplots_adjust(hspace=0.4, wspace=0.1)
    count = 0
    for key in files:
        v_sin, p_sin, A_sin, O_sin, L_sin, y_sin = get_scatter(files[key])
        v_print, p_print = print_points(v_sin, p_sin, A_sin, O_sin, L_sin, y_sin)
        cur = axes[int(count/y), int(count%y)]
        cur.plot(v_print, p_print, linewidth = 2, label="GE", color='b')

        v[key] = v[key][1:]
        p[key] = p[key][1:]
        cur.plot(v[key], p[key], label="DRL", color='r')
        # cur.scatter(v[key], p[key], label="DRL", color='r')
        cur.set_title(key + "Nm/rad")
        # cur.xticks(fontsize=12)
        count += 1

    lines, labels = fig.axes[-1].get_legend_handles_labels()
    fig.legend(lines, labels, loc = 'center', fontsize=12, ncol=2, bbox_to_anchor=(0.5, 1))

    fig.text(0.5, 0, 'Velocity (m/s)', ha='center', fontsize=15, size='large', weight='heavy')
    fig.text(0.05, 0.5, 'Average Power (W)', va='center', rotation='vertical', fontsize=15, size='large', weight='heavy')

    # Hide x labels and tick labels for top plots and y ticks for right plots.
    # for ax in axs.flat:
    #     ax.label_outer()

def plt_p_of_target_v_by_files(files, target_v_list):
    v_sin, p_sin = {}, {}
    for key in files:
        v_sin[key], p_sin[key], _, _, _, _ = get_scatter(files[key])
    n = len(target_v_list)
    fig, axs = plt.subplots(n, 1, sharex=True, figsize=(6.4, 7))
    # fig.figure(figsize=(6.4, 10))
    for index in range(n):
        v_p = {}
        target_v = target_v_list[index]
        for key in files:
            min = 1000
            for i in range(len(v_sin[key])):
                if(abs(v_sin[key][i] - target_v) < 0.01 and p_sin[key][i] < min):
                    min = p_sin[key][i]
            if min != 1000: v_p[float(key)] = min
            print(key, min)
        axs[index].plot(list(v_p.keys()), list(v_p.values()), linewidth = 2, label=str(target_v)+" m/s", color=colors[index])
        # axs[index].set_yticks(np.arange(v_p[0.5], v_p[0.5]*5))
        axs[index].legend(fontsize=12)
    # plt.xticks(range(0,11,1))
    fig.text(0.5, 0.04, 'Stiffness (Nm/rad)', ha='center', fontsize=15, size='large', weight='heavy')
    fig.text(0, 0.5, 'Average Power (W)', va='center', rotation='vertical', fontsize=15, size='large', weight='heavy')

def plt_p_of_target_v_by_vp(v, p, target_v_list):
    n = len(target_v_list)
    fig, axs = plt.subplots(n, 1, sharex=True, figsize=(6.4, 7))
    for index in range(n):
        v_p = {}
        target_v = target_v_list[index]
        for key in v:
            min = 1000
            for i in range(len(v[key])):
                if(abs(v[key][i] - target_v) < 0.01 and p[key][i] < min):
                    min = p[key][i]
            if min != 1000: v_p[float(key)] = min
            print(key, min)
        axs[index].plot(list(v_p.keys()), list(v_p.values()), linewidth = 2, label=str(target_v)+" m/s", color=colors[index])
        # axs[index].set_yticks(np.arange(v_p[0.5], v_p[0.5]*5))
        axs[index].legend(fontsize=12)
    # plt.xticks(range(0,11,1))
    fig.text(0.5, 0.04, 'Stiffness (Nm/rad)', ha='center', fontsize=15, size='large', weight='heavy')
    fig.text(0, 0.5, 'Average Power (W)', va='center', rotation='vertical', fontsize=15, size='large', weight='heavy')

def get_max_v(files=None, v=None):
    max_v = {}
    if files != None:
        for key in files:
            v_sin, p_sin, A_sin, O_sin, L_sin, y_sin = get_scatter(files[key])
            max = 0
            for i in range(len(v_sin)):
                if(v_sin[i] > max):
                    max = v_sin[i]
            max_v[float(key)] = max
            print(key, max)
    if v != None:
        for key in v:
            max = 0
            for i in range(len(v[key])):
                if(v[key][i] > max):
                    max = v[key][i]
            max_v[float(key)] = max
            print(key, max)
    return max_v

def plt_max_v_by_files(files):
    max_v = get_max_v(files=files)
    plt.plot(list(max_v.keys()), list(max_v.values()), linewidth = 2)
    plt.xticks(range(0,11,1))
    plt.xlabel('Stiffness (Nm/rad)', size='large', weight='heavy')
    plt.ylabel('Max velocity (m/s)', size='large', weight='heavy')

def plt_max_v_by_vp(v, p):
    max_v = get_max_v(v=v)
    plt.plot(list(max_v.keys()), list(max_v.values()), linewidth = 2)
    plt.xticks(range(0,11,1))
    plt.xlabel('Stiffness (Nm/rad)', size='large', weight='heavy')
    plt.ylabel('Max velocity (m/s)', size='large', weight='heavy')

def plt_max_v(v, p, files):
    max_v_GE = get_max_v(files=files)
    max_v_DRL = get_max_v(v=v)
    fig, ax1 = plt.subplots()

    ax1.set_xticks(range(0,11,1))
    ax1.set_xlabel('Stiffness (Nm/rad)', size='large', weight='heavy')
    ax1.set_ylabel('Max velocity (m/s)', size='large', weight='heavy')
    ax1.set_ylim(0.12, 0.3)

    ax2 = ax1.twinx()
    ax2.set_ylim(0.12, 0.3)
    ax2.plot(list(max_v_GE.keys()), list(max_v_GE.values()), linewidth = 2, label="GE")
    ax2.plot(list(max_v_DRL.keys()), list(max_v_DRL.values()), linewidth = 2, label="DRL")

    plt.legend(fontsize=12)


font_manager._rebuild()
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
# plt.xlabel('Velocity (m/s)', size='large', weight='heavy')
# plt.ylabel('Average Power (W)', size='large', weight='heavy')



