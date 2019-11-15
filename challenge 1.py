T = int(input())
for i in range(T):
    N = int(input())
    strC = input().split(' ')
    C = list(map(int,strC))
    strPetrol = input().split(' ')
    L = list(map(int,strPetrol))
    r = [C[i]*L[i] for i in range(N)]
    print(sum(r))
