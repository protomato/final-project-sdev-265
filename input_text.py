import pygame
import sys

class InputText:
	def __init__(self,prompt="prompt"):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode([1000, 400])
		self.base_font = pygame.font.Font(None, 24)
		self.fix_text = prompt
		self.user_text  = ""
		self.text_lines = []  # Store lines of text
		self.leftConer_x = 400
		self.leftConer_y = 10
		self.color = pygame.Color( (255, 255, 255))
		self.rect = pygame.Rect(self.leftConer_x,self.leftConer_y,380,40)
		self.runInputBox()
	
	'''
	def getInput(self):
		return '\n'.join(self.text_lines)
	'''
	
	def getInput(self):
		return self.user_text
	
	def runInputBox(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					return
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:  # Check for Enter key
						#self.text_lines.append(self.user_text)
						input_text = self.getInput()  # Retrieve the text input
						print(input_text)
						pygame.quit()
						return
						#self.user_text = ""  # Reset for new line
						
					elif event.key == pygame.K_BACKSPACE:
						self.user_text = self.user_text[:-1]  # Remove last character
					else:
						self.user_text += event.unicode

			self.screen.fill((0, 0, 0))

			#text_width = max(350, self.base_font.size(self.user_text)[0] + 10)
			#self.rect.w = text_width

			#pygame.draw.rect(self.screen,self.color,self.rect,2)

			text_surfaceFixed = self.base_font.render(self.fix_text, True, (255, 255, 255))
			self.screen.blit(text_surfaceFixed, (0, self.leftConer_y+10))

			# Render existing lines
			y_offset = 20
			for line in self.text_lines:
				text_surface = self.base_font.render(line, True, (255, 255, 255))
				 # Adjust vertical offset
				y_offset += text_surface.get_height() 
				self.screen.blit(text_surface, (170,y_offset))
			# Render the current line being typed
			current_text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
			self.screen.blit(current_text_surface,(20,50)) #( self.rect.x + 5, self.rect.y + 5))

			if current_text_surface.get_width() >= 600:
				self.text_lines.append(self.user_text)
				self.user_text = ""
				

			pygame.display.flip()
			self.clock.tick(60)


