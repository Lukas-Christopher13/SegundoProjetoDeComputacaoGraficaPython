import os
os.environ['PYOPENGL_PLATFORM'] = 'windows'

from tkinter import *
from OpenGL.GL import *
from OpenGL.GLU import *
from utils.windowtk import WindowTk  # Canvas OpenGL customizado
import numpy as np

WIDTH = 800
HEIGHT = 600

def draw_pixel(x, y, r, g, b):
    glBegin(GL_POINTS)
    glColor3f(r, g, b)
    glVertex2f(x, y)
    glEnd()

def DDA(x0, y0, xEnd, yEnd, r, g, b):
    dx = xEnd - x0
    dy = yEnd - y0
    steps = max(abs(dx), abs(dy))
    if steps == 0:
        draw_pixel(round(x0), round(y0), r, g, b)
        return
    xIncrement = dx / steps
    yIncrement = dy / steps
    x, y = x0, y0
    for _ in range(int(steps) + 1):
        draw_pixel(round(x), round(y), r, g, b)
        x += xIncrement
        y += yIncrement

def shear_x_matrix(vertices, sh_x):
    """Aplica cisalhamento em X"""
    matriz = np.array([[1, sh_x, 0],
                       [0, 1,    0],
                       [0, 0,    1]])
    return np.dot(matriz, vertices)

def render_triangle(vertices, color):
    """Desenha um polígono usando DDA"""
    n = vertices.shape[1]
    for i in range(n):
        x0, y0 = vertices[0, i], vertices[1, i]
        x1, y1 = vertices[0, (i+1)%n], vertices[1, (i+1)%n]
        DDA(x0, y0, x1, y1, *color)

def render_config_func():
    glClearColor(1, 1, 1, 1)
    glPointSize(2)
    gluOrtho2D(-WIDTH/2, WIDTH/2, -HEIGHT/2, HEIGHT/2)

def main():
    # Vértices do quadrado (x, y, 1)
    global vertices_original
    vertices_original = np.array([
        [0, 100, 100, 0],
        [0, 0,   100, 100],
        [1, 1,   1,   1]
    ], dtype=float)

    global sh_x_factor
    sh_x_factor = 0.0

    def render_func():
        glClear(GL_COLOR_BUFFER_BIT)

        # Desenha o quadrado original em vermelho
        render_triangle(vertices_original, (1, 0, 0))

        # Aplica cisalhamento em X
        vertices_cis = shear_x_matrix(vertices_original, sh_x_factor)

        # Desenha o quadrado cisalhado em verde
        render_triangle(vertices_cis, (0, 1, 0))

    root = Tk()
    root.title("Tkinter + OpenGL: Cisalhamento X")

    # Canvas OpenGL
    window = WindowTk(root, width=WIDTH, height=HEIGHT, bd=0, highlightthickness=0)
    window.pack(side=RIGHT, expand=True, fill=BOTH, padx=0, pady=0)

    # Painel lateral
    side_frame = Frame(root)
    side_frame.pack(side=LEFT, fill=Y, padx=10, pady=10)

    Label(side_frame, text="Shear X").grid(row=0, column=0, pady=5)
    shear_entry = Entry(side_frame, width=20)
    shear_entry.insert(0, "0.0")
    shear_entry.grid(row=0, column=1, pady=5)

    def aplicar_shear():
        global sh_x_factor
        try:
            sh_x_factor = float(shear_entry.get()) / 100
        except ValueError:
            print("Valor inválido")


    btn_aplicar = Button(side_frame, text="Aplicar", command=aplicar_shear)
    btn_aplicar.grid(row=1, column=0, columnspan=2, pady=10)

    window.set_init_config(render_config_func)
    window.set_render_config(render_func)
    window.animate = 1

    root.mainloop()

if __name__ == "__main__":
    main()
