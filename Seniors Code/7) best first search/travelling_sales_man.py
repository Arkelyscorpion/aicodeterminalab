import heapq as hq

def makeGraph(src, h_val, dest):
    global adj, heur
    adj[src] = dest[:]
    heur[src] = h_val

def best_first_search_tsp(src, adj, heur):
    pq, path, expanded_nodes = [], [], set()
    hq.heapify(pq)
    hq.heappush(pq, (heur[src], src))
    
    while(len(pq) != 0):
        curr_pair = hq.heappop(pq)
        curr_heur = curr_pair[0]
        curr_node = curr_pair[1]

        if(curr_node == src and src in expanded_nodes): # full tour complete
            path.append((curr_node, '$'))
            break
        elif(curr_node not in expanded_nodes):
            expanded_nodes.add(curr_node)
            path.append((curr_node, curr_heur))
        else:
            continue
        
        for dest in adj[curr_node]:
            hq.heappush(pq, (heur[dest], dest))
    
    return path

def displayResult(path, adj, heur, start):
    print("\nAdjacency List : ", adj)
    print("\nHeuristics : ", heur)
    print("\nStarting node = ", start)
    print("\nPath followed : ")
    total_cost = 0
    for node, h_val in path:
        if(h_val == "$"):
            print(node)
        else:
            total_cost += h_val
            print(f"{node} ({h_val}) -> ", end=" ")
    
    print("Total Cost = ", total_cost)
    
    
if __name__ == "__main__":
    adj, heur = dict(), dict()
    makeGraph(src = 'A', h_val = 2, dest = ['D', 'C'])
    makeGraph(src = 'B', h_val = 5, dest = ['E'])
    makeGraph(src = 'C', h_val = 4, dest = ['B', 'E'])
    makeGraph(src = 'D', h_val = 3, dest = ['C'])
    makeGraph(src = 'E', h_val = 6, dest = ['D', 'A'])
    start = 'A'
    path = best_first_search_tsp(start, adj, heur)
    displayResult(path, adj, heur, start)