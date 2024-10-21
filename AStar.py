import heapq

def a_star_search(graph, start, goal, h):
    open_list = []
    heapq.heappush(open_list, (0, start))  
    g_score = {start: 0}
    f_score = {start: h(start)}
    
    came_from = {}
    
    while open_list:
        current = heapq.heappop(open_list)[1]
        
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(neighbor)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))
    
    return None

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path

def heuristic(node, goal='G'):
    h_values = {
        'A': 6,
        'B': 5,
        'C': 4,
        'D': 7,
        'E': 3,
        'F': 2,
        'G': 0,
        'H': 5 
    }
    return h_values.get(node, float('inf'))

graph = {
    'A': [('B', 1), ('C', 2), ('D', 4)],
    'B': [('E', 2), ('F', 3)],
    'C': [('F', 1)],
    'D': [('H', 2)],
    'E': [('G', 5)],
    'F': [('G', 1)],
    'H': []
}

start_node = 'A'
goal_node = 'G'

path = a_star_search(graph, start_node, goal_node, lambda node: heuristic(node, goal_node))
if path:
    print(f"Path to goal: {path}")
else:
    print("No path found to the goal")
