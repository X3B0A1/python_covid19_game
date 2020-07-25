# coding:utf-8
import pygame
from pygame.locals import *
import time
import sys
import os

# 初始化pygame环境
pygame.init()

# 创建一个长宽分别为480/650窗口
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (400, 35)
canvas = pygame.display.set_mode((398, 600))
canvas.fill((255, 255, 255))

# 设置窗口标题
pygame.display.set_caption("抗疫知识大比拼")

# 加载图片
start = pygame.image.load("imgs/bg0.png")
loading = pygame.image.load("imgs/nbg1.png")
test1 = pygame.image.load("imgs/nbg2.png")
test2 = pygame.image.load("imgs/nbg3.png")
test3 = pygame.image.load("imgs/nbg4.png")
test4 = pygame.image.load("imgs/nbg5.png")
test5 = pygame.image.load("imgs/nbg6.png")
test6 = pygame.image.load("imgs/nbg7.png")
end0 = pygame.image.load("imgs/ebg0.png")
end1 = pygame.image.load("imgs/ebg1.png")
end2 = pygame.image.load("imgs/ebg2.png")
end3 = pygame.image.load("imgs/ebg3.png")
end4 = pygame.image.load("imgs/ebg4.png")
end5 = pygame.image.load("imgs/ebg5.png")
end6 = pygame.image.load("imgs/ebg6.png")
wait = pygame.image.load("imgs/bg12.png")
nwa = pygame.image.load("imgs/noWildAnimel.png")
end7 = pygame.image.load("imgs/last.png")

# 答案
# answer = [3, 1, 2, 1, 3, 3]


def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            checkClick(event.pos[0], event.pos[1])


class Player():
    def __init__(self):
        self.score = 0


def checkClick(x, y):
    global que, step
    if step == 0:
        step = 1
    elif step == 1:
        step = 2
    elif step == 2:
        if x > 61 and x < 346 and y > 400 and y < 434:
            if que == 4 or que == 2:
                player.score += 1
            que = que + 1
        elif x > 58 and x < 350 and y > 464 and y < 504:
            if que == 3:
                player.score += 1
            que = que + 1
        elif x > 62 and x < 354 and y > 530 and y < 568:
            if que == 1 or que == 5 or que == 6:
                player.score += 1
            que = que + 1
    if que > 6:
        step = 3
    # if step == 3:
    #     step = 4
    # if step == 4:
    #     step = 5


def sum():
    score = player.score
    if score == 0:
        canvas.blit(end0, (0, 0))
    elif score == 1:
        canvas.blit(end1, (0, 0))
    elif score == 2:
        canvas.blit(end2, (0, 0))
    elif score == 3:
        canvas.blit(end3, (0, 0))
    elif score == 4:
        canvas.blit(end4, (0, 0))
    elif score == 5:
        canvas.blit(end5, (0, 0))
    elif score == 6:
        canvas.blit(end6, (0, 0))


def control():
    global step
    if step == 0:
        canvas.blit(start, (0, 0))
    elif step == 1:
        canvas.blit(loading, (0, 0))
    elif step == 2:
        test()
    elif step == 3:
        if time < 200:
            canvas.blit(wait, (0, 0))
        else:
            sum()
            # pygame.time.delay(1000)
            step += 1
    elif step == 4:
        canvas.blit(nwa, (0, 0))
        # print(1)
        pygame.time.delay(5000)
        step += 1
    elif step == 5:
        pygame.time.delay(5000)
        canvas.blit(end7, (0, 0))
        pygame.time.delay(10000)
        step = 0

def test():
    global que
    if que == 1:
        canvas.blit(test1, (0, 0))
    elif que == 2:
        canvas.blit(test2, (0, 0))
    elif que == 3:
        canvas.blit(test3, (0, 0))
    elif que == 4:
        canvas.blit(test4, (0, 0))
    elif que == 5:
        canvas.blit(test5, (0, 0))
    elif que == 6:
        canvas.blit(test6, (0, 0))


player = Player()

step = 0
que = 1
time = 0
while True:
    control()
    if step == 3:
        time = time + 1
    # 监听有没有按下退出按钮
    handleEvent()
    # 更新屏幕内容
    pygame.display.update()
    # 延时1秒
    pygame.time.delay(10)
