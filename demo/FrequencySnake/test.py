from mujoco_py import load_model_from_path, MjSim, MjViewer
import math
import matplotlib.pyplot as plt

# test about the biggest angular velocity

model = load_model_from_path("test.xml")
sim = MjSim(model)
viewer = MjViewer(sim)
t = 0
max_angular_velocity = 0
while t < 10000:

    if t % 1000 <= 500:
        sim.data.ctrl[0] = 1
    else:
        sim.data.ctrl[0] = -1

    t += 1
    sim.step()
    angular_velocity = abs(sim.data.sensordata.copy())
    if(angular_velocity[2] > max_angular_velocity):
        max_angular_velocity = angular_velocity[2]
        print(max_angular_velocity)
    viewer.render()
