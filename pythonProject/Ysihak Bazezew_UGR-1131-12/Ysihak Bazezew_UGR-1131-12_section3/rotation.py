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


def rotated_rectangle():
    line_drawer(-0.3, -0.2, 0.0, 0.4)
    line_drawer(-0.3, 0.2, 0.6, 0.0)
    line_drawer(0.3, 0.2, 0.0, -0.4)
    line_drawer(0.3, -0.2, -0.6, 0.0)


def line_drawer(x0, y0, v0, v1):
    mat = rotation_matrix(60)
    v = np.array([v0, v1])
    p0 = (x0, y0)
    temp = p0
    # this will rotate the initial point 60 degree clockwise
    p0 = np.dot(p0, mat)
    # this will shift the initial point by a factor of .4 in both x- and y-axis
    p0 = np.add(p0, .4)
    t = 1
    # this is used to find the final point of the line
    p = temp + t * v
    # this will rotate the initial point 60 degree clockwise
    p = np.dot(p, mat)
    # this will shift the initial point by a factor of .4 in both x- and y-axis
    p = np.add(p, .4)
    glVertex2f(p0[0], p0[1])
    glVertex2f(p[0], p[1])


def axis():
    glVertex2f(1.0, 0.0)
    glVertex2f(-1, 0)
    glVertex2f(0, 1.0)
    glVertex2f(0, -1.0)
    glColor3f(1.0, .0, 1.0)


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(.0, 1.0, 1.0)
    glLineWidth(3)
    glBegin(GL_LINES)

    axis()
    rotated_rectangle()
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
