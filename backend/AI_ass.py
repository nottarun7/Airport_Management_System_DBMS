
# AI CODING ASSIGNMENT 
# TARUN - AM.EN.U4ELC22047 

from collections import deque
 

graph = {
    'S1': ['S2'], 
    'S2': ['S1', 'S3', 'S9'], 
    'S3': ['S2', 'S4'], 
    'S4': ['S3', 'S5'], 
    'S5': ['S4', 'S6', 'S10'], 
    'S6': ['S5'],
    'S7': ['S8', 'S13'], 
    'S8': [ 'S7', 'S9'], 
    'S9': ['S10'], 
    'S10': ['S5', 'S9', 'S11'], 
    'S11': ['S10', 'S12'], 
    'S12': ['S11', 'S16'],
    'S13': ['S7', 'S14', 'S17'], 
    'S14': ['S13', 'S15'], 
    'S15': ['S14', 'S16'], 
    'S16': ['S15', 'S12', 'S21'],
    'S17': ['S13','S18', 'S22'], 
    'S18': ['S17', 'S19'], 
    'S19': ['S18', 'S20','S24'], 
    'S20': ['S19', 'S21'], 
    'S21': ['S20', 'S16', 'S25'],
    'S22': ['S17', 'S23', 'S26'], 
    'S23': ['S22', 'S24', 'S28'], 
    'S24': ['S23','S25','S19'], 
    'S25': ['S21', 'S24', 'S30'],
    'S26': ['S22','S27','S31'], 
    'S27': ['S26', 'S28'], 
    'S28': ['S27', 'S29','S23'], 
    'S29': ['S28','S30'], 
    'S30': ['S25', 'S29', 'S34'],
    'S31': ['S32', 'S35','S26'], 
    'S32': ['S31', 'S33'], 
    'S33': ['S32', 'S34'], 
    'S34': ['S33', 'S30', 'S40'],
    'S35': ['S36','S31'], 
    'S36': ['S35', 'S37'], 
    'S37': ['S36', 'S38'], 
    'S38': ['S37', 'S39'], 
    'S39': ['S38', 'S40'], 
    'S40': ['S39','S34']
}

def dfs_path(graph, start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph[node]):  
                if neighbor not in visited:
                    stack.append(path + [neighbor])

    return None

start_node = 'S37'
goal_node = 'S4'
path = dfs_path(graph, start_node, goal_node)
print("DFS path from", start_node, "to", goal_node, ":")
if path:
    print(" -> ".join(path))
else:
    print("No path found.")

# BFS function to find the shortest path
def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = path + [neighbor]
                queue.append(new_path)
    
    return None

# Run the BFS
start_node = 'S36'
goal_node = 'S1'
shortest_path = bfs_shortest_path(graph, start_node, goal_node)

# Output the result
print("Shortest path from", start_node, "to", goal_node, "is:")
print(" -> ".join(shortest_path))
print(len(shortest_path))