import pygame
from pygame.math import Vector2 as vec
yellow = (255, 255, 0)

class Player:
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.dir = vec(1, 0)
        self.stored_dir = None
        self.can_move = True
        
    
    def get_pix_pos(self):
        return vec((self.grid_pos.x*self.app.cell_width)+self.app.cell_width//2, 
        (self.grid_pos.y*self.app.cell_height)+self.app.cell_height//2)
        

                
    def update(self):
        if self.can_move:
            self.pix_pos += self.dir
        if self.check_legal_move():
                if self.stored_dir != None:
                    self.dir = self.stored_dir
                self.can_move = self.able_to_move()
        self.grid_pos.x = self.pix_pos.x//self.app.cell_width
        self.grid_pos.y = self.pix_pos.y//self.app.cell_height

    def check_legal_move(self):
        if int(self.pix_pos.x+self.app.cell_width//2) % self.app.cell_width == 0:
            if self.dir == vec(1, 0) or self.dir == vec(-1, 0):
                return True
        if int(self.pix_pos.y+self.app.cell_height//2) % self.app.cell_height == 0:
            if self.dir == vec(0, 1) or self.dir == vec(0, -1):
                return True
    
    def able_to_move(self):
        for wall in self.app.walls:
            if vec(self.grid_pos+self.dir) == wall:
                return False
        return True

    def draw(self):
        pygame.draw.circle(self.app.screen, yellow, (int(self.pix_pos.x),
        int(self.pix_pos.y)), self.app.cell_width//2-2)

    def move(self, dir):
        self.stored_dir = dir 