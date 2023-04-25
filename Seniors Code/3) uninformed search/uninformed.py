from collections import deque
import time
import heapq as hq

def makeGraph():
    adj = dict()
    adj['A'], adj['B'], adj['C'], adj['D'] = ['B', 'C'], ['D', 'E'], ['F', 'G'], ['H', 'I']
    adj['E'], adj['F'], adj['G'] = ['J', 'K'], ['L', 'M'], ['N', 'O']
    adj['H'], adj['I'], adj['J'], adj['K'] = ['I'], ['J'], ['K'], ['L'] 
    adj['L'], adj['M'], adj['N'], adj['O'] = ['M'], ['N'], ['O'], []
    return adj

def breadth_first_search(adj):
    global visited
    print("\n****** Testing BFS ******\n")
    q = deque()
    q.append('A')
    while(q):
        time.sleep(0.001)
        curr = q.popleft()
        print(curr, end= " ")
        visited.add(curr)
        for dest_node in adj[curr]:
            if(dest_node not in visited):
                q.append(dest_node)
        
def depth_first_search(adj):
    global visited
    print("\n****** Testing DFS ******\n")
    def dfs_util(adj, curr):
        time.sleep(0.001)
        print(curr, end = " ")
        visited.add(curr)
        for dest_node in adj[curr]:
            if(dest_node not in visited):
                dfs_util(adj, dest_node)
    dfs_util(adj, 'A')
    
      
def iterative_deepening_search(adj):
    print("\n****** Testing IDDFS ******\n")
    def iddfs_util(adj, curr, depth):
        
        global visited
        if(depth == 0):
            return
        time.sleep(0.001)
        print(curr, end = " ")
        visited.add(curr) 
        for dest_node in adj[curr]:
            if(dest_node not in visited):
                iddfs_util(adj, dest_node, depth-1)
    for depth in range(1, 5):
        visited.clear()
        print("depth = ", depth, ":")
        iddfs_util(adj, 'A', depth)
        print()

def uniform_cost_search(not_used):
    wts = dict()
    wts['A'], wts['B'] = [('B', 1), ('C', 2)], [('D', 3), ('E', 4)],
    wts['C'], wts['D'] = [('F', 5), ('G', 6)], [('H', 7), ('I', 8)]
    wts['E'], wts['F'], wts['G'] = [('J', 1), ('K', 2)], [('L', 3), ('M', 4)], [('N', 5), ('O', 6)]
    wts['H'] = wts['I'] = wts['J'] = wts['K'] = wts['L'] = wts['M'] = wts['N'] = wts['O'] = []
    print("\n****** Testing Uniform Cost Search ******\n")
    
    pq = [(0, 'A')]
    hq.heapify(pq)
    visited = set()
    while(len(pq) != 0):
        time.sleep(0.001)
        curr = hq.heappop(pq)
        tot_wt = curr[0]
        curr_node = curr[1]
        print(curr_node, end = " ")
        
        if(curr_node not in visited):   visited.add(curr_node)
        else:   continue
        
        for dest_node, edge_val in wts[curr_node]:
            if(dest_node not in visited):
                hq.heappush(pq, (tot_wt + edge_val, dest_node))

            
def bidirectional_search(adj):
    
    print("\n****** Testing Bidirectional Search ******\n")
    fwd_queue, rev_queue = deque(['A']), deque(['H'])
    fwd_vis, rev_vis = set(), set()
    fwd_vis.add('A')
    rev_vis.add('H')
    
    while(len(fwd_queue)>0 and len(rev_queue)>0):
        if(len(fwd_queue) > 0):
            curr_fwd = fwd_queue.popleft()
            print("Forward = ", curr_fwd)
            if(curr_fwd in rev_vis):    return
            
            for dest_node in adj[curr_fwd]:
                if(dest_node not in fwd_vis):
                    fwd_vis.add(dest_node)
                    fwd_queue.append(dest_node)

        if(len(rev_queue) > 0):
            curr_rev = rev_queue.popleft()
            print("Backward = ", curr_rev)
            if(curr_rev in fwd_vis):    return
            
            for dest_node in adj[curr_rev]:
                if(dest_node not in rev_vis):
                    rev_vis.add(dest_node)
                    rev_queue.append(dest_node)
        
            

if __name__ == "__main__":
    adj = makeGraph()
    tests = [breadth_first_search,
             depth_first_search,
             iterative_deepening_search,
             uniform_cost_search,
             bidirectional_search
             ]
    best_time, best_method = float('inf'), None
    
    for test in tests:
        visited = set()
        start = time.time()
        test(adj)
        end = time.time()
        time_taken =  end - start
        print("\nTime elapsed = {:.10f}".format(time_taken), end = "\n")
    if(time_taken < best_time):
        best_time = time_taken
        best_method = test
    print("\n************\nBest method = ", best_method.__name__, "\nTime taken = ", best_time)