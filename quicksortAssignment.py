def readfile():
    file = open("QuickSort.txt")
    numbers = []
    for line in file:
        numbers.append(int(line.strip()))
    return numbers


def quickSort(List,start,end,partition = None ):
    if start < end:
        comparisions = end - start
        pivot_index = partition(List,start,end)
        comparisions += quickSort(List,start,pivot_index-1,partition)
        comparisions += quickSort(List,pivot_index+1,end,partition)
    else:
        return 0
    return comparisions


def base_partition(List,start,end):
    pivot_element = List[start]
    pivot_index = start+1
    for j in range(pivot_index,end+1):
        if List[j]<=pivot_element:
            List[j],List[pivot_index] = List[pivot_index],List[j]
            pivot_index += 1
        
    List[pivot_index-1],List[start] = pivot_element,List[pivot_index-1]
    return pivot_index-1


def firstPivot(List,start,end):
    return base_partition(List,start,end)

def lastPivot(List,start,end):
    List[start],List[end] = List[end],List[start]
    return base_partition(List,start,end)

def medianPivot(List,start,end):
    middle = (start + end)//2
    first = start
    last = end
    if List[start] < List[middle] <List[last] or List[last] < List[middle] < List[start]:
        pivot_index = middle
    elif List[middle] < List[start] < List[last] or List[last] < List[start] < List[middle]:
        pivot_index = first
    else:
        pivot_index =  last
    List[start],List[pivot_index] = List[pivot_index],List[start]
    return base_partition(List,start,end)

if __name__ == '__main__':
    List  = readfile()
    print(quickSort(List,0,len(List)-1,medianPivot))
