import os
import shutil
import pygame
import object as objectUtil
from utils import globalInfo
from utils import levelLoader
from pygame.locals import *
from math import *
verbose = True
if verbose:
    print("importing")

# Just renamed Main.py to main.py

# Clear temporary files
try:
    shutil.rmtree("./sprites/temp/")
except:
    pass
os.mkdir("./sprites/temp/")

if verbose:
    print("initialize pygame")
pygame.init()
# Variables
font = pygame.font.SysFont("Arial", 25)
flags = DOUBLEBUF
screen = pygame.display.set_mode((1080, 720), flags, 16)
run = True
clock = pygame.time.Clock()
background = pygame.image.load("./sprites/background.png")
b1 = pygame.image.load("./sprites/gun2.png")
background = pygame.transform.scale(background, (1080, 720))
experimentalLoaderText = font.render(
    "Press L to switch to experimental level loading system (DO NOT USE)", 3, pygame.Color("red"))
alive = True

pygame.mouse.set_visible(False)
pygame.display.set_caption("Geometry shoot")


def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("coral"))
    return fps_text


def commit_stop_living():
    # Commits die
    print("you died")
    global alive
    alive = False


currentframe = 0
y_vel = 0
y_pos = 0
airborne = False
experimentalLevelLoader = False
# mainloop
while 1:
    # update background
    screen.blit(background, (0, 0))

    # create ground (13 tiles long (see cell size in utils/globalInfo.py))
    for i in range(15):
        objectUtil.drawObject(screen, i, 0, 1)

    screen.blit(update_fps(), (10, 0))
    screen.blit(experimentalLoaderText, (100, 0))
    if experimentalLevelLoader:
        screen.blit(levelTexture, (0-(globalInfo.currentframe *
                    globalInfo.sideScrollSpeed), -(globalInfo.worldHeightPx - 720)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    # Player position and velocity managment

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not airborne:
        y_vel = -43
        airborne = True
    elif keys[pygame.K_l]:
        levelTexture = levelLoader.startLoader(screen)
        experimentalLevelLoader = True
        experimentalLoaderText = experimentalLoaderText = font.render(
            "EXPERIMENTAL LEVEL RENDERER IS ENABLED (RESTART TO DISABLE)", 3, pygame.Color("red"))
        globalInfo.currentframe = 0
    elif keys[pygame.K_q]:
        quit()
    y_pos += y_vel
    if airborne == True:
        if globalInfo.smallest_y < y_pos-50:
            commit_stop_living()
        elif globalInfo.smallest_y <= y_pos:
            airborne = False
            y_pos = globalInfo.smallest_y
            y_vel = 0

        else:
            # I tested this, this should give us a nice smooth jump
            y_vel += 5
            if y_vel > 50:
                y_vel = 50
            if y_vel < -50:
                y_vel = -50

    objectUtil.drawObject(screen, 5, 1-(y_pos/100), 4,
                          bypassSideScroll=True)
    # gun managment
    target_x = 400
    target_y = 200

    b2 = pygame.transform.rotate(
        b1, atan2(target_x-globalInfo.gridCellSize*6-20, 720-(target_y-globalInfo.gridCellSize*(2-y_pos/100))*180/pi-90))
    screen.blit(b2, (globalInfo.gridCellSize*6-b2.get_height()
                2+20, 720-(globalInfo.gridCellSize*(2-y_pos/100)-b2.get_height()/2)))

    if alive:
        globalInfo.currentframe += 1
    globalInfo.realCurrentFrame += 1
    deltaTime = clock.tick()
    pygame.display.update()
pygame.quit()
