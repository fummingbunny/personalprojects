# Hi my name is Bathineni Kowshik and i am doing this project by following the videos of coding spot as learning exercise.
# The entier code may be exactcly the same as that of the video with maybe a few changes here and there.
# This is the link to the video i referred to https://www.youtube.com/watch?v=pc7XhHxSgrM&t=122s


# import the required modules

import pygame, sys
import numpy as np

#initialize the pygame module
pygame.init()

#Creating the screen
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
#rgb: red green blue
RED = (255,0,0)
BG_COLOUR = (28,170,156)
LINE_COLOUR = (23,145,135)
CIRCLE_COLOUR = (239,231,200)
CROSS_COLOUR = (66,66,66)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
#To display a title for the game.
pygame.display.set_caption( 'TIC TAC TOE' )
#Add color to the screen
screen.fill(BG_COLOUR)

#creating the board
board = np.zeros((BOARD_ROWS, BOARD_COLS))
#print(board)

#draw lines in the pygame
#Arguments to pass (screen, line colour, starting postion of line, ending position, width of the line)
#pygame.draw.line( screen, RED, (10,10), (300,300), 10)

# function to draw the four main line of the game.
def draw_lines():
	#first horizontal line
	pygame.draw.line( screen,LINE_COLOUR,(0,200),(600,200), LINE_WIDTH )
	#second horizonal line
	pygame.draw.line( screen,LINE_COLOUR,(0,400),(600,400), LINE_WIDTH )
	#first vertical line
	pygame.draw.line( screen,LINE_COLOUR,(200,0),(200,600), LINE_WIDTH )
	#second vertical line
	pygame.draw.line( screen,LINE_COLOUR,(400,0),(400,600), LINE_WIDTH )

# function to draw figures X and O
def draw_figures():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 1:
				pygame.draw.circle( screen, CIRCLE_COLOUR,(int( col*200 + 100), int(row*200 + 100 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
			elif board[row][col] == 2:
				pygame.draw.line( screen, CROSS_COLOUR, (col * 200 + SPACE, row*200 + 200 - SPACE), (col*200 + 200 - SPACE, row*200 + SPACE), CROSS_WIDTH )
				pygame.draw.line( screen, CROSS_COLOUR, (col * 200 + SPACE, row*200  + SPACE), (col*200 + 200 - SPACE, row*200 + 200 - SPACE), CROSS_WIDTH )

# function to mark a square in the game.
def mark_sqaure(row, col, player):
	board[row][col] = player

#function to check if the square is available or not and return true if available 
def available_square(row, col):
	return board[row][col] == 0

#function to check if the board is full
def is_board_full():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 0:
				return False
	return True

player = 1


draw_lines()
#The created screen just flashes till here
#mainloop to keep the screen on.

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		#check if the we are clicking the screen.
		if event.type == pygame.MOUSEBUTTONDOWN:

			mouseX = event.pos[0] # x
			mouseY = event.pos[1] # y

			clicked_row = int(mouseY // 200)
			clicked_col = int(mouseX // 200)


			if available_square( clicked_row, clicked_col ):
				if player == 1:
					mark_sqaure( clicked_row, clicked_col, 1 )
					player = 2

				elif player == 2:
					mark_sqaure( clicked_row, clicked_col, 2 )
					player = 1

				draw_figures()




	#update the screen colour 
	pygame.display.update()



