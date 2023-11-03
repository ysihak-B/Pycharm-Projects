import pygame
from OpenGL.GL import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import os

VOA, program, texture = None, None, None


def getFileContents(filename):
    p = os.path.join(os.getcwd(), "shaders", filename)
    return open(p, 'r').read()


def init():
    global VOA, program, texture
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(.30, 0.20, 0.20, 1.0)
    glViewport(0, 0, 500, 500)

    vertexShader = compileShader(getFileContents(
        "shaders/vertex.shader"), GL_VERTEX_SHADER)
    fragmentShader = compileShader(getFileContents(
        "shaders/fragment.shader"), GL_FRAGMENT_SHADER)

    program = glCreateProgram()
    glAttachShader(program, vertexShader)
    glAttachShader(program, fragmentShader)
    glLinkProgram(program)

    num = 1
    VAO = glGenVertexArrays(num)
    VBO = glGenBuffers(num)

    # obj1 VAO
    glBindVertexArray(VAO)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, obj1_buffer.nbytes, obj1_buffer, GL_STATIC_DRAW)
    # obj1 vertices, textures, normals
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, obj1_buffer.itemsize * 8, ctypes.c_void_p(0))
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, obj1_buffer.itemsize * 8, ctypes.c_void_p(12))
    glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, obj1_buffer.itemsize * 8, ctypes.c_void_p(20))
    glEnableVertexAttribArray(2)

    # unbind VBO
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    # unbind VAO
    glBindVertexArray(0)


def main():
    global VOA, program, texture
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram(program)
        glBindVertexArray(VOA)
        glBindTexture(GL_TEXTURE_2D, texture)
        glDrawArrays(GL_TRIANGLES, 0, 6)
        glBindTexture(GL_TEXTURE_2D, 0)
        glBindVertexArray(0)

        pygame.display.flip()
        pygame.time.wait(10)


main()
