import os
os.environ['PYOPENGL_PLATFORM'] = 'glx'

from tkinter import * 
from OpenGL.GL import *
from OpenGL.GLU import *

from utils.windowtk import WindowTk
from utils.cg_matriz import CGMatriz
from utils.glutils import drowCartesianPlane


WIDTH = 800
HEIGHT = 600

def render_config_func():
    glClearColor(1, 1, 1, 1)

def main():
    global rectangle
    rectangle = CGMatriz([
        [0.0, 0.0, 1],
        [0.4, 0.0, 1],
        [0.2, 0.4, 1],
    ])

    def render_func():
        drowCartesianPlane()

        glColor(0, 0, 1)
        glBegin(GL_TRIANGLE_STRIP)
        for v in rectangle.matriz:
            glVertex3fv(v)
        glEnd()

    root = Tk()
    root.title("Rotação")

    window = WindowTk(root, width=WIDTH, height=HEIGHT, bd=0, highlightthickness=0)
    window.pack(side=RIGHT, expand=True, fill=BOTH, padx=0, pady=0)

    side_frame = Frame(root)
    side_frame.pack(side=LEFT, fill=Y, padx=0, pady=0)  

    Label(side_frame, text="Angle").grid(row=0, column=0, padx=0, pady=5)
    angle_entry = Entry(side_frame, width=20)
    angle_entry.grid(row=0, column=1, padx=0, pady=0)

    def rotate():
        angle = int(angle_entry.get())
        print(rectangle.rotate(angle))

    btn_aplicar = Button(side_frame, text="Aplicar", command=rotate)
    btn_aplicar.grid(row=5, column=0, columnspan=2, pady=10)

    window.set_init_config(render_config_func)
    window.set_render_config(render_func)
    window.animate = 1

    root.mainloop()

main()