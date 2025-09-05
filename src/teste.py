from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import glfw

# Constantes
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

start = Point()
end = Point()

# Conversões
def worldToNdcX(x):
    return 2.0 * (x - X_MIN) / (X_MAX - X_MIN) - 1.0

def worldToNdcY(y):
    return 2.0 * (y - Y_MIN) / (Y_MAX - Y_MIN) - 1.0

def ndcToDeviceX(ndcx, width):
    return int(round((ndcx + 1.0) / 2.0 * (width - 1)))

def ndcToDeviceY(ndcy, height):
    return int(round((ndcy + 1.0) / 2.0 * (height - 1)))

# Algoritmos de desenho
def drowLine(start, end):
    ndcx1 = worldToNdcX(start.x)
    ndcy1 = worldToNdcY(start.y)
    dcx1 = ndcToDeviceX(ndcx1, NDH)
    dcy1 = ndcToDeviceY(ndcy1, NDV)

    ndcx2 = worldToNdcX(end.x)
    ndcy2 = worldToNdcY(end.y)
    dcx2 = ndcToDeviceX(ndcx2, NDH)
    dcy2 = ndcToDeviceY(ndcy2, NDV)

    start = Point(dcx1, dcy1)
    end = Point(dcx2, dcy2)

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
        print(f": ({x}, {y})")
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
        print(f": ({x}, {y})")
        glVertex2i(x, y)
    print(f"end: ({x}, {y})")
    glEnd()

