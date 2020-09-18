import pygame, sys
from player import *
from dots import *
from pygame.math import Vector2 as vec
from ghost import *
from view import *
from item import Item

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
        self.state = 0 #0=start 1=playing 2=game over
        self.load()
        self.player = Player(self, self.playerStart)
        self.playerLives = self.player.getLifes()
        self.dot = Dot(self, self.dots)
        self.view = View
        self.makeEnemies()
        self.run()
        
    def run(self):
        while self.running:
            if self.state == 0:
                self.getStartEvents()
                self.view.drawHomeScreen(self.screen)
            elif self.state == 1:
                self.getEvents()
                self.draw()
            elif self.state == 2:
                pass
            else:
                self.running = False
        pygame.quit()
        sys.exit()

    def getStartEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = 1

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
        self.background = pygame.transform.scale(self.background, (width, height-50))
        
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
                    elif char == "B":
                        pygame.draw.rect(self.background, (0, 0, 0), (xidx*self.cell_width, yidx*self.cell_height,
                        self.cell_width, self.cell_height))
    
    def makeEnemies(self):
        for pos in self.g_pos:
            self.ghosts.append(Ghost(self, pos))

    def drawGrid(self):
        for x in range(width//self.cell_width):
            pygame.draw.line(self.background, grey, (x*self.cell_width, 0), (x*self.cell_width, height))
        for y in range(height//self.cell_height):
            pygame.draw.line(self.background, grey, (0, y*self.cell_height), (width, y*self.cell_height))
    
    def draw(self):
        self.view.drawBackground(self.background, self.screen)
        self.view.drawPlayerLifes(self.background, self.screen)
        #self.drawGrid()
        self.player.draw()
        self.dot.draw()
        for ghost in self.ghosts:
            ghost.draw()
            ghost.update()
        self.player.update()
        self.clock.tick(120)
        pygame.display.update()

