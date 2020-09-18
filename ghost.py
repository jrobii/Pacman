import pygame
import random
from item import Item
vec = pygame.math.Vector2

class Ghost(Item):
    def __init__(self, app, pos):
        super().__init__(app, pos)

    def update(self):
        self.pixPos += self.dir
        if self.checkLegalMove():
            self.move()
        self.setGridPos()

    def draw(self):
        pygame.draw.circle(self.app.screen, (255, 0, 0), (int(self.pixPos.x), int(self.pixPos.y)), 8)
    
    def move(self):
        self.dir = self.getRandomDirection()
    
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