from OpenGL.GL import *
from OpenGL.GLU import *

from utils.windowtk import WindowTk
from algorithms.PontoMedio import drowLine
from utils.point import Point
from tkinter import *
from pprint import pprint

WIDTH = 800
HEIGHT = 600

start = Point(0,0)
end = Point(x=300, y=0)
vertices = drowLine(start, end)

pprint(vertices)

def render_config_func():
    glClearColor(0, 0.1, 0.1, 1)
    glViewport(0, 0, 800, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 800, 0, 600)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glPointSize(1) 

def render_func():
    glColor3f(1, 0, 0)
    glBegin(GL_POINTS)
    for v in vertices:
        glVertex2i(v[0]+1, v[1]+1)
    glEnd()

window = WindowTk(800, 600, "app")

def main() :
    root = Tk()
    root.title("Tkinter + OpenGL")

    opengl_frame = WindowTk(root, width=WIDTH, height=HEIGHT, bd=0, highlightthickness=0)
    opengl_frame.pack(side=RIGHT, expand=True, fill=BOTH, padx=0, pady=0)
    opengl_frame.set_init_config(render_config_func)
    opengl_frame.set_render(render_func)

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

        start = Point(x1, y1)
        end = Point(x2, y2)

        opengl_frame.atualiza(start, end)
    
    btn_aplicar = Button(side_frame, text="Aplicar", command=start_render)
    btn_aplicar.grid(row=5, column=0, columnspan=2, pady=10)

    opengl_frame.animate = 1
    root.mainloop()

main()
