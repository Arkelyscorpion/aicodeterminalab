def makeList(grid):
    return list(list(row) for row in grid)

def makeTuple(grid):
    return tuple(tuple(row) for row in grid)

def puzzle_dfs(curr_state, target, zero, vis, res):
    
    if(curr_state == target):
        return True
    curr_x, curr_y = zero[0], zero[1]
    possiblities = []
    
    if(curr_x != 0):
        possiblities.append((curr_x-1, curr_y))
    if(curr_x != 2):
        possiblities.append((curr_x+1, curr_y))
    if(curr_y != 0):
        possiblities.append((curr_x, curr_y-1))
    if(curr_y != 2):
        possiblities.append((curr_x, curr_y+1))
    
    for poss in possiblities:
        new_x, new_y = poss[0], poss[1]
        temp_state = makeList(curr_state)
        temp_state[curr_x][curr_y], temp_state[new_x][new_y] = temp_state[new_x][new_y], 0
        temp_state = makeTuple(temp_state)
        
        if(temp_state not in vis):
#            print(temp_state)
            vis.add(temp_state)
            if(puzzle_dfs(temp_state, target, poss, vis, res)):
                res.append(temp_state)
                return True
        
    return False
            
def displayGrid(grid):
    for row in grid:
        for ele in row:
            print(ele, end = " ")
        print()


if __name__ == "__main__":
    
    start, end = [], []
    
    start = [[1, 2, 3], [4 ,0, 6], [7, 8, 5]]
    end =   [[1, 2, 3], [5, 6, 4], [7, 0, 8]]
    
    print("\nStarting state : \n")
    displayGrid(start)
    
    print("\nEnding state : \n")
    displayGrid(end)
    
    # Find the position of zero in the starting configuration
    zero = tuple()
    for i in range(3):
        for j in range(3):
            if(start[i][j] == 0):
                zero = (i, j)
                break
    vis = set()
    res = []
    vis.add(makeTuple(start))
    puzzle_dfs(makeTuple(start), makeTuple(end), zero, vis, res)
    res.append(start)
    
    for grid in reversed(res):
        for row in grid:
            print(row)
        print("\n")
    
    

        
    
