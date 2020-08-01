import pygame, sys

pygame.init()
width = 560
height = 620

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))
        self.running = True
        self.load()
        self.state = 1 #1=playing 0=game over
        

    def run(self):
        while self.running:
            if self.state = 1:
                self.draw()
            else:
                self.running = False
        pygame.quit()
        sys.exit()
    
    def get_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def load(self):
        self.background = pygame.image.load('maze.png')
        self.background = pygame.transform.scale(self.background, (width, height))
    
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.update()

