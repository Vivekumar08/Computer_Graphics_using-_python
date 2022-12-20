from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

flag = True

def init():  # Initialisation Function
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(0, 500, 0, 500)

# Defining region codes 
INSIDE = 0  # 0000 
LEFT = 1    # 0001 
RIGHT = 2   # 0010 
BOTTOM = 4  # 0100 
TOP = 8     # 1000 

x_max = 350
y_max = 350
x_min = 50
y_min = 50

def computeCode(x, y): 
    code = INSIDE 
    if x < x_min:      # to the left of rectangle 
        code |= LEFT 
    elif x > x_max:    # to the right of rectangle 
        code |= RIGHT 
    if y < y_min:      # below the rectangle 
        code |= BOTTOM 
    elif y > y_max:    # above the rectangle 
        code |= TOP 
    
    print(code)
    return code

def Line_clip(x1, y1, x2, y2):
    # x1 = float(entry_x1.get())
    # y1 = float(entry_y1.get())
    # x2 = float(entry_x2.get())
    # y2 = float(entry_y2.get())

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)

    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

    # my_canvas.create_line(x1, y1, x2, y2, fill = 'red')
    # my_canvas.grid(row = 6, column = 0)


    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    accept = False

    while True: 
  
        # If both endpoints lie within rectangle 
        if code1 == 0 and code2 == 0: 
            accept = True
            break
  
        # If both endpoints are outside rectangle 
        elif (code1 & code2) != 0: 
            break
  
        # Some segment lies within the rectangle 
        else: 
  
            # Line Needs clipping 
            # At least one of the points is outside,  
            # select it 
            x = 1.0
            y = 1.0
            if code1 != 0: 
                code_out = code1 
            else: 
                code_out = code2 
  
            # Find intersection point 
            # using formulas y = y1 + slope * (x - x1),  
            # x = x1 + (1 / slope) * (y - y1) 
            if code_out & TOP: 
                
                # point is above the clip rectangle 
                x = x1 + ((x2 - x1) / (y2 - y1)) * (y_max - y1) 
                y = y_max 
  
            elif code_out & BOTTOM: 
                  
                # point is below the clip rectangle 
                x = x1 + ((x2 - x1) / (y2 - y1)) * (y_min - y1) 
                y = y_min 
  
            elif code_out & RIGHT: 
                  
                # point is to the right of the clip rectangle 
                y = y1 + ((y2 - y1) / (x2 - x1)) * (x_max - x1) 
                x = x_max 
  
            elif code_out & LEFT: 
                  
                # point is to the left of the clip rectangle 
                y = y1 + ((y2 - y1) / (x2 - x1)) * (x_min - x1)  
                x = x_min 
  
            # Now intersection point x, y is found 
            # We replace point outside clipping rectangle 
            # by intersection point 
            if code_out == code1: 
                x1 = x 
                y1 = y 
                code1 = computeCode(x1, y1) 
  
            else: 
                x2 = x 
                y2 = y 
                code2 = computeCode(x2, y2) 
  
    if accept: 
        print ("Line accepted from %.2f, %.2f to %.2f, %.2f" % (x1, y1, x2, y2)) 
        # glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(0.0, 0.0, 1.0)
        glLineWidth(5.0)
        glBegin(GL_LINES)

        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()
        glFlush()

        # my_canvas.create_line(x1, y1, x2, y2, fill = 'blue',  width = 1)
        # my_canvas.grid(row = 6, column = 0)
        # Here the user can add code to display the rectangle 
        # along with the accepted (portion of) lines 
  
    else: 
        print ("Line Rejected from %.2f, %.2f to %.2f, %.2f" % (x1, y1, x2, y2)) 
        # glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 0.0, 0.0)
        glLineWidth(5.0)
        glBegin(GL_LINES)

        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()
        glFlush()

def display():
    global flag
    glClear(GL_COLOR_BUFFER_BIT)


    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(5.0)
    glBegin(GL_LINES)
    glVertex2f(50, 50)
    glVertex2f(350, 50)

    glVertex2f(350, 350)
    glVertex2f(50, 350)

    glVertex2f(50, 350)
    glVertex2f(50, 50)

    glVertex2f(350, 50)
    glVertex2f(350, 350)
    glEnd()

    # glutSwapBuffers()
    # glutPostRedisplay()

    if flag:
        Line_clip(x1=60, y1=250, x2=11, y2=60)
        Line_clip(x1=10, y1=250, x2=11, y2=60)
        Line_clip(x1=400, y1=250, x2=40, y2=60)
        Line_clip(x1=40, y1=250, x2=400, y2=60)
        flag = False

def main():
    print("starting window....")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(0, 0)
    # glutCreateWindow("Display figure")
    # glutDisplayFunc(lambda: Line_clip(x1=250, y1=250, x2=11, y2=60))
    glutCreateWindow("Line Clipping using Cohen Sutherland")
    # glutDisplayFunc(lambda: Line_clip(x1=60, y1=250, x2=11, y2=60))
    glutDisplayFunc(lambda: display())
    # glutIdleFunc(lambda: Line_2d(x1, y1, x2, y2))
    init()
    glutMainLoop()


main()