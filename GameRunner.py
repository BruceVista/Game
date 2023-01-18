import sys, pygame
from pygame.locals import *
from GameClasses import *
pygame.init()
run = True
while run:
    clock.tick(fps)
    screen.blit(bg, (0, 0))
    world.draw()
    player.update()

    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            run = False

  
  
    pygame.display.update()
  
pygame.quit