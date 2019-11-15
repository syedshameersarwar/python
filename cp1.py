N=int(input())
C = list(input().split())
count = 0;
C = [int(i) for i in C]
C = C[:N]
cl =[]
for color in C:
    if color not in cl:
        cl.append(color)
print(len(cl))

