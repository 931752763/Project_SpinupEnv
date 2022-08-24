import time
import numpy as np
from mujoco_py import load_model_from_path, MjSim, MjViewer
import math
import matplotlib.pyplot as plt
import os
import shutil

# kdirs
from demo.FrequencySnake.OneTest import oneTest

dir = "/home/zheng/spinningup/data/paper_10.11/vis=0.0001_dens=514/sin/"
path = "_s=3_" + time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
os.makedirs(dir + path)
shutil.copyfile("FreqSwimmer6.xml", dir + path + "/FreqSwimmer6.xml")
# mkdirs

NUM_OF_JOINTS = 6
TIMESTEPS = 0.01
MOMENT_OF_INERTIA = 1.0
TOTAL_EPOCH = 1000
END_EPOCH = 900
START_EPOCH = 200
GEAR = 0.1

V = []
P = []
A = []  # amplitude
O = []  # omega
L = []  # lambda
Y = []  # y

amplitude_color = []
omega_color = []
lamda_color = []
bestCase = [0, 0, 0, 0, 0, 0]
maxV = 0
# viewer = MjViewer(sim)
model = load_model_from_path("FreqSwimmer6.xml")
sim = MjSim(model)
A_skip, O_skip, L_skip = 10, 0.05, 10
for amplitude in np.arange(A_skip, 181, A_skip):  #
    for omega in np.arange(O_skip, 1, O_skip):  # 0.001 - 0.01
        for lamda in np.arange(L_skip, 181, L_skip):  # 10 - 180
            for y in np.arange(0.2, 1.01, 0.2):  # 0.1 - 0.5
                average_velocity, fp = oneTest(model, False, False, 0, 0, 0, amplitude, omega, lamda, y)
                V.append(average_velocity)
                P.append(fp)
                A.append(amplitude)
                O.append(omega)
                L.append(lamda)
                Y.append(y)

                # find a good case to view
                if (average_velocity > maxV):
                    maxV = average_velocity
                    bestCase[0] = average_velocity
                    bestCase[1] = fp
                    bestCase[2] = amplitude
                    bestCase[3] = omega
                    bestCase[4] = lamda
                    bestCase[5] = y

print("bestCase is:")
print(bestCase)

plt.figure(0)
plt.scatter(V, P)
plt.title("position")
plt.show()

file = open(dir + path
            + "/A_skip=" + str(A_skip) + "_O_skip=" + str(O_skip) + "_L_skip=" + str(L_skip) + "_"
            + time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()) + ".txt", 'w')
file.writelines(str(V) + '\n')
file.writelines(str(P) + '\n')
file.writelines(str(A) + '\n')
file.writelines(str(O) + '\n')
file.writelines(str(L) + '\n')
file.writelines(str(Y) + '\n')
