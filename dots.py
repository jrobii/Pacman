from player import *
import pygame

class Dot:
    def __init__(self, app, dots):
        self.app = app
        self.dots = dots
        
    
    def draw(self):
        for dot in self.dots:
            pygame.draw.circle(self.app.screen, (255, 255, 255), (int(dot.x*self.app.cell_width)
            +self.app.cell_width//2, int(dot.y*self.app.cell_height)+self.app.cell_height//2), 3)