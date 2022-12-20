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

    gluOrtho2D(-500, 500, -500, 500)

def Rotate_Tri(T,x1,y1,x2,y2,x3,y3):
    x11 = x1*math.cos(T) - y1*math.sin(T)
    y11 = x1*math.sin(T) + y1*math.cos(T)

    x22 = x2*math.cos(T) - y2*math.sin(T)
    y22 = x2*math.sin(T) + y2*math.cos(T)

    x33 = x3*math.cos(T) - y3*math.sin(T)
    y33 = x3*math.sin(T) + y3*math.cos(T)

    glColor3f(0.0, 1.0, 1.0)
    glLineWidth(5.0)
    glBegin(GL_LINES)

    print("Original triangle is in Cyan")

    glVertex2f(x11,y11)
    glVertex2f(x22,y22)

    glVertex2f(x22,y22)
    glVertex2f(x33,y33)
    
    glVertex2f(x11,y11)
    glVertex2f(x33,y33)


    glEnd()
    glFlush()

def Triangle(x1,y1,x2,y2,x3,y3):
    global flag
    
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(5.0)
    glBegin(GL_LINES)

    print("Original triangle is in Green")

    glVertex2f(x1,y1)
    glVertex2f(x2,y2)

    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    
    glVertex2f(x1,y1)
    glVertex2f(x3,y3)


    glEnd()
    glFlush()

    if not flag :
        theta = float(input("Enter anlge of rotation: "))
        Rotate_Tri(theta, x1,y1,x2,y2,x3,y3)
        flag = True

def main():
    # Ask for choice
            x1 = int(input("Enter x1: "))
            y1 = int(input("Enter y1: "))
            x2 = int(input("Enter x2: "))
            y2 = int(input("Enter y2: "))
            x3 = int(input("Enter x3: "))
            y3 = int(input("Enter y3: "))
            print("starting window....")
            glutInit(sys.argv)
            glutInitDisplayMode(GLUT_RGB)
            glutInitWindowSize(700, 700)
            glutInitWindowPosition(0, 0)
            glutCreateWindow("Rotate Triangle")
            glutDisplayFunc(lambda: Triangle(x1, y1, x2,y2,x3,y3))
            # glutIdleFunc(lambda: Triangle(x1, y1, x2, y2))
            init()
            glutMainLoop()


main()