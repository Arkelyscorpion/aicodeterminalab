import copy

vis=[]
res=[]

def dfs(state,target,zero):
    stack=[]
    stack.append((state,zero))
    visited=[]
    counter=0
    states=[]
    while stack:
        if counter>100:
            return False
        state,zero=stack.pop()
        states.append(state)
        if state==target:
            print("found")
            return states
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
                stack.append((new_state,pos))
        counter+=1
    return False

state=[[1,2,3],[4,5,6],[0,7,8]]
target=[[1,2,3],[4,5,6],[7,8,0]]
zero=(2,0)
states=dfs(state,target,zero)
if states:
    for state in states:
        for i in state:
            print(i)
        print()
else:
    print("No Solution found")
    
