from random import randint

def randomized_selection(List,start,end,order_statistic):

    if start==end:
        return List[start]

    if order_statistic <= 0 or order_statistic > end-start+1:
        return None

    
    pivot_index = randomizedPartition(List,start,end)
    '''
    print("start = ",start," end = ",end, \
          "pivot index = ",pivot_index, \
          "order = ",order_statistic)
    print(List[start:end+1])
    '''

    if pivot_index +1-start == order_statistic:
        return List[pivot_index]

    if pivot_index +1-start> order_statistic:
        return randomized_selection(List,start,pivot_index-1,\
                                    order_statistic)

    return randomized_selection(List,pivot_index+1,end, \
                                    order_statistic-pivot_index+start-1)
   
    

def randomizedPartition(List,start,end):

    pivot_index = randint(start,end)

    List[pivot_index],List[end]= List[end],List[pivot_index]

    return Partition(List,start,end)


def Partition(List,start,end):

    pivot = List[end]
    pivot_index  = start

    for i in range(start,end):

        if List[i]<=pivot:
            List[i],List[pivot_index]= List[pivot_index],List[i]
            pivot_index += 1

    List[end],List[pivot_index]=List[pivot_index],List[end]

    return pivot_index



def randomized_selection_max(List,start,end,order_statistic):
    
    order_statistic = (end-start+1)-order_statistic+1

    return randomized_selection(List,start,end,order_statistic)



L =[2,3,4,5,6,7,8,9,10,12]
print(randomized_selection_max(L,0,len(L)-1,9))
