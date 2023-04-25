graph={'S':{'A':3,'B':1,'C':8},
       'A':{'S':3,'D':3,'E':7,'G':15},
       'B':{'S':1,'G':20},
       'C':{'S':8,'G':5},
       'D':{'A':3},
       'E':{'A':7},
       'G':{'A':15,'B':20,'G':5}
       }
start='S'
goal='G'
parent={start:None}
def heu(start,goal):
    queue=[(start,0)]
    visited=set()
    while queue:
        node,hops=queue.pop(0)
        visited.add(node)
        if node==goal:
            return hops
        for i in graph[node]:
            if i not in visited:
                queue.append((i,hops+1))
    return None
def hill_climb(start,goal):
    tra_path=[]
    visited=set()
    cur_node=start
    cur_heu=heu(start,goal)
    while True:
        tra_path.append(cur_node)
        tra_nodes=[]
        for i in graph[cur_node]:
            if i not in visited:
                parent[i]=cur_node
                visited.add(i)
                tra_nodes.append(i)
        if len(tra_nodes)==0:
            return tra_path
        min_node=min(tra_nodes,key=lambda x:heu(x,goal))
        min_heu=heu(min_node,goal)
        if min_heu>=cur_heu:
            return False
        cur_node=min_node
        cur_heu=min_heu
    return False
tra_path=hill_climb(start,goal)
if tra_path:
    print("Traversal Path:",tra_path)
    act_path=[goal]
    while act_path[-1]!=start:
        act_path.append(parent[act_path[-1]])
    act_path.reverse()
    print("Actual Path:",act_path)
    cost=0
    for i in range(len(act_path)-1):
        cost+=graph[act_path[i]][act_path[i+1]]
    print("Cost:",cost)
else:
    print("No solution found")
