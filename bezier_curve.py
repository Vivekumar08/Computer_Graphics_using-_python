import numpy as np
import matplotlib.pyplot as plt

P0, P1, P2,P3 = np.array([
	[0, 0],
	[5, 3],
	[2, 4],
	[3, 3],
])
verts = np.array([
	P0,P1,P2
])
verts_3 = np.array([
	P0,P1,P2,P3
])

# define bezier curve
P = lambda t: (1 - t)**2 * P0 + 2 * t * (1 - t) * P1 + t**2 * P2
P_3 = lambda t: (1 - t)**3 * P0 + 3 * t *P1*(1 - t)**2 + 3 *P2*(1 - t)*t**3 +t**3 * P3

# evaluate the curve on [0, 1] sliced in 50 points
points = np.array([P(t) for t in np.linspace(0, 1, 50)])
points_3 = np.array([P_3(t) for t in np.linspace(0, 1, 50)])

# get x and y coordinates of points separately
x, y = points[:,0], points[:,1]
x3, y3 = points_3[:,0], points_3[:,1]

plt.figure(200)

xs, ys = zip(*verts)
plt.plot(xs, ys, 'x--', lw=2, color='black', ms=10)
plt.plot(x, y, 'b-', lw=2, color='black', ms=10)

plt.plot(*P0, 'r.')
plt.plot(*P1, 'r.')
plt.plot(*P2, 'r.')
plt.show()

plt.figure(200)
xs3, ys3 = zip(*verts_3)
plt.plot(xs3, ys3, 'x--', lw=2, color='black', ms=10)
plt.plot(x3, y3, 'b-', lw=2, color='black', ms=10)
# plot

plt.plot(*P0, 'r.')
plt.plot(*P1, 'r.')
plt.plot(*P2, 'r.')
plt.plot(*P3, 'r.')
plt.show()