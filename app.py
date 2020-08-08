import pygame, sys
from player import *
from dots import *
from pygame.math import Vector2 as vec
from ghost import *

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
        self.ghosts = []
        self.g_pos = []
        self.cell_width = width//28
        self.cell_height = height//30
        self.playerStart = vec()
        self.state = 1 #1=playing 0=game over
        self.load()
        self.player = Player(self, self.playerStart)
        self.dot = Dot(self, self.dots)
        self.makeEnemies()
        self.run()
        
    def run(self):
        while self.running:
            if self.state == 1:
                self.getEvents()
                self.draw()
            else:
                self.running = False
        pygame.quit()
        sys.exit()

    def getEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.move(vec(-1, 0))
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.move(vec(1, 0))
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.player.move(vec(0, -1))
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
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
                    elif char in ["2", "3", "4", "5"]:
                        self.g_pos.append(vec(xidx, yidx))
    
    def makeEnemies(self):
        for pos in self.g_pos:
            self.ghosts.append(Ghost(self, pos))

    def drawGrid(self):
        for x in range(width//self.cell_width):
            pygame.draw.line(self.background, grey, (x*self.cell_width, 0), (x*self.cell_width, height))
        for y in range(height//self.cell_height):
            pygame.draw.line(self.background, grey, (0, y*self.cell_height), (width, y*self.cell_height))
    
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        #self.drawGrid()
        self.player.draw()
        self.dot.draw()
        for ghost in self.ghosts:
            ghost.draw()
            ghost.update()
        self.player.update()
        self.clock.tick(120)
        pygame.display.update()

