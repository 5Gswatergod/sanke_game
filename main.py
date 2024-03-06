import pygame
import random

fps = pygame.time.Clock()

#Window Size
width = 500
length = 500

#Snake setting
sneak_speed = 20
sneak_position = [250, 250]

sneak_body = [
    [250, 250],
    [240, 250],
    [230, 250],
    [220, 250]
]

#Friut setting
fruit_position = [random.randrange(1, (width//10) * 10),
                  random.randrange(1, (length//10) * 10)]

fruit_spawn = True

#Directtions
direction = "RIGHT"
change_to = direction

#Define Color
red = pygame.color(255, 0 ,0)
black = pygame.color(0, 0, 0)
green = pygame.color(0, 255, 0)
blue = pygame.color(0, 0, 255)

#pygame init
pygame.init()

pygame.display.set_caption("Snake game")

game_window = pygame.display.set_mode(width, length)

#Score
score = 0
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score: ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def
