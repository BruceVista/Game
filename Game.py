import sys, pygame
pygame.init
white = (255,255,255)
Screen = pygame.display.set_mode((800, 600))

bg_img = pygame.image.load('images/bg.png')
bg_img = pygame.transform.scale(bg_img,(800,600))
Screen.blit(bg_img,(0, 0))
while True:
    Screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         pygame.quit()
   
    pygame.display.update

