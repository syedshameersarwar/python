from random import randint
from random import seed
import time

def merge(left,right):
    result = []
    i=0
    j = 0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
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

def mergeSort(List):
    if len(List)<2:
        return List[:]
    else:
        mid = len(List)//2
        left = mergeSort(List[:mid])
        right = mergeSort(List[mid:])
        return merge(left,right)

seed(1)
L = []
for i in range(1000):
    L.append(randint(-75,325))

start_time = time.time()
l = mergeSort(L)
end_time = time.time()
print("Time taken = ",end_time - start_time)
print("Final sort = " +str(l))

