import pygame
import time
# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 16:31
# @Author  : limitlc
# @Email   : limitlc@163.com
def main():
    screen = pygame.display.set_mode((480, 700), 0, 32)
    background = pygame.image.load("./res/background.png")
    screen.blit(background, (0, 0))
    hero = pygame.image.load('./res/me1.png')
    screen.blit(hero,(480/2-102/2,700-126))
    while True:
        for event in   pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # keppressed = pygame.key.get_pressed()

        pygame.display.update()
        time.sleep(0.01)

if __name__ == '__main__':
    main()
