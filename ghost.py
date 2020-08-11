import pygame
import random

vec = pygame.math.Vector2

class Ghost:
    def __init__(self, app, pos):
        self.app = app
        self.gridPos = pos
        self.pix_pos = self.getPixPos()
        self.direction = vec(1, 0)
    
    def getPixPos(self):
        return vec((self.gridPos.x*self.app.cell_width)+self.app.cell_width//2, 
        (self.gridPos.y*self.app.cell_height)+self.app.cell_height//2)

    def update(self):
        self.pix_pos += self.direction
        if self.canMove():
            self.move()
        self.gridPos.x = self.pix_pos.x//self.app.cell_width
        self.gridPos.y = self.pix_pos.y//self.app.cell_height

    def draw(self):
        pygame.draw.circle(self.app.screen, (255, 0, 0), (int(self.pix_pos.x), int(self.pix_pos.y)), 8)
    
    def canMove(self):
        if int(self.pix_pos.x+self.app.cell_width//2) % self.app.cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
                return True
        if int(self.pix_pos.y+self.app.cell_height//2) % self.app.cell_height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                return True
        return False
    
    def move(self):
        self.direction = self.getRandomDirection()
    
    def getRandomDirection(self):
        while True:
            number = random.randint(-2, 1)
            if number == -2:
                xdir, ydir = 1,0
            elif number == -1:
                xdir, ydir = 0,1
            elif number == 0:
                xdir, ydir = -1,0
            else:
                xdir, ydir = 0,-1
            nextPos = vec(self.gridPos.x + xdir, self.gridPos.y + ydir)
            if nextPos not in self.app.walls:
                break 
        return vec(xdir, ydir)