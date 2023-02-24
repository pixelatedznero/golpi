import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

from lib import simulation, utils

sim = simulation.Simulation()
util = utils.Utils()

# Define the evaluation function
def evaluate(individual):
    ch = util.checks.Checks(sim.run(sim.createboard(sim.convert2twod(individual,10)), 20, fullexport=True))
    output = ch.distance()
    return output[max(output)]

# Define the neural network that will be used to learn the optimal solution
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(100, 50)
        self.fc2 = nn.Linear(50, 1)

    def forward(self, x):
        x = torch.sigmoid(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x

# Define the genetic algorithm
class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = np.random.randint(2, size=(population_size, 100))
        self.network = Net()
        self.optimizer = optim.Adam(self.network.parameters(), lr=0.01)

    def evolve(self, num_generations):
        for i in range(num_generations):
            
            # Evaluate the population
            fitness = np.zeros(self.population_size)
            for j in range(self.population_size):
                fitness[j] = evaluate(self.population[j])

            # Normalize the fitness scores
            fitness = (fitness - np.mean(fitness)) / np.std(fitness)
            
            # Select parents using the fitness scores as probabilities
            parents = np.random.choice(self.population, size=(self.population_size, 2), p=fitness, replace=True)
            
            # Crossover parents to create new offspring
            offspring = np.zeros((self.population_size, 100))
            for j in range(self.population_size):
                crossover_point = np.random.randint(100)
                offspring[j, :crossover_point] = parents[j, 0, :crossover_point]
                offspring[j, crossover_point:] = parents[j, 1, crossover_point:]
            
            # Mutate the offspring
            mask = np.random.binomial(1, self.mutation_rate, size=(self.population_size, 100)).astype(bool)
            offspring[mask] = 1 - offspring[mask]
            
            # Evaluate the offspring
            offspring_fitness = np.zeros(self.population_size)
            for j in range(self.population_size):
                offspring_fitness[j] = evaluate(offspring[j])
            
            # Normalize the offspring fitness scores
            offspring_fitness = (offspring_fitness - np.mean(offspring_fitness)) / np.std(offspring_fitness)
            
            # Select the best individuals for the next generation
            elite_size = int(self.population_size * 0.1)
            elite_indices = np.argsort(fitness)[-elite_size:]
            next_generation = np.zeros((self.population_size, 100))
            next_generation[:elite_size] = self.population[elite_indices]
            next_generation[elite_size:] = offspring[np.argsort(offspring_fitness)[-self.population_size + elite_size:]]
            
            # Update the population
            self.population = next_generation
            
            # Train the neural network
            inputs = torch.tensor(self.population.astype(np.float32))
            targets = torch.tensor(offspring_fitness.astype(np.float32)).view(-1, 1)
            self.optimizer.zero_grad()
            outputs = self.network(inputs)
            loss = nn.MSELoss()(outputs, targets)
            loss.backward()
            self.optimizer.step



# Instantiate the genetic algorithm
gen_alg = GeneticAlgorithm(population_size=100, mutation_rate=0.01)

# Evolve the population for 100 generations
for i in range(10):
    gen_alg.evolve(num_generations=100)
    print(i)

# Get the best individual in the final population
best_individual = gen_alg.population[np.argmax([evaluate(individual) for individual in gen_alg.population])]
print(evaluate(best_individual))
print(best_individual)