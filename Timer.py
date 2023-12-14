import time
import pygame
import sys

# Set the timer duration in seconds
class Timer():

    def __init__(self,timer_duration,screen,size):
        self.timer_duration=timer_duration
        self.screen=screen
        self.start_time = time.time()
        self.size=size
    
    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("images\Font.ttf", size)

    def run_timer(self):
        pygame.font.init()
        while True:
            elapsed_time = time.time() -self.start_time 
            remaining_time = self.timer_duration - elapsed_time
            TIME_MSG = Timer.get_font(self.size).render(f"Time remaining: {remaining_time:.2f} seconds", True, "green")
            TIME_RECT=TIME_MSG.get_rect(center=(650,10))
            self.screen.blit(TIME_MSG,TIME_RECT)
            if remaining_time <= 0:
                return True
            return False
    
    def win_game(self):
        pygame.font.init()
        while True: 
            self.screen.fill("white")

            WIN_TEXT=Timer.get_font(40).render("You have won",True,"Blue")
            WIN_RECT=WIN_TEXT.get_rect(center=(400, 260))
            self.screen.blit(WIN_TEXT,WIN_RECT)

            WIN_TEXTTWO =Timer.get_font(20).render("Click the window to continue", True, "Blue")
            WIN_RECTTWO=WIN_TEXT.get_rect(center=(450, 360))
            self.screen.blit(WIN_TEXTTWO,WIN_RECTTWO)


            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    return True
            #time.sleep(1)
            pygame.display.update()

    def lost_game(self):
        pygame.font.init()
        while True: 
            self.screen.fill("white")

            LOST_TEXT=Timer.get_font(40).render("You lost the game ",True,"Blue")
            LOST_RECT=LOST_TEXT.get_rect(center=(400, 260))
            self.screen.blit(LOST_TEXT,LOST_RECT)

            LOST_TEXTTWO =Timer.get_font(20).render("Click the window to continue", True, "Blue")
            LOST_RECTTWO=LOST_TEXT.get_rect(center=(450, 360))
            self.screen.blit(LOST_TEXTTWO,LOST_RECTTWO)


            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    return True 

            pygame.display.update()
