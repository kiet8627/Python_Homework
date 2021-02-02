import pygame
pygame.init()

win_width = 1600
win_height = 870

win = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption("First Game")

bg = pygame.image.load('bg2.png')
standleft_pic = [pygame.image.load('standleft1.png'), pygame.image.load('standleft2.png'), pygame.image.load('standleft3.png'), pygame.image.load('standleft4.png'), pygame.image.load('standleft5.png'), pygame.image.load('standleft6.png')]
standright_pic = [pygame.image.load('standright1.png'), pygame.image.load('standright2.png'), pygame.image.load('standright3.png'), pygame.image.load('standright4.png'), pygame.image.load('standright5.png'), pygame.image.load('standright6.png')]
jumpleft_pic = [pygame.image.load('jumpleft1.png'), pygame.image.load('jumpleft2.png'), pygame.image.load('jumpleft3.png'), pygame.image.load('jumpleft4.png'), pygame.image.load('jumpleft5.png'), pygame.image.load('jumpleft6.png'), pygame.image.load('jumpleft7.png')]
jumpright_pic = [pygame.image.load('jumpright1.png'), pygame.image.load('jumpright2.png'), pygame.image.load('jumpright3.png'), pygame.image.load('jumpright4.png'), pygame.image.load('jumpright5.png'), pygame.image.load('jumpright6.png'), pygame.image.load('jumpright7.png')]

clock = pygame.time.Clock()

width = 130
height = 140
vel = 10
x = 50
y = win_height - 5 - height

isJump = False
jumpCount = 15
constJump = 15
jumpleft = False
jumpright = True
jumpleftCount = 0
jumprightCount = 0
downleftCount = 0
downrightCount = 0
left = False
right = False
standright = True
standleft = False
standleftCount = 0
standrightCount = 0
walkCount = 0

def redrawGameWindow():
	global standleftCount
	global standrightCount
	global jumpleftCount
	global jumprightCount
	global downleftCount
	global downrightCount
	global walkCount
	win.blit(bg, (0, 0))

	if isJump:
		if jumpleft:
			if jumpCount == 11:
				win.blit(jumpleft_pic[0], (x, y))
			elif jumpCount >= 0:
				win.blit(jumpleft_pic[1], (x, y))
			elif jumpCount >= -constJump:
				if jumpleftCount + 1 >= 6:
					jumpleftCount = 0
				win.blit(jumpleft_pic[jumpleftCount // 3 + 2], (x, y))
				jumpleftCount += 1
			else:
				if downleftCount + 1 >= 9:
					downleftCount = 0
				win.blit(jumpleft_pic[downleftCount // 3 + 4], (x, y))
				downleftCount += 1

		else:
			if jumpCount == 11:
				win.blit(jumpright_pic[0], (x, y))
			elif jumpCount >= 0:
				win.blit(jumpright_pic[1], (x, y))
			elif jumpCount >= -constJump:
				if jumprightCount + 1 >= 6:
					jumprightCount = 0
				win.blit(jumpright_pic[jumprightCount // 3 + 2], (x, y))
				jumprightCount += 1
			else:
				if downrightCount + 1 >= 9:
					downrightCount = 0
				win.blit(jumpright_pic[downrightCount // 3 + 4], (x, y))
				downrightCount += 1
	# elif left:

	# elif right:

	else:
		if standright:
			if standrightCount + 1 >= 18:
				standrightCount = 0

			win.blit(standright_pic[standrightCount // 3], (x, y))
			standrightCount += 1
		else:
			if standleftCount + 1 >= 18:
				standleftCount = 0

			win.blit(standleft_pic[standleftCount // 3], (x, y))
			standleftCount += 1

	pygame.display.update()


# gameloop
run = True
while run:
	clock.tick(18)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > vel:
		x -= vel
		left = True
		right = False
		standleft = jumpleft = True
		standright = jumpright = False
		standleftCount = standrightCount = 0
	elif keys[pygame.K_RIGHT] and x < win_width - width - vel:
		x += vel
		left = False
		right = True
		standleft = jumpleft = False
		standright = jumpright = True
		standleftCount = standrightCount = 0
	else:
		right = left = False
		walkCount = 0


	if not(isJump):
		if keys[pygame.K_SPACE]:
			isJump = True
			right = left = False
			walkCount = 0
	else:
		neg = 1
		if jumpCount >= -constJump:
			if jumpCount < 0:
				neg = -1
			y -= (jumpCount ** 2) * 0.5 * neg
			jumpCount -= 1
		else:
			isJump = False
			jumpCount = constJump
	redrawGameWindow()

pygame.quit()