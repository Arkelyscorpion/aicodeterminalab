from collections import deque

# Convert list of list to tuple of tuple
def makeTuple(grid):
    return tuple(tuple(ele) for ele in grid)

#convert tuple of tuple to list of list
def makeList(grid):
    return [[grid[i][j] for j in range(3)] for i in range(3)]

def printPath(target, parent):
    res = []
    curr = target
    src = -1
    
    while(curr != src):
        res.append(curr)
        curr = parent[curr]
    
    print("\nResult : \n")
    while(len(res) != 0):
        curr = res.pop()
        for i in range(3):
            for j in range(3):
                print(curr[i][j], end=" ")
            print()
        print(" \n*********\n ")
    

def puzzle_bfs(start, end, zero):
    
    q = deque()                         # To hold the bfs queue
    vis = set()                         # To hold the visited states
    parent = dict()                     # To store parent of each state
    parent[makeTuple(start)] = -1       # Parent of initial state = -1    
    q.append((makeTuple(start), zero))  # Current matrix state and the zero postion are pushed into queue
    vis.add(makeTuple(start))
    end = makeTuple(end)
    isSolvable = False
    
    while(len(q) != 0):
        
        curr_item = q.popleft()
        curr_state = curr_item[0]
        zero = curr_item[1]
        x, y = zero[0], zero[1]
        possiblities = []
        
        if(curr_state == end):
            isSolvable = True
            break
        
        if(x != 0): possiblities.append((x-1, y))   # Cant push zero up when it is in row 0
        if(x != 2): possiblities.append((x+1, y))   # cant push zero down when it is in row 2
        if(y != 0): possiblities.append((x, y-1))   # cant push zero left when it is in col 0
        if(y != 2): possiblities.append((x, y+1))   # cant push zero right when it is in col 2
        
        for poss in possiblities:
            new_x, new_y = poss[0], poss[1]
            temp_state = makeList(curr_state)
            temp_state[x][y], temp_state[new_x][new_y] = temp_state[new_x][new_y], 0
            temp_state = makeTuple(temp_state)
            if(temp_state not in vis):
                q.append((temp_state, poss))
                vis.add(temp_state)
                parent[temp_state] = curr_state
            
    if(isSolvable):
        printPath(end, parent)
    else:
        print("Cant work with these inputs")
            
            
def displayGrid(grid):
    for row in grid:
        for ele in row:
            print(ele, end = " ")
        print()

if __name__ == "__main__":
    
    start, end = [], []
    
#    print("\nEnter starting configuration : ")
#    for i in range(3):
#        temp = map(int, input().strip().split())
#        start.append(list(temp))
#    
#    print("\nEnter ending configuration : ")
#    for i in range(3):
#        temp = map(int, input().strip().split())
#        end.append(list(temp))
    
    start = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
    end =   [[1, 2, 3], [5, 6, 4], [7, 0, 8]]
    
    # Find the position of zero in the starting configuration
    zero = tuple()
    for i in range(3):
        for j in range(3):
            if(start[i][j] == 0):
                zero = (i, j)
                break
    
    print("\nStarting state : \n")
    displayGrid(start)
    
    print("\nEnding state : \n")
    displayGrid(end)
            
    puzzle_bfs(start, end, zero)