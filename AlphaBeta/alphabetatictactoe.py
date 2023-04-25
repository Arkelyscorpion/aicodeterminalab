board = [['X','O','X'],
         ['O','O','X'],
         ['.','.','.']]
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
def alpha_beta(board,is_max,alpha,beta):
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
                    score,_=alpha_beta(board,False,alpha,beta)
                    board[i][j]=' '
                    if score>max_score:
                        max_score=score
                        best_move=(i,j)
                    alpha=max(alpha,max_score)
                    if alpha>=beta:
                        break
        return max_score,best_move
    else:
        min_score=float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j]=='.':
                    board[i][j]='O'
                    score,_=alpha_beta(board,True,alpha,beta)
                    board[i][j]=' '
                    if score<min_score:
                        min_score=score
                        best_move=(i,j)
                    beta=min(beta,min_score)
                    if alpha>=beta:
                        break
        return min_score,best_move
score,best_move=alpha_beta(board,True,float("-inf"),float("inf"))
print("Best Score:",score)
print("Best Move:",best_move)
