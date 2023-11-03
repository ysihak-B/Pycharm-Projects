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


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)

    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)

    glColor3f(0.0, 1.0, 1.0)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(-0.5, -0.5)

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