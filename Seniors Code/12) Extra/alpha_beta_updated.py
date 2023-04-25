def buildTree():
    adj = dict()
    adj['A'] = ['B', 'Q']
    adj['B'] = ['C', 'J']
    adj['C'] = ['D', 'G']
    adj['D'] = ['10', '11']
    adj['G'] = ['9', '12']
    adj['J'] = ['K', 'N']
    adj['K'] = ['14', '15']
    adj['N'] = ['13', '14']
    adj['Q'] = ['R', 'Z']
    adj['R'] = ['S', 'V']
    adj['S'] = ['15', '2']
    adj['V'] = ['4', '1']
    adj['Z'] = ['Z1', 'Z4']
    adj['Z1'] = ['3', '22']
    adj['Z4'] = ['24', '25']
    return adj
    
def playGame(adj, curr_node, chance, alpha, beta):
    global pruned  
    
    if(curr_node.isnumeric()):
        return int(curr_node)
    
    if(chance == 1): # Turn for Max player
        node_value = float('-inf')
        for child_node in adj[curr_node]:
            if(alpha >= beta):
                pruned.append((curr_node, child_node))
                break
            node_value = max(node_value, playGame(adj, child_node, 0, alpha, beta))
            alpha = max(alpha, node_value)
            
    else:
        node_value = float('inf')
        for child_node in adj[curr_node]:
            if(alpha >= beta):
                pruned.append((curr_node, child_node))
                break
            node_value = min(node_value, playGame(adj, child_node, 1, alpha, beta))
            beta = min(beta, node_value)
            
    return node_value
    

if __name__ == "__main__":
    adj = buildTree()
    pruned = []
    root_node = 'A'
    result = playGame(adj, root_node, 1, float('-inf'), float('inf'))
    print("Result = ", result)
    print("Pruned sub-trees are :", pruned)
    
    
    