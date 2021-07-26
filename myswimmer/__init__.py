from gym.envs.registration import register
register(
    id='Swimmer5-v0',
    entry_point='myenv.swimmer5:Swimmer5Env',
)
