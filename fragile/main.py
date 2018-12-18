import pygame
from pygame.locals import *
import random

NUM_OF_POINTS = 256

pygame.init()

game_window = pygame.display.set_mode((2560, 1440), FULLSCREEN|HWACCEL)


random_points = []
for i in range(0, NUM_OF_POINTS):
	random_points.append([random.randint(0, 2559), random.randint(0, 1439), random.randint(16, 32), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])


game_ended = False
while not game_ended:

	for event in pygame.event.get():
		if event.type == QUIT:
			game_ended = True
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				game_ended = True

	for point in random_points:
		pygame.draw.ellipse(game_window, (point[3], point[4], point[5]), (point[0], point[1], int(point[2]), int(point[2])), 1)
		point[0] += random.randint(2, 4)
		point[1] += random.randint(2, 4)
		point[2] *= 1.0175
	
	pygame.display.update()

pygame.quit()