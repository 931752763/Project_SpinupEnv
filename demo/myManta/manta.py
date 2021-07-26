import os

import numpy as np
from gym import utils
from gym.envs.mujoco import mujoco_env
import math

DEFAULT_CAMERA_CONFIG = {
    'distance': 4.0,
}


class MantaEnv(mujoco_env.MujocoEnv, utils.EzPickle):
    def __init__(self, env_config,
                 path=os.getcwd(),
                 xml_file='/home/zheng/anaconda3/envs/spinningupEnv/lib/python3.6/site-packages/gym/envs/mujoco/myManta/manta-v2.xml',
                 forward_reward_weight=10.0,
                 ctrl_cost_weight=1,
                 reset_noise_scale=0.001, ):
        utils.EzPickle.__init__(self)

        self._forward_reward_weight = forward_reward_weight
        self._ctrl_cost_weight = ctrl_cost_weight
        self._reset_noise_scale = reset_noise_scale
        mujoco_env.MujocoEnv.__init__(self, os.path.join(path, xml_file), 1)

    def control_cost(self, action):
        control_cost = self._ctrl_cost_weight * (
            np.sum(np.square(action)))
        return control_cost

    def step(self, action):
        x_position_before = self.sim.data.qpos[0]
        # action=np.abs(action)
        action_new = []
        for i in range(3):
            for _ in range(20):
                action_new.append(action[i])
        action_new = np.array(action_new)
        self.do_simulation(action_new, self.frame_skip)
        x_position_after = self.sim.data.qpos[0]
        # y_position_after = self.sim.data.qpos[1]
        x_velocity = ((x_position_after - x_position_before) / self.dt)
        ctrl_cost = self.control_cost(action)
        # forward_punishment = abs(floater_f_posy) + abs(floater_m_posy) + abs(floater_b_posy)
        forward_reward = self._forward_reward_weight * x_velocity
        observation = self._get_obs()
        reward = forward_reward - ctrl_cost
        # limited_distance = np.abs(self.sim.data.sensordata.copy()[0])
        done = False
        info = {
            'x_position': x_position_after,
            'x_velocity': x_velocity,

            'reward_run': forward_reward,
            'reward_ctrl': -ctrl_cost
        }
        return observation, reward, done, info

    def _get_obs(self):
        # observation = self.sim.data.sensordata.copy().ravel()

        position = self.sim.data.qpos.flat.copy()[1::]
        velocity = self.sim.data.qvel.flat.copy()[1::]
        observation = np.concatenate((position, velocity)).ravel()
        return observation

    def reset_model(self):
        noise_low = -self._reset_noise_scale
        noise_high = self._reset_noise_scale

        qpos = self.init_qpos + self.np_random.uniform(
            low=noise_low, high=noise_high, size=self.model.nq)

        # qvelt = self.init_qvel[2::] + self._reset_noise_scale * self.np_random.randn(
        #     self.model.nv)[2::]
        # qvel = np.concatenate([self.init_qvel[0:2], qvelt], axis=0)
        qvel = self.init_qvel + self._reset_noise_scale * self.np_random.randn(
            self.model.nv)

        self.set_state(qpos, qvel)

        observation = self._get_obs()
        return observation

    def viewer_setup(self):
        for key, value in DEFAULT_CAMERA_CONFIG.items():
            if isinstance(value, np.ndarray):
                getattr(self.viewer.cam, key)[:] = value
            else:
                setattr(self.viewer.cam, key, value)
