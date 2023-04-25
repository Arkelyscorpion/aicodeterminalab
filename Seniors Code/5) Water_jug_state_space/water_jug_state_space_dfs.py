def water_jug_dfs(curr_j1, curr_j2, j1, j2, target, res, vis):
    
    print((curr_j1, curr_j2), end=" ")
    
    if((curr_j1, curr_j2) in target):
        return True
        
    # possibilies are Full jug-1, Full jug-2, Empty jug-1, Empty jug-2
    possiblities = [ (j1, curr_j2), (curr_j1, j2), (0, curr_j2), (curr_j1, 0)]
     
    # Another possiblity is transfer jug-1 contents to jug-2
    if(curr_j1 != 0 and curr_j2 != j2): 
        total_water = curr_j1 + curr_j2
        if(total_water <= j2): 
            possiblities.append((0, total_water))
        else: 
            possiblities.append((total_water - j2, j2))
    
    # Another possiblity is transfer jug-2 contents to jug-1
    if(curr_j1 != j1 and curr_j2 != 0):  
        total_water = curr_j1 + curr_j2
        if(total_water <= j1): 
            possiblities.append((total_water, 0))
        
        else: 
            possiblities.append((j1, total_water-j1))
    
    for poss in possiblities:
        if(poss not in vis):
            vis.add(poss)
            if( water_jug_dfs(poss[0], poss[1], j1, j2, target, res, vis) ):
                res.append(poss)
                return True
    return False
                


if __name__ == "__main__":
    
    jug1 = int(input("Enter jug 1 capacity : "))
    jug2 = int(input("Enter jug 2 capacity : "))
    water = int(input("Enter final capacity of water needed : "))
        
    target = [(water, 0), (0, water)]
    res = []
    vis = set()
    vis.add((0, 0))

    if(water_jug_dfs(0, 0, jug1, jug2, target, res, vis) == False):
        print("\nCant work with this input set")