import sys, pygame
pygame.init()
CharX = 0
CharY = 0
character = pygame.image.load('images\character.png')
character_rect = character.get_rect(center=(CharX, CharY))
print(character_rect)