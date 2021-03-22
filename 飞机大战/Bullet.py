# -*- coding: utf-8 -*-
# @Time    : 2021/3/22 11:29
# @Author  : limitlc
# @Email   : limitlc@163.com

import pygame


class Bullet(pygame.sprite.Sprite):

    # 构造方法中传输的是飞机所在的坐标
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./res/bullet2.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [x + 102 / 2 - 6 / 2,y - 12 / 2]
        # # 坐标
        # self.x = x + 102 / 2 - 6 / 2
        # self.y = y - 12 / 2

        self.screen = screen
        self.speed = 10

    def update(self, *args, **kwargs) -> None:
        self.rect.top -= self.speed
        if self.rect.top < -11:
            self.kill()

