def longest_run(L):
    increasing = 0
    decreasing = 0
    maxCount = 0
    result = 0
    
    for index in range(len(L)-1):
        if L[index+1]>=L[index]:
            increasing += 1
            if increasing > maxCount:
                maxCount = increasing
                result = index + 1
        else:
            increasing = 0

        if L[index+1]<=L[index]:
            decreasing += 1
            if decreasing > maxCount:
                maxCount = decreasing
                result = index + 1
        else:
            decreasing = 0
    
    start = result - maxCount
    return sum(L[start:result+1])
              
                     
        
    
    
print(longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))
