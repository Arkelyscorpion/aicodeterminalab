import copy

vis=[]
res=[]
parent={}
state=[[1,2,3],
       [4,5,6],
       [0,7,8]]
target=[[2,0,3],
        [1,5,6],
        [4,7,8]]
zero=(2,0)
parent[tuple(map(tuple,state))]=None

def dfs(state,target,zero):
    queue=[]
    queue.append((state,zero))
    visited=[]
    while queue:
        state,zero=queue.pop(0)
        if state==target:
            print("found")
            return True
        visited.append(state)
        curr_x,curr_y=zero[0],zero[1]
        possiblities=[]
        if(curr_x!=0):
            possiblities.append((curr_x-1,curr_y))
        if(curr_x!=2):
            possiblities.append((curr_x+1,curr_y))
        if (curr_y!=0):
            possiblities.append((curr_x,curr_y-1))
        if(curr_y!=2):
            possiblities.append((curr_x,curr_y+1))
        
        for pos in possiblities:
            new_x,new_y=pos[0],pos[1]
            new_state=copy.deepcopy(state)
            new_state[new_x][new_y],new_state[curr_x][curr_y]=0,state[new_x][new_y]
            if new_state not in vis:
                parent[tuple(map(tuple,new_state))]=state
                queue.append((new_state,pos))      
    return False

def printpath():
    path=[target]
    while path[-1]!=state:
        path.append(parent[tuple(map(tuple,path[-1]))])
    return path[::-1]
dfs(state,target,zero)
path=printpath()
for i in path:
    for j in i:
        print(j)
    print()
