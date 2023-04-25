from collections import deque

def isSafe(x, y):
    global visited
    if((x, y) in visited or x<0 or y<0 or x>7 or y>7):
        return False
    return True

def knight(src, dest):
    q = deque([(src, 0)])
    possiblities = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    
    while(q):
        size = len(q)
        print("\n****\n")
        for _ in range(size):
            curr = q.popleft()
            print(curr[0], end = " ")
            curr_pos, curr_lvl = curr[0], curr[1]        
            x, y = curr_pos
            
            if(curr_pos == dest):
                return curr_lvl
            
            for dx, dy in possiblities:
                x_new, y_new = x + dx, y + dy
                if(isSafe(x_new, y_new)):
                    parent[(x_new, y_new)] = (x, y)
                    q.append(((x_new, y_new), curr_lvl + 1))
                       
def printPath(parent, curr):
    if(curr == (-1, -1)):
        return
    printPath(parent, parent[curr])
    print(curr, end = " ")
        

if __name__ == "__main__":
    src, dest = (3, 4), (6, 3)
    visited, parent = set(), dict()
    res = knight(src, dest)
    print("\nNumber of steps needed = ", res)
    parent[src] = (-1, -1)
    curr = (6, 3)
    print("\nPath followed = ", end = " ")
    printPath(parent, curr)
