import pygame
import random
from Timer import *

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
GRID_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


class snake:
# Create the game window
	def __init__(self):
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption("Snake Game")
		# Snake and food variables
		self.snake = [(200, 200)]
		self.snake_dir = "RIGHT"
		self.snake_speed = 5
		self.food = (random.randint(0, WIDTH - GRID_SIZE) // GRID_SIZE * GRID_SIZE,
					random.randint(0, HEIGHT - GRID_SIZE) // GRID_SIZE * GRID_SIZE)
		self.foodTwo = (random.randint(0, WIDTH - GRID_SIZE-50) // GRID_SIZE * GRID_SIZE,
					random.randint(0, HEIGHT - GRID_SIZE-50) // GRID_SIZE * GRID_SIZE)
		self.foodThree = (random.randint(0, WIDTH - GRID_SIZE-50) // GRID_SIZE * GRID_SIZE,
					random.randint(0, HEIGHT - GRID_SIZE-50) // GRID_SIZE * GRID_SIZE)
		self.clock = pygame.time.Clock()
		self.timer = Timer(60, self.screen, 10)
		self.won = False
		self.lose = False

	def getLost(self):
		return self.lose

	def getWon(self):
		return self.won

	def timerStart(self):
		timer = Timer(10, self.screen, 10)
		return timer

# Game over condition
	def game_over(self):
		self.font = pygame.font.Font(None, 36)
		self.text = self.font.render("Game Over! Press Q to quit or C to play again", True, RED)
		self.text_rect = self.text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
		self.screen.blit(self.text, self.text_rect)
		pygame.display.update()
		self.game_over_flag = True
   
		while self.game_over_flag:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit()
						quit()
					if event.key == pygame.K_c:
						self.reset_game()
						self.run_game()
		
# Function to reset the game
	def reset_game(self):
		self.snake, self.snake_dir, self.snake_speed, self.food
		self.snake = [(random.randint(0, WIDTH - GRID_SIZE) // GRID_SIZE * GRID_SIZE,
					random.randint(0, HEIGHT - GRID_SIZE) // GRID_SIZE * GRID_SIZE)]
		self.snake_dir = "RIGHT"
		self.snake_speed = 20
		self.food = (random.randint(0, WIDTH - GRID_SIZE) // GRID_SIZE * GRID_SIZE,
					random.randint(0, HEIGHT - GRID_SIZE) // GRID_SIZE * GRID_SIZE)

# Function for the main game loop
	def Play_Mini(self):
		self.snake, self.snake_dir, self.food,self.foodTwo,self.foodThree, self.snake_speed

		self.game_exit = False
		while not self.game_exit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.game_exit = True
				elif event.type == pygame.KEYDOWN:
					#a,w,s,d
					if event.key == pygame.K_w and self.snake_dir != "DOWN":
						self.snake_dir = "UP"
					elif event.key == pygame.K_s and self.snake_dir != "UP":
						self.snake_dir = "DOWN"
					elif event.key == pygame.K_a and self.snake_dir != "RIGHT":
						self.snake_dir = "LEFT"
					elif event.key == pygame.K_d and self.snake_dir != "LEFT":
						self.snake_dir = "RIGHT"
					#arrows
					if event.key == pygame.K_UP and self.snake_dir != "DOWN":
						self.snake_dir = "UP"
					elif event.key == pygame.K_DOWN and self.snake_dir != "UP":
						self.snake_dir = "DOWN"
					elif event.key == pygame.K_LEFT and self.snake_dir != "RIGHT":
						self.snake_dir = "LEFT"
					elif event.key == pygame.K_RIGHT and self.snake_dir != "LEFT":
						self.snake_dir = "RIGHT"
					
			

		# Move the snake
			if self.snake_dir == "UP":
				self.new_head = (self.snake[0][0], self.snake[0][1] - GRID_SIZE)
			elif self.snake_dir == "DOWN":
				self.new_head = (self.snake[0][0], self.snake[0][1] + GRID_SIZE)
			elif self.snake_dir == "LEFT":
				self.new_head = (self.snake[0][0] - GRID_SIZE, self.snake[0][1])
			elif self.snake_dir == "RIGHT":
				self.new_head = (self.snake[0][0] + GRID_SIZE, self.snake[0][1])

			self.snake.insert(0, self.new_head)

		# Check for collision with food
			if self.new_head == self.food or self.new_head == self.foodTwo or self.new_head == self.foodThree :
				self.food = (random.randint(0, WIDTH - GRID_SIZE) // GRID_SIZE * GRID_SIZE,
						random.randint(0, HEIGHT - GRID_SIZE) // GRID_SIZE * GRID_SIZE)
				self.foodTwo = (random.randint(0, WIDTH - GRID_SIZE) // GRID_SIZE * GRID_SIZE,
						random.randint(0, HEIGHT - GRID_SIZE) // GRID_SIZE * GRID_SIZE)
				self.foodThree = (random.randint(0, WIDTH - GRID_SIZE) // GRID_SIZE * GRID_SIZE,
						random.randint(0, HEIGHT - GRID_SIZE) // GRID_SIZE * GRID_SIZE)
				self.snake_speed += 1
			#else:
				#self.snake.pop()
			
		# Check for collision with boundaries or itself
			if (self.new_head[0] >= WIDTH or self.new_head[0] < 0 or
					self.new_head[1] >= HEIGHT or self.new_head[1] < 0 or
					self.new_head in self.snake[1:]):
				self.lose=self.timer.lost_game()
				return

		# Draw everything
			self.screen.fill(BLACK)
			pygame.draw.rect(self.screen, GREEN, (*self.food, GRID_SIZE, GRID_SIZE))
			pygame.draw.rect(self.screen, RED, (*self.foodTwo, GRID_SIZE, GRID_SIZE))
			pygame.draw.rect(self.screen, RED, (*self.foodThree, GRID_SIZE, GRID_SIZE))


			for segment in self.snake:
				pygame.draw.rect(self.screen, WHITE, (*segment, GRID_SIZE, GRID_SIZE))

			if self.timer.run_timer():
				self.won=self.timer.win_game()
				break
			pygame.display.update()
			self.clock.tick(self.snake_speed)

		pygame.quit()

