def deterministic_selection(List,start,end,order_statistic):

    if start==end:
        return List[start]

    if order_statistic<=0 or order_statistic>(end-start+1):
        return
    
    medianOfmedians = median_of_medians(List[start:end+1])
    
    pivot_index = specPartition(List,start,end,medianOfmedians)

    
    if pivot_index-start+1 == order_statistic:
        return List[pivot_index]

    if pivot_index-start+1 > order_statistic:
        return deterministic_selection(List,start, \
                                    pivot_index-1,order_statistic)
    return deterministic_selection(List,pivot_index+1,end, \
                                   order_statistic-pivot_index+start-1)

    


def median_of_medians(List):

    sublists = [List[i:i+5] for i in range(0,len(List),5)]

    medians = []

    for List in sublists:
        medians.append(sorted(List)[len(List)//2])

    if len(List)<=5:
        return sorted(medians)[len(medians)//2]
    else:
        return median_of_medians(medians)
    


    
def specPartition(List,start,end,element):
    
    index = List.index(element)
    
    List[index],List[end]=List[end],List[index]

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



L= [12, 3, 5, 7, 4, 19, 26]
print(median_of_medians(L))
print(deterministic_selection(L,0,len(L)-1,0))
    
