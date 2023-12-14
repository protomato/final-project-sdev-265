import pygame
import random
from Timer import Timer
import sys

pygame.init()

WIDTH, HEIGHT = 800, 800
size = (WIDTH, HEIGHT)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class MiniGame_Two:

	def __init__(self):
		self.screen = pygame.display.set_mode(size)
		pygame.display.set_caption("Board")
		self.rect1_x, self.rect1_y = 100, 200  # Initial position for the first rectangle
		self.rect2_x, self.rect2_y = 700, 400  # Initial position for the second rectangle
		self.x_start, self.y_start = 100, 770
		self.x_end, self.y_end = 300, 770
		self.start_point = (self.x_start, self.y_start)
		self.end_point = (self.x_end, self.y_end)
		self.clock = pygame.time.Clock()
		self.rect1_change_x, self.rect1_change_y = 3, 3
		self.rect2_change_x, self.rect2_change_y = 3, 3
		self.done = False
		self.timer = Timer(10, self.screen, 10)
		self.won = False
		self.lose = False

	def timerStart(self):
		timer = Timer(10, self.screen, 10)
		return timer

	def getLost(self):
		return self.lose

	def getWon(self):
		return self.won

	def Play_Mini(self):
		while not self.done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.done = True
					pygame.quit()	
					sys.exit()
			self.screen.fill(BLACK)

			rect = pygame.draw.rect(self.screen, WHITE, [self.rect2_x, self.rect2_y, 50, 50])
			rec2 = pygame.draw.rect(self.screen, WHITE, [self.rect1_x, self.rect1_y, 50, 50])
			pygame.draw.rect(self.screen, RED, [self.rect1_x + 10, self.rect1_y + 10, 30, 30])

			if self.timer.run_timer():
				self.won=self.timer.win_game()
				break

			keys = pygame.key.get_pressed()
			if keys[pygame.K_LEFT]:
				self.x_start -= 10
				self.x_end -= 10
			if keys[pygame.K_RIGHT]:
				self.x_start += 10
				self.x_end += 10

			start_point = (self.x_start, self.y_start)
			end_point = (self.x_end, self.y_end)

			line = pygame.draw.line(self.screen, WHITE, start_point, end_point, 5)

			self.rect1_x += self.rect1_change_x
			self.rect1_y += self.rect1_change_y

			self.rect2_x += self.rect2_change_x
			self.rect2_y += self.rect2_change_y

			if line.colliderect(self.rect2_x, self.rect2_y, 50, 50):
				while -4<self.rect2_change_x and self.rect2_change_x<4:
					self.rect2_change_x = random.randint(-5, 5)
				self.rect2_change_y *= -1
			if line.colliderect(self.rect1_x, self.rect1_y, 50, 50):
				while -4<self.rect1_change_x and self.rect1_change_x<4:
					self.rect1_change_x = random.randint(-5, 5)
				self.rect1_change_y *= -1
			if rect.colliderect(self.rect1_x, self.rect1_y, 50, 50):
				while -4<self.rect1_change_x and self.rect1_change_x<4:
					self.rect1_change_x = random.randint(-5, 5)
				self.rect1_change_y *= -1
			if rec2.colliderect(self.rect2_x, self.rect2_y, 50, 50):
				while -4<self.rect2_change_x and self.rect2_change_x<4:
					self.rect2_change_x = random.randint(-5, 5)
				self.rect2_change_y *= -1
			
			if self.rect1_y > 750:
				self.lose=self.timer.lost_game()
				return
				break

			if self.rect2_y > 750:
				self.lose=self.timer.lost_game()
				return
				break
					   
			if self.rect1_y > 750 or self.rect1_y < 0:
				self.rect1_change_y *= -1
			if self.rect1_x > 750 or self.rect1_x < 0:
				self.rect1_change_x *= -1
			if self.rect2_y > 750 or self.rect2_y < 0:	
				self.rect2_change_y *= -1
			if self.rect2_x > 750 or self.rect2_x < 0:
				self.rect2_change_x *= -1

			pygame.display.flip()
			self.clock.tick(60)
'''
if __name__ == "__main__":
	Mini = MiniGame_Two()
	Mini.Play_Mini()
'''