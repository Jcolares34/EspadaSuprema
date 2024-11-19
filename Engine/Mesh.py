from OpenGL.GL import *
import pygame

class Mesh:
    def __init__(self):
        self.vertices = [(0.5, -0.5, 0.5),#0
                         (-0.5, -0.5, 0.5), #1
                         (0.5, 0.5, 0.5), #2
                         (-0.5, 0.5, 0.5), #3
                         (0.5, 0.5, -0.5), #4
                         (-0.5, 0.5, -0.5), #5
                         (0.5, -0.5, -0.5),  # 6
                         (-0.5, -0.5, -0.5),  # 7
                         (0.5, 0.5, 0.5),  # 8
                         (-0.5, 0.5, 0.5),  # 9
                         (0.5, 0.5, -0.5),  # 10
                         (-0.5, 0.5, -0.5),  # 11
                         (0.5, -0.5, -0.5),  # 12
                         (0.5, -0.5, 0.5),  # 13
                         (-0.5, -0.5, 0.5),  # 14
                         (-0.5, -0.5, -0.5),  # 15
                         (-0.5, -0.5, 0.5),  # 16
                         (-0.5, 0.5, 0.5),  # 17
                         (-0.5, 0.5, -0.5),  # 18
                         (-0.5, -0.5, -0.5),  # 19
                         (0.5, -0.5, -0.5),  # 20
                         (0.5, 0.5, -0.5),  # 21
                         (0.5, 0.5, 0.5),  # 22
                         (0.5, -0.5, 0.5)  # 23
                         ]
        self.triangles = [0, 2, 3, 0, 3, 1, 8, 4, 5, 8, 5, 9, 10, 6, 7, 10, 7, 11, 12,
             13, 14, 12, 14, 15, 16, 17, 18, 16, 18, 19, 20, 21, 22, 20, 22, 23]


        self.draw_type = GL_LINE_LOOP

    def draw(self):
        for t in range(0, len(self.triangles), 3):
            glBegin(self.draw_type)
            glVertex3fv(self.vertices[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            glEnd()
