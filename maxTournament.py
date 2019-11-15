def maxRecur(List):
    if len(List)==1:
        return List[0]
    mid = len(List)//2
    firstHalf = maxRecur(List[:mid])
    secondHalf = maxRecur(List[mid:])
    if firstHalf > secondHalf:
        maxElement = firstHalf
    else:
        maxElement = secondHalf
    return maxElement

print(maxRecur([3,44,32,75,23,12,-5,53,200]))
