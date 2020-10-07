import pygame
from item import Item
from pygame.math import Vector2 as vec
import wall
yellow = (255, 255, 0)

class Player(Item):
    def __init__(self, app, pos):
        super().__init__(app, pos)
        self.dir = vec(0, -1)
        self.stored_dir = None
        self.can_move = True
        self.lifes = 3

    def getLifes(self):
        return self.lifes
              
    def update(self):
        if self.checkLegalMove():
            if self.stored_dir != None:
                self.dir = self.stored_dir
            if self.able_to_move == False:
                self.stored_dir = None
            else:
                self.can_move = self.able_to_move()
        if self.can_move:
            self.pixPos += self.dir
        self.setGridPos()
        self.removeDot()
        
    def removeDot(self):
        if self.gridPos in self.app.dots:
            self.app.dots.remove(self.gridPos)

    def able_to_move(self):
        for wall in self.app.walls:
            if vec(self.gridPos + self.dir) == vec(wall):
                return False
        return True

    def draw(self):
        pygame.draw.circle(self.app.screen, yellow, (int(self.pixPos.x), int(self.pixPos.y)), self.app.cell_height//2)

    def move(self, dir):
        self.stored_dir = dir 