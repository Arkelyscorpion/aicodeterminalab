def isSafe(grid, row, col, board_size):
    for i in range(0, board_size):
        if(grid[i][col] == 'Q'):
            return False
    
    for i in range(0, board_size):
        if(grid[row][i] == 'Q'):
            return False
    
    i, j = row, col
    
    while(i >= 0 and j>=0):
        if(grid[i][j] == 'Q'):
            return False
        i-=1
        j-=1
    
    i, j = row, col
    
    while(i<board_size and j>=0):
        if(grid[i][j] == 'Q'):
            return False
        i += 1
        j -= 1
    
    return True
    
def displayBoard(grid):
    for row in grid:
        print(row)
    print("\n\n")


def queens_dfs(grid, col, board_size):
    if(col == board_size):
        return True
    
    for row in range(0, board_size):
        if(isSafe(grid, row, col, board_size)):
            grid[row][col] = 'Q'
            displayBoard(grid)
            if(queens_dfs(grid, col+1, board_size)):
                return True
            grid[row][col] = '-'
    
    return False
    

if __name__ == "__main__":
    board_size = int(input("Enter number of queens : "))
    grid = [['-' for col in range(board_size)] for row in range(0, board_size)]
    queens_dfs(grid, 0, board_size)
    for row in grid:
        for ele in row:
            print(ele, end = " ")
        print()