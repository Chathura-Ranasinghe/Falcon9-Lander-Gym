from gym.envs.registration import register

register(
    id='FalconLander-v1',
    entry_point='falcon_lander_gym.envs:FalconLander-v0',
    max_episode_steps=1000,
    reward_threshold=0,
)