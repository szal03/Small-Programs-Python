from math import pi

a = 0.11
C_D = 0.2
r = 1.2
m = 0.43
g = 9.81
A1 = pi*pow(a,2)
v1 = 120*10/36
v2 = 10*10/36

Fg = m*g
Fd1 = 1/2*C_D*r*A1*pow(v1,2)
Fd2 = 1/2*C_D*r*A1*pow(v2,2)

print("Fg", Fg)
print ("hard kick: ",Fd1)
print ("soft kick: ",Fd2)