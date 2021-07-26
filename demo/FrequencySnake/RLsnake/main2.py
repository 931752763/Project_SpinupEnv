from spinup import ddpg_pytorch
from spinup import sac_tf1
from spinup import ddpg_tf1
from spinup import ppo_tf1
import tensorflow as tf
import time
import gym

env_fn = lambda : gym.make('Swimmer6-v0')

ac_kwargs = dict(hidden_sizes=[256,256], activation=tf.nn.relu)

logger_kwargs = dict(output_dir='/home/zheng/spinningup/data/swimmer6_'+time.strftime("%Y-%m-%d_%H:%M", time.localtime()),
                     exp_name='swimmer6'+time.strftime("%Y-%m-%d_%H:%M", time.localtime()))

ppo_tf1(env_fn=env_fn, ac_kwargs=ac_kwargs, steps_per_epoch=5000,
            epochs=5000, logger_kwargs=logger_kwargs, seed=10)

