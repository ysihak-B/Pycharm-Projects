import os
import glfw
import pygame
from OpenGL.GL import *
from OpenGL.GL.shaders import compileShader
import pyrr
from pygame.constants import OPENGL, DOUBLEBUF

from graphics2.loader.TextureLoader import load_texture
from graphics2.loader.ObjLoader import ObjLoader


def get_shader_file(filename):
    p = os.path.join(os.getcwd(), filename)
    return open(p, 'r').read()

# initializing glfw
# if not glfw.init():
#     glClearColor(1.0, 1.0, 1.0, 1.0)
#     glViewport(0, 0, 500, 500)
#     raise Exception("glfw can not be initialized!")
#
# # creating glfw window
# window = glfw.create_window(1280, 700, "3D BUILDING MODEL", None, None)
# if not window:
#     glfw.terminate()
#     raise Exception("glfw window can not be created!")
# glfw.make_context_current(window)

# loading obj_files
obj1_indices, obj1_buffer = ObjLoader.load_model("obj_files/obj1.obj")
# obj2_indices, obj2_buffer = ObjLoader.load_model("obj_files/obj2.obj")
# obj3_indices, obj3_buffer = ObjLoader.load_model("obj_files/obj3.obj")
# obj4_indices, obj4_buffer = ObjLoader.load_model("obj_files/obj4.obj")
# obj5_indices, obj5_buffer = ObjLoader.load_model("obj_files/obj5.obj")
# obj6_indices, obj6_buffer = ObjLoader.load_model("obj_files/obj6.obj")
# obj7_indices, obj7_buffer = ObjLoader.load_model("obj_files/obj7.obj")
# obj8_indices, obj8_buffer = ObjLoader.load_model("obj_files/obj8.obj")
# obj9_indices, obj9_buffer = ObjLoader.load_model("obj_files/obj9.obj")
# obj10_indices, obj10_buffer = ObjLoader.load_model("obj_files/obj10.obj")
# obj11_indices, obj11_buffer = ObjLoader.load_model("obj_files/obj11.obj")
# obj12_indices, obj12_buffer = ObjLoader.load_model("obj_files/obj12.obj")
# obj13_indices, obj13_buffer = ObjLoader.load_model("obj_files/obj13.obj")
# obj14_indices, obj14_buffer = ObjLoader.load_model("obj_files/obj14.obj")
# obj15_indices, obj15_buffer = ObjLoader.load_model("obj_files/obj15.obj")
# obj16_indices, obj16_buffer = ObjLoader.load_model("obj_files/obj16.obj")


vertexShader = compileShader(get_shader_file(
    "shaders/vertex.shader"), GL_VERTEX_SHADER)
fragmentShader = compileShader(get_shader_file(
    "shaders/fragment.shader"), GL_FRAGMENT_SHADER)

shader = glCreateProgram()
glAttachShader(shader, vertexShader)
glAttachShader(shader, fragmentShader)
glLinkProgram(shader)

num = 10
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

# # obj2 VAO
# glBindVertexArray(VAO[1])
# glBindBuffer(GL_ARRAY_BUFFER, VBO[1])
# glBufferData(GL_ARRAY_BUFFER, obj2_buffer.nbytes, obj2_buffer, GL_STATIC_DRAW)
# # obj2 vertices, textures, normals
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, obj2_buffer.itemsize * 8, ctypes.c_void_p(0))
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, obj2_buffer.itemsize * 8, ctypes.c_void_p(12))
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, obj2_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)
# #
# # obj3 VAO
# glBindVertexArray(VAO[2])
# glBindBuffer(GL_ARRAY_BUFFER, VBO[2])
# glBufferData(GL_ARRAY_BUFFER, obj3_buffer.nbytes, obj3_buffer, GL_STATIC_DRAW)
# # obj3 vertices, textures, normals
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, obj3_buffer.itemsize * 8, ctypes.c_void_p(0))
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, obj3_buffer.itemsize * 8, ctypes.c_void_p(12))
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, obj3_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)
#
# # obj4 VAO
# glBindVertexArray(VAO[3])
# glBindBuffer(GL_ARRAY_BUFFER, VBO[3])
# glBufferData(GL_ARRAY_BUFFER, obj4_buffer.nbytes, obj4_buffer, GL_STATIC_DRAW)
# # obj4 vertices, textures, normals
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, obj4_buffer.itemsize * 8, ctypes.c_void_p(0))
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, obj4_buffer.itemsize * 8, ctypes.c_void_p(12))
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, obj4_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)
#
# # obj5 VAO
# glBindVertexArray(VAO[4])
# glBindBuffer(GL_ARRAY_BUFFER, VBO[4])
# glBufferData(GL_ARRAY_BUFFER, obj5_buffer.nbytes, obj5_buffer, GL_STATIC_DRAW)
# # obj5 vertices, textures, normals
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, obj5_buffer.itemsize * 8, ctypes.c_void_p(0))
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, obj5_buffer.itemsize * 8, ctypes.c_void_p(12))
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, obj5_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)
#
# # obj6 VAO
# glBindVertexArray(VAO[5])
# glBindBuffer(GL_ARRAY_BUFFER, VBO[5])
# glBufferData(GL_ARRAY_BUFFER, obj6_buffer.nbytes, obj6_buffer, GL_STATIC_DRAW)
# # obj6 vertices, textures, normals
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, obj6_buffer.itemsize * 8, ctypes.c_void_p(0))
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, obj6_buffer.itemsize * 8, ctypes.c_void_p(12))
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, obj6_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)
#
# # obj7 VAO
# glBindVertexArray(VAO[6])
# glBindBuffer(GL_ARRAY_BUFFER, VBO[6])
# glBufferData(GL_ARRAY_BUFFER, obj7_buffer.nbytes, obj7_buffer, GL_STATIC_DRAW)
# # obj7 vertices, textures, normals
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, obj7_buffer.itemsize * 8, ctypes.c_void_p(0))
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, obj7_buffer.itemsize * 8, ctypes.c_void_p(12))
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, obj7_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)
#
# # obj8 VAO
# glBindVertexArray(VAO[7])
# glBindBuffer(GL_ARRAY_BUFFER, VBO[7])
# glBufferData(GL_ARRAY_BUFFER, obj8_buffer.nbytes, obj8_buffer, GL_STATIC_DRAW)
# # obj6 vertices, textures, normals
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, obj8_buffer.itemsize * 8, ctypes.c_void_p(0))
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, obj8_buffer.itemsize * 8, ctypes.c_void_p(12))
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, obj8_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)
#
# # obj9 VAO
# glBindVertexArray(VAO[8])
# glBindBuffer(GL_ARRAY_BUFFER, VBO[8])
# glBufferData(GL_ARRAY_BUFFER, obj9_buffer.nbytes, obj9_buffer, GL_STATIC_DRAW)
# # obj6 vertices, textures, normals
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, obj9_buffer.itemsize * 8, ctypes.c_void_p(0))
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, obj9_buffer.itemsize * 8, ctypes.c_void_p(12))
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, obj9_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)
#
# # obj10 VAO
# glBindVertexArray(VAO[9])
# glBindBuffer(GL_ARRAY_BUFFER, VBO[9])
# glBufferData(GL_ARRAY_BUFFER, obj10_buffer.nbytes, obj10_buffer, GL_STATIC_DRAW)
# # obj6 vertices, textures, normals
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, obj10_buffer.itemsize * 8, ctypes.c_void_p(0))
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, obj10_buffer.itemsize * 8, ctypes.c_void_p(12))
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, obj10_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)
#
# # obj11 VAO
# glBindVertexArray(VAO[10])
# glBindBuffer(GL_ARRAY_BUFFER, VBO[10])
# glBufferData(GL_ARRAY_BUFFER, obj11_buffer.nbytes, obj11_buffer, GL_STATIC_DRAW)
# # obj6 vertices, textures, normals
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, obj11_buffer.itemsize * 8, ctypes.c_void_p(0))
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, obj11_buffer.itemsize * 8, ctypes.c_void_p(12))
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, obj11_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)
#
# # obj12 VAO
# glBindVertexArray(VAO[11])
# glBindBuffer(GL_ARRAY_BUFFER, VBO[11])
# glBufferData(GL_ARRAY_BUFFER, obj12_buffer.nbytes, obj12_buffer, GL_STATIC_DRAW)
# # obj6 vertices, textures, normals
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, obj12_buffer.itemsize * 8, ctypes.c_void_p(0))
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, obj12_buffer.itemsize * 8, ctypes.c_void_p(12))
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, obj12_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)
#
# # obj13 VAO
# glBindVertexArray(VAO[12])
# glBindBuffer(GL_ARRAY_BUFFER, VBO[12])
# glBufferData(GL_ARRAY_BUFFER, obj13_buffer.nbytes, obj13_buffer, GL_STATIC_DRAW)
# # obj6 vertices, textures, normals
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, obj13_buffer.itemsize * 8, ctypes.c_void_p(0))
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, obj13_buffer.itemsize * 8, ctypes.c_void_p(12))
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, obj13_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)
#
# # obj14 VAO
# glBindVertexArray(VAO[13])
# glBindBuffer(GL_ARRAY_BUFFER, VBO[13])
# glBufferData(GL_ARRAY_BUFFER, obj14_buffer.nbytes, obj14_buffer, GL_STATIC_DRAW)
# # obj6 vertices, textures, normals
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, obj14_buffer.itemsize * 8, ctypes.c_void_p(0))
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, obj14_buffer.itemsize * 8, ctypes.c_void_p(12))
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, obj14_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)
#
# # obj15 VAO
# glBindVertexArray(VAO[14])
# glBindBuffer(GL_ARRAY_BUFFER, VBO[14])
# glBufferData(GL_ARRAY_BUFFER, obj15_buffer.nbytes, obj15_buffer, GL_STATIC_DRAW)
# # obj6 vertices, textures, normals
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, obj15_buffer.itemsize * 8, ctypes.c_void_p(0))
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, obj15_buffer.itemsize * 8, ctypes.c_void_p(12))
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, obj15_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)
#
# # obj16 VAO
# glBindVertexArray(VAO[15])
# glBindBuffer(GL_ARRAY_BUFFER, VBO[15])
# glBufferData(GL_ARRAY_BUFFER, obj16_buffer.nbytes, obj16_buffer, GL_STATIC_DRAW)
# # obj6 vertices, textures, normals
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, obj16_buffer.itemsize * 8, ctypes.c_void_p(0))
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, obj16_buffer.itemsize * 8, ctypes.c_void_p(12))
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, obj16_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)

# loading textures
textures = glGenTextures(num)
load_texture("images/floor4.jpg", textures)
# load_texture("images/fence.jpg", textures[1])
# load_texture("images/wall.jpg", textures[2])
# load_texture("images/floor4.jpg", textures[3])
# load_texture("images/floor4.jpg", textures[4])
# load_texture("images/roof.jpg", textures[5])
# load_texture("images/floor2.jpg", textures[6])
# load_texture("images/window2.jpg", textures[7])
# load_texture("images/roof.jpg", textures[8])
# load_texture("images/wall.jpg", textures[9])
# load_texture("images/door3.jpg", textures[10])
# load_texture("images/door3.jpg", textures[11])
# load_texture("images/floor4.jpg", textures[12])
# load_texture("images/lamp.jpg", textures[13])
# load_texture("images/fence.jpg", textures[14])
# load_texture("images/fence.jpg", textures[15])

# the main application loop
# while not glfw.window_should_close(window):
#     glfw.poll_events()

while True:
    # making the 3d appropriate
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glUseProgram(shader)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # defining positions, location, matrix and rotation
    projection = pyrr.matrix44.create_perspective_projection_matrix(45, 1280 / 720, 0.1, 780)
    position = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -85, -300]))
    view = pyrr.matrix44.create_look_at(pyrr.Vector3([0, 0, 8]), pyrr.Vector3([0, 0, 0]), pyrr.Vector3([0, 1, 0]))
    model_loc = glGetUniformLocation(shader, "model")
    proj_loc = glGetUniformLocation(shader, "projection")
    view_loc = glGetUniformLocation(shader, "view")
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)
    rot_y = pyrr.Matrix44.from_y_rotation(-0.2 * glfw.get_time())
    model = pyrr.matrix44.multiply(rot_y, position)
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)

    # draw obj1
    glBindVertexArray(VAO)
    glBindTexture(GL_TEXTURE_2D, textures)
    glDrawArrays(GL_TRIANGLES, 0, len(obj1_indices))
    glBindTexture(GL_TEXTURE_2D, 0)

    # # draw obj2
    # glBindVertexArray(VAO[1])
    # glBindTexture(GL_TEXTURE_2D, textures[1])
    # glDrawArrays(GL_TRIANGLES, 0, len(obj2_indices))
    # glBindTexture(GL_TEXTURE_2D, 0)
    # #
    # # draw obj3
    # glBindVertexArray(VAO[2])
    # glBindTexture(GL_TEXTURE_2D, textures[2])
    # glDrawArrays(GL_TRIANGLES, 0, len(obj3_indices))
    # glBindTexture(GL_TEXTURE_2D, 0)
    #
    # # draw obj4
    # glBindVertexArray(VAO[3])
    # glBindTexture(GL_TEXTURE_2D, textures[3])
    # glDrawArrays(GL_TRIANGLES, 0, len(obj4_indices))
    # glBindTexture(GL_TEXTURE_2D, 0)
    #
    # # draw obj5
    # glBindVertexArray(VAO[4])
    # glBindTexture(GL_TEXTURE_2D, textures[4])
    # glDrawArrays(GL_TRIANGLES, 0, len(obj5_indices))
    # glBindTexture(GL_TEXTURE_2D, 0)
    #
    # # draw obj6
    # glBindVertexArray(VAO[5])
    # glBindTexture(GL_TEXTURE_2D, textures[5])
    # glDrawArrays(GL_TRIANGLES, 0, len(obj6_indices))
    # glBindTexture(GL_TEXTURE_2D, 0)
    #
    # # draw obj7
    # glBindVertexArray(VAO[6])
    # glBindTexture(GL_TEXTURE_2D, textures[6])
    # glDrawArrays(GL_TRIANGLES, 0, len(obj7_indices))
    # glBindTexture(GL_TEXTURE_2D, 0)
    #
    # # draw obj8
    # glBindVertexArray(VAO[7])
    # glBindTexture(GL_TEXTURE_2D, textures[7])
    # glDrawArrays(GL_TRIANGLES, 0, len(obj8_indices))
    # glBindTexture(GL_TEXTURE_2D, 0)
    #
    # # draw obj9
    # glBindVertexArray(VAO[8])
    # glBindTexture(GL_TEXTURE_2D, textures[8])
    # glDrawArrays(GL_TRIANGLES, 0, len(obj9_indices))
    # glBindTexture(GL_TEXTURE_2D, 0)
    #
    # # draw obj10
    # glBindVertexArray(VAO[9])
    # glBindTexture(GL_TEXTURE_2D, textures[9])
    # glDrawArrays(GL_TRIANGLES, 0, len(obj10_indices))
    # glBindTexture(GL_TEXTURE_2D, 0)
    #
    # # draw obj11
    # glBindVertexArray(VAO[10])
    # glBindTexture(GL_TEXTURE_2D, textures[10])
    # glDrawArrays(GL_TRIANGLES, 0, len(obj11_indices))
    # glBindTexture(GL_TEXTURE_2D, 0)
    #
    # # draw obj12
    # glBindVertexArray(VAO[11])
    # glBindTexture(GL_TEXTURE_2D, textures[11])
    # glDrawArrays(GL_TRIANGLES, 0, len(obj12_indices))
    # glBindTexture(GL_TEXTURE_2D, 0)
    #
    # # draw obj13
    # glBindVertexArray(VAO[12])
    # glBindTexture(GL_TEXTURE_2D, textures[12])
    # glDrawArrays(GL_TRIANGLES, 0, len(obj13_indices))
    # glBindTexture(GL_TEXTURE_2D, 0)
    #
    # # draw obj14
    # glBindVertexArray(VAO[13])
    # glBindTexture(GL_TEXTURE_2D, textures[13])
    # glDrawArrays(GL_TRIANGLES, 0, len(obj14_indices))
    # glBindTexture(GL_TEXTURE_2D, 0)
    #
    # # draw obj15
    # glBindVertexArray(VAO[14])
    # glBindTexture(GL_TEXTURE_2D, textures[14])
    # glDrawArrays(GL_TRIANGLES, 0, len(obj15_indices))
    # glBindTexture(GL_TEXTURE_2D, 0)
    #
    # # draw obj16
    # glBindVertexArray(VAO[15])
    # glBindTexture(GL_TEXTURE_2D, textures[15])
    # glDrawArrays(GL_TRIANGLES, 0, len(obj16_indices))
    # glBindTexture(GL_TEXTURE_2D, 0)

    # glfw.swap_buffers(window)
    pygame.display.flip()

# glfw.terminate()
