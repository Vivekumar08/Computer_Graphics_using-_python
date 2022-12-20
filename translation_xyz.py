from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos
from itertools import product, combinations


fig = plt.figure(figsize=(9,9))
fig.tight_layout(pad=5.0)

r = [-3, 3]

ax = fig.add_subplot(221, projection='3d')
plt.title("Original cube")
ax.set_autoscale_on(True)
for s, e in combinations(np.array(list(product(r,r,r))), 2):
    if np.sum(np.abs(s-e)) == r[1]-r[0]:
        ax.plot3D(*zip(s,e), color="b")

ax = fig.add_subplot(222, projection='3d')
ax.set_autoscale_on(True)
plt.title("Translated cube about 2,4,6 unit\nin x,y,z direction respectively")
t = [2,4,6]
for s, e in combinations(np.array(list(product(r,r,r))), 2):
    if np.sum(np.abs(s-e)) == r[1]-r[0]:
        s_translated = [s[0]+t[0], 
                     s[1] +t[1],
                     s[2]+t[2]]
        e_translated = [e[0] +t[0], 
                     e[1] +t[1],
                     e[2]+t[2]] 
         
        ax.plot3D(*zip(s_translated,e_translated), color="k")

ax = fig.add_subplot(223, projection='3d')
ax.set_autoscale_on(True)
theta_z = np.radians(450)
theta_y = np.radians(600)
plt.title("Rotated cube by angle 450 about z axis,\nrotation by 600 about y-axis in succession")
for s, e in combinations(np.array(list(product(r,r,r))), 2):
    if np.sum(np.abs(s-e)) == r[1]-r[0]:
        s_rotated_z = [s[0] * cos(theta_z) - s[1] * sin(theta_z), 
                     s[0] * sin(theta_z) + s[1] * cos(theta_z),
                     s[2]]
        e_rotated_z = [e[0] * cos(theta_z) - e[1] * sin(theta_z), 
                     e[0] * sin(theta_z) + e[1] * cos(theta_z),
                     e[2]] 
        s_rotated = [s_rotated_z[0] * cos(theta_y) + s_rotated_z[2] * sin(theta_y), 
                     s_rotated_z[1],
                     s_rotated_z[0] * sin(theta_y) - s_rotated_z[2] * cos(theta_y)
                     ]
        e_rotated = [e_rotated_z[0] * cos(theta_y) + e_rotated_z[2] * sin(theta_y), 
                     e_rotated_z[1],
                     e_rotated_z[0] * sin(theta_y) - e_rotated_z[2] * cos(theta_y)
                     ] 
        ax.plot3D(*zip(s_rotated,e_rotated), color="g")

ax = fig.add_subplot(224, projection='3d')
ax.set_autoscale_on(True)
plt.title("Scaled cube in x-direction by a factor of 2,\nscaling in y- direction by a factor of 3")
Sc = [2,3]
for s, e in combinations(np.array(list(product(r,r,r))), 2):
    if np.sum(np.abs(s-e)) == r[1]-r[0]:
        s_translated = [s[0]*Sc[0], 
                     s[1] *Sc[1],
                     s[2]]
        e_translated = [e[0] *Sc[0], 
                     e[1]*Sc[1],
                     e[2]] 
         
        ax.plot3D(*zip(s_translated,e_translated), color="r")

plt.show()