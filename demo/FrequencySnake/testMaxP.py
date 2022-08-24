from mujoco_py import load_model_from_path, MjSim, MjViewer
import math
import matplotlib.pyplot as plt
import time
import random

# model = load_model_from_path("FreqSwimmer6.xml")
model = load_model_from_path("/home/zheng/anaconda3/envs/spinningupEnv/lib/python3.6/site-packages/gym/envs/mujoco/RLsnake/swimmer6.xml")
sim = MjSim(model)
viewer = MjViewer(sim)
NUM_OF_JOINTS = 6
TIMESTEPS = 0.01
t = 0
fp = 0
maxP = 0
while t < 10000:
    for i in range(NUM_OF_JOINTS):
        sim.data.ctrl[i] = random.random()
    # sim.data.ctrl[0] = 10
    print(sim.data.actuator_force)
    t += 1
    viewer.render()
    sim.step()
    sensordata_after = sim.data.sensordata.copy()
    # print(sim.data.qpos)
    f = sim.data.actuator_force.copy()
    temp_fp = 0
    for i in range(0, 6):
        temp_fp += abs(f[i] * sensordata_after[i*3+2])

    if(temp_fp > maxP):
        maxP = temp_fp;
print(maxP)
