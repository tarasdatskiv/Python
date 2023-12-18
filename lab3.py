import gym
import matplotlib.pyplot as plt
import numpy as np
import ray
import random

class KingOfTheHill(gym.Env):
    def __init__(self):
        super(KingOfTheHill, self).__init__()
        self.observation_space = gym.spaces.Box(low=0, high=100, shape=(1,), dtype=np.float32)
        self.action_space = gym.spaces.Discrete(3)

    def step(self, actions):
        new_state = np.random.uniform(low=0, high=100, size=(1,))
        reward = np.random.uniform(low=0, high=1)
        done = False
        return new_state, reward, done

    def reset(self):
        initial_observation = np.random.uniform(low=0, high=100, size=(1,))
        return initial_observation

class Agent:
    def __init__(self, agent_id, observation_space, action_space, q_table):
        self.agent_id = agent_id
        self.observation_space = observation_space
        self.action_space = action_space
        self.q_table = q_table

    def choose_action(self, obs):
        action = np.argmax(self.q_table[int(obs)])
        return action

# Функція для тестування агента в модифікованому середовищі
@ray.remote
def test_agent(agent, env, num_episodes):
    rewards_per_episode = []
    for episode in range(num_episodes):
        obs = env.reset()
        done = False
        total_reward = 0
        count = 0
        value = random.randint(700, 1300)
        while not done and count < value:
            count += 1
            action = agent.choose_action(obs)
            next_obs, reward, done = env.step([action])
            obs = next_obs
            total_reward += reward
        rewards_per_episode.append(total_reward)

    return rewards_per_episode

# Модифікація середовища
class ModifiedKingOfTheHill(KingOfTheHill):
    def __init__(self):
        super(ModifiedKingOfTheHill, self).__init__()

    # Модифікуйте функцію step або інші частини за потребою

# Параметри
num_agents = 15
num_episodes_training = 20
num_episodes_testing = 10

# Створення навчених агентів та середовища
env_training = KingOfTheHill()
agents = [Agent(agent_id=i, observation_space=env_training.observation_space,
                action_space=env_training.action_space, q_table=np.random.rand(100, 3)) for i in range(num_agents)]

# Тренування агентів
for episode in range(num_episodes_training):
    for agent in agents:
        pass
        # Ваш код для тренування агентів

# Тестування агентів в модифікованому середовищі
env_testing = ModifiedKingOfTheHill()
total_rewards = 0
agentData = []
for agent in agents:
    rewards_per_episode = test_agent.remote(agent, env_testing, num_episodes_testing)
    rewards_per_episode = ray.get(rewards_per_episode)
    avg_reward = np.mean(rewards_per_episode)
    total_rewards += avg_reward
    agentData.append(avg_reward)
    print(f"Agent {agent.agent_id} - Average Reward: {avg_reward}")

# Виведення загальної середньої винагороди
average_total_reward = total_rewards / num_agents
print(f"Average Total Reward Across Agents: {average_total_reward}")

def analyze_results(rewards_per_episode):
    plt.plot(rewards_per_episode, color = "red")
    plt.xlabel('Епізод')
    plt.ylabel('Винагорода')
    plt.title('Динаміка винагороди протягом епізодів')
    plt.show()

analyze_results(agentData)