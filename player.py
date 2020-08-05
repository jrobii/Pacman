import pygame
from pygame.math import Vector2 as vec
yellow = (255, 255, 0)
class Player:
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = vec((self.grid_pos.x*app.cell_width)+self.app.cell_width//2, 
        (self.grid_pos.y*app.cell_height)+self.app.cell_height//2)
        print(self.grid_pos, self.pix_pos)
    
    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(self.app.screen, yellow, (int(self.pix_pos.x),
        int(self.pix_pos.y)), self.app.cell_width//2-2)
