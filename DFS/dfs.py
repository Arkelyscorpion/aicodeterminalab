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
tra_path=[]
visited=[]
parent={start:None}
act_path=[goal]
def dfs(graph,start,goal,visited):
    tra_path.append(start)
    visited.append(start)
    if(start==goal):
        return True
    for i in graph[start]:
        if i not in visited:
            parent[i]=start
            if dfs(graph,i,goal,visited):
                return True
    return False
dfs(graph,start,goal,visited)
print("Traversal path:",tra_path)
while act_path[-1]!=start:
    act_path.append(parent[act_path[-1]])
act_path.reverse()
print("Actual path:",act_path)
cost=0
for i in range(len(act_path)-1):
    cost+=graph[act_path[i]][act_path[i+1]]
print("Cost:",cost)

