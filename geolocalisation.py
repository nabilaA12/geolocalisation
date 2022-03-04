
from math import sqrt

# Fonction permettant la conversion des coordonées DMS en décimale
def dms_en_dd(d,m,s): 
    sec=m*60+s
    dd=sec/3600+d
    return dd


 # Fonction permettant le calcul de la distance entre deux points a(a1,b1) et b(a2,b2)
def distance(b1,b2,a1,a2): 
    return sqrt((pow(b2-b1,2)+pow(a2-a1,2)))


# DMS PARIS #

# En latitude
d=48
m=51
s=12
print ("La latitude de paris en décimale est :",dms_en_dd(d,m,s))

# En longitude
d1=2
m1=20
s1=55
print ("La longitude de paris en décimale est :",dms_en_dd(d1,m1,s1))

## Longitude et latitude du pole nord 
Pole_lat = 172
Pole_long = 86

print ("La distance entre le pole nord et paris est de :" ,distance(Pole_long,dms_en_dd(d1,m1,s1),Pole_lat,dms_en_dd(d,m,s)))
