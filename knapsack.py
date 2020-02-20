from dictSort import bookDict
from dictSort import libDict
from dictSort import dictSort
from inputprocessing import createLibrary
from maxscore import maxScores

def knapsack(days, signList, adict):
    if len(signList) == 0:
        return
    maxArgs = []
    scores = maxScores(days, adict)    
    for i in range(len(signList)):
        bdict = adict.copy()
        adict.pop(i)
        temp = signList.copy()
        signList.pop(i)
        arg = scores[i] + knapsack(days - signList[i], signList, adict)
        signList = temp
        adict = bdict
        maxArgs.append(arg)
    return max(*maxArgs)

lib = createLibrary("input/a_example.txt")
data = libDict(len(lib[1]), bookDict(lib[0],len(lib[0])), lib[1], lib[2], lib[3])

print(maxScores(data, lib[4]))
print(data)
print(knapsack(lib[4], lib[1], data))