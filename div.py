import math

def div(a,b):
    if a and b>a:
        arr.append(math.ceil(b/a))
        return div(math.ceil(b/a)*a-b,b*math.ceil(b/a))
    
    

arr = []
div(6,14)
for i in arr:
    print("1/" +str(i),end  = ' + ')

