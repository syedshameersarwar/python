'''
You are a given a unimodal array of n distinct elements, meaning that its
entries are in increasing orderup until its maximum element, after which
its elements are in decreasing order. Give an algorithm to compute the
maximum element that runs in O(log n) time.'''
def max_binary_search_unimodal(List):
    beg = 0
    end = len(List)-1
    mid  = (beg+end)//2
    while beg<= end:
        if List[mid-1]<List[mid]>List[mid+1]:
            return List[mid]
        if List[mid+1]<List[mid]<List[mid-1]:
            end = mid - 1
        else:
            beg =  mid + 1
        mid = (beg+end)//2
    return None
print(max_binary_search_unimodal([1, 3, 50, 10, 9, 7, 6] ))
                    
            
        
'''
Method 2 (Binary Search)
We can modify the standard Binary Search algorithm for the given
type of arrays.
i) If the mid element is greater than both of its adjacent elements,
then mid is the maximum.
ii) If mid element is greater than its next element and smaller than
the previous element then maximum lies on left side of mid.
Example array: {3, 50, 10, 9, 7, 6}
iii) If mid element is smaller than its next element and greater
than the previous element then maximum lies on right side of mid.
Example array: {2, 4, 6, 8, 10, 3, 1}
'''
