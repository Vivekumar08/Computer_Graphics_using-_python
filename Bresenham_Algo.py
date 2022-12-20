# First Import necessary dependencies
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys


def init():  # Initialisation Function
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(0, 70, 0, 70)


def LineBresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    dT = 2 * abs(dy - dx)
    dS = 2 * dy
    d = 2 * abs(dy)-abs(dx)
    print("Decision Parameter: ", d)

    y = y1

    print("delta x: ", dx)
    print("delta y: ", dy)

    # Finally we start ploting line :)

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)

    for x in range(x1+1, x2 + 1):
        glVertex2f(x, y)
        if d >= 0:
            y = y + 1
            d = d - dT
            print(x, y)
            print(d)
        else:
            d = d + dS
            print(x, y)
            print(d)
    # print(x2,y2)
    glEnd()
    glFlush()



def main():
        x1 = int(input("Enter x1: "))
        y1 = int(input("Enter y1: "))
        x2 = int(input("Enter x2: "))
        y2 = int(input("Enter y2: "))
        print("starting window....")
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500, 500)
        glutInitWindowPosition(0, 0)
        glutCreateWindow("Plot Line using Bresenham Algorithm")
        glutDisplayFunc(lambda: LineBresenham(x1, y1, x2, y2))
        init()
        glutMainLoop()


main()
