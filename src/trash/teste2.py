from OpenGL.GL import *

NDH = 800
NDV = 600

X_MIN = -1000.0
X_MAX = 1000.0
Y_MIN = -1000.0
Y_MAX = 1000.0

# Classe para pontos
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def init():
    glClearColor(1,1,1,1)

def drowLine(start, end):
    if abs(end.x - start.x) > abs(end.y - start.y):
        drowLineH(start, end)
    else:
        drowLineV(start, end)

def drowLineH(start, end):
    if start.x > end.x:
        start, end = end, start

    dx = end.x - start.x
    dy = end.y - start.y

    dir = 1
    if dy < 0:
        dir = -1
        dy = -dy

    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)

    x, y = start.x, start.y

    print(f"start: ({x}, {y})")

    glBegin(GL_POINTS)
    glVertex2i(x, y)
    while x < end.x:
        if d <= 0:
            d += incE
            x += 1
        else:
            d += incNE
            x += 1
            y += dir
        glVertex2i(x, y)
    print(f"end: ({x}, {y})")
    glEnd()

def drowLineV(start, end):
    if start.y > end.y:
        start, end = end, start

    dx = end.x - start.x
    dy = end.y - start.y

    dir = 1
    if dx < 0:
        dir = -1
        dx = -dx

    d = 2 * dx - dy
    incE = 2 * dx
    incNE = 2 * (dx - dy)

    x, y = start.x, start.y

    print(f"start: ({x}, {y})")

    glBegin(GL_POINTS)
    glVertex2i(x, y)
    while y < end.y:
        if d <= 0:
            d += incE
            y += 1
        else:
            d += incNE
            y += 1
            x += dir
        glVertex2i(x, y)
    print(f"end: ({x}, {y})")
    glEnd()




