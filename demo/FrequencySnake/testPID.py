import time
import math
from mujoco_py import load_model_from_path, MjSim, MjViewer
import PID
import numpy as np
import matplotlib.pyplot as plt
from demo.FrequencySnake.OneTest import oneTest

model = load_model_from_path("FreqSwimmer6.xml")
sim = MjSim(model)
P_skip, I_skip, D_skip = 20, 10, 10
A_skip, O_skip, L_skip  = 20, 0.05, 20
max_v = 0
best_P, best_I, best_D = 0, 0, 0
best_amplitude, best_omega, best_lamda, best_y = 0,0,0,0
for P in np.arange(P_skip, 101, P_skip):
    for I in np.arange(0, 50, I_skip):
        for D in np.arange(0, 20, D_skip):
            for amplitude in np.arange(A_skip, 181, A_skip):  #
                for omega in np.arange(O_skip, 0.5, O_skip):  # 0.001 - 0.01
                    for lamda in np.arange(L_skip, 181, L_skip):  # 10 - 180
                        for y in np.arange(0.2, 1.01, 0.2):  # 0.1 - 0.5
                            average_velocity, fp, _ = oneTest(model, False, False, P, I, D, amplitude, omega, lamda, y)
                            print(P, I, D, average_velocity, fp)
                            if average_velocity > max_v:
                                max_v = average_velocity
                                best_P, best_I, best_D = P, I, D
                                best_amplitude, best_omega, best_lamda, best_y = amplitude, omega, lamda, y

print(best_P, best_I, best_D, best_amplitude, best_omega, best_lamda, best_y)
