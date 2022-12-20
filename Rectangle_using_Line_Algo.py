# First Import necessary dependencies
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys


def init():  # Initialisation Function
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(0, 200, 0, 200)


def RectLineBresenham(x0, y0, l, b):
    x1 = x0
    y1= y0
    
    x2 = x1 + l
    y2 = y1

    x3 = x2+b
    y3 = y2+b

    x4 = x1
    y4 = y1+b


    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    dT = 2 * abs(dy - dx)
    dS = 2 * dy
    d = 2 * abs(dy)-abs(dx)
    print("Decision Parameter for line 1: ", d)

    dx2 = abs(x3 - x4)
    dy2 = abs(y3 - y4)
    dT2 = 2 * abs(dy2 - dx2)
    dS2 = 2 * dy2
    d2 = 2 * abs(dy2)-abs(dx2)
    print("Decision Parameter for line 2: ", d2)

    y = y1
    x_l2 = x1

    print("delta x: ", dx)
    print("delta y: ", dy)

    print("delta x3: ", dx2)
    print("delta y3: ", dy2)

    # Finally we start ploting line :)

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)

    for x in range(x1, x2 + 1):
        glVertex2f(x, y)
        glVertex2f(x, y+b)
        if d >= 0:
            y = y + 1
            d = d - dT
        else:
            d = d + dS


    for y_ in range(y1, y4 + 1):
        glVertex2f(x_l2, y_)
        glVertex2f(x_l2+l, y_)
        if d2 >= 0:
            x_l2 = x_l2 + 1
            d2 = d2 - dT2
        else:
            d2 = d2 + dS2

   
    
    # print(x2,y2)
    glEnd()
    glFlush()


def main():
    # Ask for choice
            x1 = int(input("Enter x1: "))
            y1 = int(input("Enter y1: "))
            l = int(input("Enter length of a rectangle: "))
            b = int(input("Enter breadth of a rectangle: "))
            print("starting window....")
            glutInit(sys.argv)
            glutInitDisplayMode(GLUT_RGB)
            glutInitWindowSize(500, 500)
            glutInitWindowPosition(0, 0)
            glutCreateWindow("Plot Rectangle using Line drwaing Bresenham Algorithm")
            glutDisplayFunc(lambda: RectLineBresenham(x1, y1, l ,b))
            # glutIdleFunc(lambda: RectLineBresenham(x1, y1, x2, y2))
            init()
            glutMainLoop()


main()
