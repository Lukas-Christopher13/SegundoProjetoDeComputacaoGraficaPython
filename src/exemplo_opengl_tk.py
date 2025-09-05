import os
os.environ['PYOPENGL_PLATFORM'] = 'glx'

from tkinter import *
from pyopengltk import OpenGLFrame
from OpenGL.GL import *
from OpenGL.GLU import *

from teste2 import Point, drowLine

WIDTH = 800
HEIGHT = 600

X_MIN = -1000.0
X_MAX = 1000.0
Y_MIN = -1000.0
Y_MAX = 1000.0


class MyOpenGLFrame(OpenGLFrame):
    start = Point(x=0, y=0)
    end = Point(x=100, y=100)

    def initgl(self):
        glClearColor(0.2, 0.3, 0.4, 1.0)

        # ===== Projeção ortográfica para coordenadas de dispositivo =====
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, self.width, 0, self.height)  # 0,0 canto inferior esquerdo
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def redraw(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 0.0, 0.0)
        
        drowLine(self.start, self.end)

root = Tk()
root.title("Tkinter + OpenGL")

side_frame = Frame(root)
side_frame.pack(side=LEFT, fill=Y, padx=10, pady=10)  

Label(side_frame, text="X1").grid(row=0, column=0, padx=5, pady=5)
x1_entry = Entry(side_frame, width=20)
x1_entry.grid(row=0, column=1, padx=5, pady=5)

Label(side_frame, text="Y1").grid(row=1, column=0, padx=5, pady=5)
y1_entry = Entry(side_frame, width=20)
y1_entry.grid(row=1, column=1, padx=5, pady=5)

Label(side_frame, text="X2").grid(row=2, column=0, padx=5, pady=5)
x2_entry = Entry(side_frame, width=20)
x2_entry.grid(row=2, column=1, padx=5, pady=5)

Label(side_frame, text="Y2").grid(row=3, column=0, padx=5, pady=5)
y2_entry = Entry(side_frame, width=20)
y2_entry.grid(row=3, column=1, padx=5, pady=5)


def start_render():
    x1 = int(x1_entry.get())
    y1 = int(y1_entry.get())
    x2 = int(x2_entry.get())
    y2 = int(y2_entry.get())

    global opengl_frame
    opengl_frame = MyOpenGLFrame(root, width=WIDTH, height=HEIGHT)
    opengl_frame.pack(side=RIGHT, expand=True, fill=BOTH)

    opengl_frame.start.x = x1
    opengl_frame.start.y = y1

    opengl_frame.end.x = x2
    opengl_frame.end.y = y2

    opengl_frame.animate = 0
       

btn_aplicar = Button(side_frame, text="Aplicar", command=start_render)
btn_aplicar.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()