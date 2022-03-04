
from math import sqrt

# Fonction permettant la conversion des coordonées DMS en décimale
def dms_en_dd(d,m,s): 
    sec=m*60+s
    dd=sec/3600+d
    return dd


 # Fonction permettant le calcul de la distance entre deux points a(a1,b1) et b(a2,b2)
def distance(b1,b2,a1,a2): 
    return sqrt((pow(b2-b1,2)+pow(a2-a1,2)))


# DMS PARIS en latitude
d=48
m=51
s=12
paris_lat=dms_en_dd(d,m,s)
print ("La latitude de paris en décimale est :",paris_lat)

# DMS PARIS en longitude
d1=2
m1=20
s1=55
paris_long=dms_en_dd(d1,m1,s1)
print ("La longitude de paris en décimale est :",paris_long)

## Longitude et latitude du pole nord en décimale
Pole_lat = 172
Pole_long = 86


print ("La distance entre le pole nord et paris est de :" ,distance(Pole_long,paris_long,Pole_lat,paris_lat))
