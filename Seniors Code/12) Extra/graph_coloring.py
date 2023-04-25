def solve(domain, adj):
    q=list(adj.keys())
    
    while(q):
        curr_node = q.pop(0)
        domain[curr_node] = list(domain[curr_node][0])
        
        for dest_node in adj[curr_node]:    
            colors = domain[dest_node]
            if(domain[curr_node][0] in colors):
                colors.remove(domain[curr_node][0])
            
graph= dict()
graph['q'] = ['nt', 'nsw', 'sa']
graph['sa'] = ['wa', 'nt', 'q', 'nsw', 'v']
graph['nsw'] = ['sa', 'q', 'v','nt']
graph['nt'] = ['wa', 'sa', 'q','nsw']
graph['wa'] = ['nt', 'sa']
graph['v'] = ['sa', 'nsw']
graph['t'] = []
domain =  dict()
colors = ['r', 'g', 'b']
for key in graph:
    domain[key] = colors[:]
try:
    solve(domain, graph)
    print(domain)
except:
    print("No solution found")
