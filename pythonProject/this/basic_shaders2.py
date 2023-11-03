
from OpenGL.GL import shaders

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os


VAO, program= None, None

#
# def getFileContents(filename):
#     p = os.path.join(os.getcwd(), "shader", filename)
#     return open(p, 'r').read()
rotation_matrix = [.866,-0.5,   0.0,0.0,
                        .5,   0.866,0,  0,
                        0,    0,    1,  0,
                        0,    0,    0,  1]
rotation_matrix = np.array(rotation_matrix,dtype=np.float32)

def init():
    global VAO, program
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(1, 1.0, 1.0, 1.0)
    glViewport(0, 0, 500, 500)

    vertexShaderContent = getFileContents('vertx2.shader')
    fragmentShaderContent = getFileContents('fragment2.shader')

    vertexShader = shaders.compileShader(vertexShaderContent, GL_VERTEX_SHADER)
    fragmentShader = shaders.compileShader(fragmentShaderContent, GL_FRAGMENT_SHADER)
    program = glCreateProgram()
    glAttachShader(program, vertexShader)
    glAttachShader(program, fragmentShader)
    glLinkProgram(program)
    glDeleteShader(vertexShader)
    glDeleteShader(fragmentShader)



    vertices = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
                 0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
                 0.5, 0.5, 0.0, 0.0, 0.0, 1.0]


    # convert to 32bit float

    vertices = np.array(vertices, dtype=np.float32)

    # Creating Indices

    indices = [0, 1, 2,
               2, 3, 0]

    indices = np.array(indices, dtype=np.uint32)




    VBO = glGenBuffers(1)
    # EBO = glGenBuffers(1)
    VAO = glGenVertexArrays(1)

    glBindVertexArray(VAO)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    # glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 2 * vertices.itemsize, None)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
    # glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices, GL_STATIC_DRAW)

    colorLocation = glGetAttribLocation(program, "color")
    positionLocation = glGetAttribLocation(program, "position")




    glEnableVertexAttribArray(colorLocation)
    glEnableVertexAttribArray(positionLocation)
    # glEnableVertexAttribArray(rotated)
    #
    # glUniformMatrix4fv(rotated,1,GL_FALSE,rotation_matrix)

    glVertexAttribPointer(positionLocation, 3, GL_FLOAT, GL_FALSE, 6 * vertices.itemsize, ctypes.c_void_p(0))
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * vertices.itemsize, ctypes.c_void_p(12))


    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)


def draw():
    global VAO, program

    glClear(GL_COLOR_BUFFER_BIT)
    glUseProgram(program)

    glBindVertexArray(VAO)
    rotated = glGetUniformLocation(program, "transform")
    glUniformMatrix4fv(rotated, 1, GL_FALSE, rotation_matrix)
    glDrawArrays(GL_TRIANGLES,0,3)
    # glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)
    glBindVertexArray(0)

#
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
        # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        draw()
        pygame.display.flip()
        pygame.time.wait(10)


main()