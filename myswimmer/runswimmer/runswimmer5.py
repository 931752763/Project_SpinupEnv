from spinup import ppo_tf1
import tensorflow as tf
import gym
# from mySwimmer import my_env
import argparse
from spinup.utils.test_policy import load_tf_policy, run_policy
from spinup.utils.plot import make_plots

parser = argparse.ArgumentParser(description='Train or test NN controller.')
parser.add_argument('--train', dest='train', action='store_true', default=True)
parser.add_argument('--test', dest='test', action='store_false')
args = parser.parse_args()

if __name__ == "__main__":
    if args.train:
        env_fn = lambda: gym.make('Swimmer5-v0')

        ac_kwargs = dict(hidden_sizes=[120, 84, 32], activation=tf.nn.selu)

        logger_kwargs = dict(output_dir='./spinup_record/swimmer5', exp_name='swimmer5')

        ppo_tf1(env_fn=env_fn, ac_kwargs=ac_kwargs, steps_per_epoch=50000,
            epochs=1000, logger_kwargs=logger_kwargs, seed=0)

    elif args.test:
        _, get_action = load_tf_policy('./spinup_record/swimmer5')
        env = gym.make('Swimmer5-v0')
        run_policy(env, get_action)

