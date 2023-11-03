import numpy as np
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


def init():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def draw_line():

    v1 = np.array([.3, .4])
    p0 = (0.1, 0.2)
    p = p0 + 2 * v1
    glVertex2f(p0[0], p0[1])
    glVertex2f(p[0], p[1])


def rectangle_drawer():

    v1 = np.array([-0.3, .3])
    v2 = np.array([-0.2, .2])
    # p0 = (0.0, 0.0)
    t = 1
    p1 =  v1
    p2 =  v2
    glVertex2f(p1[0], p2[0])
    glVertex2f(p1[0], p2[1])
    glVertex2f(p1[1], p2[0])
    glVertex2f(p1[1], p2[1])


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(3)
    glBegin(GL_LINES)

    glVertex2f(1.0, 0.0)
    glVertex2f(-1, 0)
    glVertex2f(0, 1.0)
    glVertex2f(0, -1.0)
    glColor3f(.0, .0, 1.0)
    # rectangle_drawer()
    draw_line()
    glEnd()
    glFlush()


def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        pygame.display.flip()
        pygame.time.wait(10)


main()
