import os
os.environ['PYOPENGL_PLATFORM'] = 'glx'  

from tkinter import *
from pyopengltk import OpenGLFrame
from OpenGL.GL import *

class MyOpenGLFrame(OpenGLFrame):
    def initgl(self):
        glClearColor(0.2, 0.3, 0.4, 1.0)  # cor de fundo

    def redraw(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_TRIANGLES)
        glColor3f(1, 0, 0); glVertex2f(-0.5, -0.5)
        glColor3f(0, 1, 0); glVertex2f( 0.5, -0.5)
        glColor3f(0, 0, 1); glVertex2f( 0.0,  0.5)
        glEnd()

def aplicar_valor():
    print("Valor digitado:", entry.get())

root = Tk()
root.title("Tkinter + OpenGL")

# Área OpenGL
ogl_frame = MyOpenGLFrame(root, width=400, height=400)
ogl_frame.grid(row=0, column=0, rowspan=3)

# Botões e campos
Label(root, text="Digite um valor:").grid(row=0, column=1, padx=10, pady=5)
entry = Entry(root)
entry.grid(row=0, column=2, padx=10, pady=5)

btn = Button(root, text="Aplicar", command=aplicar_valor)
btn.grid(row=1, column=1, columnspan=2, pady=10)

quit_btn = Button(root, text="Sair", command=root.quit)
quit_btn.grid(row=2, column=1, columnspan=2, pady=10)

ogl_frame.animate = 1  # ativa loop de renderização
root.mainloop()
