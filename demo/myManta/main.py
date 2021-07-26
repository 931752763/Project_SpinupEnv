from spinup import ddpg_pytorch
from spinup import sac_tf1
from spinup import ddpg_tf1
from spinup import ppo_tf1
import tensorflow as tf
import time
import gym

env_fn = lambda : gym.make('MyManta-v0')

ac_kwargs = dict(hidden_sizes=[256,256], activation=tf.nn.relu)

logger_kwargs = dict(output_dir='/home/zheng/spinningup/data/manta_'+time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()),
                     exp_name='manta'+time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()))

sac_tf1(env_fn=env_fn, ac_kwargs=ac_kwargs, steps_per_epoch=10000,
            epochs=1000, logger_kwargs=logger_kwargs, seed=0)

