import pygame
import sys
import random
from pygame.locals import *
from Timer import *

# Set up display
WIDTH, HEIGHT = 800, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

class  flappyBird:

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption("Flappy Bird")
		# Set up bird
		self.bird_size = 30
		self.bird_x = 500
		self.bird_y = HEIGHT // 4 - self.bird_size // 2
		self.bird_speed = 5
		# Set up pipes
		self.pipe_width = 50
		self.pipe_gap = 400  # Increased pipe gap
		self.pipe_speed = 3
		self.pipes = []

		# Set up game variables
		self.gravity = 0.9  # Reduced gravity
		self.jump_strength = 12
		self.bird_alive = True
		self.timer = Timer(10, self.screen, 10)
		self.won = False
		self.lose = False

	def getLost(self):
		return self.lose

	def getWon(self):
		return self.won

	def timerStart(self):
		timer = Timer(10, self.screen, 10)
		return timer

	# Function to draw the bird
	def draw_bird(self):
		pygame.draw.rect(self.screen, BLUE, (self.bird_x, self.bird_y, self.bird_size, self.bird_size))

	# Function to draw the pipes
	def draw_pipes(self):
		for pipe_pair in self.pipes:
			pygame.draw.rect(self.screen, BLACK, (pipe_pair[0], 0, self.pipe_width, pipe_pair[1]))
			pygame.draw.rect(self.screen, BLACK, (pipe_pair[0], pipe_pair[1] + self.pipe_gap, self.pipe_width, HEIGHT - pipe_pair[1] - self.pipe_gap))

	# Function to move the bird
	def move_bird(self):
		self.bird_y += self.bird_speed
		self.bird_speed += self.gravity

	# Function to check for collisions with pipes
	def check_collision(self):
		global bird_alive
		if self.bird_y < 0 or self.bird_y + self.bird_size > HEIGHT:
			bird_alive = False
			self.lose=self.timer.lost_game()
			return self.lose
		for pipe_pair in self.pipes:
			if (
				self.bird_x < pipe_pair[0] + self.pipe_width
				and self.bird_x + self.bird_size > pipe_pair[0]
				and (self.bird_y < pipe_pair[1] or self.bird_y + self.bird_size > pipe_pair[1] + self.pipe_gap)
			):
				bird_alive = False
				self.lose=self.timer.lost_game()
				return self.lose

			
	def Play_Mini(self):
		# Main game loop
		while True:
			# Event handling
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == KEYDOWN:
					if event.key == K_SPACE and self.bird_alive:
						self.bird_speed = -self.jump_strength

			# Move bird
			if self.bird_alive:
				self.move_bird()

			# Move pipes
			for self.pipe_pair in self.pipes:
				self.pipe_pair[0] -= self.pipe_speed

			# Spawn new pipes
			if not self.pipes or self.pipes[-1][0] < WIDTH - 200:
				self.pipe_height = random.randint(50, HEIGHT - self.pipe_gap - 50)
				self.pipes.append([WIDTH, self.pipe_height])

			# Remove off-screen pipes
			self.pipes = [self.pipe_pair for self.pipe_pair in self.pipes if self.pipe_pair[0] + self.pipe_width > 0]

			# Check for collisions
			if(self.check_collision()):
				return

			# Clear the screen
			self.screen.fill(WHITE)

			# Draw bird and pipes
			self.draw_bird()
			self.draw_pipes()

			if self.timer.run_timer():
				self.won=self.timer.win_game()
				return
				
				
			# Update display
			pygame.display.update()

			# Set the frame rate
			pygame.time.Clock().tick(30)

#i=flappyBird()
#i.Play_Mini()
