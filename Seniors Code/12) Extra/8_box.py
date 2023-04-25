def makeGraph():
    adj, domain = dict(), dict()

    adj['a'] = ['b', 'c', 'd', 'e']
    adj['b'] = ['a', 'd', 'e', 'f']
    adj['c'] = ['a', 'd', 'g']
    adj['d'] = ['a', 'b', 'c', 'e', 'g', 'h']
    adj['e'] = ['a', 'b', 'd', 'f', 'g', 'h']
    adj['f'] = ['f', 'e', 'h']
    adj['g'] = ['c', 'd', 'e', 'h']
    adj['h'] = ['d', 'e', 'f', 'g']
    
    sorted_keys = sorted(adj, key = lambda ele : len(adj[ele]), reverse = True)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    for num in numbers:
        domain[num] = sorted_keys[:]
    return adj, domain

def remove_current_node_from_all_numbers(curr_node):
    global adj, domain
    for key, val in domain.items():
            li = domain[key]
            if(curr_node in li):
                li.remove(curr_node)
            domain[key] = li[:]

def remove_adj_nodes_from_next_number(target_number, adj_nodes):
    for node in adj_nodes:
            if(node in domain[target_number]):
                domain[target_number].remove(node)
    
def solve(adj, domain):
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    for curr_num in numbers:
        
        curr_node = domain[curr_num][0]
        remove_current_node_from_all_numbers(curr_node)
        domain[curr_num] = [curr_node]
        
        if(curr_num == 8):
            break
        
        adj_nodes = adj[curr_node]
        remove_adj_nodes_from_next_number(curr_num + 1, adj_nodes)
        
if __name__ == "__main__":
    adj, domain = makeGraph()
    result = dict()
    solve(adj, domain)
    print(domain)