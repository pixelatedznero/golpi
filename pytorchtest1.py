import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

import gameoflife


class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(225, 128)
        self.fc2 = nn.Linear(128, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.fc1(x)
        x = self.sigmoid(x)
        x = self.fc2(x)
        x = self.sigmoid(x)
        return x


class ReinforcementLearningAlgorithm:
    def __init__(self):
        self.environment = gameoflife.GameOfLife()
        self.model = NeuralNetwork()
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.01)

    def get_action(self):
        state = np.random.randint(2, size=225)
        state = torch.from_numpy(state).float()
        action = self.model(state)
        action = action.detach().numpy().squeeze()
        return np.round(action)

    def update(self, reward):
        loss = torch.nn.MSELoss()(self.model(torch.from_numpy(np.random.randint(2, size=225)).float()), torch.tensor(reward).float())
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()


def train(num_episodes):
    rl_algorithm = ReinforcementLearningAlgorithm()
    for episode in range(num_episodes):
        action = rl_algorithm.get_action()
        reward = rl_algorithm.environment.check(action)
        rl_algorithm.update(reward)

        # Print the reward for this episode
        print("Episode: {}, reward: {}".format(episode, reward))


def test(num_tests):
    rl_algorithm = ReinforcementLearningAlgorithm()
    for i in range(num_tests):
        output_data = rl_algorithm.get_action()
        result = rl_algorithm.environment.check(output_data)
        print("Test {}: output={}, result={}".format(i, output_data, result))


train(100)
test(10)