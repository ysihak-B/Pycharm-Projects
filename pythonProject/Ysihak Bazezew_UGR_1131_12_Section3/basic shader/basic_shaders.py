from OpenGL.GL import shaders

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os

triangleVAO, program = None, None


def getFileContents(filename):
    p = os.path.join(os.getcwd(), "shader", filename)
    return open(p, 'r').read()


def init():
    global triangleVAO, program
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(.30, 0.20, 0.20, 1.0)
    glViewport(0, 0, 500, 500)

    vertexShaderContent = getFileContents('triangle.vertex.shader')
    fragmentShaderContent = getFileContents('triangle.fragment.shader')

    vertexShader = shaders.compileShader(vertexShaderContent, GL_VERTEX_SHADER)
    fragmentShader = shaders.compileShader(fragmentShaderContent, GL_FRAGMENT_SHADER)
    program = glCreateProgram()
    glAttachShader(program, vertexShader)
    glAttachShader(program, fragmentShader)
    glLinkProgram(program)

    vertices = np.array([
        [0.5, 0, 0],
        [-0.5, 0, 0],
        [0, 0.5, 0]], dtype=np.float32)

    triangleVBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, triangleVBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    triangleVAO = glGenVertexArrays(1)
    glBindVertexArray(triangleVAO)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * vertices.itemsize, None)
    glEnableVertexAttribArray(0)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)


def draw():
    global triangleVAO, program
    glClear(GL_COLOR_BUFFER_BIT)
    glUseProgram(program)
    glBindVertexArray(triangleVAO)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glBindVertexArray(0)


def getFileContents(filename):
    p = os.path.join(os.getcwd(), filename)
    return open(p, 'r').read()


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
