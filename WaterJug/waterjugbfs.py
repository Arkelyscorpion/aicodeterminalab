def waterjug(jug1,jug2,need):
    visited=set()
    queue=[(0,0,[])]
    while queue:
        x,y,steps=queue.pop(0)
        if x==0 and y==need or x==need and y==0:
            return steps+[f"Result = ({x},{y})"]
        if (x,y) in visited:
            continue
        visited.add((x,y))
        queue.append((jug1,y,steps+[f"Fill jug1 ({jug1},{y})"]))
        queue.append((x,jug2,steps+[f"Fill jug2 ({x},{jug2})"]))
        queue.append((0,y,steps+[f"Empty jug1 ({0},{y})"]))
        queue.append((x,0,steps+[f"Empty jug2 ({x},{0})"]))
        if x+y>=jug2:
            queue.append((x+y-jug2,jug2,steps+[f"Transfer {jug2+jug1-x-y} from jug1 to jug2 ({x+y-jug2},{jug2})"]))
        else:
            queue.append((0,x+y,steps+[f"Transfer {x} from jug1 to jug2 ({0},{x+y})"]))
        if x+y>=jug1:
            queue.append((jug1,x+y-jug1,steps+[f"Transfer {jug2+jug1-x-y} from jug2 to jug1 ({jug1},{x+y-jug1})"]))
        else:
            queue.append((x+y,0,steps+[f"Transfer {y} from jug2 to jug1 ({x+y},{0})"]))
    return False
jug1=int(input("Enter capacity of jug1: "))
jug2=int(input("Enter capacity of jug2: "))
need=int(input("Enter need: "))
steps=waterjug(jug1,jug2,need)
if steps:
    for i in steps:
        print(i)
else:
    print("No solution found")                    
