import pygame, sys
from player import *
from dots import *
from pygame.math import Vector2 as vec

pygame.init()
pygame.display.set_caption("Pac-Man")
width = 560
height = 620
grey = (107, 107, 107)

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.walls = []
        self.dots = []
        self.cell_width = width//28
        self.cell_height = height//30
        self.playerStart = vec()
        self.state = 1 #1=playing 0=game over
        self.load()
        self.player = Player(self, self.playerStart)
        self.dot = Dot(self, self.dots)
        self.run()
        
    def run(self):
        while self.running:
            if self.state == 1:
                self.get_events()
                self.draw()
            else:
                self.running = False
        pygame.quit()
        sys.exit()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1, 0))
                if event.key == pygame.K_RIGHT:
                    self.player.move(vec(1, 0))
                if event.key == pygame.K_UP:
                    self.player.move(vec(0, -1))
                if event.key == pygame.K_DOWN:
                    self.player.move(vec(0, 1))
    
    def load(self):
        self.background = pygame.image.load('maze.png')
        self.background = pygame.transform.scale(self.background, (width, height))
        
        with open("maze_info.txt", "r") as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xidx, yidx))
                    elif char == "C":
                        self.dots.append(vec(xidx, yidx))
                    elif char == "P":
                        self.playerStart = vec(xidx, yidx)
    

    def draw_grid(self):
        for x in range(width//self.cell_width):
            pygame.draw.line(self.background, grey, (x*self.cell_width, 0), (x*self.cell_width, height))
        for y in range(height//self.cell_height):
            pygame.draw.line(self.background, grey, (0, y*self.cell_height), (width, y*self.cell_height))
    
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.draw_grid()
        self.player.draw()
        self.dot.draw()
        self.player.update()
        self.clock.tick(120)
        pygame.display.update()

