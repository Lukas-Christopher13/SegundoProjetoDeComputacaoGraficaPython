from OpenGL.GL import *
from OpenGL.GLU import *

from algorithms.circle_pontomedio import CircleMidpoint
from utils.window import Window 

WIDTH = 800
HEIGHT = 600

def render_config_func():
    glClearColor(1, 1, 1, 1)
    glViewport(0, 0, WIDTH, HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-WIDTH//2, WIDTH//2, -HEIGHT//2, HEIGHT//2)  # centralizado
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glPointSize(2.0)

def main():
    raio = int(input("Digite o raio do círculo: "))

    def render_func():
        glColor3f(0, 0, 1)  # azul
        circle = CircleMidpoint(raio)
        circle.circle_midpoint()

    window = Window(WIDTH, HEIGHT, "Círculo - Ponto Médio")
    window.set_render_config(render_config_func)
    window.render(render_func)
    window.main_loop()

main()
