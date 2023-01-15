import sys, pygame
pygame.init



#Screen
red = (255,0 ,0)
white = (255, 255, 255)
Screen = pygame.display.set_mode((800, 600))
bg = pygame.image.load('images/bg.png')
bg = pygame.transform.scale(bg, (800, 600))

#Platform and floor
Floor = pygame.image.load('images/platform.png')
Floor = pygame.transform.scale(Floor,(1000, 200))
P1X = 300
P1Y = 350
Platform1 = pygame.image.load('images/platform.png')
Platform1 = pygame.transform.scale(Platform1,(100, 20))
collision = False
#character
Jumping = False

Move_Speed = 10
Y_Gravity = 1
Jump_Height = 18
Y_Velocity = Jump_Height

PlatformCollision = P1Y - Jump_Height

character = pygame.image.load('images/character.png')
character = pygame.transform.scale(character, (100, 100))
character_jumping = pygame.image.load('images/Character.png')
character_jumping = pygame.transform.scale(character_jumping, (100, 100))
CharX = 350
CharY = 450
character_rect = character.get_rect(center=(CharX, CharY))


running = True
while running:
    Screen.fill(white)
    Screen.blit(bg ,(0, 0))
    Screen.blit(Floor,(-100, 500))
    Screen.blit(Platform1,(P1X, P1Y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         running = False
    
    #Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        P1X += Move_Speed
    if keys[pygame.K_d]:
        P1X -= Move_Speed


    #jump
    if keys[pygame.K_w]:
        Jumping = True
    
    if Jumping == True:
        CharY -= Y_Velocity
        Y_Velocity -= Y_Gravity
        if Y_Velocity < -Jump_Height:
             Jumping = False
             Y_Velocity = Jump_Height
        character_rect = character.get_rect(center=(CharX, CharY))
        Screen.blit(character_jumping, character_rect)
    else: 
        character_rect = character.get_rect(center=(CharX, CharY))
        Screen.blit(character, character_rect)
    


    #collision
    P1Col = pygame.draw.rect(Screen, red, pygame.Rect(P1X, P1Y, 100, 20),2) 
    CharCol = pygame.draw.rect(Screen, red, pygame.Rect(CharX-30, CharY-10, 60, 100),2)
    collide = pygame.Rect.colliderect(CharCol, P1Col)
    if collide:
        collision = True
    else:
        collision = False
    while CharX >= P1X and CharX <= P1X+100 and collision == True:
            #jump
        if keys[pygame.K_w]:
         Jumping = True
    
        if Jumping == True:
         CharY -= Y_Velocity
         Y_Velocity -= Y_Gravity
         if Y_Velocity < -Jump_Height:
             Jumping = False
             Y_Velocity = Jump_Height
             character_rect = character.get_rect(center=(CharX, CharY))
             Screen.blit(character_jumping, character_rect)
        else: 
         character_rect = character.get_rect(center=(CharX, CharY))
         Screen.blit(character, character_rect)
        #collision
        P1Col = pygame.draw.rect(Screen, red, pygame.Rect(P1X, P1Y, 100, 20),2) 
        CharCol = pygame.draw.rect(Screen, red, pygame.Rect(CharX-30, CharY-50, 60, 100),2)
        collide = pygame.Rect.colliderect(CharCol, P1Col)
        CharY = P1Y-50
        if not CharX >= P1X and CharX <= P1X+100 and collision == True:
            collision = False
        CharY = P1Y-50

        pygame.display.update()
        pygame.time.Clock().tick(60)
    #Exit Collision loop
   
    pygame.display.update()
    pygame.time.Clock().tick(60)
pygame.quit
