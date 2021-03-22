# -*- coding: utf-8 -*-
# @Time    : 2021/3/22 11:31
# @Author  : limitlc
# @Email   : limitlc@163.com
import random
import pygame

from 飞机大战.direnbullet import DiRenBullet


class Diren:

    # 飞机初始化方法
    def __init__(self, screen):
        # 飞机所在位置的纵坐标以左上角为0，0

        self.y = 0
        # 飞机所在位置的横坐标以左上角为0，0
        self.x = random.randint(0, 480 - 57)
        # 飞机移动速度
        self.speed = 3
        self.screen = screen
        self.image = pygame.image.load('./res/enemy1.png')
        self.bullets = []
        # self.isfly = True
        # 敌机无需监控自动飞行

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        if 1 == random.randint(0,50):
            bullet = DiRenBullet(self.screen, self.x, self.y)
            self.bullets.append(bullet)
        for  drb in  self.bullets:
            drb.display()

    def auto_move(self):
        self.y += self.speed
        for bullet in self.bullets:
            bullet.display()