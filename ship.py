#!/home/wkt/pygame/bin/python
import pygame
class Ship(): #飞船类
    def __init__(self,ai_settings,screen):
        self.screen=screen #获得当前屏幕的surface对象　
        self.image=pygame.image.load('images/ship.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.center=float(self.rect.centerx) #centerx不能存储浮点数，所以使用
        self.moving_right=False
        self.moving_left=False
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #self.rect.centerx +=1
            self.center+=self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            #self.rect.centerx -=1
            self.center-=self.ai_settings.ship_speed_factor
        self.rect.centerx=self.center
