
import time
import pygame


# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 16:31
# @Author  : limitlc
# @Email   : limitlc@163.com
from pygame import *


def main():
    screen = pygame.display.set_mode((480, 700), 0, 32)
    background = pygame.image.load("./res/background.png")

    hero = pygame.image.load('./res/me1.png')

    heroY = 700 - 126
    heroX = 480 / 2 - 102 / 2

    herospeed = 1
    while True:
        screen.blit(background, (0, 0))
        screen.blit(hero, (heroX, heroY))
        for event in   pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keypressed = pygame.key.get_pressed()
        if keypressed[K_w] or keypressed[K_UP]:
            print("上")
            heroY -= herospeed
        if keypressed[K_a] or keypressed[K_LEFT]:
            print("左")
            heroX -= herospeed
        if keypressed[K_s] or keypressed[K_DOWN]:
            print("下")
            heroY += herospeed
        if keypressed[K_d] or keypressed[K_RIGHT]:
            print("右")
            heroX += herospeed
        if keypressed[K_SPACE]:
            print("发射子弹")


        pygame.display.update()
        # time.sleep(0.01)

if __name__ == '__main__':
    main()
