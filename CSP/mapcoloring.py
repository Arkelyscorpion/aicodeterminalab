graph={}
"""variables=int(input("Enter the no of variables: "))
for i in range(variables):
    var=input("Enter variable name: ")
    adj=eval(input("Enter its adjacents: "))
    graph[var]=adj"""

graph['q'] = ['nt', 'nsw', 'sa']
graph['sa'] = ['wa', 'nt', 'q', 'nsw', 'v']
graph['nsw'] = ['sa', 'q', 'v']
graph['nt'] = ['wa', 'sa', 'q']
graph['wa'] = ['nt', 'sa']
graph['v'] = ['sa', 'nsw']
graph['t'] = []

domains=input("Enter the domains: ").split(',')
solution={}
print(domains)
for i in graph:
    solution[i]=domains[:] #shallow copy

print(solution)
def solve(graph,domain):
    queue=['q','sa','nsw','nt','wa','v','t']
    # queue = list(graph.keys())
    while queue:
        node=queue.pop(0)
        for neighbour in graph[node]:
            if domain[node][0] in domain[neighbour]:
                domain[neighbour].remove(domain[node][0])
                
try:
    solve(graph,solution)
    print(solution)
except:
    print("No solution found")
    
