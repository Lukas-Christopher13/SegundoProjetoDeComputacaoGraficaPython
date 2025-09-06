from pprint import pprint

from OpenGL.GL import *
from OpenGL.GLU import *

from utils.window import Window
from algorithms.DDA import drowLineDDA


WIDHT = 800
HEIGHT = 600

def render_config_func():
    glClearColor(0, 0.1, 0.1, 1)
    glViewport(0, 0, 800, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 800, 0, 600)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glPointSize(1) 

def main():
    x1 = float(input("Digite o valor de x1: "))
    y1 = float(input("Digite o valor de y1: "))
    x2 = float(input("Digite o valor de x2: "))
    y2 = float(input("Digite o valor de y2: "))

    vertices = drowLineDDA(x1, y1, x2, y2)
    
    print("valor dos pontos (x,y):")
    pprint(vertices)

    def render_func():
        glColor3f(1, 0, 0)
        glBegin(GL_POINTS)
        for v in vertices:
            glVertex2f(v[0]+1, v[1]+1)
        glEnd()

    window = Window(WIDHT, HEIGHT, "Ponto Médio")
    window.set_render_config(render_config_func)
    window.render(render_func)
    window.main_loop()

main()