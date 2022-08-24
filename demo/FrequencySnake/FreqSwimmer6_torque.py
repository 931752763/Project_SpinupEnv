import time
import numpy as np
from mujoco_py import load_model_from_path, MjSim, MjViewer
import math
import matplotlib.pyplot as plt
import os

NUM_OF_JOINTS = 6
TIMESTEPS = 0.01
MOMENT_OF_INERTIA = 1.0
TOTAL_EPOCH = 2000
END_EPOCH = 1900
START_EPOCH = 300

V = []
P = []
A = []  #amplitude
O = []  #omega
L = []  #lambda
Y = []  #y

amplitude_color = []
omega_color = []
lamda_color = []
bestCase = [0,0,0,0,0,0]
maxV = 0

model = load_model_from_path("FreqSwimmer6_torque.xml")
sim = MjSim(model)
A_skip, O_skip, L_skip = 0.1, 0.1, 30
for amplitude in np.arange(A_skip, 1.01, A_skip):  #
    for omega in np.arange(O_skip, 1.01, O_skip):  # 0.001 - 0.01
        for lamda in np.arange(L_skip, 181, L_skip):  # 10 - 180
            for y in np.arange(1, 1.01, 0.2):  # 0.1 - 0.5
                t = 0
                sim.reset()
                average_velocity = 0
                fp = 0
                while t < TOTAL_EPOCH:
                    for i in range(NUM_OF_JOINTS):
                        sim.data.ctrl[i] = amplitude * math.sin(omega * t - lamda / 180.0 * math.pi * i) \
                                                           * (i / NUM_OF_JOINTS * (1 - y) + y)
                    sensordata_before = sim.data.sensordata.copy()
                    t += 1
                    for _ in range(4):
                        sim.step()
                    # viewer.render()
                    sensordata_after = sim.data.sensordata.copy()
                    sensordata_delta = (sensordata_after - sensordata_before) / (TIMESTEPS * 4)

                    f = sim.data.actuator_force.copy()
                    temp_fp = 0
                    for i in range(0, 6):
                        temp_fp += abs(f[i] * sim.data.qvel[3+i])

                    # print(sim.data.qpos)
                    current_velocity_x = 0
                    current_velocity_y = 0
                    for i in range(0,7):
                        current_velocity_x += sensordata_delta[18+i*3]
                        current_velocity_y += sensordata_delta[19+i*3]

                    current_velocity_x /= 7
                    current_velocity_y /= 7
                    cur_v = (current_velocity_x ** 2 + current_velocity_y ** 2) ** 0.5
                    if(t >= START_EPOCH and t <= END_EPOCH):
                        average_velocity += cur_v
                        fp += temp_fp

                average_velocity = average_velocity / (END_EPOCH - START_EPOCH)
                fp = fp / (END_EPOCH - START_EPOCH)
                V.append(average_velocity)
                P.append(fp)
                A.append(amplitude)
                O.append(omega)
                L.append(lamda)
                Y.append(y)

                # find a good case to view
                if(average_velocity > maxV):
                    maxV = average_velocity
                    bestCase[0] = average_velocity
                    bestCase[1] = fp
                    bestCase[2] = amplitude
                    bestCase[3] = omega
                    bestCase[4] = lamda
                    bestCase[5] = y

                print(amplitude, omega, lamda, y, average_velocity, fp)

print("bestCase is:")
print(bestCase)

plt.figure(0)
plt.scatter(V, P)
plt.title("torque")
plt.show()

file = open("/home/zheng/spinningup/data/paper_10.11/torque/arma=0.001_stif=0_A_skip="+str(A_skip)+"_O_skip="+str(O_skip)+"_L_skip="+str(L_skip)+"_"+
                        time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()) + ".txt", 'w')
file.writelines(str(V)+'\n')
file.writelines(str(P)+'\n')
file.writelines(str(A)+'\n')
file.writelines(str(O)+'\n')
file.writelines(str(L)+'\n')
file.writelines(str(Y)+'\n')
