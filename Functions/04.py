#Create a function that retuns both area and circumfernce wehn radius is provided
import math
def circle_stat (r):
    area = math.pi*(r**2)
    circumfernce=2*math.pi*r
    return area,circumfernce

a,c=circle_stat(32)
print("Area : ",round(a,2),"circumfernce: ",round(c,2) )
