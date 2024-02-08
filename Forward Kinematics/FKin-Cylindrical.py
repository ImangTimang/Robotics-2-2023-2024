import numpy as np
import math

# link lengths in mm
a1 = float(input("a1= "))
a2 = float(input("a2= "))
a3 = float(input("a3= "))

# joint variables: is mm if d, is degrees if theta
T1 = float(input("T1 = "))
d2 = float(input("d2 = "))
d3 = float(input("d3 = "))

# degree to radian
T1 = (T1/180.0)*np.pi

# Parametric Table (theta, alpha, r, d)

PT = [[T1, (0.0/180.0)*np.pi, 0, a1],
      [(270.0/180.0)*np.pi, (270.0/180.0)*np.pi, 0, a2+d2],
      [(0.0/180.0)*np.pi, (0.0/180.0)*np.pi, 0, a3+d3]]

# HTM Formulae
i = 0
H0_1 = [[np.cos(PT[i][0]), -np.sin(PT[i][0])*np.cos(PT[i][1]), np.sin(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.cos(PT)[i][0]],
        [np.sin(PT[i][0]), np.cos(PT[i][0])*np.cos(PT[i][1]), -np.cos(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.sin(PT)[i][0]],
        [0, np.sin(PT[i][1]), np.cos(PT[i][1]), PT[i][3]],
        [0,0,0,1]]

i = 1
H1_2 = [[np.cos(PT[i][0]), -np.sin(PT[i][0])*np.cos(PT[i][1]), np.sin(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.cos(PT)[i][0]],
        [np.sin(PT[i][0]), np.cos(PT[i][0])*np.cos(PT[i][1]), -np.cos(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.sin(PT)[i][0]],
        [0, np.sin(PT[i][1]), np.cos(PT[i][1]), PT[i][3]],
        [0,0,0,1]]

i = 2
H2_3 = [[np.cos(PT[i][0]), -np.sin(PT[i][0])*np.cos(PT[i][1]), np.sin(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.cos(PT)[i][0]],
        [np.sin(PT[i][0]), np.cos(PT[i][0])*np.cos(PT[i][1]), -np.cos(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.sin(PT)[i][0]],
        [0, np.sin(PT[i][1]), np.cos(PT[i][1]), PT[i][3]],
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


