import os
os.environ['PYOPENGL_PLATFORM'] = 'glx'

from tkinter import *
from pyopengltk import OpenGLFrame
from OpenGL.GL import *
from OpenGL.GLU import *

from trash.teste2 import Point, drowLine

WIDTH = 800
HEIGHT = 600

X_MIN = -1000.0
X_MAX = 1000.0
Y_MIN = -1000.0
Y_MAX = 1000.0


class MyOpenGLFrame(OpenGLFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # valores padrão
        self.start = Point(0, 0)
        self.end = Point(0, 0)
        self.ready = False  # flag para indicar que initgl terminou

    def initgl(self):
        glClearColor(0.2, 0.3, 0.4, 1.0)

        # Projeção ortográfica no sistema lógico
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(X_MIN, X_MAX, Y_MIN, Y_MAX)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        self.ready = True  # contexto pronto

    def redraw(self):
        if not self.ready:
            return  # não tenta desenhar antes do contexto

        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 0.0, 0.0)

        # desenha a linha usando a função drowLine
        drowLine(self.start, self.end)

        glFlush()  # força renderização

    def atualiza(self, start, end):
        self.start = start
        self.end = end

        # garante redraw após contexto estar ativo
        def try_redraw():
            if self.ready:
                self.redraw()
            else:
                self.after(50, try_redraw)  # tenta novamente daqui 50ms
        try_redraw()


def main():
    root = Tk()
    root.title("Tkinter + OpenGL")

    opengl_frame = MyOpenGLFrame(root, width=WIDTH, height=HEIGHT)
    opengl_frame.pack(side=RIGHT, expand=True, fill=BOTH)

    side_frame = Frame(root)
    side_frame.pack(side=LEFT, fill=Y, padx=10, pady=10)

    # Entradas X1,Y1,X2,Y2
    Label(side_frame, text="X1").grid(row=0, column=0)
    x1_entry = Entry(side_frame, width=20)
    x1_entry.grid(row=0, column=1)

    Label(side_frame, text="Y1").grid(row=1, column=0)
    y1_entry = Entry(side_frame, width=20)
    y1_entry.grid(row=1, column=1)

    Label(side_frame, text="X2").grid(row=2, column=0)
    x2_entry = Entry(side_frame, width=20)
    x2_entry.grid(row=2, column=1)

    Label(side_frame, text="Y2").grid(row=3, column=0)
    y2_entry = Entry(side_frame, width=20)
    y2_entry.grid(row=3, column=1)

    def start_render():
        try:
            x1 = int(x1_entry.get())
            y1 = int(y1_entry.get())
            x2 = int(x2_entry.get())
            y2 = int(y2_entry.get())
        except ValueError:
            print("⚠️ Insira apenas valores numéricos")
            return

        start = Point(x1, y1)
        end = Point(x2, y2)
        opengl_frame.atualiza(start, end)

    btn_aplicar = Button(side_frame, text="Aplicar", command=start_render)
    btn_aplicar.grid(row=5, column=0, columnspan=2, pady=10)

    # força um primeiro redraw após pack
    opengl_frame.after(100, opengl_frame.redraw)

    root.mainloop()


if __name__ == "__main__":
    main()
