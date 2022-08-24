from spinup.utils.test_policy import load_policy_and_env, run_policy
from mujoco_py import load_model_from_path, MjSim, MjViewer
import time
import joblib
import os
import os.path as osp
import tensorflow as tf
import torch
import math
import numpy as np
import matplotlib.pyplot as plt
from spinup import EpochLogger

path = "/home/zheng/spinningup/data/paper_10.11/water/z2021-12-26_11:36:58_m_gear=0.1_a=0.01_d=0.01_s=2_"
# path = "/home/zheng/spinningup/data/paper_10.11/water/z2021-12-21_11:00:53_m_gear=0.1_a=0.01_d=0.01_s=0_"
# path = "/home/zheng/spinningup/data/paper_10.11/water/2022-01-20_15:01:09position_s=0_"
env, get_action = load_policy_and_env(path, itr=10000)
# model = load_model_from_path(path + "/FreqSwimmer6.xml")
# env = MjSim(model)
# viewer = MjViewer(env)
logger = EpochLogger()
GEAR = 0.1
TIMESTEPS = 0.01
TOTAL_EPOCH = 1000
START_EPOCH = 200
END_EPOCH = 800
STIFFNESS = 2
t = 0
qvel = 0
fp = 0
p_joint = [0, 0, 0, 0, 0, 0]
p_spring = [0, 0, 0, 0, 0, 0]
v = []
o, r, d, ep_ret, ep_len, n = env.reset(), 0, False, 0, 0, 0
v_range = np.arange(-1, 1, 0.02)
v_count = np.zeros(100)
v_reward = 0
pos_start = []
pos_end = []
while t < TOTAL_EPOCH:

    env.render()
    sensordata_before = env.data.sensordata.copy()
    a = get_action(o)
    o, r, d, dict = env.step(a)
    sensordata_after = env.data.sensordata.copy()
    sensordata_delta = (sensordata_after - sensordata_before) / 0.04
    # print(dict)
    ep_ret += r
    ep_len += 1
    f = env.data.actuator_force.copy()
    print(sensordata_after)
    print(env.data.qvel)
    temp_fp = 0
    # print(env.data.qpos[1])
    average_pos_y = 0
    for i in range(0, 6):
        # temp_fp += abs(f[i] * env.data.sensordata.copy()[i*3+2])
        temp_fp += abs(f[i] * env.data.qvel[3 + i]) * GEAR
        average_pos_y += abs(sensordata_after[19 + i * 3])
    vx = 0
    for i in range(0, 7):
        vx += sensordata_delta[18 + i * 3]
    vx /= 7
    v.append(vx)
    v_head = env.data.qvel[0]
    # v.append(v_head)
    v_reward += pow(1 - abs(v_head - 0.2) / 0.2, 5)
    if (v_head % 0.02 <= 0.01):
        v_count[math.floor(vx // 0.02) + 48] += 1
    else:
        v_count[math.floor(vx // 0.02) + 49] += 1
    if (t >= START_EPOCH and t <= END_EPOCH):
        qvel += v_head
        # average_power_efficiency = average_power_efficiency + current_power_efficiency
        fp += temp_fp
        for i in range(0, 6):
            p_joint[i] += abs(f[i] * env.data.qvel[3 + i]) * GEAR
            p_spring[i] += abs(STIFFNESS * env.data.qvel[3 + i])
    if (t == START_EPOCH): pos_start = env.data.qpos.copy()
    if (t == END_EPOCH): pos_end = env.data.qpos.copy()

    # if d or (ep_len == 10000):
    #     logger.store(EpRet=ep_ret, EpLen=ep_len)
    #     print('Episode %d \t EpRet %.3f \t EpLen %d'%(n, ep_ret, ep_len))
    #     o, r, d, ep_ret, ep_len = env.reset(), 0, False, 0, 0
    #     n += 1

    # if(t == 400 or t == 410 or t == 420):
    if (t == 200):
        time.sleep(2)
    t += 1
vel = (pos_end - pos_start) / (TIMESTEPS * 4 * (END_EPOCH - START_EPOCH))
average_velocity = (vel[0] ** 2 + vel[1] ** 2) ** 0.5
print(average_velocity)
print("v = " + str(qvel / (END_EPOCH - START_EPOCH)))
print("p = " + str(fp / (END_EPOCH - START_EPOCH)))
print("v_reward = " + str(v_reward))

plt.figure(1)
plt.plot(range(len(v)), v)

plt.figure(2)
p_joint = np.divide(p_joint, (END_EPOCH - START_EPOCH))
print(p_joint)
plt.bar(range(len(p_joint)), p_joint)

plt.figure(3)
p_spring = np.divide(p_spring, (END_EPOCH - START_EPOCH))
print(p_spring)
plt.bar(range(len(p_spring)), p_spring)

plt.figure(4)
plt.bar(v_range, v_count, width=0.01)
plt.show()

file = open("../viscosity=0.0009_result/DRL_s=2_v=0.12.txt", 'w')
file.writelines(str(v))
