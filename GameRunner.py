import sys, pygame
from pygame.locals import *
from GameClasses import *

pygame.init()

run = True
while run:
    clock.tick(fps)
    screen.blit(bg, (0, 0))
    world.draw()
    lava_group.draw(screen)
    if game_over == 0:
        enemy_group.update()
    enemy_group.draw(screen)
    game_over = player.update(game_over)
    
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit