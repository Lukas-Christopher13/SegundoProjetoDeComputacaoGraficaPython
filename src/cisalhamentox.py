import os
os.environ['PYOPENGL_PLATFORM'] = 'windows'

from tkinter import *
from OpenGL.GL import *
from OpenGL.GLU import *
from utils.windowtk import WindowTk
from utils.cg_matriz import CGMatriz
from utils.glutils import drowCartesianPlane  # eixo cartesiano

WIDTH = 800
HEIGHT = 600

def render_config_func():
    glClearColor(1, 1, 1, 1)
    glPointSize(4)
    gluOrtho2D(-1, 1, -1, 1)

def main():
    global triangle
    triangle = CGMatriz([
        [0.0, 0.0, 1],
        [0.4, 0.0, 1],
        [0.2, 0.4, 1],
    ])

    def render_func():
        glClear(GL_COLOR_BUFFER_BIT)
        drowCartesianPlane()

        glColor(0, 0, 1)
        glBegin(GL_TRIANGLE_STRIP)
        for v in triangle.matriz:
            glVertex3fv(v)
        glEnd()

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
        try:
            sh_x = float(shear_entry.get())
            triangle.shear_x(sh_x)
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
