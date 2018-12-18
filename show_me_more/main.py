import pygame
from pygame.locals import *
import random

NUM_OF_POINTS = 1024
POINT_SIZE = 1

pygame.init()

game_window = pygame.display.set_mode((2560, 1440), FULLSCREEN|HWACCEL)


random_points = []
for i in range(0, NUM_OF_POINTS):
	random_points.append([random.randint(0, 2559), random.randint(0, 1439), random.randint(0, 256)])


game_ended = False
while not game_ended:

	for event in pygame.event.get():
		if event.type == QUIT:
			game_ended = True
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				game_ended = True

	for point in random_points:
		pygame.draw.rect(game_window, (point[0] % 255, point[1] % 255, point[2] % 255), (point[0], point[1], POINT_SIZE, POINT_SIZE))
		point[0] += random.randint(-2, 2)
		point[1] += random.randint(-2, 2)
	
	pygame.display.update()

pygame.quit()