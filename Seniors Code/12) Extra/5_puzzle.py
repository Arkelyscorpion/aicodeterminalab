def makeList(grid):
    return list(list(row) for row in grid)

def makeTuple(grid):
    return tuple(tuple(row) for row in grid)

def isSafe(x, y):
    if(x<0 or y<0 or x>1 or y>2):   return False
    else:   return True

def solve_5_puzzle(curr, target, zero, temp_list):
    global visited, result
    temp_list.append(curr)
    
    if(curr == target):
        result.append(temp_list[:])
        return
    
    possiblities = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    x, y = zero[0], zero[1]
    
    for dx, dy in possiblities:
        new_x, new_y = x + dx, y + dy
        if(isSafe(new_x, new_y)):
            new_state = makeList(curr)
            new_state[new_x][new_y], new_state[x][y] = 0, new_state[new_x][new_y]
            new_state = makeTuple(new_state)
            if(new_state not in visited):
                visited.add(new_state)
                solve_5_puzzle(new_state, target, (new_x, new_y), temp_list)
    
    temp_list.pop()

def displayResult(start, target, result):
    print("\nStarting state = ", start)
    print("\nEnding state = ", target)
    print("\nResult : \n")
    for grid in result[0]:
        for row in grid:
            for ele in row:
                print(ele, end = " ")
            print()
        print("\n***\n")
    
    
if __name__ == "__main__":
    start = [[1, 2, 3], [5, 0, 4]]
    target = [[2, 5, 3], [1, 0, 4]]
    zero = (1, 1)
    visited, result = set(), list()
    visited.add(makeTuple(start))
    solve_5_puzzle(makeTuple(start), makeTuple(target), zero, [])
    displayResult(start, target, result)
    
    