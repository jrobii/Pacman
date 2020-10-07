import pygame

class Wall(object):
    def __init__(self, pos):
        self.rect = pygame.Rect(int(pos.x), int(pos.y), 5, 5)