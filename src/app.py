from OpenGL.GL import *

from utils.window import Window
from algoritimo import drowLine
from point import Point

from pprint import pprint

start = Point(0,0)
end = Point(x=300, y=0)
vertices = drowLine(start, end)

pprint(vertices)

def run():
    glColor3f(1, 0, 0)
    glBegin(GL_POINTS)
    for v in vertices:
        glVertex2i(v[0]+1, v[1]+1)
    glEnd()

window = Window(800, 600, "app")
window.render(run)
window.main_loop()
