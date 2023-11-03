import numpy as np
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


def rotation_matrix(degree):
    radian = degree * np.pi / 180.0
    mat = np.array([
        [np.cos(radian), -np.sin(radian)],
        [np.sin(radian), np.cos(radian)],
    ])
    return mat


def draw_rectangle():
    # this function draws the rectangular shape with the given vertex
    vertices = (
        (0.3, 0.2),
        (0.3, -0.2),
        (-0.3, -0.2),
        (-0.3, 0.2),
    )
    edges = (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0)
    )
    glBegin(GL_LINES)
    glColor3f(0, 0, 1)
    for edge in edges:
        for vertex in edge:
            glVertex2fv(draw_rotated(vertices[vertex]))
    glEnd()


def draw_rotated(point):
    # this function provides a utility function to rotate a given point with 60 degrees
    mat = rotation_matrix(60)
    point = np.array(point)
    point = np.dot(point, mat)
    point = np.add(point, 0.4)  # shifting the point by 0.4
    return point


def draw_axis():
    # this function draws the x and y coordinate axis
    glColor3f(1, 0, 0)
    x_coordinate = np.linspace(-10, 10, 10)
    y_coordinate = np.linspace(-10, 10, 10)
    glBegin(GL_LINES)
    for a in x_coordinate:
        glVertex2f(a, 0)
    for b in y_coordinate:
        glVertex2f(0, b)
    glEnd()
    glFlush()


def init():
    # initialize a window
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_axis()
        draw_rectangle()
        pygame.display.flip()
        pygame.time.wait(10)

main()
