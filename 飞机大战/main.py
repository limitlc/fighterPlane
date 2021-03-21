import time
import random
import pygame
# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 16:31
# @Author  : limitlc
# @Email   : limitlc@163.com
from pygame.constants import *


# 飞机类
class Hero:

    # 飞机初始化方法
    def __init__(self, screen):
        # 飞机所在位置的纵坐标以左上角为0，0
        self.y = 700 - 126
        # 飞机所在位置的横坐标以左上角为0，0
        self.x = 480 / 2 - 102 / 2
        # 飞机移动速度
        self.speed = 3
        self.screen = screen
        self.image = pygame.image.load('./res/me1.png')
        self.image2 = pygame.image.load('./res/me2.png')
        self.bullets = []
        self.isfly = True

    def key_control(self):
        keypressed = pygame.key.get_pressed()
        if keypressed[K_w] or keypressed[K_UP]:
            print("上")
            self.y -= self.speed
        if keypressed[K_a] or keypressed[K_LEFT]:
            print("左")
            self.x -= self.speed
        if keypressed[K_s] or keypressed[K_DOWN]:
            print("下")
            self.y += self.speed
        if keypressed[K_d] or keypressed[K_RIGHT]:
            print("右")
            self.x += self.speed
        if keypressed[K_SPACE]:
            print("发射子弹")
            bullet = Bullet(self.screen, self.x, self.y)
            self.bullets.append(bullet)
            pass

    def display(self):
        if self.isfly:
            self.screen.blit(self.image, (self.x, self.y))
            self.isfly = False
        else:
            self.screen.blit(self.image2, (self.x, self.y))
            self.isfly = True
        for bullet in self.bullets:
            bullet.display()


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
        self.y += self.speed
        for bullet in self.bullets:
            bullet.display()


class Bullet(object):
    # 构造方法中传输的是飞机所在的坐标
    def __init__(self, screen, x, y):
        # 坐标
        self.x = x + 102 / 2 - 6 / 2
        self.y = y - 12 / 2
        self.image = pygame.image.load("./res/bullet1.png")
        self.screen = screen
        self.speed = 10

    def display(self):
        # 飞机的位置是发生着变化的
        self.screen.blit(self.image, (self.x, self.y))
        self.y -= self.speed


def main():
    screen = pygame.display.set_mode((480, 700), 0, 32)
    background = pygame.image.load("./res/background.png")
    hero = Hero(screen)
    screen.blit(background, (0, 0))
    direns = []
    while True:
        screen.blit(background, (0, 0))
        if 8 == random.randint(0,30):
            direns.append(Diren(screen))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        hero.key_control()
        hero.display()
        for diren in direns:
            diren.display()
        pygame.display.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
