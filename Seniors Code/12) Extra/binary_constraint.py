from collections import deque

def solve_problem(variables, domain):
    q = deque([('x3', 'x4'),
              ('x2', 'x3'),
              ('x1', 'x2'),
              ('x2', 'x1'),
              ('x3', 'x2'),
              ('x4', 'x3')])
    
    while(len(q) != 0):
        
        curr_rule = q.popleft()
        rule_left = curr_rule[0]
        rule_right = curr_rule[1]
        
        if(rule_left == 'x3' and rule_right == 'x4'):
            res = []
            for d3 in domain['x3']:
                condn = False
                for d4 in domain['x4']:
                    if(d3 != d4):
                        condn = True
                if(condn == True):
                    res.append(d3)
            domain['x3'] = res
            
        
        if(rule_left == 'x2' and rule_right == 'x3'):
            res = []
            for d2 in domain['x2']:
                condn = False
                for d3 in domain['x3']:
                    if(d2 > d3):
                        condn = True
                if(condn == True):
                    res.append(d2)
            domain['x2'] = res
            
            
        if(rule_left == 'x1' and rule_right == 'x2'):
            res = []
            for d1 in domain['x1']:
                condn = False
                for d2 in domain['x2']:
                    if(d1 >= d2):
                        condn = True
                if(condn == True):
                    res.append(d1)
            domain['x1'] = res
            
        
        if(rule_left == 'x2' and rule_right == 'x1'):
            res = []
            for d2 in domain['x2']:
                condn = False
                for d1 in domain['x1']:
                    if(d2 <= d1):
                        condn = True
                if(condn == True):
                    res.append(d2)
            domain['x2'] = res
            
        
        if(rule_left == 'x3' and rule_right == 'x2'):
            res = []
            for d3 in domain['x3']:
                condn = False
                for d2 in domain['x2']:
                    if(d3 < d2 or (d3-d2==2)):
                        condn = True
                if(condn == True):
                    res.append(d3)
            domain['x3'] = res
            
        
        if(rule_left == 'x4' and rule_right == 'x3'):
            res = []
            for d4 in domain['x4']:
                condn = False
                for d3 in domain['x3']:
                    if(d4 != d3):
                        condn = True
                if(condn == True):
                    res.append(d4)
            domain['x4'] = res
            
                
if __name__ == "__main__":
    variables = ['x1', 'x2', 'x3', 'x4']
    domain = {'x1' : [1, 2, 3, 4],
               'x2' : [3, 4, 5, 8, 9],
               'x3' : [2, 3, 5, 6,7, 9],
               'x4' : [3, 5, 7, 8, 9]
               }
    print("\nInitially domain : ", domain)
    solve_problem(variables, domain)
    print("\nAfter applying constraints :", domain)
    print("\nOne possible solution = : \n")
    for key, val in domain.items():
        print(key, " : ", str(val[0]))