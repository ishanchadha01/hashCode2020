from dictSort import bookDict
from dictSort import libDict
from dictSort import dictSort
from inputprocessing import createLibrary

def maxScores(dict, days):
    scoreList = []
    for i in range(len(data)):
        sum = 0
        scores = (days - data[i][1]) * (data[i][2])
        count = 0
        for v in data[i][0].values():
            sum += v
            count+=1
            if count == scores:
                break
        scoreList.append(sum)
    return scoreList   


lib = createLibrary("input/a_example.txt")
data = libDict(len(lib[1]), bookDict(lib[0],len(lib[0])), lib[1], lib[2], lib[3])

print(maxScores(data, lib[4]))
print(data)