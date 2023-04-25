def makeGraph():
    adj = dict()
    adj['A'] = ['B', 'C']
    adj['B'] = ['D']
    adj['C'] = ['E', 'F', 'G']
    adj['D'] = ['H', 'I']
    adj['E'] = ['J', 'K']
    adj['F'] = adj['G'] = adj['H'] = adj['I'] = adj['J'] = adj['K'] = []
    return adj

def printGraph(adj):
    print("\nGiven graph : ")
    for node, dest in adj.items():
        if(len(dest)==0):
            continue
        print("\n\n", node, end = " : ")
        for pair in dest:
            print(pair, end = " ")
        print()

def search(adj, curr, depth, target):
    if(depth == 0):
        return False
    
    print(curr, end = " ")
    
    if(curr == target):
        return True
    
    for node in adj[curr]:
        if(search(adj, node, depth-1, target) == True):
            return True
            

def iter_deep_search(adj, src, target):
    depth = 1
    while True:
        print("\ndepth = ", depth, ":")
        if(search(adj, src, depth, target) == True):        
            print("found")
            break
        else:
            depth += 1
            print("\n\n********")
        

if __name__ == "__main__":
    adj = makeGraph()
    printGraph(adj)
    src, target = 'A', 'I'
    print("\nStarting node = ", src)
    print("Target node = ", target)
    iter_deep_search(adj, src, target)
    