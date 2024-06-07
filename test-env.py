import gymnasium as gym
import gym.spaces
import falcon_lander_gym

env_name = 'FalconLander-v1'

env = gym.make(env_name)
PRINT_DEBUG_MSG = True

def run_simulation(env, num_episodes=1):
    for episode in range(num_episodes):
        observation = env.reset()
        done = False
        total_reward = 0
        step_count = 0

        while not done:
            env.render()
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            total_reward += reward
            step_count += 1

            if PRINT_DEBUG_MSG:
                print(f"Episode: {episode + 1}, Step: {step_count}")
                print("Action Taken  ", action)
                print("Observation   ", observation)
                print("Reward Gained ", reward)
                print("Info          ", info, end='\n\n')

        print(f"Episode {episode + 1} finished after {step_count} steps with total reward {total_reward}")

if __name__ == "__main__":
    run_simulation(env, num_episodes=20)
    env.close()
