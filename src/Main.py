# imports
import sys


verbose = True


if verbose:
    print("importing")
#pygame setup
import pygame

if verbose:
    print("initialize pygame")

pygame.init()
win=pygame.display.set_mode((1300,700))
pygame.display.set_caption("tutoring")
#variables
run=True
clock=pygame.time.Clock()
x=0
#mainloop
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()
pygame.quit()
