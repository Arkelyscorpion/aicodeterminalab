import copy
start=[]
for i in range(3):
    temp=input().split();
    temp=[int(x) for x in temp]
    start.append(temp)
goal=[[1,2,3],[4,5,6],[7,8,0]]
def distance(state):
    dist=0
    for i in range(3):
        for j in range(3):
            if state[i][j]!=0:
                row,col=divmod(state[i][j]-1,3)
                dist+=abs(row-i)+abs(col-j)
    return dist
curr_state=start
curr_h=distance(curr_state)
while True:
    print("Current State :")
    for row in curr_state:
        print(row)
    neighbours=[]
    for i in range(3):
        for j in range(3):
            if curr_state[i][j]==0:
                if i>0:
                    neighbour=copy.deepcopy(curr_state)
                    neighbour[i][j],neighbour[i-1][j]=neighbour[i-1][j],neighbour[i][j]
                    neighbours.append(neighbour)
                if i<2:
                    neighbour=copy.deepcopy(curr_state)
                    neighbour[i][j],neighbour[i+1][j]=neighbour[i+1][j],neighbour[i][j]
                    neighbours.append(neighbour)
                if j>0:
                    neighbour=copy.deepcopy(curr_state)
                    neighbour[i][j],neighbour[i][j-1]=neighbour[i][j-1],neighbour[i][j]
                    neighbours.append(neighbour)
                if j<2:
                    neighbour=copy.deepcopy(curr_state)
                    neighbour[i][j],neighbour[i][j+1]=neighbour[i][j+1],neighbour[i][j]
                    neighbours.append(neighbour)
    if not neighbours:
        break
    best_neighbour=min(neighbours,key=distance)
    best_h=distance(best_neighbour)
    if best_h>=curr_h:
        break
    curr_state=best_neighbour
    curr_h=best_h
print("Solution")
for row in curr_state:
    print(row)
