import pygame
import numpy as np
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import *

pygame.init()

screen_width = 800
screen_height = 600
ortho_left = -400
ortho_right = 400
ortho_top = -400
ortho_bottom = 400

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Polygons in PyOpenGL")

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)


def plot_polygon():
    glColor(0.2, 0.2, 0.2, 1)
    glBegin(GL_TRIANGLES)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()


    glColor(0.5, 0.5, 0.5, 1)
    for i in np.arange(0, len(points) - 2, 3):
        glBegin(GL_LINE_LOOP)
        glVertex2f(points[i][0], points[i][1])
        glVertex2f(points[i+1][0], points[i+1][1])
        glVertex2f(points[i+2][0], points[i+2][1])
        glEnd()

done = False

init_ortho()
glPointSize(5)
points = []
glLineWidth(3)
while not done:
    p = None
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            p = pygame.mouse.get_pos()
            points.append((map_value(0, screen_width, ortho_left, ortho_right, p[0]),
                           map_value(0, screen_height, ortho_bottom, ortho_top, p[1])))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_polygon()
    pygame.display.flip()
    #pygame.time.wait(100)

pygame.quit()