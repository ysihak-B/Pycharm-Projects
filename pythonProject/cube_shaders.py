from OpenGL.GL import shaders

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import numpy as np
import os
import time

triangleVAO, program = None, None


def getFileContents(filename):
    p = os.path.join(os.getcwd(), filename)
    return open(p, 'r').read()


def rotation_matrix(degree):
    V = np.array([0.0, 0.6, 0.4])
    radian = degree * np.pi / 180.0
    rotateMat = np.array([
        [V[0]*V[0]*(1-V[0]*V[0]) + np.cos(radian), V[0]*V[1]*(1-np.cos(radian))-V[2]*np.sin(radian),
         V[0]*V[2]*(1-np.cos(radian))+V[1]*np.sin(radian), 0.0],
        [V[0]*V[1]*(1-np.cos(radian))+V[2]*np.sin(radian), V[1]*V[1]*(1-V[1]*V[1])+np.cos(radian),
         V[1]*V[2]*(1-np.cos(radian))-V[0]*np.sin(radian), 0.0],
        [V[0]*V[2]*(1-np.cos(radian))-V[1]*np.sin(radian), V[1]*V[2]*(1-np.cos(radian))+V[0]*np.sin(radian),
         V[2]*V[2]*(1-V[2]*V[2])+np.cos(radian), 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])
    return rotateMat


def init():
    global triangleVAO, program
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glViewport(0, 0, 500, 500)

    vertexShaderContent = getFileContents(
        'Ysihak_Bazezew_UGR_1131_12_3/Ysihak_Bazezew_UGR_1131_12_3_cube/triangle.vertex.shader')
    fragmentShaderContent = getFileContents(
        'Ysihak_Bazezew_UGR_1131_12_3/Ysihak_Bazezew_UGR_1131_12_3_cube/triangle.fragment.shader')

    vertexShader = shaders.compileShader(vertexShaderContent, GL_VERTEX_SHADER)
    fragmentShader = shaders.compileShader(fragmentShaderContent, GL_FRAGMENT_SHADER)
    program = glCreateProgram()
    glAttachShader(program, vertexShader)
    glAttachShader(program, fragmentShader)
    glLinkProgram(program)

    vertices = np.array([
        [0.5, -0.5, -0.5, 1.0, 0.0, 0.0],
        [0.5, 0.5, -0.5, 1.0, 0.0, 1.0],
        [-0.5, 0.5, -0.5, 0.0, 1.0, 1.0],
        [-0.5, -0.5, -0.5, 1.0, 0.0, 0.0],
        [0.5, -0.5, 0.5, 1.0, 0.0, 0.0],
        [0.5, 0.5, 0.5, 1.0, 0.0, 1.0],
        [-0.5, -0.5, 0.5, 1.0, 1.0, 0.0],
        [-0.5, 0.5, 0.5, 0.0, 1.0, 1.0]], dtype=np.float32)

    index_data = np.array([
        [0, 1, 2],
        [0, 2, 3],
        [4, 5, 6],
        [5, 6, 7],
        [0, 1, 5],
        [0, 4, 5],
        [2, 3, 6],
        [2, 6, 7],
        [0, 3, 6],
        [0, 4, 6],
        [1, 2, 7],
        [1, 5, 7]], dtype=np.uint32)

    triangleVBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, triangleVBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    triangleVAO = glGenVertexArrays(1)
    glBindVertexArray(triangleVAO)

    ElementBufferObject = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ElementBufferObject)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, index_data.nbytes, index_data, GL_STATIC_DRAW)

    positionLocation = glGetAttribLocation(program, "position")
    glVertexAttribPointer(positionLocation, 3, GL_FLOAT, GL_FALSE, 6 * vertices.itemsize, ctypes.c_void_p(0))
    glEnableVertexAttribArray(positionLocation)

    colorLocation = glGetAttribLocation(program, "color")
    glVertexAttribPointer(colorLocation, 3, GL_FLOAT, GL_FALSE, 6 * vertices.itemsize, ctypes.c_void_p(12))
    glEnableVertexAttribArray(colorLocation)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)


def draw():
    global triangleVAO, program
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    glUseProgram(program)
    glBindVertexArray(triangleVAO)
    rotateMatLocation = glGetUniformLocation(program, "transform")
    rotation_time = 10 * time.time()
    rotateMat = rotation_matrix(rotation_time)
    # rotateMat = rotation_matrix(30)
    glUniformMatrix4fv(rotateMatLocation, 1, GL_TRUE, rotateMat)
    glDrawElements(GL_TRIANGLES, 36, GL_UNSIGNED_INT, None)
    glBindVertexArray(0)


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
