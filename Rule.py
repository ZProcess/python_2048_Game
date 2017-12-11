#!/usr/bin/python3
#-*- coding:utf-8 -*-

import random
import pygame
from pygame.locals import *
class game_2048():
	def __init__(self,screen,myfont):
		self.map=[]
		self.is_game_over=False
		self.myfont=myfont
		self.screen=screen
		self.image_0=None
		self.image_2=None
		self.image_4=None
		self.image_8=None
		self.image_16=None
		self.image_32=None
		self.image_64=None
		self.image_128=None
		self.image_256=None
		self.image_512=None
		self.image_1024=None
		self.image_2048=None
		self.image_dict={}


	def map_init(self):
		temp=[]
		for n in range(0,4):
			for m in range(0,4):
				temp.append(0)
			self.map.append(temp)
			temp=[]

	def is_2048(self):
		for n in self.map:
			if n==2048:
				return True
		return False

	def random_numb(self):
		temp=random.randint(1,2)*2
		Empty=[]
		for n in range(0,4):
			for m in range(0,4):
				l=[]
				if self.map[n][m]==0:
					l.append(n)
					l.append(m)
					Empty.append(l)
		c=random.choice(Empty)
		n=c[0]
		m=c[1]
		self.map[n][m]=temp
		temp_image=self.myfont.render(str(temp),True,(0,0,0))
		self.screen.blit(temp_image,(75+120*m,65+120*n))

	def move(self,direction):
		if direction==1:
			next_lay=1
			while next_lay<=3:
				last_lay=next_lay-1
				while last_lay>=0:
					for n in range(0,4):
						if self.map[last_lay][n]==0 or self.map[last_lay+1][n]==self.map[last_lay][n]:
							self.map[last_lay][n]+=self.map[last_lay+1][n]
							self.map[last_lay+1][n]=0
					last_lay-=1
				next_lay+=1

		if direction==2:
			next_lay=2
			while next_lay>=0:
				last_lay=next_lay+1
				while last_lay<=3:
					for n in range(0,4):
						if self.map[last_lay][n]==0 or self.map[last_lay-1][n]==self.map[last_lay][n]:
							self.map[last_lay][n]+=self.map[last_lay-1][n]
							self.map[last_lay-1][n]=0
					last_lay+=1
				next_lay-=1

		if direction==3:
			next_lay=1
			while next_lay<=3:
				last_lay=next_lay-1
				while last_lay>=0:
					for n in range(0,4):
						if self.map[n][last_lay]==0 or self.map[n][last_lay+1]==self.map[n][last_lay]:
							self.map[n][last_lay]+=self.map[n][last_lay+1]
							self.map[n][last_lay+1]=0
					last_lay-=1
				next_lay+=1

		if direction==4:
			next_lay=2
			while next_lay>=0:
				last_lay=next_lay+1
				while last_lay<=3:
					for n in range(0,4):
						if self.map[n][last_lay]==0 or self.map[n][last_lay-1]==self.map[n][last_lay]:
							self.map[n][last_lay]+=self.map[n][last_lay-1]
							self.map[n][last_lay-1]=0
					last_lay+=1
				next_lay-=1
				

	def is_full(self):
		for n in range(0,4):
			for m in range(0,4):
				if self.map[n][m] == 0:
					return False
		self.is_game_over=True
		return True
	def print_result(self,result):
		win_image=self.myfont.render('You have got 2048',True,(0,0,0))
		lost_image=self.myfont.render('Game Over',True,(0,0,0))
		if result==1:
			self.screen.blit(win_image,(200,200))
		if result==2:
			self.screen.blit(lost_image,(160,200))

	def creat_image(self):
		color=(0,0,0)
		self.image_0=self.myfont.render('0',True,color)
		self.image_2=self.myfont.render('2',True,color)
		self.image_4=self.myfont.render('4',True,color)
		self.image_8=self.myfont.render('8',True,color)
		self.image_16=self.myfont.render('16',True,color)
		self.image_32=self.myfont.render('32',True,color)
		self.image_64=self.myfont.render('64',True,color)
		self.image_128=self.myfont.render('128',True,color)
		self.image_256=self.myfont.render('256',True,color)
		self.image_512=self.myfont.render('512',True,color)
		self.image_1024=self.myfont.render('1024',True,color)
		self.image_2048=self.myfont.render('2048',True,color)

	def creat_dict(self):
		self.image_dict[2]=self.image_2
		self.image_dict[4]=self.image_4
		self.image_dict[8]=self.image_8
		self.image_dict[16]=self.image_16
		self.image_dict[32]=self.image_32
		self.image_dict[64]=self.image_64
		self.image_dict[128]=self.image_128
		self.image_dict[256]=self.image_256
		self.image_dict[512]=self.image_512
		self.image_dict[1024]=self.image_1024
		self.image_dict[2048]=self.image_2048



	def draw_numb(self):
		for n in range(0,4):
			for m in range(0,4):
				if self.map[n][m]==0:
					continue
				elif self.map[n][m]<10:
					self.screen.blit(self.image_dict[self.map[n][m]],(75+120*m,65+120*n))
				elif self.map[n][m]<100:
					self.screen.blit(self.image_dict[self.map[n][m]],(65+120*m,65+120*n))
				elif self.map[n][m]<1000:
					self.screen.blit(self.image_dict[self.map[n][m]],(55+120*m,65+120*n))
				else :
					self.screen.blit(self.image_dict[self.map[n][m]],(45+120*m,65+120*n))

