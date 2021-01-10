# Simple pygame program

# Import and initialize the pygame library
import pygame
import random
import time

pygame.init()
# set clock and font for FPS display
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 40)
# function of printing FPS on screen
def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("red"))
    return fps_text

# Set up the drawing window
screen = pygame.display.set_mode([320, 240])

# Run until the user asks to quit
running = True
# define dots colors
black = (0,0,0)
white = (255,255,255)
color_list=[black,white]

while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(0,321):
        for j in range(0,241):
            # random color for each pixel
            is_black = color_list[random.randint(0,1)]
            pygame.draw.circle(screen, is_black, (i, j),1)

    screen.blit(update_fps(), (10,0))
    clock.tick(100)
    pygame.display.update()
    # # Flip the display
    # pygame.display.flip()

    # update image every second
    # time.sleep(1)

# Done! Time to quit.
pygame.quit()