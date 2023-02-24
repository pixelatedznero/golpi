import torch
import numpy as np

from lib import simulation, utils

sim = simulation.Simulation()
util = utils.Utils()

# Define the function to check the quality of the output list
def check_quality(lst):
    ch = util.checks.Checks(sim.run(sim.createboard(sim.convert2twod(lst[0],10)), 20, fullexport=True))
    output = ch.distance()
    return output[max(output)]/100

# Define the model architecture
class BinaryListModel(torch.nn.Module):
    def __init__(self):
        super(BinaryListModel, self).__init__()
        self.fc1 = torch.nn.Linear(100, 128)
        self.fc2 = torch.nn.Linear(128, 256)
        self.fc3 = torch.nn.Linear(256, 512)
        self.fc4 = torch.nn.Linear(512, 1024)
        self.fc5 = torch.nn.Linear(1024, 100)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = torch.relu(self.fc4(x))
        x = torch.sigmoid(self.fc5(x))
        return x

# Create the model
model = BinaryListModel()

# Define the optimizer and loss function
optimizer = torch.optim.Adam(model.parameters(), lr=0.03)
criterion = torch.nn.MSELoss()

# Train the model
for epoch in range(10000):
    # Generate random binary list
    input_list = torch.randint(0, 2, (1, 100)).float()

    # Evaluate the quality of the output list
    target = check_quality(input_list)
    # Forward pass
    output = model(input_list)
    # Compute the loss
    loss = criterion(output, torch.tensor([target]))
    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    # Print the loss
    if epoch % 100 == 0:
        print('Epoch: {}/{}, Loss: {}'.format(epoch+1, 1000, loss.item()))

# Generate the optimal binary list
input_list = torch.randint(0, 2, (1, 100)).float()
output = model(input_list)

print(torch.round(output).int().numpy())

optimal_list = [list(torch.round(output).int().numpy()[0])]

# Check the quality of the optimal list
quality = check_quality(optimal_list)
print('Optimal list: {}, Quality: {}'.format(optimal_list[0], quality))
