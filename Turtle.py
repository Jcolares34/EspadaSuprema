import turtle
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import *
import numpy as np
import math

pygame.init()

screen_width = 800
screen_height = 800
ortho_left = -400
ortho_right = 400
ortho_top = -400
ortho_bottom = 400

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Turtle")


current_position = (0, 0)
direction = np.array([0, 1, 0])
draw_length = 50

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)

def line_to(x,y):
    global current_position
    glBegin(GL_LINE_STRIP)
    glVertex2f(current_position[0], current_position[1])
    glVertex2f(x, y)
    current_position = (x, y)
    glEnd()

def reset_turtle():
    global current_position
    global direction
    current_position = (0, 0)
    direction = np.array([0, 1, 0])

def draw_turtle():
    forward()
    rotate(90)
    forward()

def forward():
    new_x = current_position[0] + direction[0] * draw_length
    new_y = current_position[1] + direction[1] * draw_length
    line_to(new_x, new_y)

def rotate(angle):
    global direction
    direction = z_rotation(direction, math.radians(angle))




init_ortho()
done = False
glLineWidth(5)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
    glVertex2f(0,0)
    glEnd()
    reset_turtle()
    draw_turtle()
    line_to(100, 100)
    line_to(100, 200)

    pygame.display.flip()
    # pygame.time.wait(100)
pygame.quit()
