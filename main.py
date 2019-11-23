import numpy as np

def clauses():
    fName = open("Lab-data/Inst/uf20-09.cnf", "r")
    inst = []
    for line in fName:
        if not line.startswith("c") \
            and not line.startswith("p") \
            and not line.startswith("0") \
            and line.strip() \
            and not line.startswith("%") :
                line = line.split()
                line = [int(literal) for literal in line]
                inst.append(line)  
    for clause in inst:
        clause.remove(0)    
    fName.close()    
    #print(inst)
    return inst

def variables():
    fName = open("Lab-data/sols/9.txt", "r")
    inst = []
    list_zeroes = []
    list_ones = []
    for line in fName:
        #print(line)
        if line.startswith("v"):
            s = line
            line = s[1:]
            line = line.split()
            line = [int(literal) for literal in line]
            print(line)
            if not line == [0]:
                inst.append(line)   
    fName.close()
    for i in inst[0]:
        if i < 0:
            list_zeroes.append(-i)
        else:
            list_ones.append(i)
    for j in inst[1]:
        if j < 0:
            list_zeroes.append(-j)
        else:
            list_ones.append(j)
    inst = []
    inst.append(list_ones)
    inst.append(list_zeroes)
    return inst


def checkSolution():
    clauses_list = []
    variables_list = []

    clauses_list = clauses()
    variables_list = variables()

    #print(clauses_list)
    print(variables_list)

    for clause in clauses_list:
        #sat = ""
        for c in clause:
            if c < 0:
                if -c in variables_list[1]:
                    sat = True
                    break
                elif -c in variables_list[0]:
                    sat = False
            else:
                if c in variables_list[0]:
                    sat = True
                    break
                elif c in variables_list[1]:
                    sat = False            
        if sat == False:
            print("encountered an unsatisfied clause: ", clause)
            break

    if sat == False:
        print("not satified")
    elif sat == True:
        print("satisfied")

checkSolution()