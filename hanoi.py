def printMove(fr,to):
    print("Moving Disk from Tower : "+str(fr)+" to "+"Tower : "+str(to))

def TowerOfHanoi(n,fr,to,sp):
    global count;
    if n==1:
        count +=1
        printMove(fr,to)
    else:
        TowerOfHanoi(n-1,fr,sp,to)
        TowerOfHanoi(1,fr,to,sp)
        TowerOfHanoi(n-1,sp,to,fr)

count = 0
TowerOfHanoi(16,"A","B","C")
print("Moves : "+str(count))
