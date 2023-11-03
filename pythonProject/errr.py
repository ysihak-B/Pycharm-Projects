import numpy as np
from OpenGL.GL import*
import glfw

glfw.init()
window = glfw.create_window(400, 300, "PyOpenGL Triangle", None, None)
glfw.set_window_pos(window, 200, 300)
glfw.make_context_current(window)

vertices = [-0.2, -0.2, 0.0, 0.2, -0.2, 0.0, 0.0, 0.2, 0.0]
colors = [0.5, 0, 0, 0, 0, 1, 0, 1, 0]
v = np.array(vertices, dtype=np.float32)
c = np.array(colors, dtype=np.float32)
glVertexPointer(3, GL_FLOAT, 0, v)
glEnableClientState(GL_COLOR_ARRAY)
glColorPointer(3, GL_FLOAT, 0, c)
glClearColor(0.6, 0.8, 0.3, 0.1)

while glfw.window_should_close(window):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(0.1, 1, 0, 0)
    glDrawArrays(GL_TRIANGLES, 0, 2)
    glfw.swap_buffers(window)

glfw.terminate()

