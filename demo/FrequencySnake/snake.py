from mujoco_py import load_model_from_path, MjSim, MjViewer
import math
# import numpy as np
import time

#
# import matplotlib.pyplot as plt

model = load_model_from_path("./xml/DEA/snake_ver3_modelbase.xml")
sim = MjSim(model)
viewer = MjViewer(sim)
t = 0

direction_index = 0
a = 100
w = 5
phi = 0.33 * math.pi
posx = []
posy = []
posz = []
velx = []
vely = []
velz = []
gyrox = []
gyroy = []
gyroz = []
sim.step()
start_pos = sim.data.sensordata.copy().ravel()[0]
time_interval = 500  # ms
while t < 10000:
    t = t + 1
    for i in [0,1,2]:
        for k in range(time_interval):
            sim.data.ctrl[12 * i:12 * (i + 1)] = -0.05 - 0.01 * k
            time.sleep(0.001)
            sim.step()
            viewer.render()

    for i in [0,2,1]:
        for k in range(time_interval):
            sim.data.ctrl[12 * i:12 * (i + 1)] = 0.05 + 0.03 * k
            time.sleep(0.001)
            sim.step()
            viewer.render()
    com = sim.data.sensordata.copy().ravel()[::]
    # vel = (finish_pos - start_pos) / (t * 6 * time_interval / 1000)
    # print(vel)
    print(com)

# plt.plot(range(len(posx)), posx)
# plt.plot(range(len(posx)),posy)
# plt.plot(range(len(posx)),posz)
# plt.plot(range(len(posx)),velx)
# plt.plot(range(len(posx)),vely)
# plt.plot(range(len(posx)), gyrox)
# plt.plot(range(len(posx)), gyroy)
# plt.show()
