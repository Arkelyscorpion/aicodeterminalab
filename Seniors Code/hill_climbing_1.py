def makeGraph():
    adj = dict()
    adj['A'] = [('B', 10), ('C', 8), ('D', 4)]
    adj['B'] = [('E', 8)]
    adj['C'] = [('F', 8), ('G', 5)]
    adj['D'] = [('X', 0)]
    adj['E'] = adj['F'] = []
    adj['G'] = [('H', 4)]
    adj['H'] = [('X', 0)]
    return adj
    

def hill_climbing(adj, curr_node, curr_val, goal):
    global path
    path.append((curr_node, curr_val))
    
    if(curr_node == goal):
        return
    
    target_node, target_val = '', 0
    for node, value in adj[curr_node]:
        if(value < curr_val):
            target_node = node
            target_val = value
            break
    
    hill_climbing(adj, target_node, target_val, goal)
        

if __name__ == "__main__":
    adj = makeGraph()
    print("\nInput Graph : ", adj)
    start, starting_val, goal = 'A', 9, 'X'
    print("\nStarting node = ", start)
    print("Goal node", goal)
    path = []
    hill_climbing(adj, start, starting_val,  goal)
    print("\nPath taken - ", path)
    