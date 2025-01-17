import turtle
import pygame
import numpy as np
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import *

t = turtle.Turtle()

for _ in range(26):
    t.forward(100)
    t.right(90)


turtle.done()

pygame.init()

screen_width = 800
screen_height = 800
ortho_left = -400
ortho_right = 400
ortho_top = -400
ortho_bottom = 400

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Turtle")

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)

init_ortho()
done = False
glLineWidth(1)

while not done:
    #p = None
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        '''elif event.type == MOUSEBUTTONDOWN:
            p = pygame.mouse.get_pos()
            points.append((map_value(0, screen_width, ortho_left, ortho_right, p[0]),
                            map_value(0, screen_height, ortho_bottom, ortho_top, p[1])))
'''
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glBegin(GL_POINTS)
glVertex2f(0, 0)
pygame.display.flip()
#pygame.time.wait(100)

pygame.quit()


