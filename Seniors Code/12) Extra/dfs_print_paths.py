def makeGraph():
    adj = dict()
    adj['a'] = ['b', 'c', 'e']
    adj['b'] = ['d', 'e']
    adj['c'] = ['e']
    adj['d'] = ['c']
    adj['e'] = []
    return adj

def findAllPaths(adj, curr, target, temp_list):
    
    global paths
    temp_list.append(curr)
    
    if(curr == target):  
        paths.append(temp_list[:])
        temp_list.pop()
        return
    
    for dest_node in adj[curr]:
        findAllPaths(adj, dest_node, target, temp_list)
    
    temp_list.pop()


if __name__ == "__main__":
    adj = makeGraph()
    start, target = 'a', 'e'
    print("\nStarting node = ", start)
    print("\nTarget node = ", target)
    paths = []
    findAllPaths(adj, start, target, [])
    for path in paths:
        print(path)