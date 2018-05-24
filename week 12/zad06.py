from math import log
from math import pi

p = 1.038
c = 3.7
k = 5.4 * pow(10,-3)
small_egg = 47
large_egg = 67
Tw = 100
Ty = 70
To = 4
T_room = 20

#1
t_4 = (pow(large_egg,2/3)*c*pow(p,1/3))/(k*pow(pi,2)*pow(4*pi/3,2/3))*log(0.76*(To-Tw)/(Ty-Tw))
t_4_f = "%.2f"% t_4
t_4_f_seconds = t_4/60
#2
t_20 = (pow(large_egg,2/3)*c*pow(p,1/3))/(k*pow(pi,2)*pow(4*pi/3,2/3))*log(0.76*(T_room-Tw)/(Ty-Tw))
t_20_f = "%.2f"% t_20
t_20_f_seconds = t_20/60

print("jajko z lodowki potrzebuje ")
print(t_4_f," sekund")
print( "%.2f"%t_4_f_seconds, " minut")
print("jajko z pokoju potrzebuje ")
print(t_20_f," sekund")
print("%.2f"%t_20_f_seconds, " minut")