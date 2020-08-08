import pygame

vec = pygame.math.Vector2

class Ghost:
    def __init__(self, app, pos):
        self.app = app
        self.gridPos = pos
        self.pix_pos = self.getPixPos()
    
    def getPixPos(self):
        return vec((self.gridPos.x*self.app.cell_width)+self.app.cell_width//2, 
        (self.gridPos.y*self.app.cell_height)+self.app.cell_height//2)

    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(self.app.screen, (255, 0, 0), (int(self.pix_pos.x), int(self.pix_pos.y)), 8)