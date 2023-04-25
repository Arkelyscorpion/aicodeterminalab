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
def minmax(node,is_max):
    if not graph[node]:
        return score1[node]
    if is_max:
        max_score=float("-inf")
        for i in graph[node]:
            score=minmax(i,False)
            max_score=max(max_score,score)
        return max_score
    else:
        min_score=float("inf")
        for i in graph[node]:
            score=minmax(i,True)
            min_score=min(min_score,score)
        return min_score
score=minmax('A',True)
print("Best Score:",score)
