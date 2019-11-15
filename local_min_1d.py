def local_min(List,beg,end,n):
    mid = (beg + end)//2
    if (mid ==0 or List[mid-1]>List[mid]) and ( mid == n-1 or List[mid+1]>List[mid]):
        return mid
    elif (mid > 0 and List[mid-1]<List[mid]):
        return local_min(List,beg,mid-1,n)
    return local_min(List,mid+1,end,n)

L = [4, 3, 1, 14, 16, 40]
print("Index of local minima : "+str(local_min(L,0,len(L)-1,len(L))))

'''
https://www.geeksforgeeks.org/find-local-minima-array/
'''
