def dictSort(x):
    y = {k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse = True)}
    return y
def bookDict(lista, numbooks):
    newDict = {}
    for i in range(numbooks):
        newDict[i] = lista[i]
    return newDict
def libDict(numLib, bookDict, listSign, idList, rateList):
    newDict = {}
    for i in range(numLib):
        otherDict = {}
        x = idList[i]
        for j in x:
            otherDict[j] = bookDict[j]
        otherDict = dictSort(otherDict)
        newDict[i] = [otherDict, listSign[i], rateList[i]]
    return newDict