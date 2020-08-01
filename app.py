import pygame, sys

width = 600
height = 600

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))
        self.running = True

    def run(self):
        while self.running:
            ##
        pygame.quit()
        sys.exit()
    
    def get_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

