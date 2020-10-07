import pygame

class View:
    def drawBackground(background, screen):
        screen.blit(background, (0, 25))

    def drawPlayerLifes(background, screen):
        pass

    def drawScore():
        pass

    def drawHomeScreen(screen):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont("comicsansms", 72, bold=False, italic=False)
        text = font.render("PUSH SPACE BAR TO START", False, (255, 0, 0))
        screen.blit(text, (100, 100))
        pygame.display.update()
    
    def drawPlayer():
        pass

    def drawEnemies():
        pass

    def drawDots():
        pass