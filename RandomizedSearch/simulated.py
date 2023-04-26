import random
import math
"""
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
"""

graph = {
    0: {1:10,2:15,3:20},
    1: {0:10,2:35,3:25},
    2: {0:15,1:35,3:30},
    3: {0:20,1:25,2:30},
}

start=0
def path_cost(path):
    cost=0
    for i in range(len(path)-1):
        cost+=graph[path[i]][path[i+1]]
    return cost
def get_path(graph):
    path=[start]
    all_keys=graph.keys()
    need_keys=[]
    for i in all_keys:
        if i!=start:
            path.append(i)
    path.append(start)
    return path
temperature=1000
cooling_rate=0.003
cur_path=get_path(graph)
cur_cost=path_cost(cur_path)
best_path=cur_path.copy()
best_cost=cur_cost
while temperature>1:
    new_path=cur_path.copy()
    i=random.randint(1,len(cur_path)-2)
    j=random.randint(1,len(cur_path)-2)
    while i==j:
        j=random.randint(1,len(cur_path)-2)
    new_path[i],new_path[j]=new_path[j],new_path[i]
    new_cost=path_cost(new_path)
    diff_cost=new_cost-cur_cost
    if diff_cost<0 or math.exp(-diff_cost/temperature)>random.uniform(0,1):
        cur_path=new_path
        cur_cost=new_cost
    if cur_cost<best_cost:
        best_cost=cur_cost
        best_path=cur_path.copy()
    temperature*=1-cooling_rate

print("Path:",best_path)
print("Cost:",best_cost)

