from pprint import pprint

from OpenGL.GL import *
from OpenGL.GLU import *

from utils.window import Window
from utils.cg_matriz import CGMatriz
from utils.glutils import drowCartesianPlane


WIDHT = 800
HEIGHT = 600

def render_config_func():
    glClearColor(1, 1, 1, 1)

def main():
    rectangle = CGMatriz([
        [0.1, 0.1],
        [0.1, 0.4],
        [0.4, 0.1],
        [0.4, 0.4]
    ])

    def render_func():
        drowCartesianPlane()

        glColor(0, 0, 1)
        glBegin(GL_TRIANGLE_STRIP)
        for v in rectangle.matriz:
            glVertex2fv(v)
        glEnd()
    
    input()

    window = Window(WIDHT, HEIGHT, "Ponto Médio")
    window.set_render_config(render_config_func)
    window.render(render_func)
    window.main_loop()

main()