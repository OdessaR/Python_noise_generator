# Simple pygame program

# Import and initialize the pygame library
import pygame
import random
import time
from PIL import Image, ImageTk

pygame.init()
# set clock for FPS display
clock = pygame.time.Clock()
# set font and font size
font = pygame.font.SysFont("Arial", 20)

# function of printing FPS on screen
def update_fps():
    # show FPS with 2 decimal (rounded)
    fps = str(format(clock.get_fps(),'.2f'))
    fps_text = "Current FPS: "+ fps
    return fps_text

# Set up the drawing window 
size= (320, 240)
screen = pygame.display.set_mode(size)
img = Image.new("RGB",size)
# Run until the user asks to quit
running = True
# define dots colors
black = (0,0,0)
white = (255,255,255)
# random number between 0-1
rnd = random.random
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    npixels = size[0] * size[1]
    data = [white if rnd() > 0.5 else black for i in range(0,npixels)]
    img.putdata(data)
    screen.blit(pygame.image.fromstring(img.tobytes(), size, img.mode), (0,0))
    
    # print fps on screen
    fps = font.render(update_fps(),1,"red")

    screen.blit(fps, (10,0))
    clock.tick(100)
    pygame.display.update()
    # # Flip the display
    # pygame.display.flip()

    # update image every second
    # time.sleep(1)

# Done! Time to quit.
pygame.quit()