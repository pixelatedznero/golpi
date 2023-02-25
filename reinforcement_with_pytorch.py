import torch
import torch.nn as nn
import numpy as np

from lib import simulation, utils

sim = simulation.Simulation()
util = utils.Utils()

iterations = 60

# Define the evaluation function
def evaluate(individual, device):
    # Evaluate the fitness of an individual
    individual_tensor = individual.unsqueeze(0).to(device)

    reallist = list(torch.round(individual_tensor.cpu()).int().numpy()[0])

    ch = util.checks.Checks(sim.run(sim.createboard(sim.convert2twod(reallist,10)), iterations, fullexport=True))
    output = ch.distance()

    fitness_score = output[max(output)]
    return fitness_score


def animate(individual, device, iteration):
    individual_tensor = individual.unsqueeze(0).to(device)

    reallist = list(torch.round(individual_tensor.cpu()).int().numpy()[0])

    util.animategif(sim.convert2twod(reallist,10), iterations, f"anim{iteration}")


# Define the neural network that will be used to learn the optimal solution
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(100, 50)
        self.fc2 = nn.Linear(50, 25)
        self.fc3 = nn.Linear(25, 10)
        self.fc4 = nn.Linear(10, 1)

    def forward(self, x):
        x = torch.sigmoid(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        x = torch.sigmoid(self.fc4(x))
        return x

# Define the genetic algorithm
class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        if self.device == "cuda":
            print("--- Using CUDA ---")
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = self.initialize_population().to(self.device)

    def initialize_population(self):
        population = torch.randint(low=0, high=2, size=(self.population_size, 100)).to(self.device)
        return population.float()

    def crossover(self, parent1, parent2):
        # Perform crossover between two parents
        child = torch.zeros(100).to(self.device)
        crossover_point = torch.randint(low=0, high=100, size=(1,)).to(self.device)
        child[:crossover_point] = parent1[:crossover_point]
        child[crossover_point:] = parent2[crossover_point:]
        return child

    def mutate(self, individual):
        # Perform mutation on individual
        for i in range(100):
            if torch.rand(1).to(self.device) < self.mutation_rate:
                individual[i] = 1 - individual[i]
        return individual

    def evolve(self, num_generations):
        for generation in range(num_generations):
            # Evaluate the fitness of the population
            fitness_scores = self.evaluate_population(self.population)

            # Select parents for the next generation
            parents = self.select_parents(self.population, fitness_scores)

            # Create new offspring through crossover and mutation
            offspring = self.generate_offspring(parents)

            # Evaluate the fitness of the offspring
            offspring_fitness_scores = self.evaluate_population(offspring)

            # Select individuals for the next generation
            self.population = self.select_individuals(self.population, fitness_scores, offspring, offspring_fitness_scores)

            print(f"Gen: {generation} | Best: {max(offspring_fitness_scores).cpu().int().numpy()} | Avg: {(sum(offspring_fitness_scores.int())/len(offspring_fitness_scores)).cpu().int().numpy()}")

    def evaluate_population(self, population):
        # Evaluate the fitness of each individual in the population
        fitness_scores = []
        for individual in population:
            fitness_score = evaluate(individual, self.device)
            fitness_scores.append(fitness_score)
        return torch.tensor(fitness_scores).to(self.device)

    def select_parents(self, population, fitness_scores):
        # Select parents for the next generation
        fitness_scores = fitness_scores.float()
        fitness_scores += 1e-3
        parent_indices = torch.multinomial(fitness_scores, self.population_size, replacement=True).to(self.device)
        parents = population[parent_indices]
        return parents

    def generate_offspring(self, parents):
        # Generate new offspring through crossover and mutation
        offspring = []
        for i in range(self.population_size):
            parent1 = parents[i]
            parent2 = parents[(i + 1) % self.population_size]
            child = self.crossover(parent1, parent2)
            child = self.mutate(child)
            offspring.append(child)
        return torch.stack(offspring)

    def select_individuals(self, population, fitness_scores, offspring, offspring_fitness_scores):
        # Select individuals for the next generation
        combined_population = torch.cat([population, offspring])
        combined_fitness_scores = torch.cat([fitness_scores, offspring_fitness_scores])
        _, indices = torch.topk(combined_fitness_scores, self.population_size)
        selected_individuals = combined_population[indices]
        return selected_individuals



# Instantiate the genetic algorithm
gen_alg = GeneticAlgorithm(population_size=100, mutation_rate=0.01)

for i in range(6):
    gen_alg.evolve(num_generations=30)
    best_individual = gen_alg.population[np.argmax([evaluate(individual, gen_alg.device) for individual in gen_alg.population])]
    animate(best_individual, gen_alg.device, i)

# Get the best individual in the final population
best_individual = gen_alg.population[np.argmax([evaluate(individual.cpu(), gen_alg.device) for individual in gen_alg.population])].cpu()

pattern = list(torch.round(best_individual.cpu().unsqueeze(0).to(gen_alg.device)).cpu().int().numpy()[0])

print(evaluate(best_individual, gen_alg.device))
print(pattern)

util.animategif(sim.convert2twod(pattern,10), iterations, "final")

net=Net()

print(net.fc1)
print(net.fc2)
print(net.fc3)
print(net.fc4)