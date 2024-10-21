def dfs_limited(graph, node, goal, depth_limit):
    if depth_limit == 0 and node == goal:
        return [node]
    elif depth_limit > 0:
        for neighbor in graph.get(node, []):
            path = dfs_limited(graph, neighbor, goal, depth_limit - 1)
            if path:
                return [node] + path
    return None

def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        path = dfs_limited(graph, start, goal, depth)
        if path:
            return path
    return None

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H'],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}

start_node = 'A'
goal_node = 'G'
max_depth = 5

result = iddfs(graph, start_node, goal_node, max_depth)
if result:
    print(f"Path to goal: {result}")
else:
    print("Goal not found")
