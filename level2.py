import sys, pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 100

screen_width = 1000
screen_height = 1000


                                                                  
screen = pygame.display.set_mode((screen_width, screen_height))                                                                  
pygame.display.set_caption('Super Pablo')                                                                  
                                                                  
tile_size = 50                                                                  
game_over = 0                                                                  
LMC = 1                                                                  
#colors                                                                   
BLACK = (0, 0, 0)                                                                  
WHITE = (255, 255, 255)                                                                  
HOVER_COLOR = (50, 70, 90)                                                                  
# font                                                                  
FONT = pygame.font.SysFont ("Times New Norman", 60)                                                                  
                                                                  
                                                                  
# text
text1 = FONT.render("START", True, WHITE)
text2 = FONT.render("MENU", True, WHITE)
text3 = FONT.render("RESTART", True, WHITE)
#rect
rect1 = pygame.Rect(400,300,205,80)
rect2 = pygame.Rect(400,300,205,80)
rect3 = pygame.Rect(300,300,205,80)
#buttons text rect and color.
button1 = [
    [text1, rect1, BLACK]]
button2 = [
    [text2, rect2, BLACK]]
button3 = [
    [text3, rect3, BLACK]]

class Player():
    def __init__(self, x, y):
        dead_img = pygame.image.load('images/dead.png')
        self.dead_img = pygame.transform.scale(dead_img,(100, 70))
        img = pygame.image.load('images/man.png')
        self.img = pygame.transform.scale(img,(70, 100))
        img_right = pygame.image.load('images/forward.png')
        self.img_right  =  pygame.transform.scale(img_right, (70, 100))
        img_left = pygame.image.load('images/backwords.png')
        self.img_left = pygame.transform.scale(img_left, (70, 100))
        win_img = pygame.image.load('images/win.png')
        self.win_img = pygame.transform.scale(win_img,(1150, 1300))
        lose_img = pygame.image.load('images/lose.png')
        self.lose_img = pygame.transform.scale(lose_img,(1150, 1300))
         
        self.image = pygame.transform.scale(img,(70, 100)) 
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False

    def update(self, game_over):
     dx = 0
     dy = 0
     if game_over == 0:
            #get keypresses
            key = pygame.key.get_pressed()
            for tile in world.tile_list:
                if key[K_w] and self.jumped == False and tile[1].colliderect(self.rect.x, self.rect.y +1, self.width, self.height):
                    self.vel_y = -18
                    self.jumped = True
            if key[K_w] == False:
                self.jumped = False
            if key[K_a]:
                dx -= 10
                self.image = self.img_left
            elif key[K_d]:
                dx += 10
                self.image = self.img_right
            else:
                self.image = self.img

            #add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y
            
            #check for collision
            for tile in world.tile_list:
                #Check X 
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                #check Y
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if below the ground
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top


                        #check if above the ground
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
            #check for collision with enemies
            if pygame.sprite.spritecollide(self, enemy_group, False):
                game_over -= 1
            #check for collision with lava
            if pygame.sprite.spritecollide(self, lava_group, False):
                game_over -= 1
            #check for collision with win
            if pygame.sprite.spritecollide(self, win_group, False):
                game_over += 1
            
            #update player position
            self.rect.x += dx
            self.rect.y += dy
        

     


        #draw player onto screen
     screen.blit(self.image, self.rect)
     
     return game_over



class World():
    def __init__(self, data):

        self.tile_list = []
        dirt_img = pygame.image.load('images/dirt.png')
        grass_img = pygame.image.load('images/gras.png')
        edge_img = pygame.image.load('images/edge.png')
        blackje_img = pygame.image.load('images/blackje.png')
        magma_img = pygame.image.load('images/magma.png')
        
        row_count = 0
        for row in data: 
            col_count = 0
            for tile in row:
                if tile == 1: 
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
    
                if tile == 2: 
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 3: 
                    img = pygame.transform.scale(edge_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                
                if tile == 4:
                    enemy = Enemy(col_count * tile_size, row_count *tile_size + 3)
                    enemy_group.add(enemy)

                
                if tile == 5:
                    lava = Lava(col_count * tile_size, row_count * tile_size)
                    lava_group.add(lava)
                
                if tile == 6:
                    win = Win(col_count * tile_size, row_count * tile_size)
                    win_group.add(win)

                if tile == 7: 
                    img = pygame.transform.scale(magma_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                    
                col_count += 1
            row_count += 1


    def draw(self):
        for tile in self.tile_list:
         screen.blit(tile[0], tile[1])    
         


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/enemy.png')
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1


class Lava(pygame.sprite.Sprite):
     def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('images/lava.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
class Win(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('images/blackje.png')
        self.image = pygame.transform.scale(img, (tile_size, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    
world_data = [
[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
[7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
[7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
[7, 0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
[7, 0, 0, 0, 0, 7, 7, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 0, 7],
[7, 7, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 0, 7],
[7, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7],
[7, 0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7],
[7, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
[7, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
[7, 7, 0, 0, 0, 7, 0, 0, 7, 7, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7],
[7, 0, 0, 0, 7, 7, 0, 0, 0, 7, 0, 0, 0, 0, 0, 7, 0, 0, 0, 7],
[7, 0, 0, 0, 0, 7, 0, 0, 0, 7, 0, 4, 4, 4, 0, 7, 6, 0, 0, 7],
[7, 7, 0, 0, 0, 7, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 7, 0, 0, 7],
[7, 0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
[7, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
[7, 0, 0, 0, 0, 7, 7, 7, 7, 0, 0, 0, 7, 0, 0, 0, 7, 7, 7, 7],
[7, 5, 7, 7, 5, 7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7],
[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],

] 

player = Player(100,screen_height-245)

enemy_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
win_group = pygame.sprite.Group()
world = World(world_data)





bg = pygame.image.load('images/level2bg.png')
run = True
menu = True
game = False
win = False
lose = False
mousedown = False

while run:
    while menu:
        screen.fill((20, 50, 70))
        for text, rect, color in button1:
            pygame.draw.rect(screen, color, rect)
            screen.blit(text, rect)
        player = Player(100,screen_height-245)
        game_over = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                run = False
            
            if event.type == pygame.MOUSEMOTION:
                for button in button1:

                    if button[1].collidepoint(event.pos):
                       button[2] = HOVER_COLOR 
                    else:
                        button[2] = BLACK
            if event.type == pygame.MOUSEBUTTONUP and event.button == LMC and button[1].collidepoint(event.pos):
                    menu = False
                    game = True
        pygame.display.update()
        clock.tick(fps)
        


    while game:
        clock.tick(fps)
        screen.blit(bg, (0, 0))
        world.draw()
        lava_group.draw(screen)
        if game_over == 0:
            enemy_group.update()
        enemy_group.draw(screen)
        win_group.draw(screen)
        game_over = player.update(game_over)
        if game_over < 0:
            player.image = player.dead_img
            game = False
            lose = True
        elif game_over > 0:
            game = False
            win = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                game = False
        pygame.display.update()
        clock.tick(fps)

    
    while win:
        screen.fill((20, 50, 70))
        for text, rect, color in button2:
            pygame.draw.rect(screen, color, rect)
            screen.blit(text, rect)
            screen.blit(player.win_img, (-75 , -100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                win = False
                run = False
            if event.type == pygame.MOUSEMOTION:
                for button in button2:
                    if button[1].collidepoint(event.pos):
                       button[2] = HOVER_COLOR
                    else:
                        button[2] = BLACK
            if event.type == pygame.MOUSEBUTTONUP and event.button == LMC and button[1].collidepoint(event.pos):
                    win = False
                    menu = True

        pygame.display.update()
        clock.tick(fps)


    while lose:
        screen.fill((20, 50, 70))
        for text, rect, color in button3:
            pygame.draw.rect(screen, color, rect)
            screen.blit(text, rect)
            screen.blit(player.lose_img, (-75 , -100))
        player = Player(100,screen_height-245)
        game_over = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lose = False
                run = False
            if event.type == pygame.MOUSEMOTION:
                for button in button3:
                    if button[1].collidepoint(event.pos):
                       button[2] = HOVER_COLOR
                    else:
                        button[2] = BLACK
            if event.type == pygame.MOUSEBUTTONUP and event.button == LMC and button[1].collidepoint(event.pos):
                    lose = False
                    game = True
        pygame.display.update()
        clock.tick(fps)
    
    pygame.display.update()
    clock.tick(fps)   

pygame.quit