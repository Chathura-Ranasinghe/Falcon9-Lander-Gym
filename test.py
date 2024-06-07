import gymnasium as gym
import gym.spaces
from stable_baselines3 import PPO
import falcon_lander_gym

# Load the environment
env = gym.make('FalconLander-v1')

# Load the trained model
model = PPO.load("./train/best_model_8000000")
#model = PPO.load("./train/model_final")

def run_simulation(env, model, num_episodes=1):
    for episode in range(num_episodes):
        observation = env.reset()
        done = False
        total_reward = 0
        step_count = 0

        while not done:
            env.render()
            action, _states = model.predict(observation)
            observation, reward, done, info = env.step(action)
            total_reward += reward
            step_count += 1

            print(f"Episode: {episode + 1}, Step: {step_count}")
            print("Action Taken  ", action)
            print("Observation   ", observation)
            print("Reward Gained ", reward)
            print("Info          ", info, end='\n\n')

        print(f"Episode {episode + 1} finished after {step_count} steps with total reward {total_reward}")

if __name__ == "__main__":
    run_simulation(env, model, num_episodes=10)
    env.close()
