import pygame, sys

pygame.init()
width = 560
height = 620
cell_width = width//28
cell_height = height//30
grey = (107, 107, 107)

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))
        self.running = True
        self.load()
        self.state = 1 #1=playing 0=game over
        

    def run(self):
        while self.running:
            if self.state == 1:
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

    def draw_grid(self):
        for x in range(width//cell_width):
            pygame.draw.line(self.screen, grey, (x*cell_width, 0), (x*cell_width, height))
        for y in range(height//cell_height):
            pygame.draw.line(self.screen, grey, (0, y*cell_height), (width, y*cell_height))
    
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.draw_grid()
        pygame.display.update()

