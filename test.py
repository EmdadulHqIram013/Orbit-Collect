# import numpy as np
# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from engine.input import KeyboardInput  # Import your new KeyboardInput class


# xx = 75
# yy = 275


# def addPixel(a, b):
#     glPointSize(5)
#     glBegin(GL_POINTS)
#     glVertex2f(a, b)
#     glEnd()


# """
# Mid-point line drawing algorithm
# """

# digiNet = {
#     0: [[100, 300, 50, 300], [50, 350, 350, 350], [300, 50, 350, 50], [50, 300, 50, 350], [350, 50, 350, 350],
#         [150, 150, 150, 200], [200, 200, 200, 350], [150, 200, 200, 200], [50, 100, 100, 100],
#         [100, 100, 100, 200], [150, 100, 200, 100], [200, 50, 250, 50], [200, 250, 250, 250], [250, 200, 300, 200],
#         [250, 100, 350, 100], [50, 250, 150, 250], [50, 50, 200, 50], [200, 150, 300, 150],
#         [250, 300, 300, 300], [150, 250, 150, 300], [50, 50, 50, 250], [200, 50, 200, 150], [300, 150, 300, 300]],
# }


# def loadDigits():
#     for ii in digiNet:
#         if ii == int(0):
#             for k in digiNet[ii]:
#                 printLine(k[0], k[1], k[2], k[3])


# def keyPressed(key, x, y):
#     if key == b'\x1b':  # ESC key
#         glutDestroyWindow(wind)
#         sys.exit(0)


# def specialKeyPressed(key, x, y):
#     pass  # Your other key handling code here if needed


# def findZone(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     if abs(dx) <= abs(dy):
#         if dx >= 0 and dy >= 0:
#             return 1
#         elif dx <= 0 and dy >= 0:
#             return 2
#         elif dx >= 0 and dy <= 0:
#             return 6
#         elif dx <= 0 and dy <= 0:
#             return 5
#     else:
#         if dx >= 0 and dy >= 0:
#             return 0
#         elif dx <= 0 and dy >= 0:
#             return 3
#         elif dx >= 0 and dy <= 0:
#             return 7
#         elif dx <= 0 and dy <= 0:
#             return 4


# def convertZero(z, x, y):
#     if z == 0:
#         return x, y
#     elif z == 1:
#         return y, x
#     elif z == 2:
#         return y, -x
#     elif z == 3:
#         return -x, y
#     elif z == 4:
#         return -x, -y
#     elif z == 5:
#         return -y, -x
#     elif z == 6:
#         return -y, x
#     elif z == 7:
#         return x, -y


# def midpoint(z, x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     d = (2 * dy) - dx
#     dE = 2 * dy
#     dNE = 2 * (dy - dx)
#     y = y1
#     x = x1
#     while x < x2:
#         a, b = convertBack(z, x, y)
#         addPixel(a, b)
#         if d < 0:  # next pixel: NE
#             x += 1
#             d += dE

#         else:
#             y += 1
#             x += 1
#             d += dNE  # next pixel: E


# def convertBack(z, x, y):
#     if z == 0:
#         return x, y
#     elif z == 1:
#         return y, x
#     elif z == 2:
#         return -y, x
#     elif z == 3:
#         return -x, y
#     elif z == 4:
#         return -x, -y
#     elif z == 5:
#         return -y, -x
#     elif z == 6:
#         return y, -x
#     elif z == 7:
#         return x, -y


# def printLine(x1, y1, x2, y2):
#     zone = findZone(x1, y1, x2, y2)
#     a, b = convertZero(zone, x1, y1)
#     c, d = convertZero(zone, x2, y2)
#     midpoint(zone, a, b, c, d)


# # ----------------------------------------------------------


# """
# Mid-point circle drawing algorithm
# """


# def midPointCircle(X, Y, r):
#     d = 1 - r
#     x = 0
#     y = r
#     while x <= y:
#         x += 1
#         if d < 0:
#             d += 2 * x + 3
#         else:
#             y -= 1
#             d += 2 * (x - y) + 5
#         addPixel(X + x, Y + y)
#         addPixel(X - x, Y + y)
#         addPixel(X + x, Y - y)
#         addPixel(X - x, Y - y)
#         addPixel(X + y, Y + x)
#         addPixel(X - y, Y + x)
#         addPixel(X + y, Y - x)
#         addPixel(X - y, Y - x)


# def drawCircles(X, Y, R):
#     for i in range(R):
#         midPointCircle(X, Y, R)
#         R = R - 1


# # ----------------------------------------------------------

# """
# Transformation algorithm
# """


# def translation(x, y, dx, dy):
#     t = np.array([[1, 0, dx],
#                   [0, 1, dy],
#                   [0, 0, 1]])

#     v1 = np.array([[x],
#                    [y],
#                    [1]])

#     v11 = np.matmul(t, v1)

#     drawCircles(v11[0][0], v11[1][0], 15)


# # ----------------------------------------------------------

# """
# WASD keyboard control
# """


# def game():
#     keyboard.read_key()
#     arrow = keyboard.read_key()
#     global xx, yy
#     if xx == 75 and yy == 275:  # 28
#         if arrow == 'w' or arrow == 'a' or arrow == 's':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 125 and yy == 275:  # 01
#         if arrow == 'd' or arrow == 's':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 75 and yy == 325:  # 27
#         if arrow == 'w' or arrow == 'a' or arrow == 's':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 125 and yy == 325:  # 02
#         if arrow == 'w':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 175 and yy == 325:  # 03
#         if arrow == 'w' or arrow == 'd':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 175 and yy == 275:  # 04
#         if arrow == 'a' or arrow == 'd':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 175 and yy == 225:  # 05
#         if arrow == 's' or arrow == 'd':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 125 and yy == 225:  # 06
#         if arrow == 'w':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 75 and yy == 225:  # 29
#         if arrow == 'w' or arrow == 'a':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 75 and yy == 175:  # 30
#         if arrow == 'a' or arrow == 'd':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 75 and yy == 125:  # 31
#         if arrow == 'a' or arrow == 's' or arrow == 'd':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 75 and yy == 75:  # 32
#         if arrow == 'w' or arrow == 'a' or arrow == 's':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 125 and yy == 175:  # 07
#         if arrow == 'a' or arrow == 'd':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 125 and yy == 125:  # 08
#         if arrow == 'a':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 125 and yy == 75:  # 33
#         if arrow == 's':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 175 and yy == 75:  # 34
#         if arrow == 'w' or arrow == 'd' or arrow == 's':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 175 and yy == 125:  # 09
#         if arrow == 'd' or arrow == 's':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 175 and yy == 175:  # 10
#         if arrow == 'w' or arrow == 'a':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 225 and yy == 325:  # 16
#         if arrow == 'w' or arrow == 'a':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 275 and yy == 325:  # 17
#         if arrow == 'w' or arrow == 's':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 325 and yy == 325:  # 18
#         if arrow == 'w' or arrow == 'd':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 225 and yy == 275:  # 15
#         if arrow == 'a' or arrow == 's':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 275 and yy == 275:  # 14
#         if arrow == 'w' or arrow == 'd':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 325 and yy == 275:  # 19
#         if arrow == 'a' or arrow == 'd':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 225 and yy == 225:  # 12
#         if arrow == 'w' or arrow == 'a':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 275 and yy == 225:  # 13
#         if arrow == 'd' or arrow == 's':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 325 and yy == 225:  # 20
#         if arrow == 'a' or arrow == 'd':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 225 and yy == 175:  # 11
#         if arrow == 's':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 275 and yy == 175:  # 36
#         if arrow == 'w' or arrow == 'd' or arrow == 's':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 325 and yy == 175:  # 21
#         if arrow == 'd' or arrow == 'a':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 225 and yy == 125:  # 24
#         if arrow == 'w' or arrow == 'a':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 275 and yy == 125:  # 23
#         if arrow == 'w' or arrow == 's':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 325 and yy == 125:  # 22
#         if arrow == 'd' or arrow == 's':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 225 and yy == 75:  # 25
#         if arrow == 'a' or arrow == 's':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#     if xx == 275 and yy == 75:  # 26
#         if arrow == 'w':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return
#         elif arrow == 's':
#             drawCircles(75, 275, 15)
#             xx = 75
#             yy = 275
#             print("GAME OVER")
#             return
#     if xx == 325 and yy == 75:  # 35
#         if arrow == 'w' or arrow == 'd' or arrow == 's':
#             drawCircles(xx, yy, 15)
#             print("Can not move.")
#             return

#     if arrow == 'r':
#         drawCircles(75, 275, 15)
#         xx = 75
#         yy = 275
#         return
#     elif arrow == 'd':
#         translation(xx, yy, 50, 0)
#         xx = xx + 50
#         return
#     elif arrow == 'w':
#         translation(xx, yy, 0, 50)
#         yy = yy + 50
#         return
#     elif arrow == 'a':
#         translation(xx, yy, -50, 0)
#         xx = xx - 50
#         return
#     elif arrow == 's':
#         translation(xx, yy, 0, -50)
#         yy = yy - 50
#         return


# # ----------------------------------------------------------


# def iterate():
#     glViewport(0, 0, 500, 500)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()


# def showScreen():
#     global xx, yy
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     iterate()
#     glColor3f(1.0, 1.0, 1.0)
#     loadDigits()

#     glColor3f(0.73, 0.169, 0.183)

#     game()
#     glutKeyboardFunc(keyPressed)
#     glutSpecialFunc(specialKeyPressed)
#     glutSwapBuffers()


# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(800, 600)
# glutInitWindowPosition(0, 0)
# wind = glutCreateWindow(b"Maze Game")
# print("To Start the game PRESS r")

# glutDisplayFunc(showScreen)
# glutIdleFunc(showScreen)
# glutMainLoop()
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from objects.maze import Maze

# Initialize the maze
maze = Maze(rows=15, cols=15, cell_size=20)

def display():
    """Render the game frame."""
    glClear(GL_COLOR_BUFFER_BIT)
    maze.draw()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Rectangular Maze Test")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 800, 0, 600)  # Set up 2D projection
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
