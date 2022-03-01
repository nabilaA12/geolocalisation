
from math import sqrt

#fonction permet de convertir les coordonées DMS en décimale
def dms_en_dd(d,m,s): 
    sec=m*60+s
    dd=sec/3600+d
    return dd

 # fonction permet de calculer la distance entre deux points a(a1,b1) et b(a2,b2)
def distance(a1,b1,a2,b2): 
    return sqrt((pow(a2-a1,2)+pow(b2-b1,2)))

Pole_lat=176
Pole_long=86

##### DMS PARIS ######

# en latitude
d=48
m=51
s=52
print ("la latitude de paris en décimale est: ",dms_en_dd(d,m,s))

#en longitude
d1=2
m1=20
s1=56
print ("la longitude de paris en décimale est: ",dms_en_dd(d1,m1,s1))


print ("la distance entre paris et le pole nord est :" ,distance(Pole_lat,dms_en_dd(d,m,s),Pole_long,dms_en_dd(d1,m1,s1)))
