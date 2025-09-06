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
        self.render_config()

        while not glfw.window_should_close(self._window):
            glfw.poll_events()

            glClear(GL_COLOR_BUFFER_BIT)
            self.func()
            glfw.swap_buffers(self._window)

        glfw.terminate()

    def set_render_config(self, func):
        self.render_config = func

    def render(self, func):
        self.func = func




    



