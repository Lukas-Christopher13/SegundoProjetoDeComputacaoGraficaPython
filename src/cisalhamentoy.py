# arquivo: shear_y_square.py
import os
os.environ['PYOPENGL_PLATFORM'] = 'windows'

from tkinter import *
from OpenGL.GL import *
from OpenGL.GLU import *

from utils.windowtk import WindowTk
from utils.cg_matriz import CGMatriz
from utils.glutils import drowCartesianPlane
import numpy as np

WIDTH = 800
HEIGHT = 600

def render_config_func():
    glClearColor(1, 1, 1, 1)

# Função de cisalhamento em Y
def shear_y(vertices: CGMatriz, sh_y: float):
    shear_matrix = np.array([
        [1,    0, 0],
        [sh_y, 1, 0],
        [0,    0, 1]
    ])
    matriz_np = np.array(vertices.matriz).T
    resultado = np.dot(shear_matrix, matriz_np).T
    vertices.matriz = resultado.tolist()
    return vertices

def main():
    global square
    square = CGMatriz([
        [0.0, 0.0, 1],
        [0.4, 0.0, 1],
        [0.4, 0.4, 1],
        [0.0, 0.4, 1]
    ])

    sh_y_factor = 0.0

    def render_func():
        drowCartesianPlane()

        # Quadrado original azul
        glColor(0, 0, 1)
        glBegin(GL_QUADS)
        for v in square.matriz:
            glVertex3fv(v)
        glEnd()

        # Quadrado cisalhado em Y vermelho
        if sh_y_factor != 0:
            glColor(1, 0, 0)
            glBegin(GL_QUADS)
            temp = CGMatriz([row.copy() for row in square.matriz])
            shear_y(temp, sh_y_factor)
            for v in temp.matriz:
                glVertex3fv(v)
            glEnd()

    root = Tk()
    root.title("Tkinter + OpenGL: Cisalhamento Y - Quadrado")

    window = WindowTk(root, width=WIDTH, height=HEIGHT, bd=0, highlightthickness=0)
    window.pack(side=RIGHT, expand=True, fill=BOTH, padx=0, pady=0)

    side_frame = Frame(root)
    side_frame.pack(side=LEFT, fill=Y, padx=10, pady=10)

    Label(side_frame, text="Shear Y").grid(row=0, column=0, pady=5)
    shear_y_entry = Entry(side_frame, width=20)
    shear_y_entry.insert(0, "0.0")
    shear_y_entry.grid(row=0, column=1, pady=5)

    def aplicar_shear_y():
        nonlocal sh_y_factor
        try:
            # Divide por 10 para suavizar o efeito
            sh_y_factor = float(shear_y_entry.get()) / 10.0
        except ValueError:
            print("Valor inválido")

    btn_aplicar = Button(side_frame, text="Aplicar", command=aplicar_shear_y)
    btn_aplicar.grid(row=1, column=0, columnspan=2, pady=10)

    window.set_init_config(render_config_func)
    window.set_render_config(render_func)
    window.animate = 1

    root.mainloop()

if __name__ == "__main__":
    main()
