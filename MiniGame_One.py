# Import the required libraries
import pygame
import random
from pygame.locals import Rect
import math
from Timer import Timer  # Import Timer class from Timer module
import sys

# Initialize the game engine
pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

class MiniGame_One:

	def __init__(self):
		# Create an empty array
		self.window_width = 800
		self.window_height = 800
		# Set the height and wi	dth of the screen
		SIZE = [self.window_width,self.window_height]
		self.screen = pygame.display.set_mode(SIZE)
		pygame.display.set_caption("Snow Animation")
		self.snow_list = []
		self.spaceship = pygame.image.load("images\spaceship.png")
		self.spaceship = pygame.transform.scale(self.spaceship, (40, 40))
		self.spaceship_x = self.window_width // 2
		self.spaceship_y = self.window_height - 50
		self.spaceship_rect = Rect(self.spaceship_x, self.spaceship_y, 40, 40)
		self.collided_snowflakes = []
		self.frame_count = 1
		self.generator()
		self.clock = pygame.time.Clock()
		self.count = 0	
		self.clockTime = 500
		self.won = False
		self.lose = False

	def distance(self, point1, point2):
		return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

	def generator(self):
		if self.frame_count % 200 == 0:
			for i in range(5):
				x = random.randrange(0, 800)
				y = random.randrange(0, 100)
				self.snow_list.append([x, y])

	def getLost(self):
		return self.lose

	def getWon(self):
		return self.won

	def Play_Mini(self):
		
		done = False
		timer = Timer(10, self.screen, 10)

		while not done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
					pygame.quit()
					sys.exit()
			self.screen.fill(BLACK)
	
			if timer.run_timer():
				self.won=timer.win_game()
				print(self.won)
				break

			keys = pygame.key.get_pressed()
			if keys[pygame.K_LEFT]:
				self.spaceship_x -= 1
			if keys[pygame.K_RIGHT]:
				self.spaceship_x += 1
			if keys[pygame.K_UP]:
				self.spaceship_y -= 1
			if keys[pygame.K_DOWN]:
				self.spaceship_y += 1

			self.screen.blit(self.spaceship, (self.spaceship_x, self.spaceship_y))
			self.generator()
			self.frame_count += 1

			for i in range(len(self.snow_list)):
				snowflake_rect=pygame.draw.circle(self.screen, WHITE, self.snow_list[i], 2)

				snowflake_x, snowflake_y = self.snow_list[i]
				snowflake_center = [snowflake_x, snowflake_y]

				if self.distance(snowflake_center, [self.spaceship_x + 20, self.spaceship_y + 20]) <= 20:
					if i not in self.collided_snowflakes:
						self.collided_snowflakes.append(i)
						self.count += 1
						#print("Collision detected " + str(self.count))
						self.lose=timer.lost_game()
						#print(self.won)
						return 
						break
				self.snow_list[i][1] += 1

			pygame.display.flip()
			self.clock.tick(500)

		pygame.quit()
'''
if __name__ == "__main__":
	Mini = MiniGame_One()
	Mini.Play_Mini()
'''