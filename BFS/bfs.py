graph={}
vertices=int(input("Enter the no of vertices : "))
for i in range(vertices):
    graph[i]={}
edges=int(input("Enter the no of edges : "))
for i in range(edges):
    print("The nodes for edge",i+1)
    v1=int(input("Enter vertex 1: "))
    v2=int(input("Enter vertex 2: "))
    cost=int(input("Enter cost: "))
    graph[v1][v2]=cost
    graph[v2][v1]=cost
start=int(input("Enter starting node: "))
goal=int(input("Enter goal node: "))
queue=[]
visited=[]
tra_path=[]
queue.append(start)
parent={start:None}
while(len(queue)>0):
    node=queue.pop(0)
    visited.append(node)
    tra_path.append(node)
    if node==goal:
        print("Traversal path:",tra_path)
        break
    for i in graph[node].keys():
        if i not in visited:
            queue.append(i)
            parent[i]=node
else:
    print("Cannot reach goal node")
act_path=[goal]
while act_path[-1]!=start:
    act_path.append(parent[act_path[-1]])
act_path.reverse()
print("Actual path:",act_path)
cost=0
for i in range(len(act_path)-1):
    cost=cost+graph[act_path[i]][act_path[i+1]]
print("Cost:",cost)
