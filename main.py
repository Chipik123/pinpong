from pygame import *

window = display.set_mode((600,500 ))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed =player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] == True:
            self.rect.y = self.rect.y - self.speed
           
        if keys[K_DOWN] == True:
            self.rect.y = self.rect.y + self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] == True:
            self.rect.y = self.rect.y - self.speed
        if keys[K_s] == True:
            self.rect.y = self.rect.y + self.speed
window.fill((200,255,255))

game = True
finish = False

clock = time.Clock()
FPS = 60
