#!/usr/bin/python3
#-*- coding:utf-8 -*-

import pygame
from pygame.locals import *
import random,sys
from Rule import *

def print_numb(numb,x,y):
	text=str(numb)
	text_image=myfont.render(text,True,(0,0,0))
	screen.blit(text_image,(x,y))




pygame.init()
screen=pygame.display.set_mode((546,537))
pygame.display.set_caption('2048 Game')
myfont=pygame.font.Font(None,55)

bg=pygame.image.load('bg_2048.jpg').convert_alpha()
screen.fill((255,255,255))
screen.blit(bg,(0,0))
test_image=myfont.render('16',True,(0,0,0))


game=game_2048(screen,myfont)
game.map_init()
game.random_numb()
game.random_numb()
game.creat_image()
game.creat_dict()

while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			sys.exit()
		if event.type==KEYDOWN:
			if event.key==pygame.K_UP:
				game.move(1)
				screen.blit(bg,(0,0))
				game.random_numb()
				game.draw_numb()
			if event.key==pygame.K_DOWN:
				game.move(2)
				screen.blit(bg,(0,0))
				game.random_numb()
				game.draw_numb()
			if event.key==pygame.K_LEFT:
				game.move(3)
				screen.blit(bg,(0,0))
				game.random_numb()
				game.draw_numb()
			if event.key==pygame.K_RIGHT:
				game.move(4)
				screen.blit(bg,(0,0))
				game.random_numb()
				game.draw_numb()
	if game.is_2048():
		game.print_result(1)
	if game.is_full():
		game.print_result(2)

	keys=pygame.key.get_pressed()
	if keys[K_ESCAPE]:
		sys.exit()

		
	pygame.display.update()

