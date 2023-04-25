graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': [],
    'J': []
}
score1 = {
    'E':3,
    'F':4,
    'G':5,
    'H':1,
    'I':9,
    'J':8
}
def alpha_beta(node,is_max,alpha,beta):
    if not graph[node]:
        return score1[node]
    if is_max:
        max_score=float("-inf")
        for i in graph[node]:
            score=alpha_beta(i,False,alpha,beta)
            max_score=max(max_score,score)
            alpha=max(max_score,alpha)
            if alpha>=beta:
                break
        return max_score
    else:
        min_score=float("inf")
        for i in graph[node]:
            score=alpha_beta(i,True,alpha,beta)
            min_score=min(min_score,score)
            beta=min(beta,min_score)
            if alpha>=beta:
                break
        return min_score
score=alpha_beta('A',True,float("-inf"),float("inf"))
print("Best Score:",score)
