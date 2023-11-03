import numpy as np
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


def init():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def rotation_matrix(degree):
    radian = degree * np.pi / 180.0
    mat = np.array([
        [np.cos(radian), -np.sin(radian)],
        [np.sin(radian), np.cos(radian)],
    ])

    return mat


def rectangle_drawer():
    p = np.array([-0.3, -0.2, .2, .3])
    line(-0.3, -0.2, -0.3, 0.2)
    line(-0.3, 0.2, 0.3, 0.2)
    line(0.3, 0.2, 0.3, -0.2)
    line(0.3, -0.2, -0.3, -0.2)


def line(x0, y0, x1, y1):
    mat = rotation_matrix(60)
    p0 = np.array([x0, y0])
    p0 = np.dot(p0, mat)
    p0 = np.add(p0, .4)
    p1 = np.array([x1, y1])
    p1 = np.dot(p1, mat)
    p1 = np.add(p1, .4)
    glVertex2f(p0[0], p0[1])
    glVertex2f(p1[0], p1[1])


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, .0, 1.0)
    glBegin(GL_LINES)

    glVertex2f(1.0, 0.0)
    glVertex2f(-1, 0)
    glVertex2f(0, 1.0)
    glVertex2f(0, -1.0)
    glColor3f(1.0, 1.0, .0)
    rectangle_drawer()
    glEnd()
    glFlush()


def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw()

        pygame.display.flip()
        pygame.time.wait(10)


main()
