from tkinter import Tk, Canvas, Frame, Label ,Button
from PIL import Image, ImageTk
import sys
import pygame
import random
from MiniGame_One import MiniGame_One 
from MiniGame_Two import MiniGame_Two 
from input_text import InputText
from flappy_bird import flappyBird


boardsize=24
qsize=6
board_code =["&","x","_","+","_","x"]*4



ROWS,COLS = 7,7 
WIDTH, HEIGHT = 100,100
SQUARE_SIZE = 100  

SQUARE_SIZE_X = WIDTH // COLS 
SQUARE_SIZE_Y = WIDTH // COLS 


# Define color constants
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)

class Player:
    image_path_temp =""
    def __init__(self,tempplayernumber):               
        if tempplayernumber==1:
            self.pos =0
            image_path_temp = "images\playerOne.png"
            self.grid=(0,0)
        if tempplayernumber==2:
            self.pos =6
            image_path_temp = "images\playerTwo.png"
            self.grid=(6,0)
        if tempplayernumber==3:
            self.pos =12
            image_path_temp = "images\playerThree.png"
            self.grid=(6,6)
        if tempplayernumber==4:
            self.pos =18
            image_path_temp = "images\playerFour.png"
            self.grid=(0,6)

        self.coins=0
        self.min_roll=1
        self.max_roll=6
        self.movesToWin=boardsize
        self.playnum=tempplayernumber
        original_image_temp = Image.open(image_path_temp)
        resized_image_temp = original_image_temp.resize((SQUARE_SIZE-50, SQUARE_SIZE-50))           
        self.image =ImageTk.PhotoImage(resized_image_temp)
            
    #function position 
    
    def setgrid(self):
        #roll=1   
        global boardsize, qsize # Add player_positions to the list of global variables
        #self.pos=(self.pos+roll)%boardsize

        fliped=(self.pos>=(qsize*2))
        temp=self.pos%(qsize*2)
        if fliped:
            temp=(qsize*2)-temp
        fi,si=0,0
        if temp < qsize:
            fi=0
            si=temp%qsize
        elif temp == qsize*2:
            fi=qsize
            si=qsize
        else:
            fi=temp%qsize
            si=qsize
        if fliped:
            self.grid = (fi,si)  #player_four position update
        else:
            self.grid = (si,fi)


    def move(self,x):
        self.pos= (self.pos+x)%boardsize
        self.movesToWin-=x
        self.setgrid()
    
    def position(self):
        self.x =self.grid[0]   # x position 
        self.y =self.grid[1]    #y position
        
    def lose_coins(self,x):
        if self.coins>=x:
            self.coins-=x
        else:
            self.move(self.coins-x)
            self.coins=0

    def roll(self):
        return random.randrange(self.min_roll,self.max_roll)
        

    def draw(self,rect,player):  #load the image on the board on the giving position by the function position
        if player==1:
            rect.create_image(50, 50, anchor="nw", image=self.image)
        if player==2:
            rect.create_image(0, 50, anchor="nw", image=self.image)
        if player==3:
            rect.create_image(0, 0, anchor="nw", image=self.image)
        if player==4:
            rect.create_image(50, 0, anchor="nw", image=self.image)    


class EndTurnButton(Button):
    def __init__(self,root,my_button_move):
        super().__init__(root,text="End Turn ",command=self.on_button_click,width=10,height=3)
        self.my_button_move=my_button_move

    def on_button_click(self):
        self.grid_remove()
        self.my_button_move.grid(row=ROWS // 2, column=COLS // 2)
"""        
class PlayButton(Button):
    def __init__(self, root):
        # Call the constructor of the base class (Button)
        super().__init__(root, text="Play ", command=self.on_button_click,width=10,height=3)
        self.gameWon = False
        self.button_move = MyButtonMove(root,False,text="Move")
        self.button_move.grid(row=ROWS//2, column=COLS//2)
        self.button_move = MyButtonMove(root,False,text="Move")
        self.button_move.grid(row=(ROWS//2)+1, column=COLS//2)
        self.endTurn = False
        self.row=0
        self.col=0


    def on_button_click(self):
        pass

    


    def getendTurn(self):
        return self.endTurn

class MyButtonMove(Button):
    def __init__(self, root,endTurn,text="Play "):
        # Call the constructor of the base class (Button)
        super().__init__(root, text=text, command=self.on_button_click,width=10,height=3)
        #self.player_positions = player_positions
        self.endTurn = endTurn
        #self.button_move = MyButtonMove(root,player_positions,False,text="Move")
        self.button_End = EndTurnButton(root,self)

    def getEndButton(self):
        return self.button_End 

    def on_button_click(self):
        roll=random.randrange(1,6)
        #roll=1
        # (roll)
        Ptemp=board.get_current_player()
        Ptemp.move(roll)
        if board_code[Ptemp.pos]=="x":
            Ptemp = red_land(Ptemp)
        Ptemp.setgrid()
        board.move_player(Ptemp.grid[1],Ptemp.grid[0],board.get_current_player_index()-1)
        board.set_current_player(Ptemp)
        if board_code[Ptemp.pos]=="&":
            Ptemp = blue_land()
        board.update_players()"""


class ButtonRoll(Button):
    def __init__(self, root,www,text="Play "):
        super().__init__(root, text=text, command=self.on_button_click,width=10,height=3)


    def on_button_click(self):
        board.rollFun()

class ButtonMove(Button):
    def __init__(self, root,www,text="Play "):
        super().__init__(root, text=text, command=self.on_button_click,width=10,height=3)


    def on_button_click(self):
        board.moveFun()

class ButtonEnd(Button):
    def __init__(self, root,www,text="Play "):
        super().__init__(root, text=text, command=self.on_button_click,width=10,height=3)


    def on_button_click(self):
        board.endFun()
        

class Board:
    def __init__(self,menu,num_of_players_in=3):
        self.num_of_players=num_of_players_in
        self.menu=menu
        self.PLAYERS=[]
        for x in range(self.num_of_players):
            self.PLAYERS.append(Player(x+1))
        self.board = [] # Initialize an empty list to represent the game board.
        #self.player_positions = [(0, 0), (6,0), (6, 6), (0,6)]    
        self.squares = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.create_board(0,0)
        self.draw_squares()
        #root.bind("<Key>", self.on_key_press)
        self.gameWon = False
        #self.buttonPlay= MyButtonMove(root,False,"Move",self)
        #self.buttonPlay.grid(row=ROWS//2, column=COLS//2)
        self.buttonTop= ButtonRoll(root,1,text="roll")
        self.buttonTop.grid(row=ROWS//2, column=COLS//2)
        self.stage=1
        self.current_player_index = 1
        self.roll=0
        self.label = Label(root, text="Turn Player 1", bg="#D3D3D3",padx=10, pady=10)
        self.labelTwo = Label(root, text="Blue", bg="#D3D3D3",padx=10, pady=10)
        self.labelWin = Label(root, text="You Have Won ", bg="#D3D3D3",padx=10, pady=10)
        self.sideLabel= Label(root)
        self.labelPlayer(self.current_player_index)


    def stage1(self):
        self.buttonTop= ButtonRoll(root,1,text="roll")
        self.buttonTop.grid(row=ROWS//2, column=COLS//2)
        self.buttonBot.destroy()
        self.sideLabel.destroy()
        self.stage=1

    def stage2(self):
        self.buttonTop.destroy()
        self.buttonTop= ButtonMove(root,1,text="move")
        self.buttonTop.grid(row=ROWS//2, column=COLS//2)
        self.buttonBot= ButtonEnd(root,1,text="end")
        self.buttonBot.grid(row=(ROWS//2)+1, column=COLS//2)
        self.sideLabel=Label(root, text=str(self.roll), bg="#D3D3D3",padx=10, pady=10)
        self.sideLabel.grid(row=3, column=2,columnspan=2,sticky='nw')
        self.stage=2

    def stage3(self):
        self.buttonTop= ButtonEnd(root,1,text="end")
        self.buttonTop.grid(row=ROWS//2, column=COLS//2)
        self.buttonBot.destroy()
        self.stage=3
        self.sideLabel.destroy()
    
    def stageChange(self):
        if self.stage==1:
            self.stage2()
        elif self.stage==2:
            self.stage3()
        elif self.stage==3:
            self.stage1()

    def rollFun(self):
        self.roll=self.PLAYERS[self.current_player_index-1].roll()
        #self.roll=60
        self.stage2()

    def moveFun(self):
        self.PLAYERS[self.current_player_index-1].move(1)
        board.move_player()
        self.roll-=1
        self.sideLabel.config(text=str(self.roll))
        #self.sideLabel=Label(root, text=str(self.roll), bg="#D3D3D3",padx=10, pady=10)
        if self.roll==0:
            self.stage3()

    def endFun(self):
        Ptemp=self.PLAYERS[self.current_player_index-1]
        if board_code[Ptemp.pos]=="x":
            Ptemp = red_land(Ptemp)
        elif board_code[Ptemp.pos]=="&":
            Ptemp = blue_land(Ptemp)
        elif board_code[Ptemp.pos]=="+":
            Ptemp = green_land(Ptemp)
            
        board.move_player()
        board.update_players()
        self.stage1()




    def get_current_player_index(self):
        return self.current_player_index
    
    def get_current_player(self):
        return self.PLAYERS[self.current_player_index-1]
    
    def set_current_player(self,temp):
        self.PLAYERS[self.current_player_index-1]=temp
        if  self.PLAYERS[self.current_player_index-1].movesToWin<=0:
            self.buttonPlay.destroy()
            #pygame.quit()
            #sys.exit()

    def swap_current_player(self):
        # Toggle the current player's index (0 to 1, 1 to 0)
        self.current_player_index = 2 if self.current_player_index == 1 else 1


    def update_players(self):
        if self.PLAYERS[self.current_player_index-1].movesToWin<=0:
            self.buttonBot.destroy()
            self.buttonTop.destroy()
            self.sideLabel.destroy()
            #self.labelWin.grid(row=3, column=3,columnspan=3,sticky='nw')
            self.redraw_board()
            self.__init__(self.menu)
            self.open_mainMenuAgain()
        self.current_player_index += 1
        if self.current_player_index>self.num_of_players:
            self.current_player_index = 1
        self.labelPlayer(self.current_player_index)


    def getPlayButton(self):
        return self.buttonPlay
    

    def draw_squares(self):
        for rows in range(ROWS):
            for col in range (COLS):
                if  col == 0 or (rows < 1) or col == COLS-1 or rows>ROWS-2:
                    if col in range (rows%2==0,COLS,2): 
                        colorBg="red"
                    else:
                        colorBg="black"
                else:
                    colorBg="white"
                rect = Canvas(root, width=SQUARE_SIZE, height=SQUARE_SIZE, bg=colorBg)
                rect.grid(row=rows, column=col)
                self.squares[rows][col]=rect
                frame = Frame(root, bg="yellow", width=100, height=100)
                frame.grid(row=ROWS//2, column=COLS//2)
        self.redraw_board()
    
    def create_board(self,row,col):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if (row, col) in [(0, 0), (0, 6), (6, 6), (6, 0)]:
                    # (str(row)+" "+str(col))
                    for x in self.PLAYERS:
                        self.board[row].append(x)
                else:
                    self.board[row].append(0)
        
    def move_player(self):
        self.player_positions=[]
        for x in self.PLAYERS:
            self.player_positions.append(x.grid)

        self.redraw_board()    

    def redraw_board(self,fillerBg="white"):
        # Redraw the board with updated player position

        for row in range(ROWS):
            for col in range(COLS):
                if  col == 0 or (row < 1) or col == COLS-1 or row>ROWS-2:
                    if col in range (row%2==0,COLS,2): 
                        colorBg="red"
                    else:
                        colorBg="black"
                else:
                    colorBg="white"
                if (col==0 and row==0)or(col==0 and row==6)or(col==6 and row==0)or(col==6 and row==6):
                    colorBg="blue"
                if ((col+row==3)and(col==0 or row==0)) or ((col+row==9)and(col==6 or row==6)):
                    colorBg="green"
                rect = self.squares[row][col]
                rect.config(bg=colorBg)
                rect.delete("all")
                #player 1
                count=0
                for x in self.PLAYERS:
                    canvas_widget=self.squares[x.grid[1]][x.grid[0]]
                    if count ==0:
                        canvas_widget.create_image(0, 0, anchor="nw", image=x.image)
                    if count ==1:
                        canvas_widget.create_image(50, 0, anchor="nw", image=x.image)
                    if count ==2:
                        canvas_widget.create_image(50, 50, anchor="nw", image=x.image)
                    if count ==3:
                        canvas_widget.create_image(0, 50, anchor="nw", image=x.image)
                    count=count+1


    
    def labelPlayer(self,currentPlayer):
            if currentPlayer==1:
                self.label.grid(row=1, column=1,columnspan=2,sticky='nw')
                self.labelTwo.grid(row=1, column=1,columnspan=2,sticky='sw')
                self.labelTwo.config(text="Blue")
            elif currentPlayer==2:
                self.label.grid(row=1, column=5,columnspan=2,sticky='nw')
                self.labelTwo.grid(row=1, column=5,columnspan=2,sticky='sw')
                self.labelTwo.config(text="Green")
            elif currentPlayer==3:
                self.label.grid(row=5, column=5,columnspan=2,sticky='nw')
                self.labelTwo.grid(row=5, column=5,columnspan=2,sticky='sw')
                self.labelTwo.config(text="Red")
            elif currentPlayer==4:
                self.label.grid(row=5, column=1,columnspan=2,sticky='nw')
                self.labelTwo.grid(row=5, column=1,columnspan=2,sticky='sw')
                self.labelTwo.config(text="Yellow")
            self.label.config(text="Turn Player "+str(self.current_player_index))


    
    def open_mainMenuAgain(self):
        #board.reset_game()
        self.menu.__init__()
        root.destroy()
        self.menu.main_menu()
        #root.quit()


        



def blue_land(player):


    rand=random.randrange(1,4)




    def blue_land_1():
        rand=random.randrange(1,4)
        itt= InputText("what player would you like to move back")
        aceptable=["1","2","3","4"]
        if itt.getInput() in aceptable:
            Ptemp=board.PLAYERS[int(itt.getInput())]
            #board.move_player(Ptemp.grid[1],Ptemp.grid[0],int(itt.getInput()))
            board.PLAYERS[int(itt.getInput())-1].move(-5)
            board.move_player()
            #board.PLAYERS[int(itt.getInput())]=Ptemp
        else:
            i= InputText("invalid input "+itt.getInput())
        return player
    
    def blue_land_2():
        temp_coins=player.coins
        player.move(temp_coins-5)
        return player

    
    def blue_land_3():
        rand=random.randrange(1,11)
        itt= InputText("make a guess x if guess is under random number move forward x if its over move backwards x")
        aceptable=["1","2","3","4","5","6","7","8","9","10"]
        if itt.getInput() in aceptable:
            x= int(itt.getInput())
            if x>rand:
                itt= InputText("you guesed over the random number was "+str(rand)+" moving back "+str(x))
                player.move(-x)
            else:
                itt= InputText("you guesed under the random number was "+str(rand)+" moving forward "+str(x))
                player.move(x)
        else:
            i= InputText("invalid input "+itt.getInput())
        return player
    
    if rand==1:
        t = InputText("move other")

        return blue_land_1()
    elif rand==2:
        t = InputText("purse check")
        return blue_land_2()
    elif rand==3:
        t = InputText("test your luck minigame")
        return blue_land_3()
    else:

        return player
        
def red_land(player):


    rand=random.randrange(1,4)



    def red_land_1():
        rand=random.randrange(1,4)
        if rand==1:
            game = MiniGame_One()
        elif rand==2:
            game = MiniGame_Two()
        elif rand==3:
            game = flappyBird()
        else:
             ("HGBI*YGBI*YB")

        game.Play_Mini()
        if game.getWon():
            player.coins+=1
            return player
        player.move(-3)
        return player
    
    def red_land_2():
        temp_coins=player.coins
        player.lose_coins(4)
        player.coins=temp_coins
        return player

    
    def red_land_3():
        rand=random.randrange(1,4)
        if rand==1:
            game = MiniGame_One()
        elif rand==2:
            game = MiniGame_Two()
        elif rand==3:
            game = flappyBird()
        else:
             ("HGBI*YGBI*YB")

        game.Play_Mini()
        if game.getWon():
            player.coins+=1
            return player
        player.lose_coins(5)
        return player
    
    if rand==1:
        t = InputText("move back minigame")

        return red_land_1()
    elif rand==2:
        t = InputText("purse check minigame")
        return red_land_2()
    elif rand==3:
        t = InputText("lose coins minigame")
        return red_land_3()
    else:

        return player

def green_land(player):


    rand=random.randrange(1,4)
    rand=3


    def green_land_1():
        rand=random.randrange(1,4)

        player.coins+=rand
        t = InputText("you gained "+str(rand)+" coins")
        return player
   
    def green_land_2():
        rand=random.randrange(1,4)
        if rand==1:
            game = MiniGame_One()
        elif rand==2:
            game = MiniGame_Two()
        elif rand==3:
            game = flappyBird()
        else:
             ("HGBI*YGBI*YB")

        game.Play_Mini()
        if game.getWon():
            player.coins+=4
            return player
        player.lose_coins(1)
        return player
    
    def green_land_3():
        t = InputText("welcome to the shop you have  "+str(player.coins)+" coins")
        t = InputText("enter 1 to move forward 5 spaces for 3 coins or enter 2 to add 1 to your rolls for 4 coins, enter 3 to pruchase neither")
        aceptable=["1","2","3"]
        if t.getInput() in aceptable:
            x=t.getInput()
            if x=="1":
                if player.coins<3:
                    t = InputText("insufisent funds you only have  "+str(player.coins)+" coins")
                    return player
                player.lose_coins(3)
                player.move(5)
            elif x=="2":
                if player.coins<4:
                    t = InputText("insufisent funds you only have  "+str(player.coins)+" coins")
                    return player
                player.lose_coins(4)
                player.min_roll+=1
                player.max_roll+=1
        else:
            i= InputText("invalid input "+t.getInput())
        return player
    
    if rand==1:
        return green_land_1()
    elif rand==2:
        t = InputText("money gain minigame")
        return green_land_2()
    elif rand==3:
        t = InputText("shop")
        return green_land_3()
    else:

        return player


    
info = pygame.display.Info()

# Get screen width and height
screen_width = info.current_w
screen_height = info.current_h

# Calculate the center of the screen
center_x = screen_width // 2
center_y = screen_height // 2

#i=InputText()

def play(menu,players):
    global root
    global  board
    root = Tk()
    root.title("Board")
    board = Board(menu,players)
    root.mainloop()

