from math import *
def polysum(n,s):
    '''n:number of sides of regular polygon
       s:length of each side

       returns the value(i.e sum_area_perimeter),equals the area and square of perimeter of polygon'''
    area = (0.25*n*(s**2))/(tan(pi/n)) #calculates the area of polygon
    perimeter = n*s #calculates the perimeter of polygon
    sum_area_perimeter = area + (perimeter**2)#add area and square of perimeter
    return round(sum_area_perimeter,4) #rounds the sum_area_parimeter to 4 decimal places(using round()) and returns
print(polysum(5,4))
