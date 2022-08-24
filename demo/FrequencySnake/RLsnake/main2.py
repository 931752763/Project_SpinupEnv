from spinup import ddpg_pytorch
from spinup import sac_tf1
from spinup import ddpg_tf1
from spinup import ppo_tf1
import tensorflow as tf
import time
import gym

env_fn = lambda : gym.make('Swimmer6-v0')

ac_kwargs = dict(hidden_sizes=[256,256], activation=tf.nn.relu)

path = '/home/zheng/spinningup/data/paper_10.11/vis=0.01_dens=1097/'\
       + time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()) + 's=0_'

logger_kwargs = dict(output_dir=path, exp_name='swimmer6'+time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()))

ppo_tf1(env_fn=env_fn, ac_kwargs=ac_kwargs, steps_per_epoch=3000, epochs=16000, save_freq=1000,
        target_kl=0.01, logger_kwargs=logger_kwargs, seed=20, pi_lr=3e-4)

