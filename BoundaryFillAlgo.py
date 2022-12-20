# First Import necessary dependencies
from turtle import fillcolor
import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import time
from math import *
import sys 
sys.setrecursionlimit(15000)


def init():  # Initialisation Function
    global width, height
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(0.0, width, 0.0, height)
    # gluOrtho2D(0, 10, 0, 10)


def boundary_fill_8(x, y, fillColor, bc):
    color = glReadPixels(x, y, 1.0, 1.0, GL_RGB, GL_UNSIGNED_BYTE, None)

    if (color != fillColor and color != bc):
        glColor3f(0.0, 1.0, 0.0)
        glPointSize(5.0)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()
        glFlush()
        # time.sleep(1)
        boundary_fill_8(x+5, y, fillColor, bc)
        boundary_fill_8(x-5, y, fillColor, bc)
        boundary_fill_8(x, y+5, fillColor, bc)
        boundary_fill_8(x, y-5, fillColor, bc)
        boundary_fill_8(x-5, y+5, fillColor, bc)
        boundary_fill_8(x-5, y-5, fillColor, bc)
        boundary_fill_8(x+5, y+5, fillColor, bc)
        boundary_fill_8(x+5, y-5, fillColor, bc)


def Mouse(button, state, x, y):
    global mouse_x, mouse_y, get_input

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        mouse_x = x
        mouse_y = height - y  # the y coordinate of the mouse has to be flipped
        get_input = True


def readinput(x, y):
    # xc = int(input("Enter x: "))
    # yc = int(input("Enter y: "))
    fillColor = b'\x00\xff\x00'
    bc = b'\x00\xff\x00'
    color = glReadPixels(x, y, 1.0, 1.0, GL_RGB, GL_UNSIGNED_BYTE, None)
    if (color != fillColor and color != bc):
        glColor3f(0.0, 1.0, 0.0)
        glPointSize(5.0)
        glBegin(GL_POINTS)
        glVertex2i(x, y)
        glEnd()
        glFlush()
        readinput(x, y+5)
        readinput(x, y-5)
        readinput(x+5, y)
        readinput(x-5, y)
    else:
        glutLeaveMainLoop()


def RectLineBresenham(x0=220, y0=110, l=200, b=150):
    x1 = x0
    y1 = y0

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

    dx2 = abs(x3 - x4)
    dy2 = abs(y3 - y4)
    dT2 = 2 * abs(dy2 - dx2)
    dS2 = 2 * dy2
    d2 = 2 * abs(dy2)-abs(dx2)

    y = y1
    x_l2 = x1

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
    glEnd()


def circle():
    glLineWidth(6.0)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        m = float(120*cos(i*pi/180.0))+320
        n = float(120*sin(i*pi/180.0))+320
        glVertex2f(m, n)
    glEnd()


def display():
    global mouse_x, mouse_y, get_input
    glClear(GL_COLOR_BUFFER_BIT)
    circle()
    # RectLineBresenham()

    glutSwapBuffers()
    glutPostRedisplay()

    if get_input:
        readinput(mouse_x, mouse_y)
        get_input = False


def main():
    global width, height
    # Ask for choice
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(10, 10)
    glutCreateWindow("Plot Line using Bresenham Algorithm")

    glutDisplayFunc(display)
    glutMouseFunc(Mouse)

    init()
    glutMainLoop()


width = 640
height = 640
mouse_x = 22
mouse_y = 22
get_input = False
main()
