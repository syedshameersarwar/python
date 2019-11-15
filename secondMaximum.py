'''You are given as input an unsorted array of n distinct numbers,
where n is a power of 2.Give an algorithm that identifies the
second-largest number in the array,and that uses at most
n+log2n−2 comparisons.'''

def findMaxTournament(List):
    if len(List)==1:
        return List[:]
    mid = len(List)//2
    firstHalf = findMaxTournament(List[:mid])
    secondHalf = findMaxTournament(List[mid:])
    if firstHalf[0]>secondHalf[0]:
        firstHalf.append(secondHalf[0])
        return firstHalf
    else:
        secondHalf.append(firstHalf[0])
        return secondHalf


def findSecondMax(List):
    result_set = findMaxTournament(List)
    comparedElements = result_set[1:]
    second_max = comparedElements[0]
    for i in range(1,len(comparedElements)):
        if comparedElements[i]>second_max:
            second_max = comparedElemets[i]
    return second_max


print(findSecondMax([3,1,10,17,12,4]))
    
'''
Function FindMaxTournament(I,J, A[I..J],N) returns Compared[0..K]
begin
    if I = J then //base case
        Compared[0..N];
        Compared[0]← 1;
        Compared[1]← A[I];
        return Compared;
    endif
    Compared1← FindMaxTournament(I, I+(J-I)/2, A,N);
    Compared2← FindMaxTournament(1+I+(J-I)/2,J, A,N);
    if Compared1[1]>Compared2[1] then
        K←Compared1[0]+1;
        Compared1[0]←K;
        Compared1[K]←Compared2[1];
        return Compared1;
    else
        K←Compared2[0]+1;
        Compared2[0]←K;
        Compared2[K]←Compared1[1];
        return Compared2;
    endif
end


Efficient Algorithm for Finding the second largest element
Using the two observations from above, an efficient algorithm for finding the
second largest number will work as follows:
1. Find the largest element of the array using the tournament method.
2. Collect all elements of the array that were compared to the largest
element.
3. Find the largest element among the elements collected in step 2 (can
use any method here).
Step 2 Issues. How can we efficiently collect all elements of the input
array that were compared to the largest element of the array?
Essentially, we would like to associate with the largest element of A an
array Compared[] of elements A was compared to. This, however, needs to
be done carefully. We do not know upfront which array element is going to
be the largest, so we will carry information about all comparisons an array
element won until this element loses a comparison.
From the technical side, we will change the FindMaxRecursive() algorithm
to return an array of integers Compared[0..K]. We will establish the following
convention:
• Compared[0] = K (i.e., the 0th element of the array holds the length
of the array);
• Compared[1] = max (i.e., the first element of the array is the number
that FindMaxRecursive() would return;
• Compared[2], . . . ,Compared[K] are all numbers with which max has
been compared thus far.
Using these conventions, the Algorithm FindSecondMax() can be written
as shown in Figure 2.
'''
