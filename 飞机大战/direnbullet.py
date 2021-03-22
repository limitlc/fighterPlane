# -*- coding: utf-8 -*-
# @Time    : 2021/3/22 11:33
# @Author  : limitlc
# @Email   : limitlc@163.com
import pygame


class DiRenBullet(object):
    # 构造方法中传输的是飞机所在的坐标 57*43
    def __init__(self, screen, x, y):
        # 坐标
        self.x = x + 58/2-6/2
        self.y = y + 43
        self.image = pygame.image.load("./res/bullet1.png")
        self.screen = screen
        self.speed = 3

    def display(self):
        # 飞机的位置是发生着变化的
        self.screen.blit(self.image, (self.x, self.y))
        self.y += self.speed
