import sys, pygame
from pygame.locals import *
import time

pygame.init()

clock = pygame.time.Clock()
fps = 100

screen_width = 1000
screen_height = 1000


                                                                  
screen = pygame.display.set_mode((screen_width, screen_height))                                                                  
pygame.display.set_caption('Super Pablo')                                                                  
                                                                  
tile_size = 50                                                                  
game_over = 0  
coins = 0                                       
LMC = 1                                                                  
#colors                                                                   
BLACK = (0, 0, 0)                                                                  
WHITE = (255, 255, 255)                                                                  
HOVER_COLOR = (50, 70, 90)                                                                  
# font                                                                  
FONT = pygame.font.SysFont ("Times New Norman", 60)                                                                  



level1 = pygame.image.load('images/level1.png')

level2 = pygame.image.load('images/level2.png')

level3 = pygame.image.load('images/level3.png')

class Button(): 
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width* scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        #mouse over and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))                                                               
        return action                                                          
# text

text2 = FONT.render("MENU", True, WHITE)
text3 = FONT.render("RESTART", True, WHITE)

#rect

rect2 = pygame.Rect(400,300,205,80)
rect3 = pygame.Rect(300,300,205,80)
#buttons text rect and color.

button2 = [
    [text2, rect2, BLACK]]
button3 = [
    [text3, rect3, BLACK]]

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img,(x, y))


class Player1():
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
            for tile in world1.tile_list:
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
            for tile in world1.tile_list:
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
            if pygame.sprite.spritecollide(self, enemy_group1, False):
                game_over -= 1
            #check for collision with lava
            if pygame.sprite.spritecollide(self, lava_group1, False):
                game_over -= 1
            #check for collision with win
            if pygame.sprite.spritecollide(self, win_group1, False):
                game_over += 1
            
            #update player position
            self.rect.x += dx
            self.rect.y += dy
        

     


        #draw player onto screen
     screen.blit(self.image, self.rect)
     
     return game_over

class Player2():
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
            for tile in world2.tile_list:
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
            for tile in world2.tile_list:
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
            if pygame.sprite.spritecollide(self, enemy_group2, False):
                game_over -= 1
            #check for collision with lava
            if pygame.sprite.spritecollide(self, lava_group2, False):
                game_over -= 1
            #check for collision with win
            if pygame.sprite.spritecollide(self, win_group2, False):
                game_over += 1
            
            #update player position
            self.rect.x += dx
            self.rect.y += dy
        
            #draw player onto screen
            screen.blit(self.image, self.rect)
     
            return game_over
        

class Player3():
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
            for tile in world3.tile_list:
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
            for tile in world3.tile_list:
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
            if pygame.sprite.spritecollide(self, enemy_group3, False):
                game_over -= 1
            #check for collision with lava
            if pygame.sprite.spritecollide(self, lava_group3, False):
                game_over -= 1
            #check for collision with win
            if pygame.sprite.spritecollide(self, win_group3, False):
                game_over += 1
            
            #update player position
            self.rect.x += dx
            self.rect.y += dy
        

     


        #draw player onto screen
     screen.blit(self.image, self.rect)
     
     return game_over




class World1():
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
                    enemy = Enemy1(col_count * tile_size, row_count *tile_size + 3)
                    enemy_group1.add(enemy)

                
                if tile == 5:
                    lava = Lava1(col_count * tile_size, row_count * tile_size)
                    lava_group1.add(lava)
                
                if tile == 6:
                    win = Win1(col_count * tile_size, row_count * tile_size)
                    win_group1.add(win)

                if tile == 7:
                    coin = Coin1(col_count * tile_size, row_count * tile_size)
                    coin_group1.add(coin)
                
                if tile == 8: 
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

class World2():
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
                    enemy = Enemy2(col_count * tile_size, row_count *tile_size + 3)
                    enemy_group2.add(enemy)

                
                if tile == 5:
                    lava = Lava2(col_count * tile_size, row_count * tile_size)
                    lava_group2.add(lava)
                
                if tile == 6:
                    win = Win2(col_count * tile_size, row_count * tile_size)
                    win_group2.add(win)

                if tile == 7:
                    coin = Coin2(col_count * tile_size, row_count * tile_size)
                    coin_group2.add(coin)
                
                if tile == 8: 
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

class World3():
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
                    enemy = Enemy3(col_count * tile_size, row_count *tile_size + 3)
                    enemy_group3.add(enemy)

                
                if tile == 5:
                    lava = Lava3(col_count * tile_size, row_count * tile_size)
                    lava_group3.add(lava)
                
                if tile == 6:
                    win = Win3(col_count * tile_size, row_count * tile_size)
                    win_group3.add(win)

                if tile == 7:
                    coin = Coin3(col_count * tile_size, row_count * tile_size)
                    coin_group3.add(coin)
                
                if tile == 8: 
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
      
         


class Enemy1(pygame.sprite.Sprite):
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


class Lava1(pygame.sprite.Sprite):
     def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('images/lava.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
class Win1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('images/blackje.png')
        self.image = pygame.transform.scale(img, (tile_size, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Coin1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('images/man.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Enemy2(pygame.sprite.Sprite):
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


class Lava2(pygame.sprite.Sprite):
     def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('images/lava.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
class Win2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('images/blackje.png')
        self.image = pygame.transform.scale(img, (tile_size, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Coin2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('images/man.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Enemy3(pygame.sprite.Sprite):
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


class Lava3(pygame.sprite.Sprite):
     def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('images/lava.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
class Win3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('images/blackje.png')
        self.image = pygame.transform.scale(img, (tile_size, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Coin3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('images/man.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
world_data1 = [
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 6, 3],
[3, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 2, 2, 2, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3],
[3, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 3],
[2, 2, 2, 2, 2, 2, 5, 5, 5, 2, 5, 5, 5, 2, 2, 2, 1, 2, 2, 2],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

] 
world_data2 = [
[8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
[8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
[8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
[8, 0, 0, 0, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
[8, 0, 0, 0, 0, 8, 8, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 0, 8],
[8, 8, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 0, 0, 8],
[8, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 8],
[8, 0, 0, 0, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 8],
[8, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
[8, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
[8, 8, 0, 0, 0, 8, 0, 0, 8, 8, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8],
[8, 0, 0, 0, 8, 8, 0, 0, 0, 8, 0, 0, 0, 0, 0, 8, 0, 0, 0, 8],
[8, 0, 0, 0, 0, 8, 0, 0, 0, 8, 0, 4, 4, 4, 0, 8, 6, 0, 7, 8],
[8, 8, 0, 0, 0, 8, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 0, 0, 8],
[8, 0, 0, 0, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
[8, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
[8, 0, 0, 0, 0, 8, 8, 8, 8, 0, 0, 0, 8, 0, 0, 0, 8, 8, 8, 8],
[8, 5, 8, 8, 5, 8, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 8],
[8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
[8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],

] 
world_data3 = [
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 7, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 6, 6, 3],
[3, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 2, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 1, 0, 4, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 2, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2, 2, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3],
[3, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 3],
[2, 2, 2, 2, 2, 2, 5, 5, 2, 5, 5, 5, 5, 2, 2, 2, 1, 2, 2, 2],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

] 
player1 = Player1(100,screen_height-245)
player2 = Player2(100,screen_height-245)
player3 = Player3(100,screen_height-245)

enemy_group1 = pygame.sprite.Group()
lava_group1 = pygame.sprite.Group()
win_group1 = pygame.sprite.Group()
coin_group1 = pygame.sprite.Group()
enemy_group2 = pygame.sprite.Group()
lava_group2 = pygame.sprite.Group()
win_group2 = pygame.sprite.Group()
coin_group2 = pygame.sprite.Group()
enemy_group3 = pygame.sprite.Group()
lava_group3 = pygame.sprite.Group()
win_group3 = pygame.sprite.Group()
coin_group3 = pygame.sprite.Group()
world1 = World1(world_data1)
world2 = World2(world_data2)
world3 = World3(world_data3)
level1_button = Button(300, 100, level1, 1)
level2_button = Button(300, 350, level2, 1)
level3_button = Button(300, 600, level3, 1)





bg2 = pygame.image.load('images/level2bg.png')
bg = pygame.image.load('images/bg.png')
run = True
menu = True
game1 = False
game2 = False
game3 = False
win = False
lose1 = False
lose2 = False
lose3 = False
mousedown = False

while run:
    while menu:
        
        start_time = time.time()
        screen.fill((20, 50, 70))
        game_over = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                run = False
            
            
        if level1_button.draw():
            game1 = True
            menu = False
            
        if level2_button.draw():
            game2 = True
            menu = False
             
        if level3_button.draw():
            game3 = True
            menu = False
            
        draw_text("Coins: " + str(coins), FONT, WHITE, tile_size - 10, 30)    
        pygame.display.update()
        clock.tick(fps)
        


    while game1:
        end_time = time.time()
        TimeScore = end_time - start_time
        TimeScore = '{:.3f}'.format(TimeScore)
        
        text4 = FONT.render(TimeScore, True, WHITE)
        textRect = text4.get_rect()
        textRect.center = (600, 30)
        clock.tick(fps)
        screen.blit(bg, (0, 0))
        world1.draw()
        lava_group1.draw(screen)
        game_over = player1.update(game_over)
        
        if game_over == 0:
            enemy_group1.update()
            #check for collision with coin
            if pygame.sprite.spritecollide(player1, coin_group1, True):
                coins += 1
            draw_text("Coins: " + str(coins), FONT, WHITE, tile_size - 10, 30)    
        enemy_group1.draw(screen)
        win_group1.draw(screen)
        coin_group1.draw(screen)
       
        
        if game_over < 0:
            player1 = Player1(100,screen_height-245)
            player1.image = player1.dead_img
            game1 = False
            lose1 = True
        elif game_over > 0:
            player1 = Player1(100,screen_height-245)
            game1 = False
            win = True
            coins_collected = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                game1 = False
        screen.blit(text4, textRect)
        pygame.display.update()
        clock.tick(fps)


    while game2:
        end_time = time.time()
        TimeScore = end_time - start_time
        TimeScore = '{:.3f}'.format(TimeScore)
        
        text4 = FONT.render(TimeScore, True, WHITE)
        textRect = text4.get_rect()
        textRect.center = (600, 30)
        clock.tick(fps)
        screen.blit(bg2, (0, 0))
        world2.draw()
        lava_group2.draw(screen)
        game_over = player2.update(game_over)

        if game_over == 0:
            enemy_group2.update()
            #check for collision with coin
            if pygame.sprite.spritecollide(player2, coin_group2, True):
                coins += 1
            draw_text("Coins: " + str(coins), FONT, WHITE, tile_size - 10, 30)    
        enemy_group2.draw(screen)
        win_group2.draw(screen)
        coin_group2.draw(screen)
        
        
        if game_over < 0:
            player2 = Player2(100,screen_height-245)
            player2.image = player2.dead_img
            game2 = False
            lose2 = True
        elif game_over > 0:
            player2 = Player2(100,screen_height-245)
            game2 = False
            win = True
            coins_collected = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                game2 = False
        screen.blit(text4, textRect)
        pygame.display.update()
        clock.tick(fps)
    

    while game3:
        end_time = time.time()
        TimeScore = end_time - start_time
        TimeScore = '{:.3f}'.format(TimeScore)
        
        text4 = FONT.render(TimeScore, True, WHITE)
        textRect = text4.get_rect()
        textRect.center = (600, 30)
        clock.tick(fps)
        screen.blit(bg, (0, 0))
        world3.draw()
        lava_group3.draw(screen)
        game_over = player3.update(game_over)
        if game_over == 0:
            enemy_group3.update()
            #check for collision with coin
            if pygame.sprite.spritecollide(player3, coin_group3, True):
                coins += 1
            draw_text("Coins: " + str(coins), FONT, WHITE, tile_size - 10, 30)    
        enemy_group3.draw(screen)
        win_group3.draw(screen)
        coin_group3.draw(screen)
        
        
        if game_over < 0:
            player3 = Player3(100,screen_height-245)
            player3.image = player3.dead_img
            game3 = False
            lose3 = True
        elif game_over > 0:
            player3 = Player3(100,screen_height-245)
            game3 = False
            win = True
            coins_collected = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                game3 = False
        screen.blit(text4, textRect)
        pygame.display.update()
        clock.tick(fps)


    while win:
    
        screen.fill((20, 50, 70))
        for text, rect, color in button2:
            pygame.draw.rect(screen, color, rect)
            screen.blit(text, rect)
            screen.blit(player1.win_img, (-75 , -100))
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
        draw_text("Coins: " + str(coins), FONT, WHITE, tile_size - 10, 30)    
        screen.blit(text4, textRect)
        pygame.display.update()
        clock.tick(fps)


    while lose1:
        
        start_time = time.time()
        screen.fill((20, 50, 70))
        for text, rect, color in button3:
            pygame.draw.rect(screen, color, rect)
            screen.blit(text, rect)
            screen.blit(player1.lose_img, (-75 , -100))
        player1 = Player1(100,screen_height-245)
        game_over = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lose1 = False
                run = False
            if event.type == pygame.MOUSEMOTION:
                for button in button3:
                    if button[1].collidepoint(event.pos):
                       button[2] = HOVER_COLOR
                    else:
                        button[2] = BLACK
            if event.type == pygame.MOUSEBUTTONUP and event.button == LMC and button[1].collidepoint(event.pos):
                    game1 = True
                    lose1 = False
        pygame.display.update()
        clock.tick(fps)
        
    pygame.display.update()
    clock.tick(fps)   



    while lose2:
        
        start_time = time.time()
        screen.fill((20, 50, 70))
        for text, rect, color in button3:
            pygame.draw.rect(screen, color, rect)
            screen.blit(text, rect)
            screen.blit(player2.lose_img, (-75 , -100))
        player2 = Player2(100,screen_height-245)
        game_over = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lose2 = False
                run = False
            if event.type == pygame.MOUSEMOTION:
                for button in button3:
                    if button[1].collidepoint(event.pos):
                       button[2] = HOVER_COLOR
                    else:
                        button[2] = BLACK
            if event.type == pygame.MOUSEBUTTONUP and event.button == LMC and button[1].collidepoint(event.pos):
                    game2 = True
                    lose2 = False
                   
        
        pygame.display.update()
        clock.tick(fps)
        
    pygame.display.update()
    clock.tick(fps)   



    while lose3:
        
        start_time = time.time()
        screen.fill((20, 50, 70))
        for text, rect, color in button3:
            pygame.draw.rect(screen, color, rect)
            screen.blit(text, rect)
            screen.blit(player3.lose_img, (-75 , -100))
        player3 = Player3(100,screen_height-245)
        game_over = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lose3 = False
                run = False
            if event.type == pygame.MOUSEMOTION:
                for button in button3:
                    if button[1].collidepoint(event.pos):
                       button[2] = HOVER_COLOR
                    else:
                        button[2] = BLACK
            if event.type == pygame.MOUSEBUTTONUP and event.button == LMC and button[1].collidepoint(event.pos):
                    game3 = True
                    lose3 = False
                    
        
        pygame.display.update()
        clock.tick(fps)
        
    pygame.display.update()
    clock.tick(fps)   
pygame.quit
