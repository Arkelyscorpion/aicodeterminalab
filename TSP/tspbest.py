from queue import PriorityQueue
"""graph={}
heuristic=[]
vertices=int(input("Enter the no of vertices : "))
for i in range(vertices):
    graph[i]={}
    heuristic[i]=0
edges=int(input("Enter the no of edges : "))
for i in range(edges):
    print("The nodes for edge",i+1)
    v1=int(input("Enter vertex 1: "))
    v2=int(input("Enter vertex 2: "))
    cost=int(input("Enter cost: "))
    heuristic[i]=int(input("Enter heuristic: "))
    graph[v1][v2]=cost
    graph[v2][v1]=cost
start=int(input("Enter starting node: "))"""
graph = {
    0: {1:10,2:15,3:20},
    1: {0:10,2:35,3:25},
    2: {0:15,1:35,3:30},
    3: {0:20,1:25,2:30},
}
start=0
heuristic={0:1,1:7,2:12,3:4}
tra_path=[]
visited=set()
queue=PriorityQueue()
queue.put((heuristic[start],start))
while not queue.empty():
    cost,node=queue.get()
    if node in visited:
        continue
    visited.add(node)
    tra_path.append(node)
    if len(graph)==len(tra_path):
        tra_path.append(start)
        break
    for i in graph[node]:
        if i not in visited:
            queue.put((heuristic[i],i))
print("Traversal path:",tra_path)
cost=0
for i in range(len(tra_path)-1):
    cost+=graph[tra_path[i]][tra_path[i+1]]
print("Cost:",cost)
