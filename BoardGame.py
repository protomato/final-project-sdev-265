import pygame
import sys
from Board import *
import tkinter as tk
from tkinter import *



pygame.init()

BG = pygame.image.load("images\BackGround.png")

def get_font(size): # Returns Press-Start-2P in the desired size
	return pygame.font.Font("images\Font.ttf", size)

class Button():
	def __init__(self,screen ,image, x_pos, y_pos, text_input , font , base_color , hovering_color):
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
		self.screen=screen

	def update(self):
		if self.image is not None:
			self.screen.blit(self.image, self.rect)
		self.screen.blit(self.text, self.text_rect)
	
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


class MainMenu():
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((800, 800))
		self.newBG = pygame.transform.scale(BG, (800, 800))
		self.gameover=False
		self.players=4


	def options(self):
		while True:
  
			self.screen.fill("white")

			OPTIONS_TEXT = get_font(40).render("This is the OPTIONS screen.", True, "Green")
			OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(550, 260))
			self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
						self.main_menu()
						return
			pygame.display.update()
	
	def main_menu(self):

		pygame.display.set_caption("Menu")
	
		menu_text = get_font(70).render("Main Menu",True , "#b68f40")
		menu_rect = menu_text.get_rect(center=(400, 100))

		PLAY_BUTTON = Button(self.screen, button_surface, 400, 250, "PLAY", get_font(75), "#d7fcd4", "White")
		OPTIONS_BUTTON = Button(self.screen, button_surfaceOptions, 400, 450, "OPTIONS", get_font(75), "#d7fcd4", "White")
		QUIT_BUTTON = Button(self.screen, button_surface, 400, 650, "QUIT", get_font(75), "#d7fcd4", "White")

		while True:
				self.screen.blit(self.newBG,(0,0))
				self.screen.blit(menu_text, menu_rect)
			
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
							True
							play(self,self.players)
							return
						if OPTIONS_BUTTON.checkForInput():
							t=animate_win("how many players are there","1","2","3","4")
							self.players=t.get()
						if QUIT_BUTTON.checkForInput():
							pygame.quit()
							sys.exit()
				PLAY_BUTTON.update()
				OPTIONS_BUTTON.update()
				QUIT_BUTTON.update()
				pygame.display.update()

class animate_win:
	def __init__(self,msg,button1="",button2="",button3="",button4=""):
		self.data=0
		reg_font = ("Verdana", 22)
  #popup = tk.Tk()
		self.popup = Tk()
		frame = Frame(self.popup)
		frame.pack(side="bottom")
		self.popup.minsize(800, 600) #
		self.popup.wm_title("Result")
		text = tk.Label(self.popup, text=msg, font=reg_font)
		text.pack(side="top",padx=30,pady=30)

	


		if button1!="":
			b1 = tk.Button(frame, text=button1, padx=5,pady=5, command = self.set1)
			b1.config(height = 3, width = 2,padx=5,pady=5)
			b1.pack(side=LEFT,padx=30,pady=30)
			
		if button2!="":
			b1 = tk.Button(frame, text=button2, padx=5,pady=5, command = self.set2)
			b1.config(height = 3, width = 2,padx=5,pady=5)
			b1.pack(side=LEFT,padx=30,pady=30)
		
		if button3!="":
			b1 = tk.Button(frame, text=button3, padx=5,pady=5, command = self.set3)
			b1.config(height = 3, width = 2,padx=5,pady=5)
			b1.pack(side=LEFT,padx=30,pady=30)

		if button4!="":
			b1 = tk.Button(frame, text=button4, padx=5,pady=5, command = self.set4)
			b1.config(height = 3, width = 2,padx=5,pady=5)
			b1.pack(side=LEFT,padx=30,pady=30)


		""""
		b2 = tk.Button(frame, text=":(", command=self.popup.destroy,padx=5,pady=5)
  
		b1.config(height = 3, width = 2,padx=5,pady=5) 
		b2.config(height = 10, width = 10,padx=5,pady=5)
  
  
		b1.pack(side=LEFT,padx=30,pady=30)
		b2.pack(side=LEFT,padx=30,pady=30)

		"""
		self.popup.mainloop()

	def set1(self):
		self.data=1
		self.popup.destroy()

	def set2(self):
		self.data=2
		self.popup.destroy()

	def set3(self):
		self.data=3
		self.popup.destroy()

	def set4(self):
		self.data=4
		self.popup.destroy()

	def get(self):
		return self.data
