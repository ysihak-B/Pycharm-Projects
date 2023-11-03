import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Select Two Functions To Be Drawn")
window.geometry('400x500')

style = Style()
style.configure('W.TButton', font=('calibre', 10, 'bold'), foreground='red')

func1 = IntVar()
func2 = IntVar()
func3 = IntVar()
func4 = IntVar()
func5 = IntVar()
func6 = IntVar()

c1 = Checkbutton(window, text='SQUARE', variable=func1, onvalue=1, offvalue=0)
c1.pack()
c2 = Checkbutton(window, text='CUBIC', variable=func2, onvalue=1, offvalue=0)
c2.pack()
c3 = Checkbutton(window, text='LOGX', variable=func3, onvalue=1, offvalue=0)
c3.pack()
c4 = Checkbutton(window, text='SINE', variable=func4, onvalue=1, offvalue=0)
c4.pack()
c5 = Checkbutton(window, text='COSINE', variable=func5, onvalue=1, offvalue=0)
c5.pack()
c6 = Checkbutton(window, text='TANGENT', variable=func6, onvalue=1, offvalue=0)
c6.pack()

draw_button = Button(window, text='DRAW', style='W.TButton', command=window.destroy)
draw_button.pack(pady=20)

window.mainloop()


def init():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def square():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_LINE_STRIP)
    x = np.linspace(-1, 1, 100)
    q = np.power(x, 2)
    for a, b in zip(x, q):
        glVertex(a, b)
    glEnd()
    glFlush()
    pygame.display.flip()
    pygame.time.wait(10)


def cubic():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 1.0)
    glBegin(GL_LINE_STRIP)
    x = np.linspace(-1, 1, 100)
    y = np.power(x, 3)
    for a, b in zip(x, y):
        glVertex(a, b)
    glEnd()
    glFlush()
    pygame.display.flip()
    pygame.time.wait(10)


def logx():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINE_STRIP)
    x = np.linspace(-1, 1, 100)
    y = np.log10(x)
    for a, b in zip(x, y):
        glVertex(a, b)
    glEnd()
    glFlush()
    pygame.display.flip()
    pygame.time.wait(10)


def sine():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_STRIP)
    x = np.linspace(-1, 1, 100)
    y = np.sin(x)
    for a, b in zip(x, y):
        glVertex(a, b)
    glEnd()
    glFlush()
    pygame.display.flip()
    pygame.time.wait(10)


def cosine():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.19, 0.29, 1.0)
    glBegin(GL_LINE_STRIP)
    x = np.linspace(-1, 1, 100)
    y = np.cos(x)
    for a, b in zip(x, y):
        glVertex(a, b)
    glEnd()
    glFlush()
    pygame.display.flip()
    pygame.time.wait(10)


def tangent():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)
    glBegin(GL_LINE_STRIP)
    x = np.linspace(-1, 1, 100)
    y = np.tan(x)
    for a, b in zip(x, y):
        glVertex(a, b)
    glEnd()
    glFlush()
    pygame.display.flip()
    pygame.time.wait(10)


def axis():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(0.0, 1.0)
    glVertex2f(0.0, -1.0)
    glVertex2f(1.0, 0.0)
    glVertex2f(-1.0, 0.0)
    glEnd()
    glFlush()
    pygame.display.flip()
    pygame.time.wait(15)


def draw(axis, graph1, graph2):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        globals()[axis]()
        globals()[graph1]()
        globals()[graph2]()


def main():
    init()
    if (func1.get() == 1 and func2.get() == 1) and (
            func3.get() == 0 and func4.get() == 0 and func5.get() == 0 and func6.get() == 0):
        draw("axis", "square", "cubic")
    elif (func1.get() == 1 and func3.get() == 1) and (
            func2.get() == 0 and func4.get() == 0 and func5.get() == 0 and func6.get() == 0):
        draw("axis", "square", "logx")
    elif (func1.get() == 1 and func4.get() == 1) and (
            func2.get() == 0 and func3.get() == 0 and func5.get() == 0 and func6.get() == 0):
        draw("axis", "square", "sine")
    elif (func1.get() == 1 and func5.get() == 1) and (
            func2.get() == 0 and func3.get() == 0 and func4.get() == 0 and func6.get() == 0):
        draw("axis", "square", "cosine")
    elif (func1.get() == 1 and func6.get() == 1) and (
            func2.get() == 0 and func3.get() == 0 and func4.get() == 0 and func5.get() == 0):
        draw("axis", "square", "tangent")
    elif (func2.get() == 1 and func3.get() == 1) and (
            func1.get() == 0 and func4.get() == 0 and func5.get() == 0 and func6.get() == 0):
        draw("axis", "cubic", "logx")
    elif (func2.get() == 1 and func4.get() == 1) and (
            func1.get() == 0 and func3.get() == 0 and func5.get() == 0 and func6.get() == 0):
        draw("axis", "cubic", "sine")
    elif (func2.get() == 1 and func5.get() == 1) and (
            func1.get() == 0 and func3.get() == 0 and func4.get() == 0 and func6.get() == 0):
        draw("axis", "cubic", "cosine")
    elif (func2.get() == 1 and func6.get() == 1) and (
            func1.get() == 0 and func3.get() == 0 and func4.get() == 0 and func5.get() == 0):
        draw("axis", "cubic", "tangent")
    elif (func3.get() == 1 and func4.get() == 1) and (
            func1.get() == 0 and func2.get() == 0 and func5.get() == 0 and func6.get() == 0):
        draw("axis", "logx", "sine")
    elif (func3.get() == 1 and func5.get() == 1) and (
            func1.get() == 0 and func2.get() == 0 and func4.get() == 0 and func6.get() == 0):
        draw("axis", "logx", "cosine")
    elif (func3.get() == 1 and func6.get() == 1) and (
            func1.get() == 0 and func2.get() == 0 and func4.get() == 0 and func5.get() == 0):
        draw("axis", "logx", "tangent")
    elif (func4.get() == 1 and func5.get() == 1) and (
            func1.get() == 0 and func2.get() == 0 and func3.get() == 0 and func6.get() == 0):
        draw("axis", "sine", "cosine")
    elif (func4.get() == 1 and func6.get() == 1) and (
            func1.get() == 0 and func2.get() == 0 and func3.get() == 0 and func5.get() == 0):
        draw("axis", "sine", "tangent")
    elif (func5.get() == 1 and func6.get() == 1) and (
            func1.get() == 0 and func2.get() == 0 and func3.get() == 0 and func4.get() == 0):
        draw("axis", "cosine", "tangent")
    else:
        print("INVALID INPUT")
        print("HINT: SELECT TWO AND ONLY TWO FUNCTIONS (NOT MORE OR LESS THAN TWO)")


main()
