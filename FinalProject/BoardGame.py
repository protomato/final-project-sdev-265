import pygame
import sys
from Board import *

pygame.init()
screen = pygame.display.set_mode((800, 800))

BG = pygame.image.load("images\BackGround.png")
newBG = pygame.transform.scale(BG, (800, 800))

def get_font(size): # Returns Press-Start-2P in the desired size
	return pygame.font.Font("images\Font.ttf", size)

class Button():
	def __init__(self, image, x_pos, y_pos, text_input , font , base_color , hovering_color):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.font = font
		self.base_color = base_color
		self.hovering_color = hovering_color
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)
	
	def checkForInput(self):
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			return True
		return False

	def changeColor(self):
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)


button_surface = pygame.image.load("images\Button.png")
button_surface = pygame.transform.scale(button_surface, (400, 150))

button_surfaceOptions = pygame.transform.scale(button_surface, (600, 150))


def options():
	while True:
  
		screen.fill("white")

		OPTIONS_TEXT = get_font(40).render("This is the OPTIONS screen.", True, "Green")
		OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(550, 260))
		screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
					main_menu()
					return
		pygame.display.update()
	
def main_menu():

	pygame.display.set_caption("Menu")
	
	menu_text = get_font(70).render("Main Menu",True , "#b68f40")
	menu_rect = menu_text.get_rect(center=(400, 100))
	
	PLAY_BUTTON = Button(button_surface, 400,250,"PLAY", get_font(75), "#d7fcd4","White")
	OPTIONS_BUTTON = Button(button_surfaceOptions, 400,450,"OPTIONS", get_font(75), "#d7fcd4","White")
	QUIT_BUTTON = Button(button_surface, 400,650,"QUIT", get_font(75), "#d7fcd4","White")

	while True:
			screen.blit(newBG,(0,0))
			screen.blit(menu_text, menu_rect)
			
			menu_text=get_font(70).render("Main Menu",True , "#b68f40")
			menu_rect = menu_text.get_rect(center=(400, 100))

			if menu_rect.collidepoint(pygame.mouse.get_pos()):
				menu_text = get_font(70).render("Main Menu", True, "White")
			else: 
				menu_text=get_font(70).render("Main Menu",True , "#b68f40")

			for button in [PLAY_BUTTON,OPTIONS_BUTTON,QUIT_BUTTON]:
				button.changeColor()
				button.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()	
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if PLAY_BUTTON.checkForInput():
						pygame.quit()
						play()
						return
					if OPTIONS_BUTTON.checkForInput():
						options()
						return
					if QUIT_BUTTON.checkForInput():
						pygame.quit()
						sys.exit()
			PLAY_BUTTON.update()
			OPTIONS_BUTTON.update()
			QUIT_BUTTON.update()
			pygame.display.update()

main_menu()
