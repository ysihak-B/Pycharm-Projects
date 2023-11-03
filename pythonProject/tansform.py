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
    mat = rotation_matrix(-30)
    v1 = np.array([-0.3, 0.3])
    v1 = np.dot(v1, mat)
    v2 = np.array([-0.2, 0.2])
    v2 = np.dot(v2, mat)
    glVertex2f(v1[0], v2[0])
    glVertex2f(v1[0], v2[1])
    glVertex2f(v1[0], v2[1])
    glVertex2f(v1[1], v2[1])
    glVertex2f(v1[1], v2[1])
    glVertex2f(v1[1], v2[0])
    glVertex2f(v1[1], v2[0])
    glVertex2f(v1[0], v2[0])


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(.0, 1.0, 1.0)
    glBegin(GL_LINES)

    glVertex2f(1.0, 0.0)
    glVertex2f(-1, 0)
    glVertex2f(0, 1.0)
    glVertex2f(0, -1.0)
    glColor3f(1.0, .0, 1.0)
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



