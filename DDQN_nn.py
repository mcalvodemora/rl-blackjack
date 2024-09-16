import random

import torch
import torch.nn as nn


class Memory:
    def __init__(self, max_memory):
        self._max_memory = max_memory
        self._samples = []

    def add_sample(self, sample):
        self._samples.append(sample)
        if len(self._samples) > self._max_memory:
            self._samples.pop(0)

    def sample(self, no_samples):
        if no_samples > len(self._samples):
            return random.sample(self._samples, len(self._samples))
        else:
            return random.sample(self._samples, no_samples)

    @property
    def num_samples(self):
        return len(self._samples)


class DuelingQNetwork(nn.Module):
    def __init__(self, input_size, num_actions):
        super().__init__()
        self.fc1 = nn.Linear(input_size, 32)
        self.fc2_adv = nn.Linear(32, 32)
        self.fc2_val = nn.Linear(32, 32)
        self.fc3_adv = nn.Linear(32, num_actions)
        self.fc3_val = nn.Linear(32, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        adv = torch.relu(self.fc2_adv(x))
        val = torch.relu(self.fc2_val(x))
        adv = torch.relu(self.fc3_adv(x))
        val = torch.relu(self.fc3_val(x))

        q_values = val + (adv - adv.mean(dim=1, keepdim=True))
        return q_values
