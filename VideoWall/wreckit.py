import pygame, sys, time
from pygame.locals import *
import lirc
import RPi.GPIO as GPIO

pygame.init()

# Setup our button GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
screen = pygame.display.get_surface()

# set up the window

screen = pygame.display.set_mode((0,0), FULLSCREEN, 32)
#screen = pygame.display.set_mode((1080,768),0,32)
pygame.display.set_caption('LTA 2015')
w,h = screen.get_size()
winx,winy = (10,10)

#Setup the game screen and add splash screen
WHITE = (255, 255, 255)
BLACK = (0,0,0)

winImg = pygame.image.load('insert_coin.jpg')
winImg=pygame.transform.scale(winImg,(w, h))
screen.fill(BLACK)
screen.blit(winImg, (winx, winy))
#Start the socket for the IR
sockid = lirc.init("wreckit", blocking = False)

#Determine what no. monitor we should be
done = False
pygame.display.update()
while not done:
    codeIR = lirc.nextcode()
    if codeIR:
        if codeIR[0] == 'ir_one':
           monitor = 1
           done = True
        elif codeIR[0] == 'ir_two':
            monitor = 2
            done = True
        elif codeIR[0] == 'ir_three':
            monitor = 3
            done = True
        elif codeIR[0] == 'ir_four':
            monitor = 4
            done = True
        elif codeIR[0] == 'ir_five':
            monitor = 5
            done = True
        elif codeIR[0] == 'ir_six':
            monitor = 6
            done = True

#Start the game
winImg=pygame.image.load('window_LTA.png')
winImg=pygame.transform.scale(winImg,(w, h))

#Configure the interrupt for the GPIO pin
GPIO.add_event_detect(17,GPIO.FALLING)

while True: # the main game loop

    #If the button is pressed break the window
    #if (GPIO.input(17) == True):
    if GPIO.event_detected(17):
        winImg=pygame.image.load('windowbroken_LTA.png')
        winImg=pygame.transform.scale(winImg,(w, h))

    screen.fill(BLACK)
    screen.blit(winImg, (winx, winy))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    codeIR = lirc.nextcode()
    if codeIR:
        if codeIR[0] == 'ir_nine':
            winImg=pygame.image.load('window_LTA.png')
            winImg=pygame.transform.scale(winImg,(w, h))
        elif codeIR[0] == 'ir_zero':
            winImg=pygame.image.load('windowbroken_LTA.png')
            winImg=pygame.transform.scale(winImg,(w, h))
        elif codeIR[0] == 'ir_one' and (monitor==1):
            winImg=pygame.image.load('window_LTA.png')
            winImg=pygame.transform.scale(winImg,(w, h))
        elif codeIR[0] == 'ir_two' and (monitor==2):
            winImg=pygame.image.load('window_LTA.png')
            winImg=pygame.transform.scale(winImg,(w, h))
        elif codeIR[0] == 'ir_three' and (monitor==3):
            winImg=pygame.image.load('window_LTA.png')
            winImg=pygame.transform.scale(winImg,(w, h))
        elif codeIR[0] == 'ir_four' and (monitor==4):
            winImg=pygame.image.load('window_LTA.png')
            winImg=pygame.transform.scale(winImg,(w, h))
        elif codeIR[0] == 'ir_five' and (monitor==5):
            winImg=pygame.image.load('window_LTA.png')
            winImg=pygame.transform.scale(winImg,(w, h))
        elif codeIR[0] == 'ir_six' and (monitor==6):
            winImg=pygame.image.load('window_LTA.png')
            winImg=pygame.transform.scale(winImg,(w, h))
        elif codeIR[0] == 'ir_pwr':
            pygame.quit()
            sys.exit()

    screen.blit(winImg, (winx, winy))
    pygame.display.update()
    fpsClock.tick(FPS)
