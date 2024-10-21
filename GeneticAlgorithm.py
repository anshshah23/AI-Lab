import random

# Parameters for Genetic Algorithm
POPULATION_SIZE = 10
GENES = 5  # Number of bits in the binary string (for range 0-31)
MUTATION_RATE = 0.01
GENERATIONS = 100

# Fitness function: maximize f(x) = x^2
def fitness(individual):
    # Convert binary string to integer and calculate fitness (x^2)
    x = int(''.join(map(str, individual)), 2)
    return x ** 2

# Create an individual (random binary string)
def create_individual():
    return [random.randint(0, 1) for _ in range(GENES)]

# Create initial population
def create_population():
    return [create_individual() for _ in range(POPULATION_SIZE)]

# Selection: Tournament Selection
def tournament_selection(population, fitnesses):
    # Select two individuals and return the one with better fitness
    i, j = random.sample(range(POPULATION_SIZE), 2)
    return population[i] if fitnesses[i] > fitnesses[j] else population[j]

# Crossover: Single-point crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, GENES - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation: Flip a random bit with some probability
def mutate(individual):
    for i in range(GENES):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]  # Flip the bit
    return individual

# Genetic Algorithm main loop
def genetic_algorithm():
    population = create_population()

    for generation in range(GENERATIONS):
        # Evaluate fitness of the population
        fitnesses = [fitness(individual) for individual in population]
        
        # If the best individual is found
        best_fitness = max(fitnesses)
        best_individual = population[fitnesses.index(best_fitness)]
        
        print(f"Generation {generation}: Best Fitness = {best_fitness}")
        
        # Create new population (next generation)
        new_population = []
        
        # Select and breed individuals to create the next generation
        while len(new_population) < POPULATION_SIZE:
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            if len(new_population) < POPULATION_SIZE:
                new_population.append(mutate(child2))
        
        # Replace old population with new population
        population = new_population
    
    # Return the best individual from the final population
    return best_individual, best_fitness

# Run the genetic algorithm
best_individual, best_fitness = genetic_algorithm()

# Convert the best individual (binary string) to integer
best_solution = int(''.join(map(str, best_individual)), 2)
print(f"\nBest Individual: {best_individual}")
print(f"Best Solution (Integer): {best_solution}")
print(f"Best Fitness: {best_fitness}")
