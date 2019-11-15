from mergeSortPoints import mergeSort
import math


def closest(P):
    return closestPair(mergeSort(P,'x'),mergeSort(P,'y'))


def distance(p1,p2):
    return math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)


def closestPair(Px,Py):
    if len(Px)<= 3:
        return bruteForce(Px)
    mid = len(Px)//2
    midpoint = Px[mid][0]
    Qx = Px[:mid]
    Rx = Px[mid:]
    Qy = Qx
    Ry = Rx
    
    (p1,q1,dl) = closestPair(Qx,Qy)
    (p2,q2,dr) = closestPair(Rx,Ry)
    if dl<dr:
        d = dl
        (p,q) = (p1,q1)
    else:
        d = dr
        (p,q) = (p2,q2)
    (p3,q3,d3)= closestSplitPair(Px,Py,d,midpoint,(p,q))
    if d<=d3:
        return (p,q,d)
    else:
        return(p3,q3,d3)


def closestSplitPair(Px,Py,delta,midpoint_x,best_pair):
    Sy = [p for p in Py if (midpoint_x-delta)<=p[0]<=(midpoint_x+delta)]
    best = delta
    for i in range(len(Sy)-1):
        for j in range(i+1,min(i+7,len(Sy)-i)):
            (p,q) = (Sy[i],Sy[j])
            dist = distance(p,q)
            if dist <best:
                best_pair = (p,q)
                best = dist
    return (best_pair[0],best_pair[1],best)


def bruteForce(ListOfPoints):
    p = ListOfPoints[0]
    q = ListOfPoints[1]
    best = distance(p,q)
    for i in range(len(ListOfPoints)-1):
        for j in range(i+1,len(ListOfPoints)):
            dist = distance(ListOfPoints[i],ListOfPoints[j])
            if dist<best:
                best = dist
                (p,q) = (ListOfPoints[i],ListOfPoints[j])
    return (p,q,best)


if __name__=='__main__':
    Points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4),(2.5,3.5),(2.8,14),(2.2,3.3)]
    (p,q,d) = closest(Points)
    print("The closest Pair is ("+str(p)+","+str(q)+ \
          ") with distance : "+str(round(d,4))+" units.")
        
       
