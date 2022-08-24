import time
import numpy as np
from mujoco_py import load_model_from_path, MjSim, MjViewer
import math
import matplotlib.pyplot as plt
import os

NUM_OF_JOINTS = 6
TIMESTEPS = 0.005
MOMENT_OF_INERTIA = 1.0
TOTAL_EPOCH = 15000
START_EPOCH = 5000

V = []
P = []
A = []  #amplitude
O = []  #omega
L = []  #lambda
Y = []  #y

amplitude_color = []
omega_color = []
lamda_color = []
average_velocity = 0
# average_power_efficiency = 0
fp = 0
maxP = 0
bestCase = [0,0,0,0,0,0]
b = 0
# plt.ion()
# fig = plt.figure()

for amplitude in range(10, 91, 10):  #
    for omega in np.arange(0.0001, 0.01, 0.0001):  # 0.001 - 0.01
        for lamda in range(10, 181, 10):  # 10 - 180
            for y in np.arange(0.1, 0.5, 0.1):  # 0.1 - 0.5
                model = load_model_from_path("FreqSwimmer6.xml")
                sim = MjSim(model)
                t = 0
                while t < TOTAL_EPOCH:
                    for i in range(NUM_OF_JOINTS):
                        # -180:180 === ctrl signal -1:1
                        sim.data.ctrl[i] = amplitude / 180.0 * math.pi * \
                                           math.sin(omega * t - lamda / 180.0 * math.pi * i) * (
                                                       i / NUM_OF_JOINTS * (1 - y) + y)

                    angular_velocity_before = sim.data.sensordata.copy()

                    t += 1
                    sim.step()

                    angular_velocity_after = sim.data.sensordata.copy()
                    # w = abs((angular_velocity_after - angular_velocity_before) / TIMESTEPS)
                    # current_power_efficiency = w * abs(angular_velocity_after)
                    # current_power_efficiency = sum(abs(current_power_efficiency))

                    f = sim.data.actuator_force.copy()
                    temp_fp = 0
                    for i in range(0, 6):
                        temp_fp = temp_fp + abs(f[i] * angular_velocity_after[i * 3 + 2])

                    current_velocity = sim.data.qvel[0]

                    if (t >= START_EPOCH):
                        average_velocity = average_velocity + current_velocity
                        fp = fp + temp_fp

                average_velocity = average_velocity / (TOTAL_EPOCH - START_EPOCH)
                fp = fp / (TOTAL_EPOCH - START_EPOCH)
                V.append(average_velocity)
                P.append(fp)
                A.append(amplitude)
                O.append(omega)
                L.append(lamda)
                Y.append(y)

                # find a good case to view
                if(fp - 600 * average_velocity < b):
                    b = fp - 600 * average_velocity
                    bestCase[0] = average_velocity
                    bestCase[1] = fp
                    bestCase[2] = amplitude
                    bestCase[3] = omega
                    bestCase[4] = lamda
                    bestCase[5] = y

                # amplitude_color.append(colors[int(amplitude / 30) - 1])
                # omega_color.append(colors[int(omega / 0.001) - 1])
                # lamda_color.append(colors[int(lamda / 30) - 1])

                # if(average_power_efficiency < 40 and average_velocity > 0.1):
                print(amplitude, omega, lamda, y, average_velocity, fp)

                # plt.scatter(v, p)
                # # re-drawing the figure
                # fig.canvas.draw()
                #
                # # to flush the GUI events
                # fig.canvas.flush_events()

print("bestCase is:")
print(bestCase)

plt.figure(0)
plt.scatter(V, P)
plt.show()

file = open("/home/zheng/spinningup/data/water_stiffness_damping/freq_stiffness=10_10_0.0001_10.txt", 'w')
file.writelines(str(V)+'\n')
file.writelines(str(P)+'\n')
file.writelines(str(A)+'\n')
file.writelines(str(O)+'\n')
file.writelines(str(L)+'\n')
file.writelines(str(Y)+'\n')
