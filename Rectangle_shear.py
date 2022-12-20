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

    gluOrtho2D(-100, 250, -100, 250)

def Shear_Rect(x1,y1,l,b,Shx,Shy):
    x11 = x1 + Shx*y1
    y11 = y1 + Shy*x1

    x22 = (x1+l) + Shx*y1
    y22 = y1 + Shy*(x1+l)

    x33 = (x1+l) + Shx*(y1+b)
    y33 = (y1+b) + Shy*(x1+l)

    x44 = (x1) + Shx*(y1+b)
    y44 = (y1+b) + Shy*(x1)

    glColor3f(0.0, 1.0, 1.0)
    glLineWidth(5.0)
    glBegin(GL_LINES)

    print("Original triangle is in Cyan")

    glVertex2f(x11,y11)
    glVertex2f(x22,y22)

    glVertex2f(x22,y22)
    glVertex2f(x33,y33)
    
    glVertex2f(x33,y33)
    glVertex2f(x44,y44)

    glVertex2f(x11,y11)
    glVertex2f(x44,y44)

    glEnd()
    glFlush()

def Reactangle_shear(x1,y1,l,b):
    global flag
    
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(5.0)
    glBegin(GL_LINES)

    print("Original triangle is in Green")

    glVertex2f(x1,y1)
    glVertex2f(x1+l,y1)

    glVertex2f(x1+l,y1)
    glVertex2f(x1+l,y1+b)
    
    glVertex2f(x1,y1+b)
    glVertex2f(x1+l,y1+b)

    glVertex2f(x1,y1+b)
    glVertex2f(x1,y1)


    glEnd()
    glFlush()

    if not flag :
        Shx = int(input("Enter Shearing about x: "))
        Shy = int(input("Enter Shearing about y: "))
        Shear_Rect(x1,y1,l,b,Shx,Shy)
        flag = True

def main():
    # Ask for choice
            x1 = int(input("Enter x1: "))
            y1 = int(input("Enter y1: "))
            l = int(input("Enter Length: "))
            b = int(input("Enter Breadth: "))
            print("starting window....")
            glutInit(sys.argv)
            glutInitDisplayMode(GLUT_RGB)
            glutInitWindowSize(700, 700)
            glutInitWindowPosition(0, 0)
            glutCreateWindow("Shear Rectangle")
            glutDisplayFunc(lambda: Reactangle_shear(x1, y1,l,b))
            # glutIdleFunc(lambda: Reactangle_shear(x1, y1, x2, y2))
            init()
            glutMainLoop()


main()