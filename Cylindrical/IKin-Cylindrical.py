### Inverse Kinematics of Cylindrical

import numpy as np

# link lengths in mm
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))

# Position Vector in mm
x0_3 = float(input("x0_3 = "))
y0_3 = float(input("y0_3 = "))
z0_3 = float(input("z0_3 = "))
    
# Inverse Kinematic Solutions using Graphical Method

# Solution 1
theta1 = np.arctan(y0_3/x0_3)

# Solution 2
r = np.sqrt((x0_3**2)+(y0_3**2))

# Solution 3
d3 = r-a3

# Solution 4
d2 = z0_3-a1-a2

print("theta1 = ", np.around(theta1,3))
print("d2 = ", np.around(d2,3))
print("d3 = ", np.around(d3,3))
