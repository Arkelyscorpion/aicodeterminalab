n=int(input("Enter the no of queens: "))
board=[["_"]*n for _ in range(n)]
def backtrack(board,col):
    if col==n:
        return True
    for row in range(n):
        if is_valid(board,row,col,n):
            board[row][col]="Q"
            if backtrack(board,col+1):
                return True
            board[row][col]="_"
    return False
def is_valid(board,row,col,n):
    for i in range(n):
        if board[row][i]=="Q" or board[i][col]=="Q":
            return False
    for i in range(n):
        for j in range(n):
            if (i+j==row+col or i-j==row-col) and board[i][j]=="Q":
                return False
    return True
if backtrack(board,0):
    for i in board:
        print(i)
else:
    print("No solution found")
