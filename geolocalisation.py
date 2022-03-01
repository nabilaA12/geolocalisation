
from math import sqrt


def dms_en_dd(d,m,s):
    sec=m*60+s
    dd=sec/3600+d
    return dd

def distance(a1,b1,a2,b2):  # calculer la distance entre deux points a(a1,b1) et b(a2,b2)
    return sqrt((pow(a2-a1,2)+pow(b2-b1,2)))

Pole_lat=176
Pole_long=86
##### DMS PARIS ######
# en latitude
d=48
m=51
s=52
la=dms_en_dd(d,m,s)
print ("la latitude de paris en dd ",dms_en_dd(d,m,s))

#en longitude
d1=2
m1=20
s1=56
lo=dms_en_dd(d1,m1,s1)
print ("la longitude de paris en dd ",dms_en_dd(d1,m1,s1))

print ("la distance est " ,distance(Pole_lat,la,Pole_long,lo))
