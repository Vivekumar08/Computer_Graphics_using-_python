import matplotlib.pyplot as plt  
import numpy as np
from matplotlib.animation import FuncAnimation

firstcircle = 30
secondcircle = 8
isInside = input("Press i for inside (else outside): ")
inside = True if isInside == 'i' or isInside == 'I' else False
largest = int(firstcircle*2+secondcircle*2)
difference = int(0-(largest))
difference2 = int(0+(largest))


def createList(r1, r2):
    return [item for item in range(r1, r2+1)]


x = (createList(difference,difference2))
y = (createList(difference,difference2))

print(x)
print(difference)
print(difference2)


def circle():
  theta = np.linspace(0, 2*np.pi, 100)

  r = np.sqrt(firstcircle**2)

  x1 = (r+2*secondcircle)*np.cos(theta) if inside else r*np.cos(theta)
  x2 = (r+2*secondcircle)*np.sin(theta) if inside else r*np.sin(theta)

  theta2 = np.linspace(0, 2*np.pi, 100)
  r1 = np.sqrt(secondcircle**2)
  x3 = r1*np.cos(theta2)+firstcircle+secondcircle
  x4 = r1*np.sin(theta2)

  fig = plt.figure()

  ax = fig.add_subplot(1, 1, 1)
  ax.plot(x1,x2)
  circlemove ,= ax.plot(x3,x4)  

  ax.set_aspect(1)
  plt.tight_layout()
    

  def update(angle):
    r_a = r1 + firstcircle
    x_a = x3 + r_a * np.cos(angle) - firstcircle - secondcircle
    y_a = x4 + r_a * np.sin(angle)
    circlemove.set_data(x_a, y_a)
    return circlemove

  anim = FuncAnimation(fig, update, frames=theta2, repeat=True)
  plt.show()

circle()