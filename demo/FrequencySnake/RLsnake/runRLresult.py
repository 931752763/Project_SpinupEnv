from spinup.utils.test_policy import load_policy_and_env, run_policy
from mujoco_py import load_model_from_path, MjSim, MjViewer
import time
import joblib
import os
import os.path as osp
import tensorflow as tf
import torch
import math
import matplotlib.pyplot as plt
from spinup import EpochLogger

env, get_action = load_policy_and_env("/home/zheng/spinningup/data/swimmer6_2021-07-25_13:11")
logger = EpochLogger()
TOTAL_EPOCH = 3000
START_EPOCH = 1000
END_EPOCH = 2900
t = 0
qvel = 0
fp = 0
v = []
o, r, d, ep_ret, ep_len, n = env.reset(), 0, False, 0, 0, 0
while t < TOTAL_EPOCH:

    env.render()

    a = get_action(o)
    o, r, d, dict = env.step(a)
    # print(dict)
    ep_ret += r
    ep_len += 1
    f = env.data.actuator_force.copy()
    temp_fp = 0
    for i in range(0, 6):
        temp_fp += abs(f[i] * env.data.sensordata.copy()[i*3+2])

    v.append(env.data.qvel[0])
    if(t >= START_EPOCH and t <= END_EPOCH):
        qvel += env.data.qvel[0]
        # average_power_efficiency = average_power_efficiency + current_power_efficiency
        fp += temp_fp

    # if d or (ep_len == 10000):
    #     logger.store(EpRet=ep_ret, EpLen=ep_len)
    #     print('Episode %d \t EpRet %.3f \t EpLen %d'%(n, ep_ret, ep_len))
    #     o, r, d, ep_ret, ep_len = env.reset(), 0, False, 0, 0
    #     n += 1
    t += 1

print(qvel / (END_EPOCH - START_EPOCH))
print(fp / (END_EPOCH - START_EPOCH))
plt.figure(1)
plt.plot(range(len(v)), v)
plt.show()

