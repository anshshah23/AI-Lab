import random

def hill_climb_search(problem, initial_state):
    current_state = initial_state
    current_value = problem(current_state)
    
    while True:
        neighbors = get_neighbors(current_state)
        next_state = None
        next_value = float('-inf')
        
        for neighbor in neighbors:
            value = problem(neighbor)
            if value > next_value:
                next_state = neighbor
                next_value = value
        
        if next_value <= current_value:
            return current_state
        
        current_state = next_state
        current_value = next_value

def get_neighbors(state):
    return [state - 1, state + 1]  
def problem(state):
    return -(state ** 2) + 10  
initial_state = random.randint(-10, 10)

solution = hill_climb_search(problem, initial_state)
print(f"Solution found: {solution}")
print(f"Value at solution: {problem(solution)}")
