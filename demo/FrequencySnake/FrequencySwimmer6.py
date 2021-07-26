import time
import numpy as np
from mujoco_py import load_model_from_path, MjSim, MjViewer
import math
import matplotlib.pyplot as plt
import os

NUM_OF_JOINTS = 6
TIMESTEPS = 0.005
MOMENT_OF_INERTIA = 1.0
TOTAL_EPOCH = 30000
START_EPOCH = 10000
v = []
p = []
average_velocity = 0
# average_power_efficiency = 0
fp = 0
maxP = 0
# plt.ion()
# fig = plt.figure()
# for y in range(0.1, 0.5, 0.1):
for amplitude in range(30, 180, 20):
    for omega in np.arange(0.001, 0.01, 0.001):
        for lamda in range(10, 180, 20):
            for y in np.arange(0.1, 0.5, 0.1):
                model = load_model_from_path("FrequencySwimmer6.xml")
                sim = MjSim(model)
                t = 0
                while t < TOTAL_EPOCH:
                    for i in range(NUM_OF_JOINTS):
                        sim.data.ctrl[i] = amplitude / 360.0 * math.pi * \
                                                       math.sin(omega * t - lamda / 360.0 * math.pi * i) * (i/NUM_OF_JOINTS * (1-y) + y)

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
                        temp_fp = temp_fp + abs(f[i] * angular_velocity_after[i*3+2])

                    current_velocity = sim.data.qvel[0]

                    if(t >= START_EPOCH):
                        average_velocity = average_velocity + current_velocity
                        fp = fp + temp_fp

                    # if(maxP < temp_fp):
                    #     maxP = temp_fp
                    #     print(maxP)

                average_velocity = average_velocity / (TOTAL_EPOCH - START_EPOCH)
                v.append(average_velocity)
                fp = fp / (TOTAL_EPOCH - START_EPOCH)
                p.append(fp)

                # if(average_power_efficiency < 40 and average_velocity > 0.1):
                print(amplitude, omega, lamda, y, average_velocity, fp)

                # plt.scatter(v, p)
                # # re-drawing the figure
                # fig.canvas.draw()
                #
                # # to flush the GUI events
                # fig.canvas.flush_events()
print(maxP)
plt.scatter(v, p)
plt.show()
