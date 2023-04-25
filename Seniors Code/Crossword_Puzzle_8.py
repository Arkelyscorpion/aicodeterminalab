# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 17:30:05 2021

@author: Srinidhi
"""

from collections import defaultdict

# ************************************* INITIALIZATION FUNCTIONS ************************************* #

def initDomains():
    domain, position = dict(), dict()
    li2, li3 = ["HEEL", "HIKE", "KEEL", "KNOT", "LINE"], ["AFT", "ALE", "EEL", "LEE", "TIE"]
    li1 = ["HOSES", "LASER", "SAILS", "SHEET", "STEER"]
    domain = {"1A" : li1[:], "4A" : li2[:], "7A" : li3[:], "8A" : li1[:], 
              "2D" : li1[:], "3D" : li1[:], "5D" : li2[:], "6D" : li3[:] }
    position = {"1A" : (0, 0, 'A'), "4A" : (2, 1, 'A'), "7A" : (3, 2, 'A'), "8A" : (4, 0, 'A'), 
                "2D" : (0, 2, 'D'), "3D" : (0, 4, 'D'), "5D" : (2, 3, 'D'), "6D" : (3, 0, 'D') }
    return domain, position

def initConstraints():
    constr = defaultdict(list)
    li = [('1A', '2D', 3, 1), ('1A', '3D', 5, 1), ('4A', '2D', 2, 3), ('4A', '5D', 3, 1),
          ('4A', '3D', 4, 3), ('7A', '2D', 1, 4), ('7A', '5D', 2, 2), ('7A', '3D', 3, 4),
          ('8A', '6D', 1, 2), ('8A', '2D', 3, 5), ('8A', '5D', 4, 3), ('8A', '3D', 5, 5)]
    for var1, var2, x, y in li:
        constr[var1].append((var2, x, y))
        constr[var2].append((var1, y, x))
    return constr

def initGrid():
    grid = [ ['1A', ' ', '2D', ' ', '3D'], ['-', '-', ' ', '-', ' '],
             ['-', '4A', ' ', '5D', ' '],  ['6D', '-', '7A', ' ', ' '],
             ['8A', ' ', ' ', ' ', ' '],   [' ', '-', '-', ' ', '-'] ]
    return grid
    
# ************************************* DISPLAY HELPER FUNCTIONS ************************************* #

def displayGrid(grid):
    for row in range(6):
        print("\n","----" * 9, "\n|", end = " ")
        for col in range(5):
            print('{0: <5}|'.format(grid[row][col]), end= " ")

def organizeResult(domain, position):
    res = [['-' for col in range(5)] for row in range(6)]
    for var, domain in domain.items():
        row, col, direction = position[var]
        domain = list(domain[0])
        length, index = len(domain), 0
        while(index < length):
            res[row][col] = domain[index]
            index += 1
            if(direction == "D"):
                row += 1
            else:
                col += 1
    return res

def displayDomain(domain):
    for key, val in domain.items():
        print(key, " : ", val)
    print()

# ************************************* CONSTRAINT SATISFACTION ALGORITHM ************************************* #

def arc_reduce(li_1, li_2, ind1, ind2):
    change = False
    for ele_1 in li_1:
        flag = True
        for ele_2 in li_2:
            if(list(ele_1)[ind1-1] == list(ele_2)[ind2-1]):
                flag = False
                break
        if(flag == True):
            change = True
            li_1.remove(ele_1)
    return change
    
def apply_constraints(domain, constr):    
    no_change = True
    for xi in constr.keys():
        for xj, x, y in constr[xi]:
            if(arc_reduce(domain[xi], domain[xj], x, y)):
                if(len(domain[xi]) == 0):
                    return -1
                else:
                    no_change = False
    return no_change
                    
# ************************************* MAIN FUNCTION ************************************* #

if __name__ == "__main__":
    
    domain, position =  initDomains()
    constr = initConstraints()
    grid = initGrid()
    
    print("\n\nGiven question : \n")
    displayGrid(grid)
    
    print("\n\nDomain before optimizations : \n")
    displayDomain(domain)
    
    while(True):
        no_change = apply_constraints(domain, constr)
        if(no_change == -1):
            print("Not possible to solve")
        elif(no_change == True):
            break
        elif(no_change == False):
        	continue
    
    print("\n\nReduced domain after applying constraints : \n")
    displayDomain(domain)
    
    print("\n\n Final Answer : \n")
    result = organizeResult(domain, position)
    displayGrid(result)
    print("\n\n")
