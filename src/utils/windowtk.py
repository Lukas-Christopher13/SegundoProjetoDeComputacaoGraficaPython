import os
os.environ['PYOPENGL_PLATFORM'] = 'glx'  

from tkinter import *
from pyopengltk import OpenGLFrame
from OpenGL.GL import *

class WindowTk(OpenGLFrame):
    def initgl(self):
        self._init_config()

    def redraw(self):
        self._render()
    
    def set_render(self, func):
        self._render = func

    def set_init_config(self, func):
        self._init_config = func

