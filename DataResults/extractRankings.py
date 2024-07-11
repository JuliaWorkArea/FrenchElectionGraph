import numpy as np # For the creation of the order
import copy
import sys
import os

def readfile():
    # Check for an argument
    if len(sys.argv) > 1:
        first_arg = sys.argv[1]
        fileName = 'pres'+first_arg+'comm.csv'
        if not os.path.exists(fileName):
            print("The date indicated does not exist in the DataResults folder.")
            exit(2)
        file1 = open(fileName,'r')
        datas = file1.readlines()
        file1.close()
    else:
        print("The date of the presidential elections is missing from the argument.")
        exit(1)
    columnsNames = datas[0].split(",")
    return (first_arg,datas,columnsNames)

def takeCandidates(columnsNames):
    candidates = []
    posOfCandidates = []
    for i in range(7,len(columnsNames)):
        if(columnsNames[i].startswith("voix")): # Only takes votes
            nom = columnsNames[i].split("voix")[1]
            if("T2" not in nom): # Choice of first round only
                candidates.append(nom)
                posOfCandidates.append(i)
        else:
            break
    return (posOfCandidates,candidates)

def sumForEachDep(datas,posOfCandidates):
    namesOfDep = []
    votes = []
    # department extraction
    for j in range(1,len(datas)):
        name = datas[j].split(",")[1]
        if len(namesOfDep)==0 or namesOfDep[len(namesOfDep)-1] != name:
            namesOfDep.append(name)
            tab = []
            for i in posOfCandidates:
                tab.append(0)
            votes.append(tab)
    # Merge results by department
    for j in range(1,len(datas)):
        line = datas[j].split(",")
        name = line[1]
        count = 0
        for i in range(0,len(namesOfDep)):
            if(namesOfDep[i]==name):
                count = i
        v=0
        for i in posOfCandidates:
            votes[count][v]+=int(line[i])
            v+=1
    return namesOfDep, votes

def generateOrderByDep(votes):
    orderList = copy.deepcopy(votes)
    # Find order
    for i in range(0,len(votes)):
        tab = []
        x = np.array(votes[i])
        t = np.argsort(x)
        arg = np.flip(t)
        for j in range(0,len(votes[0])):
            tab.append(int(np.where(arg == j)[0][0])+1)
        orderList[i] = tab
    return orderList

def writeResults(date,candidates,namesOfDep,values):
    f = open("resultRankings"+date+".txt", "w")
    f.write("dep;"+';'.join(candidates)+"\n")
    for i in range (0,len(namesOfDep)):
        f.write(str(namesOfDep[i])+",")
        for j in range(0, len(values[i])):
            f.write(str(values[i][j]))
            if j<len(values[i])-1:
                f.write(",")
        f.write("\n")
    f.close()

def main():
    date, datas, columnsNames = readfile()
    posOfCandidates, candidates = takeCandidates(columnsNames)
    namesOfDep, votes = sumForEachDep(datas,posOfCandidates)
    values = generateOrderByDep(votes) # You can also just use the number of votes
    writeResults(date,candidates,namesOfDep,values)

main()