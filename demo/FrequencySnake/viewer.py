from mujoco_py import load_model_from_path, MjSim, MjViewer
import math
import matplotlib.pyplot as plt
import time

model = load_model_from_path("FrequencySwimmer6.xml")
sim = MjSim(model)
viewer = MjViewer(sim)
NUM_OF_JOINTS = 6
TIMESTEPS = 0.005
MOMENT_OF_INERTIA = 1.0
TOTAL_EPOCH = 30000
START_EPOCH = 10000
END_EPOCH = 29000
pos_start = 0
pos_end = 0
t = 0
amplitude = 100
omega = 0.007
lamda = 100
y = 0.4
v = []
p = []
pos = []
average_power_efficiency = 0
fp = 0
average_velocity = 0
GEAR = 1
# for y in [0.1, 0.2, 0.3, 0.4]:
while t < TOTAL_EPOCH:
    # for frame_skip in range(FRAME_SKIP):
    for i in range(NUM_OF_JOINTS):
        sim.data.ctrl[i] = amplitude / 360.0 * math.pi * \
                                       math.sin(omega * t - lamda / 360.0 * math.pi * i) * (i/NUM_OF_JOINTS * (1-y) + y)

    sensordata_before = sim.data.sensordata.copy()
    # print(sim.data.sensordata)
    # print(sim.data.xfrc_applied)
    average_pos_after = 0

    sim.step()
    t += 1
    viewer.render()

    sensordata_after = sim.data.sensordata.copy()
    sensordata_delta = (sensordata_after - sensordata_before) / TIMESTEPS
    # w = abs(sensordata_delta / TIMESTEPS)
    # current_power_efficiency = MOMENT_OF_INERTIA * w * sensordata_after
    # current_power_efficiency = sum(abs(current_power_efficiency))
    # p.append(current_power_efficiency)

    f = sim.data.actuator_force.copy()
    temp_fp = 0
    for i in range(0, 6):
        temp_fp += abs(f[i] * [i*3+2])
    p.append(temp_fp)

    # print(sim.data.qpos)
    current_velocity = 0
    average_pos_after = 0
    for i in range(0,7):
        current_velocity += sensordata_delta[18+i*3]
        average_pos_after += sim.data.sensordata[18+i*3]
    current_velocity /= 7
    pos.append(average_pos_after / 7)
    v.append(current_velocity)
    if(t >= START_EPOCH and t <= END_EPOCH):
        average_velocity += current_velocity
        # qvel += sim.data.qvel[0]
        # average_power_efficiency = average_power_efficiency + current_power_efficiency
        fp += temp_fp

average_velocity = average_velocity / (END_EPOCH - START_EPOCH)
print(average_velocity)
# print(qvel / (END_EPOCH - START_EPOCH))
# print((pos_end - pos_start) / (TIMESTEPS * (END_EPOCH - START_EPOCH)))
# average_power_efficiency = average_power_efficiency / (TOTAL_EPOCH - START_EPOCH)
# print(average_power_efficiency)
fp = fp / (END_EPOCH - START_EPOCH)
print(fp)

plt.figure(1)
plt.plot(range(len(v)), v)

plt.figure(2)
plt.plot(range(len(p)), p)

plt.figure(3)
plt.plot(range(len(pos)), pos)

plt.show()
