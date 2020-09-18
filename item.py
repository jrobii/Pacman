import pygame
from pygame.math import Vector2 as vec

class Item:
    def __init__(self, app, pos):
        self.app = app
        self.gridPos = pos
        self.pixPos = self.getPixPos()
        self.dir = vec(1, 0)

    def getPixPos(self):
        return vec((self.gridPos.x*self.app.cell_width)+self.app.cell_width//2, 
        (self.gridPos.y*self.app.cell_height)+self.app.cell_height//2)

    def checkLegalMove(self):
        if int(self.pixPos.x+self.app.cell_width//2) % self.app.cell_width == 0:
            if self.dir == vec(1, 0) or self.dir == vec(-1, 0):
                return True
        if int(self.pixPos.y+self.app.cell_height//2) % self.app.cell_height == 0:
            if self.dir == vec(0, 1) or self.dir == vec(0, -1):
                return True
        
    def setGridPos(self):
        self.gridPos.x = self.pixPos.x//self.app.cell_width
        self.gridPos.y = self.pixPos.y//self.app.cell_height