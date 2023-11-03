import pygame
from OpenGL.GL import *
from pygame.locals import *
from OpenGL.GL.shaders import *
import os

from graphics2.loader.ObjLoader import ObjLoader
from graphics2.loader.TextureLoader import load_texture

vao, shader, textures, ground1_indices = None, None, None, None


def getFileContents(filename):
    p = os.path.join(os.getcwd(), filename)
    return open(p, 'r').read()


def init():
    global vao, shader, textures, ground1_indices
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glViewport(0, 0, 500, 500)

    vertexShader = compileShader(getFileContents("graphics2/shaders/vertex.shader"), GL_VERTEX_SHADER)
    fragmentShader = compileShader(getFileContents("graphics2/shaders/fragment.shader"), GL_FRAGMENT_SHADER)

    shader = glCreateProgram()
    glAttachShader(shader, vertexShader)
    glAttachShader(shader, fragmentShader)
    glLinkProgram(shader)

    ground1_indices, ground1_buffer = ObjLoader.load_model("graphics2/obj_files/ground1.obj")

    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)

    glBindVertexArray(vao)
    # ground1 Vertex Buffer Object
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, ground1_buffer.nbytes, ground1_buffer, GL_STATIC_DRAW)

    # ground1 vertices
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, ground1_buffer.itemsize * 8, ctypes.c_void_p(0))
    # ground1 textures
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, ground1_buffer.itemsize * 8, ctypes.c_void_p(12))
    # ground1 normals
    glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, ground1_buffer.itemsize * 8, ctypes.c_void_p(20))
    glEnableVertexAttribArray(2)

    textures = glGenTextures(1)
    load_texture("graphics2/images/floor4.jpg", textures)



    # unbind VBO
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    # unbind VAO
    glBindVertexArray(0)


def draw():
    global vao, shader, textures
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glUseProgram(shader)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glBindVertexArray(vao)
    glBindTexture(GL_TEXTURE_2D, textures)
    glDrawArrays(GL_TRIANGLES, 0, 878)
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
