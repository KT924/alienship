#!/home/wkt/pygame/bin/python
import sys
import pygame
from bullet import Bullet
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False
        

def check_events(ai_settings,screen,ship,bullets): #检测事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:  #退出游戏事件
            sys.exit()
        elif event.type==pygame.KEYDOWN: #通过飞船类的移动标志决定飞船的移动
            #if event.key==pygame.K_RIGHT: #飞船的移动由飞船类控制，该处只需通过健的(UP,DOWN)来决定飞船是否移动
            #    ship.moving_right=True
            #elif event.key==pygame.K_LEFT:
            #    ship.moving_left=True
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            #if event.key==pygame.K_RIGHT:
            #    ship.moving_right=False
            #elif event.key==pygame.K_LEFT:
            #    ship.moving_left=False
            check_keyup_events(event,ship)
def update_screen(ai_settings,screen,ship,bullets): #刷新屏幕
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)


def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets)<ai_settings.bullets_allowed:
        new_bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
