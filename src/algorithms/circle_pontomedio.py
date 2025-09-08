from OpenGL.GL import *

class CircleMidpoint:
    def __init__(self, raio: int):
        self.raio = raio

    def draw_pixel(self, x, y):
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()

    def draw_circle_symmetry(self, x, y):
        for px, py in [(x,y),(y,x),(y,-x),(x,-y),(-x,-y),(-y,-x),(-y,x),(-x,y)]:
            self.draw_pixel(px, py)

    def circle_midpoint(self):
        x = 0
        y = self.raio
        d = 5/4 - self.raio

        self.draw_circle_symmetry(x, y)

        while y > x:
            if d < 0:
                d += 2 * x + 3
            else:
                d += 2 * (x - y) + 5
                y -= 1
            x += 1
            self.draw_circle_symmetry(x, y)
