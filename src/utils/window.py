import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

class Window:
    def __init__(self, width: int, height: int, title: str):
        if not glfw.init():
            raise Exception("O glfw não foi inicializado")
        
        self._window = glfw.create_window(width, height, title, None, None)

        if not self._window:
            glfw.terminate()
            raise Exception("Janela glfw não pode ser criada")

        glfw.make_context_current(self._window)


    def main_loop(self):
        #setBackgroudColor
        glClearColor(0, 0.1, 0.1, 1)
        glViewport(0, 0, 800, 600)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, 800, 0, 600)  # 0,0 canto inferior esquerdo
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glPointSize(1) 

        while not glfw.window_should_close(self._window):
            glfw.poll_events()

            glClear(GL_COLOR_BUFFER_BIT)
            self.func()
            glfw.swap_buffers(self._window)

        glfw.terminate()

    def render(self, func):
        self.func = func




    



