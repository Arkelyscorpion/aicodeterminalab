from collections import deque

def printPath(target, parent):
    res = []
    curr = target
    src = (-1, -1)
    
    while(curr != src):
        res.append(curr)
        curr = parent[curr]
    
    print()
    while(len(res) != 0):
        print(res.pop(), end = " -> ")
    print("GOAL")

# Available operations:
#    1. Fill the jug
#    2. Empty the jug
#    3. Transfer jug contents
    
def water_jug_bfs(j1, j2, water):
    
    visited = set()                     # To hold the already visited nodes
    q = deque()                         # To hold the bfs queue
    parent = dict()                     # To store parent of any node
    q.append((0, 0))                    # initially we start with (0, 0) as the starting state
    visited.add((0, 0))
    parent[(0, 0)] = (-1, -1)           # the starting state has no parent
    isSolvable = False                  # Sometimes problem cant be solved
    target = [(0, water), (water, 0)]   # required target state
    
    while(len(q) != 0):

        curr = q.popleft();
        if(curr in target):
            isSolvable = True
            break
        
        curr_j1, curr_j2 = curr[0], curr[1]
        possiblities = []
        
        possiblities.append((j1, curr_j2))  # 1a) Fill jug1
        possiblities.append((curr_j1, j2))  # 1b) Fill jug2
            
        possiblities.append((0, curr_j2))   # 2a) Empty jug1
        possiblities.append((curr_j1, 0))   # 2b) Empty jug2
            
        # 3a) Jug-1 to Jug-2
        # cant transfer when jug-1 is empty and jug-2 is already full
        if(curr_j1 != 0 and curr_j2 != j2): 
            total_water = curr_j1 + curr_j2
            # when total capacity is less than jug-2 capacity
            if(total_water <= j2):  possiblities.append((0, total_water))
            # when total capacity is greater than jug-2 capacity
            else:   possiblities.append((total_water-j2, j2))
        
        # 3b) Jug-2 to Jug-1
        # cant transfer when jug-2 is empty and jug-1 is already full
        if(curr_j1 != j1 and curr_j2 != 0):  
            total_water = curr_j1 + curr_j2
            # when total capacity is less than jug-1 capacity
            if(total_water <= j1):  possiblities.append((total_water, 0))
            # when total capacity is greater than jug-1 capacity
            else:   possiblities.append((j1, total_water-j1))
        
        for poss in possiblities:
            if(poss not in visited):
                q.append(poss)
                visited.add(poss)
                parent[poss] = curr
            
    if(isSolvable):
        printPath(curr, parent)
    else:
        print("Not possible to work with these inputs")
            

if __name__ == "__main__":
    
    jug1 = int(input("Enter jug 1 capacity : "))
    jug2 = int(input("Enter jug 2 capacity : "))
    water = int(input("Enter final capacity of water needed : "))
    water_jug_bfs(jug1, jug2, water)    