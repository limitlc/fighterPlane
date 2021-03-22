# -*- coding: utf-8 -*-
# @Time    : 2021/3/22 11:27
# @Author  : limitlc
# @Email   : limitlc@163.com
import pygame
from pygame.constants import *

from 飞机大战.Bullet import Bullet


class Plane(pygame.sprite.Sprite):
    # 存放所有飞机的子弹的组
    bullets = pygame.sprite.Group()
    # 飞机初始化方法
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./res/me1.png')
        self.image2 = pygame.image.load('./res/me2.png')
        # 获得图片的矩形
        self.rect = self.image.get_rect()
        self.rect.topleft = [480 / 2 - 102 / 2, 700 - 126]
        self.rect2 = self.image2.get_rect()
        self.rect2.topleft = [480 / 2 - 102 / 2, 700 - 126]
        # 飞机移动速度
        self.speed = 3
        self.screen = screen

        self.bullets = pygame.sprite.Group()
        self.isfly = True

    def key_control(self):
        keypressed = pygame.key.get_pressed()
        if keypressed[K_w] or keypressed[K_UP]:
            self.rect.top -= self.speed

        if keypressed[K_a] or keypressed[K_LEFT]:
            self.rect.left -= self.speed
        if keypressed[K_s] or keypressed[K_DOWN]:
                self.rect.bottom += self.speed
        if keypressed[K_d] or keypressed[K_RIGHT]:
                self.rect.right += self.speed
        if keypressed[K_SPACE]:
            bullet = Bullet(self.screen, self.rect.left, self.rect.top)
            self.bullets.add(bullet)
            Plane.bullets.add(bullet)


    def update(self, *args, **kwargs) -> None:
        self.key_control()
        self.display()

    def display(self):
        """显示飞机到窗口"""
        self.screen.blit(self.image, self.rect)
        # 更新子弹坐标
        self.bullets.update()

        # 把所有的子弹全部添加到屏幕
        self.bullets.draw(self.screen)

    @classmethod
    def clear_bullets(cls):
        cls.bullets.empty()