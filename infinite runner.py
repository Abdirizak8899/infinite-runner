"""
Aouthor : Abdirizak abdullahi hussein
Date : 18/6/2022
"""
import pygame as pyg , random as  rand ,sys as ss,time
from pygame.locals import *

# setting the screen
sw,sh = 720,500
pyg.init()
screen =  pyg.display.set_mode([sw,sh])
pyg.display.set_caption('infinite runner')

# Game variables
player_x = 100
player_y = sh-170
vel = 20
jump_hight = vel 
gravity = 1
player_speed = 5
enemy_speed = 3
jump = False
timer = pyg.time.Clock()
obstacles_list = []
enemy_list =  []
score = 0

def enemy(obstacles_list):
	while len(obstacles_list) <=5:
		x_pos = rand.randint(sw//2,sw+sw+sw+sw+sw)
		y_pos = sh-170
		new_enemy = [x_pos,y_pos]
		obstacles_list.append(new_enemy)

enemy(obstacles_list)
# RGB VALUES
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
yellow  = [0,255,255]




# Creating enemies

def draw(obstacles_list):
	for nw_enemy in obstacles_list:
		nw_en = pyg.draw.rect(screen,[0,255,0],[nw_enemy[0],nw_enemy[1],20,20])
		enemy_list.append(nw_en)


gameover = False 
while not gameover:

	screen.fill([0,0,0])
	timer .tick(60)

	# floor is the white rectangle in the middle of the screen
	floor = pyg.draw.rect(screen,[255,255,255],[0,sh-150,sw,20])
	
	# player is the box that we can control
	player = pyg.draw.rect(screen,[255,0,0],[player_x,player_y,20,20])
	
	# drawing enemy into the screen
	draw(obstacles_list)

	# event handling 
	for even in pyg.event.get():
		if even.type == QUIT:
			gameover = True

	# moving enemy until offscreen and reseting their position
	for enemy_pos in obstacles_list:
		if enemy_pos[0] > -20:
			enemy_pos[0] -= enemy_speed
		else:
			enemy_pos[0] = rand.randint(sw//2,sw+sw+sw+sw+sw+sw)

	# detecting collisions
	for enemy_pos in obstacles_list:
		ex = enemy_pos[0] # ex = enemy position x
		if ex >= player_x and ex <= player_x+20 and enemy_pos[1] == player_y or player_x+20 == ex and enemy_pos[1] == player_y: 
			gameover = True        

	# score font drawing into the screen
	font  = pyg.font.SysFont('carbel',35)
	tex = 'Score: ' +str(score)
	label = font.render(tex,1,[255,255,255])
	screen.blit(label,[50,50])

	# listening what key is pressed then moving the player
	key_pressed = pyg.key.get_pressed()
	if key_pressed[K_RIGHT] and player_x <= sw-20-8:
		player_x += player_speed
	elif key_pressed[K_LEFT] and player_x >=0+8:
		player_x -= player_speed
	elif key_pressed[K_SPACE]:
		jump = True
	# jum motion
	if jump:
		player_y -= vel
		vel -= gravity 
		if vel <-jump_hight:
			jump = False
			vel  = jump_hight
			score +=1

	pyg.display.update()