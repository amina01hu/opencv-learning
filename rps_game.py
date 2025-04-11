import cv2
import math
import pygame, sys
from hand_tracking_project.hand_tracking_modules import HandDetection


pygame.init()

#CREATE GAME WINDOW

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

#game variables
game_paused = False

# define fonts
font = pygame.font.SysFont("arialblack", 30)

#define colours
TEXT_COL = (255, 255, 255)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((52, 78, 91)) # screen colour
    
    #check if game is paused
    if game_paused == True:
        pass
        #display menu
    else:
        draw_text("Press Space to Close Window", font, TEXT_COL, 160, 250)
    
    # render game here, using flip to show screen
    pygame.display.flip()
    
    clock.tick(60) #limits to 60 FPS
    
pygame.quit()
        