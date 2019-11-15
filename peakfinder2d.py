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

def peakFinder2d(List,rows,columns,midColumn):
    maxOfColumn = maxRecur([(List[i][midColumn],i) for i in\
                                   range(rows)])

    maxElement,maxElementRow = maxOfColumn[0],maxOfColumn[1]
    if midColumn==0 or midColumn==columns - 1:
        return maxElement
    if List[maxElementRow][midColumn-1]<=maxElement \
                           >=List[maxElementRow][midColumn+1]:
        return maxElement
    if maxElement < List[maxElementRow][midColumn-1]:
        return peakFinder2d(List,rows,columns,midColumn-midColumn//2)
    return peakFinder2d(List,rows,columns,midColumn+midColumn//2)

def peakFinder2dWrap(List):
    cols = maxRecur([len(x) for x in List])
    rows = len(List)
    midColumn = cols//2
    return peakFinder2d(List,rows,cols,midColumn)

if __name__=='__main__':
     matrix = [[10,8,10,10], \
               [14,13,12,11], \
               [15,23,55,33],  \
               [16,17,19,20]]
     print(peakFinder2dWrap(matrix))
