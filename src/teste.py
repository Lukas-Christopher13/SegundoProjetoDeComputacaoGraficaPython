import ctypes
import numpy as np
from pprint import pprint

from OpenGL.GL import *
from OpenGL.GLU import *

from utils.point import Point
from utils.window import Window
from algorithms.PontoMedio import drowLine


WIDHT = 800
HEIGHT = 600

vertices = [
    [-0.8, 0.5],
    [0.3, -0.9],
    [0.7, 0.2],
    [-0.4, -0.6],
    [0.1, 0.8],
    [-0.9, -0.3],
    [0.5, -0.1],
    [-0.2, 0.9]
    ]

vaoId = 0

def render_config_func():
    global vertices, vaoId
    glClearColor(0, 0.1, 0.1, 1)

    vertices = np.array(vertices, np.dtype(np.float32))

    vaoId = glGenVertexArrays(1)
    glBindVertexArray(vaoId)

    vboId = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vboId)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2*4, ctypes.c_void_p(0))

    glEnableVertexAttribArray(0)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)
    
def main():    
    def render_func():
        glBindVertexArray(vaoId)
        glDrawArrays(GL_TRIANGLES, 0, 8)
        glBindVertexArray(0)

    window = Window(WIDHT, HEIGHT, "teste")
    window.set_render_config(render_config_func)
    window.render(render_func)
    window.main_loop()

main()