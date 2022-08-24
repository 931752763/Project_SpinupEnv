import time
from sys import stdin
from mujoco_py import load_model_from_path, MjSim, MjViewer
import math
import matplotlib.pyplot as plt
import demo.FrequencySnake.PID as PID
import numpy as np


def oneTest(model, view, plot, P, I, D, amplitude, omega, lamda, y):
    sim = MjSim(model)
    sim.reset()
    if view: viewer = MjViewer(sim)
    NUM_OF_JOINTS = 6
    TIMESTEPS = 0.01
    TOTAL_EPOCH = 1200
    START_EPOCH = 400
    END_EPOCH = 1100
    GEAR = 1
    STIFFNESS = 2
    t = 0

    v = []
    p = []
    p_joint = [0, 0, 0, 0, 0, 0]
    p_spring = [0, 0, 0, 0, 0, 0]
    pos_start = []
    pos_end = []
    pos = []
    posy = []
    fp = 0
    average_velocity = 0
    if P != 0: pid = PID.PID(P, I, D)
    # pre run

    while t < TOTAL_EPOCH:
        # pre run
        if t < 200:
            for i in range(NUM_OF_JOINTS):
                ctrl_i = t / 200 * amplitude / 180.0 * math.pi \
                         * math.sin(omega * t - lamda / 180.0 * math.pi * i) \
                         * (i / NUM_OF_JOINTS * (1 - y) + y)
                if P == 0:
                    sim.data.ctrl[i] = ctrl_i
                else:
                    sim.data.ctrl[i] = pid.update(ctrl_i, sim.data.qpos[i + 3])
        else:
            for i in range(NUM_OF_JOINTS):
                ctrl_i = amplitude / 180.0 * math.pi \
                         * math.sin(omega * t - lamda / 180.0 * math.pi * i) \
                         * (i / NUM_OF_JOINTS * (1 - y) + y)
                if P == 0:
                    sim.data.ctrl[i] = ctrl_i
                else:
                    sim.data.ctrl[i] = pid.update(ctrl_i, sim.data.qpos[i + 3])
        sensordata_before = sim.data.sensordata.copy()
        t += 1
        for _ in range(4):
            sim.step()

        if view: viewer.render()
        sensordata_after = sim.data.sensordata.copy()
        sensordata_delta = (sensordata_after - sensordata_before) / (TIMESTEPS * 4)

        f = sim.data.actuator_force.copy()
        temp_fp = 0
        for i in range(0, 6):
            temp_fp += abs(f[i] * sim.data.qvel[3 + i])
        p.append(temp_fp)

        current_velocity_x = 0
        current_velocity_y = 0
        average_pos_after = 0
        average_pos_y = 0
        for i in range(0, 7):
            current_velocity_x += sensordata_delta[18 + i * 3]
            current_velocity_y += sensordata_delta[19 + i * 3]
            average_pos_after += sim.data.sensordata[18 + i * 3]
            average_pos_y += sim.data.sensordata[19 + i * 3]
        pos.append(average_pos_after / 7)
        posy.append(average_pos_y / 7)

        current_velocity_x /= 7
        current_velocity_y /= 7
        cur_v = (current_velocity_x ** 2 + current_velocity_y ** 2) ** 0.5
        v.append(cur_v)
        if (t >= START_EPOCH and t <= END_EPOCH):
            for i in range(0, 6):
                p_joint[i] += abs(f[i] * GEAR * sim.data.qvel[3 + i])
                p_spring[i] += abs(STIFFNESS * sim.data.qvel[3 + i])
            average_velocity += current_velocity_x
            fp += temp_fp
        if (t == START_EPOCH): pos_start = sim.data.qpos.copy()
        if (t == END_EPOCH): pos_end = sim.data.qpos.copy()

        # if (t == 500 or t == 510 or t == 520):
        # if (t == 200):
        #     time.sleep(2)

    vel = (pos_end - pos_start) / (TIMESTEPS * 4 * (END_EPOCH - START_EPOCH))
    average_velocity = (vel[0] ** 2 + vel[1] ** 2) ** 0.5
    # average_velocity = average_velocity / (END_EPOCH - START_EPOCH)
    fp = fp / (END_EPOCH - START_EPOCH)
    if P != 0: fp = fp * 0.1
    print(amplitude, omega, lamda, y, average_velocity, fp)

    if plot:
        plt.figure(1)
        plt.plot(range(len(v)), v)
        #
        # plt.figure(2)
        # plt.plot(range(len(p)), p)
        #
        # plt.figure(3)
        # plt.plot(range(len(posy)), posy)
        #
        plt.figure(2)
        p_joint = np.divide(p_joint, (END_EPOCH - START_EPOCH))
        print(p_joint)
        p_spring = np.divide(p_spring, (END_EPOCH - START_EPOCH))
        print(p_spring)
        plt.bar(range(len(p_joint)), p_joint)
        plt.figure(3)
        plt.bar(range(len(p_spring)), p_spring)
        plt.show()

    return average_velocity, fp, v
