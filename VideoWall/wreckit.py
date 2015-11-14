import pygame, sys, time
from pygame.locals import *
import lirc
pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((1280, 1080), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
BLACK = (0,0,0)
winImg = pygame.image.load('window2.png')
winx = 10
winy = 10
direction = 'right'
sockid = lirc.init("wreckit", blocking = False)
while True: # the main game loop
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(winImg, (winx, winy))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    codeIR = lirc.nextcode()
    if codeIR:
        if codeIR[0] == 'fix':
            winImg=pygame.image.load('window2.png')
        elif codeIR[0] == 'break':
            winImg=pygame.image.load('g66841.png')

    if event.type == pygame.KEYDOWN:
        if (event.key == K_1):
            winImg=pygame.image.load('window.png')
        elif (event.key == K_2):
            winImg=pygame.image.load('broken.png')

    DISPLAYSURF.blit(winImg, (winx, winy))

    pygame.display.update()
    fpsClock.tick(FPS)
