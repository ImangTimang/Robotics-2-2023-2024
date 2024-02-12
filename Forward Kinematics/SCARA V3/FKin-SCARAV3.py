#import necessary libraries

import numpy as np

#link lengths in mm

a1 = float(input("a1= "))
a2 = float(input("a2= "))
a3 = float(input("a3= "))
a4 = float(input("a4= "))

#joint variables: mm if d; degrees if theta

d1 = float(input("d1= "))
t2 = float(input("t2= "))
t3 = float(input("t3= "))

#conversion of degrees to radian
t2 = (t2/180)*np.pi
t3 = (t3/180)*np.pi

#Parametric Table (theta, alpha, r, d) respectively
PT = [[(0.0/180)*np.pi,(0.0/180)*np.pi,0,a1+d1],
      [t2,(0.0/180)*np.pi,a2,0],
      [t3,(0.0/180)*np.pi,a4,a3]]


# HTM Formulae
i = 0
H0_1 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])], [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]

i = 1

H1_2 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])], [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]

i = 2

H2_3 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])], [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]

H0_1 = np.matrix(H0_1)
print("H0_1= ")
print(H0_1)

H1_2 = np.matrix(H1_2)
print("H1_2= ")
print(H1_2)

H2_3 = np.matrix(H2_3)
print("H2_3= ")
print(H2_3)

H0_2 = np.dot(H0_1, H1_2)
H0_3 = np.dot(H0_2, H2_3)
print("H0_3= ")
print(np.matrix(np.around(H0_3,3)))
