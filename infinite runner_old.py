
"""
Aouther : Abdirizak abdullahi hussein 
DATE : 6/4/2022
instegram : @Abdirizak_8899
clubhouse : @binyamin_rd6
"""

import pygame , sys , time , random 

#initialize the screen 
pygame .init()


WIDTH = 400
HIGHT = 400

screen = pygame.display.set_mode([WIDTH,HIGHT])

pygame.display.set_caption('player movement')
# GAME VARIABLE 
player_x = 50
player_y = 280
fps = 60
x_movement = 0 
y_movement = 0
jumping = False
y_velocity = 20 
jumping_hight = y_velocity
gravity = 1 
obstacles = [300,400,600]
obstacles_speed = 2
active = False
score = 0

#codadka gameka
pygame.mixer.init()
backround = pygame.mixer.Sound('music.mp3')
font = pygame.font.Font('freesansbold.ttf' , 16)
colock = pygame.time.Clock()
# rgb colors
red = pygame.Color(255,0,0)
black = pygame.Color(0,0,0)
green = pygame.Color(0,255,0)
white = pygame.Color(255,255,255)
yellow = pygame.Color(255,255,0)
pink  = pygame.Color(255,192,203)
# drawing the player

run = True
while run:
	screen.fill(black)
	colock.tick(60)
	player = pygame.draw.rect(screen,green, [player_x,player_y,20,20])
	line = pygame.draw.rect(screen,[119,118,110],[0,300, WIDTH,10])
	backround.play()
	text_score = font.render(f'DHIBCAHA: {score}', True , white , black)
	screen.blit(text_score,[160,330])
	# that we drawing the obstacles
	obstacle0 = pygame.draw.rect(screen,red , [obstacles[0],280, 20,20])
	obstacle1 = pygame.draw.rect(screen,green , [obstacles[1],280, 20,20])
	obstacle2 = pygame.draw.rect(screen,pink , [obstacles[2],280, 20,20])
	#event handling 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_movement -= 5
				y_movement = 0 
			if event.key == pygame.K_RIGHT:
				x_movement += 5
				y_movement = 0
			if event.type == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				x_movement = 0
				y_movement = 0 
			if event.key == pygame.K_RIGHT:
				x_movement = 0
				y_movement = 0
	key_pressed = pygame.key.get_pressed()


	# waxa dhaqajinaya dhanka playerka uu jogo haddi uu ku dhoco wuu gafayaa loopkana wuu update garesmayaa
	for i in range(len(obstacles)):
		if active:
			backround.play()
			obstacles[i] -= obstacles_speed
			if obstacles[i] < -20:
				obstacles[i] = random.randint(470,570)
				score += 1
			if player.colliderect(obstacle0) or player.colliderect(obstacle1) or player.colliderect(obstacle2):
				active = False
				score = 0
				obstacles = [300,400,600]
				pass
	player_x = player_x + x_movement
	player_y = player_y + y_movement


	# codekaan wuxuu sheegayaa in haddii escape lataabto uu loopka false noqonayo yacnii kabaxayo gameka
	if key_pressed[pygame.K_ESCAPE]:
		run = False
	#kor uboodida playerka ayuu qeexayaaa codekan
	if key_pressed[pygame.K_SPACE]:
		jumping = True
	if jumping:
		player_y -= y_velocity
		y_velocity -= gravity
		if y_velocity <-jumping_hight:
			jumping = False
			y_velocity = jumping_hight
	#---------------------------------------------
	#xuduudaha inuusan kabixin ayuu qeexayaa codekan
	if player_x < 0:
		player_x = 0
	if player_x > 380:
	 	player_x = 380
	#--------------------------------------------------
	if key_pressed[pygame.K_SPACE]:
		active = True
	pygame.display.flip()

pygame.quit()