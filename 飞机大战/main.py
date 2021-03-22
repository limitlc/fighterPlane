import time
import random
import pygame
# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 16:31
# @Author  : limitlc
# @Email   : limitlc@163.com
from pygame.constants import *

from 飞机大战.Diren import Diren
from 飞机大战.Plane import Plane





def main():
    screen = pygame.display.set_mode((480, 700), 0, 32)
    background = pygame.image.load("./res/background.png")
    hero = Plane(screen)
    screen.blit(background, (0, 0))
    direns = []
    while True:
        screen.blit(background, (0, 0))
        if 8 == random.randint(0, 50):
            direns.append(Diren(screen))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        hero.key_control()
        hero.display()
        for diren in direns:
            diren.display()
            diren.auto_move()
        pygame.display.update()
        time.sleep(0.01)
if __name__ == '__main__':
    main()
