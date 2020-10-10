import pygame

class View:

    def drawBackground(background, screen):
        screen.blit(background, (25, 25))

    def drawPlayerLifes(screen, lifes):
        font = pygame.font.SysFont("arial black", 15, bold=False, italic=False)
        text = font.render("Current Lifes: " + lifes, False, (255, 0, 0))
        screen.blit(text, (400, 1))

    def drawScore(screen, score):
        font = pygame.font.SysFont("arial black", 15, bold=False, italic=False)
        text = font.render("Current Score: " + score, False, (255, 0, 0))
        screen.blit(text, (1, 1))

    def drawHomeScreen(screen):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont("comicsansms", 30, bold=False, italic=False)
        text = font.render("PUSH SPACE BAR TO START", False, (255, 0, 0))
        screen.blit(text, (100, 100))
        pygame.display.update()
    
    def drawPlayer(self):
        pass

    def drawEnemies(self):
        pass

    def drawDots(self):
        pass