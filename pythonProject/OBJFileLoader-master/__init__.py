from OBJFileLoader import objloader

OBJ = objloader

import pygame
from OpenGL.GL import *
from pygame.locals import *


def init():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glViewport(0, 0, 500, 500)


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    box = OBJ.OBJ('../graphics/graphics.obj')
    glPushMatrix()
    glTranslatef(0, 0, 0)
    box.render()
    glPopMatrix()


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
