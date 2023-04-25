board = [['X','O','X'],
         ['O','O','X'],
         ['.','.','.']]
def minmax(board,is_max):
    result=evaluate(board)
    if result is not None:
        return result,None
    best_move=None
    if is_max:
        max_score=float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j]=='.':
                    board[i][j]='X'
                    score,_=minmax(board,False)
                    board[i][j]='.'
                    if score>max_score:
                        max_score=score
                        best_move=(i,j)
        return max_score,best_move
    else:
        min_score=float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j]=='.':
                    board[i][j]='O'
                    score,_=minmax(board,True)
                    board[i][j]='.'
                    if score<min_score:
                        min_score=score
                        best_move=(i,j)
        return min_score,best_move
def evaluate(board):
    for row in board:
        if row[0]==row[1]==row[2] and row[0]!='.':
            return 1 if row[0]=='X' else -1
    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col] and board[0][col]!='.':
            return 1 if board[0][col]=='X' else -1
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!='.':
        return 1 if board[0][0]=='X' else -1
    if board[0][2]==board[1][1]==board[2][0] and board[0][2]!='.':
        return 1 if board[0][2]=='X' else -1
    for row in board:
        if '.' in row:
            return None
    return 0
score,best_move=minmax(board,True)
print("Score:",score)
print("Best Move:",best_move)
