import random
import sys
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
with contextlib.redirect_stdout(None):
	from pygame.locals import *

NUM_OF_POINTS = 256
ITERATION = 400

pygame.init()

try:
	w = int(sys.argv[1])
	h = int(sys.argv[2])
	try:
		filename = sys.argv[3]
	except:
		print("You can also specify the path to save the screen capture: 'python main.py \x1B[3mwidht height pathToSave\x1B[23m'\n")
		filename = "capture.png"
except:
	print("For a custom size windows type: 'python main.py \x1B[3mwidht height pathToSave\x1B[23m'\n")
	w = 800
	h = 400

print("Instructions: \n\t-Key 'R' to restart the simulation \n\t-Key 'S' to save the simulation \n\t-Key 'ESC' to quit the simulation ")

game_window = pygame.display.set_mode((w, h), HWACCEL)

counter = 0
random_points = []
for i in range(0, NUM_OF_POINTS):
	random_points.append([random.randint(0, w - 1), 
		random.randint(0, h - 1), random.randint(16, 32), 
		random.randint(0, 255), random.randint(0, 255), 
		random.randint(0, 255)])
	random.shuffle(random_points)

game_ended = False
while not game_ended:
	for event in pygame.event.get():
		if event.type == QUIT:
			game_ended = True
		if event.type == KEYDOWN:
			if event.key == K_r:
				game_window.fill((0, 0, 0))
				counter = 0
				random_points = []
				for i in range(0, NUM_OF_POINTS):
					random_points.append([random.randint(0, w - 1), 
						random.randint(0, h - 1), random.randint(16, 32), 
						random.randint(0, 255), random.randint(0, 255), 
						random.randint(0, 255)])
			if event.key == K_s:
				pygame.image.save(game_window, filename)
				print("SUCCESSFULLY SAVED")
			if event.key == K_ESCAPE:
				game_ended = True

	if counter < ITERATION:
		for point in random_points:
			pygame.draw.ellipse(game_window, (point[3], point[4], point[5]), (point[0], point[1], int(point[2]), int(point[2])), 1)
			point[0] += random.randint(2, 4)
			point[1] += random.randint(2, 4)
			point[2] *= 1.0175
		counter += 1

	pygame.display.update()

pygame.quit()