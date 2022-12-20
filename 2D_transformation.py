# First Import necessary dependencies
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

flag = False


def init():  # Initialisation Function
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(-300, 500, -300, 500)


def Line_Trans(x1, y1, x2, y2, tx, ty):
    x11 = x1 + tx
    y11 = y1 + ty

    x22 = x2 + tx
    y22 = y2 + ty

    glColor3f(0.0, 1.0, 1.0)
    glLineWidth(5.0)
    glBegin(GL_LINES)

    print("Translated Line is in Cyan")

    glVertex2f(x11, y11)
    print(x1, y1)
    print(x11, y11)

    glVertex2f(x22, y22)
    print(x2, y2)
    print(x22, y22)

    glEnd()
    glFlush()


def Line_Rot(T, x1, y1, x2, y2):
    x11 = round(x1*math.cos(T) - y1*math.sin(T))
    y11 = round(x1*math.sin(T) + y1*math.cos(T))

    x22 = round(x2*math.cos(T) - y2*math.sin(T))
    y22 = round(x2*math.sin(T) + y2*math.cos(T))

    glColor3f(0.0, 1.0, 1.0)
    glLineWidth(5.0)
    glBegin(GL_LINES)

    print("Rotated Line is in Cyan")

    glVertex2f(x11, y11)
    print(x1, y1)
    print(x11, y11)

    glVertex2f(x22, y22)
    print(x2, y2)
    print(x22, y22)

    glEnd()
    glFlush()


def Line_scale(x1, y1, x2, y2, Sx, Sy):
    x11 = round(x1*Sx)
    y11 = round(y1*Sy)

    x22 = round(x2*Sx)
    y22 = round(y2*Sy)

    glColor3f(0.0, 1.0, 1.0)
    glLineWidth(5.0)
    glBegin(GL_LINES)

    print("Scaled Line is in Cyan")

    glVertex2f(x11, y11)
    print(x1, y1)
    print(x11, y11)
    glVertex2f(x22, y22)
    print(x2, y2)
    print(x22, y22)

    glEnd()
    glFlush()


def Line_2d(x1, y1, x2, y2):
    global flag

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(5.0)
    glBegin(GL_LINES)

    glVertex2f(x1, y1)
    glVertex2f(x2, y2)

    print("Original Line is in Green")

    glEnd()
    glFlush()

    if not flag:
        ch = int(
            input("Enter the Transformation\n1. Translation\n2. Rotation\n3. Scaling\n"))
        if ch == 1:
            tx = int(input("Enter Translation point x: "))
            ty = int(input("Enter Translation point y: "))
            Line_Trans(x1, y1, x2, y2, tx, ty)
            flag = True
        elif ch == 2:
            theta = float(input("Enter anlge of rotation: "))
            Line_Rot(theta, x1, y1, x2, y2)
            flag = True
        elif ch == 3:
            Sx = int(input("Enter Scaling point x: "))
            Sy = int(input("Enter Scaling point y: "))
            Line_scale(x1, y1, x2, y2, Sx, Sy)
            flag = True
        else:
            print("invalid choice")


def main():
    # Ask for choice
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    print("starting window....")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Line Transformation")
    glutDisplayFunc(lambda: Line_2d(x1, y1, x2, y2))
    # glutIdleFunc(lambda: Line_2d(x1, y1, x2, y2))
    init()
    glutMainLoop()


main()
