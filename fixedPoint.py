'''
You are given a sorted (from smallest to largest) array A of n distinct
integers which can be positive, negative, or zero. You want to decide
whether or not there is an index i such that A[i] = i. Design the fastest
algorithm that you can for solving this problem.
'''
def binary_search_recur_mode(List,beg,end):
    if end>=beg:
        mid = (beg+end)//2
    if List[mid]==mid:
        return List[mid]
    if mid>List[mid]:
        return binary_search_recur_mode(List,mid+1,end)
    else:
        return binary_search_recur_mode(List,beg,mid-1)
    return None
    
List = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
n = len(List)-1
print("Fixed point is : "+str(binary_search_recur_mode(List,0,n)))



'''
Method 2 (Binary Search)
First check whether middle element is Fixed Point or not. If it is, then return
it; otherwise check whether index of middle element is greater than value at the
index. If index is greater, then Fixed Point(s) lies on the right side of the
middle point (obviously only if there is a Fixed Point). Else the Fixed Point(s)
lies on left side.
'''
