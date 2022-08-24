from sys import stdin
from mujoco_py import load_model_from_path, MjSim, MjViewer
import math
import matplotlib.pyplot as plt
import time

model = load_model_from_path("FreqSwimmer6_torque.xml")
# model = load_model_from_path("FreqSwimmer6.xml")
sim = MjSim(model)
viewer = MjViewer(sim)
NUM_OF_JOINTS = 6
TIMESTEPS = 0.01
MOMENT_OF_INERTIA = 1.0
TOTAL_EPOCH = 1000
START_EPOCH = 300
END_EPOCH = 900
pos_start = 0
pos_end = 0
t = 0
amplitude, omega, lamda, y = 1.0, 0.2, 30, 1.0

v = []
p = []
pos = []
posy = []
average_power_efficiency = 0
fp = 0
average_velocity = 0
# for y in [0.1, 0.2, 0.3, 0.4]:
while t < TOTAL_EPOCH:
    # for frame_skip in range(FRAME_SKIP):
    for i in range(NUM_OF_JOINTS):
        # sim.data.ctrl[i] = amplitude / 180.0 * math.pi\
        #                    * math.sin(omega * t - lamda / 180.0 * math.pi * i)\
        #                    * (i/NUM_OF_JOINTS * (1-y) + y)
        sim.data.ctrl[i] = amplitude * math.sin(omega * t - lamda / 180.0 * math.pi * i) \
                                           * (i / NUM_OF_JOINTS * (1 - y) + y)
    sensordata_before = sim.data.sensordata.copy()
    t += 1
    for _ in range(4):
        sim.step()

    viewer.render()
    sensordata_after = sim.data.sensordata.copy()
    sensordata_delta = (sensordata_after - sensordata_before) / (TIMESTEPS * 4)

    f = sim.data.actuator_force.copy()
    temp_fp = 0
    for i in range(0, 6):
        temp_fp += abs(f[i] * sim.data.qvel[3+i])
    p.append(temp_fp)

    # print(sim.data.qvel)
    current_velocity_x = 0
    current_velocity_y = 0
    average_pos_after = 0
    average_pos_y = 0
    for i in range(0,7):
        current_velocity_x += sensordata_delta[18+i*3]
        current_velocity_y += sensordata_delta[19+i*3]
        average_pos_after += sim.data.sensordata[18+i*3]
        average_pos_y += sim.data.sensordata[19+i*3]
    pos.append(average_pos_after / 7)
    posy.append(average_pos_y / 7)

    current_velocity_x /= 7
    current_velocity_y /= 7
    cur_v = (current_velocity_x ** 2 + current_velocity_y ** 2) ** 0.5
    v.append(cur_v)
    if(t >= START_EPOCH and t <= END_EPOCH):
        average_velocity += cur_v
        fp += temp_fp

    # if(t == 5000 or t == 5400 or t == 5800):
    #     time.sleep(5)

average_velocity = average_velocity / (END_EPOCH - START_EPOCH)
print(average_velocity)
# print(qvel / (END_EPOCH - START_EPOCH))
# print((pos_end - pos_start) / (TIMESTEPS * (END_EPOCH - START_EPOCH)))
# average_power_efficiency = average_power_efficiency / (TOTAL_EPOCH - START_EPOCH)
# print(average_power_efficiency)
fp = fp / (END_EPOCH - START_EPOCH)
print(fp)

# plt.figure(1)
# plt.plot(range(len(v)), v)
#
# plt.figure(2)
# plt.plot(range(len(p)), p)
#
# plt.figure(3)
# plt.plot(range(len(posy)), posy)
#
# plt.show()
