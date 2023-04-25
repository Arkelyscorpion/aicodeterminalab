def hill_climbing(graph, curr_node, curr_val, goal):
    global path,cost
    path.append(curr_node)
    cost+=curr_val
    
    if(curr_node == goal):
        return
    
    target_node, target_val = '', float('inf')
    for node, value in graph[curr_node].items():
        if value < target_val and node not in path:
            target_node = node
            target_val = value
    if target_node == '':
        return
    
    hill_climbing(graph, target_node, target_val, goal)

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'D': 1},
    'C': {'A': 3, 'E': 5},
    'D': {'B': 1, 'G': 3},
    'E': {'C': 5, 'F': 1},
    'F': {'E': 1, 'G': 2},
    'G': {'D': 3, 'F': 2}
}

start='A'
goal='G'

path=[]
cost=0

hill_climbing(graph,start,0,goal)
if(len(path)>0):
    print("Path : "," -> ".join(path))
else:
    print("No path found")
print(cost)
