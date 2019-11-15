from random import seed
from random import randint
import time

def randomizedQuickSort(List,start,end):
    
    if start<end:
        pivot_index = RandomizedPartition(List,start,end)

        randomizedQuickSort(List,start,pivot_index-1)

        randomizedQuickSort(List,pivot_index+1,end)
    

def Partition(List,start,end):
    
    pivot = List[end]
    
    pivot_index = start
    
    for i in range(start,end):
        if List[i]<=pivot:
            List[i],List[pivot_index]=List[pivot_index],List[i]
            pivot_index += 1

    List[end],List[pivot_index] = List[pivot_index],pivot
    return pivot_index


def RandomizedPartition(List,start,end):
    
    
    random_index = randint(start,end)
    
    List[end],List[random_index]=List[random_index],List[end]
    
    return Partition(List,start,end)





if __name__=='__main__':
    seed(1)
    L = []
    for i in range(1000):
        L.append(randint(-75,325))

    start_time = time.time()
    randomizedQuickSort(L,0,len(L)-1)
    end_time = time.time()
    print("Time taken = ",end_time-start_time)
    print(L)
    
