import random
POPULATION_SIZE = 10
GENES = 5
MUTATION_RATE = 0.01
GENERATIONS = 100
def fitness(individual):
    x = int(''.join(map(str, individual)), 2)
    return x ** 2
def create_individual():
    return [random.randint(0, 1) for _ in range(GENES)]
def create_population():
    return [create_individual() for _ in range(POPULATION_SIZE)]
def tournament_selection(population, fitnesses):
    i, j = random.sample(range(POPULATION_SIZE), 2)
    return population[i] if fitnesses[i] > fitnesses[j] else population[j]
def crossover(parent1, parent2):
    crossover_point = random.randint(1, GENES - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2
def mutate(individual):
    for i in range(GENES):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]  # Flip the bit
    return individual
def genetic_algorithm():
    population = create_population()
    for generation in range(GENERATIONS):
        fitnesses = [fitness(individual) for individual in population]
        best_fitness = max(fitnesses)
        best_individual = population[fitnesses.index(best_fitness)]
        
        print(f"Generation {generation}: Best Fitness = {best_fitness}")
        
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            if len(new_population) < POPULATION_SIZE:
                new_population.append(mutate(child2))
        population = new_population
    
    return best_individual, best_fitness
best_individual, best_fitness = genetic_algorithm()

best_solution = int(''.join(map(str, best_individual)), 2)
print(f"\nBest Individual: {best_individual}")
print(f"Best Solution (Integer): {best_solution}")
print(f"Best Fitness: {best_fitness}")
