import heapq as hq

# When there is a tie in weight, sort by ascending order of nodes
def new_cmp_lt(self,a,b):
    if(a[0] < b[0]):    return True
    elif(a[0] == b[0]): return (a[2] < b[2])
    else:               return False
        
hq.cmp_lt=new_cmp_lt

def addNode(src, dest):
    global adj
    adj[src] = dest[:]

def makeGraph():
    addNode('S', [(3, 'A'), (1, 'B'), (5, 'C')])
    addNode('A', [(10, 'G1'), (7, 'E')])
    addNode('B', [(2, 'C'), (2, 'F')])
    addNode('C', [(11, 'G3')])
    addNode('D', [(6, 'S'), (4, 'B'), (5, 'G2')])
    addNode('E', [(2, 'G1')])
    addNode('F', [(1, 'D')])

def printGraph(adj):
    for node, dest in adj.items():
        print("\n\n", node, end = " : ")
        for pair in dest:
            print(pair, end = " ")
    print("\n\nGoal States = G1, G2, G3")

def uniform_cost_search(adj, src, goals):
    pq = [(0, 0, src, '$')]
    hq.heapify(pq)
    visited = dict()
    while(len(pq) != 0):
        
        curr = hq.heappop(pq)
        tot_wt = curr[0]
        edge_wt = curr[1]
        curr_node = curr[2]
        parent = curr[3]
        
        if(curr_node in goals):
            visited[curr_node] = (parent, edge_wt)
            break
        elif(curr_node not in visited):
            visited[curr_node] = (parent, edge_wt)
        else:
            continue
        
        for edge_val, dest_node in adj[curr_node]:
            if(dest_node not in visited):
                hq.heappush(pq, (tot_wt + edge_val, edge_val, dest_node, curr_node))
    
    return visited
                
        
def displayResult(visited):
    path = []
    child = list(visited.keys())[-1]
    
    while(child != '$'):
        path.append((child, visited[child][1]))
        child = visited[child][0]
        
    tot_cost = 0
    print("\nResult\n")
    for node, edge_val in reversed(path):
        print(f"{node} ({edge_val}) -> ", end = " ")
        tot_cost += edge_val
    print("GOAL")
    print("\nTotal Cost = ", tot_cost)
        
    
if __name__ == "__main__":
    adj = dict()
    makeGraph()
    printGraph(adj)
    src = input("Enter starting node : ")
    goals = ["G1", "G2", "G3"]
    visited = uniform_cost_search(adj, src, goals)
    displayResult(visited)
    