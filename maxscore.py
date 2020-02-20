from dictSort import bookDict
from dictSort import libDict
from dictSort import dictSort
from inputprocessing import createLibrary

def maxScores(adict, days):
    scoreList = []
    for i in range(len(adict)):
        sum = 0
        scores = (days - adict[i][1]) * (adict[i][2])
        count = 0
        for v in adict[i][0].values():
            sum += v
            count+=1
            if count == scores:
                break
        scoreList.append(sum)
    return scoreList