#!/home/wkt/pygame/bin/python
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    pygame.init()  #初始化pygame
    ai_settings=Settings()  #Settings类（参数，分辨率，背景色）
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))#（设置分辨率）
    pygame.display.set_caption("Alien Invasion")    #（窗口标题）
    ship=Ship(ai_settings,screen)  #（初始化飞船）
    bullets=pygame.sprite.Group()
    bg_color=(ai_settings.bg_color)
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        #gf.check_events(ship) #（事件监听）
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        print(len(bullets))
        gf.update_screen(ai_settings,screen,ship,bullets) #（刷新屏幕）
run_game()
