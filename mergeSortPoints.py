def merge(left,right,compareWith):
    if compareWith == 'x' or compareWith == 'X' \
          or compareWith == 'Y' or compareWith == 'y':
        compared_ref = True
    else:
        compared_ref = False  
    result = []
    i=0
    j = 0
    while i<len(left) and j<len(right):
        if compared_ref == False:
            if left[i]<right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j+=1
        else:
            if compareWith == 'X' or compareWith == 'x':
                if left[i][0]<right[j][0]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j+=1
            else:
                if left[i][1]<right[j][1]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j+=1
            
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result
def mergeSort(List,compareWith = None):
    if len(List)<2:
        return List[:]
    else:
        mid = len(List)//2
        left = mergeSort(List[:mid],compareWith)
        right = mergeSort(List[mid:],compareWith)
        return merge(left,right,compareWith)
if __name__=='__main__':
    List = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print("Final sort = " +str(mergeSort(List,'x')))
