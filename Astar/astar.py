from queue import PriorityQueue
graph = {}
vertices = int(input("Enter the no of vertices : "))
for i in range(vertices):
    graph[i] = {}
edges = int(input("Enter the no of edges : "))
for i in range(edges):
    print("The nodes for edge", i+1)
    v1 = int(input("Enter vertex 1: "))
    v2 = int(input("Enter vertex 2: "))
    cost = int(input("Enter cost: "))
    graph[v1][v2] = cost
    graph[v2][v1] = cost
start = int(input("Enter starting node: "))
goal = int(input("Enter goal node: "))


def heu(graph, start, goal):
    queue = [(start, 0)]
    visited = set()
    while queue:
        node, hops = queue.pop(0)
        if node == goal:
            return hops
        visited.add(node)
        for i in graph[node]:
            if i not in visited:
                queue.append((i, hops+1))
    return None


heuristic = [heu(graph, i, goal) for i in graph]
tra_path = []
visited = []
queue = PriorityQueue()
queue.put((0, start))
parent = {start: None}
cost_so_far = {start: 0}
while not queue.empty():
    cost, node = queue.get()
    visited.append(node)
    tra_path.append(node)
    if node == goal:
        break
    for i in graph[node]:
        if i not in visited:
            parent[i] = node
            cost_so_far[i] = cost_so_far[node]+graph[i][node]
            queue.put((heuristic[i]+cost_so_far[i], i))
print("Traversal path:", tra_path)
act_path = [goal]
while act_path[-1] != start:
    act_path.append(parent[act_path[-1]])
act_path.reverse()
print("Actual Path:", act_path)
cost = 0
for i in range(len(act_path)-1):
    cost += graph[act_path[i]][act_path[i+1]]
print("Cost:", cost)
