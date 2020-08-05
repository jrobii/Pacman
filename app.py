import pygame, sys
from player import *
from pygame.math import Vector2 as vec

pygame.init()
width = 560
height = 620
grey = (107, 107, 107)

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))
        self.running = True
        self.load()
        self.cell_width = width//28
        self.cell_height = height//30
        self.state = 1 #1=playing 0=game over
        self.player = Player(self, vec(1, 1))
        self.run()
        
        

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            if self.state == 1:
                self.draw()
            else:
                self.running = False
        pygame.quit()
        sys.exit()
    
    def get_event(self):
        pass
    
    def load(self):
        self.background = pygame.image.load('maze.png')
        self.background = pygame.transform.scale(self.background, (width, height))

    def draw_grid(self):
        for x in range(width//self.cell_width):
            pygame.draw.line(self.background, grey, (x*self.cell_width, 0), (x*self.cell_width, height))
        for y in range(height//self.cell_height):
            pygame.draw.line(self.background, grey, (0, y*self.cell_height), (width, y*self.cell_height))
    
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.draw_grid()
        self.player.draw()
        pygame.display.update()

