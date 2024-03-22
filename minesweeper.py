import pygame
import pygame.freetype
import random
import pygame.sprite
from datetime import datetime

beginner,intermediate,expert = (10,9,9),(40,16,16),(99,30,16)
values=["empty", "1","2","3","4","5","6","7","8","bomb","flag","hidden"]
class Block(pygame.sprite.Sprite):
    def __init__(self,x:int,y:int,coord_x:int,coord_y:int):
        pygame.sprite.Sprite.__init__(self)
        
        self.tile=values.index("hidden")
        self.pictures=[]
        for name in values:
            self.pictures.append(pygame.image.load(name + ".png")) 
            
        self.current=self.pictures[values.index("hidden")]
        self.rect = self.current.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y
        self.index_x=x
        self.index_y=y
        
    def markMine(self):
        #self.current=self.pictures[values.index("bomb")]
        self.tile=values.index("bomb")
    
    def markFlag(self):
        if self.current == self.pictures[values.index("hidden")]:
            self.current = self.pictures[values.index("flag")]
            return True
        elif self.current == self.pictures[values.index("flag")]:
            self.current = self.pictures[values.index("hidden")]
            return False
        else:
            return False
            
        #self.tile=values.index("flag")
        
    def markNeighbours(self,value:int):
        #self.current=self.pictures[value]
        self.tile=value
        
    def openTile(self):
        self.current=self.pictures[self.tile]
        
    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):   
            return True
        return False
    
    def state(self):
        return self.tile
                
    
            
class MinesweeperBoard():
    screen_width=640
    screen_height=480
    checkedTiles=[]
        
    def __init__(self):
        pygame.init()
        self.game_screen = pygame.display.set_mode((MinesweeperBoard.screen_width, MinesweeperBoard.screen_height+20))
        self.game_screen.fill((224,224,224))
        self.game_font = pygame.font.SysFont("Comic Sans MS", 24)
        self.game_freefont = pygame.freetype.SysFont("Comic Sans MS", 24)
        self.game_clock = 0
        self.field=[]
        pygame.display.set_caption("MineSweeper")
        
        self.gameInfo()
        self.difficulty=self.ChooseDifficulty()
        self.mines_left = self.difficulty[0]
        self.preparefield()
        self.gameLoop()
    
    
    # This is the game loop which controlls the whole game
    def gameLoop(self):
        end="Lose"
        
        while True:
            #check clicks and game state
            if self.checkClicks()==False:
                end="Lose"
                print("clicks")
                break
            
            if self.checkTilesForEnd()==False:
                end="Win"
                print("tiles")
                break
            
            #draw screen again
            self.drawscreen() 
        
        if end=="Win":
            print("Onneksi olkeoon löysit pommit")
        else:
            print("peli loppui pommin räjähdykseen")
    
    def checkClicks(self):
        for buttonPress in pygame.event.get():
            if buttonPress.type == pygame.QUIT:
                #print("pygame.QUIT")
                exit()    
            if buttonPress.type == pygame.KEYDOWN:
                if buttonPress.key == pygame.K_ESCAPE:
                   # print("pygame.K_ESCAPE")
                    exit() 
            if buttonPress.type == pygame.MOUSEBUTTONDOWN:
                
                if self.game_clock == 0:
                    self.game_clock = datetime.now()
                mouse_position = pygame.mouse.get_pos()
                print(f"pygame.MOUSEBUTTONDOWN {pygame.mouse.get_pressed()}")
                buttons_pressed=pygame.mouse.get_pressed()
                for y in self.field:
                    for x in y:
                        value=x.check_click(mouse_position)
                        if value==True:
                            if buttons_pressed==(True,False,False):
                                x.current=x.pictures[x.tile]
                                print(f"1: {buttonPress.button}")
                                if x.tile == values.index("bomb"):
                                    return False
                                elif x.tile == values.index("empty"):    
                                    #print(f" (x,y):{x.index_x},{x.index_y} checkClicks Value: {value}")
                                    self.openTiles((x.index_x,x.index_y))          
                                    if x.tile == values.index("empty"):
                                        self.checkedTiles=[]  
                                else: 
                                    return True
                            elif buttons_pressed==(False,False,True):
                                print(f"3: {buttonPress.button}")
                                if x.markFlag()==True: # flag inserted
                                    self.mines_left-=1
                                else:                  # Flag removed
                                    self.mines_left+=1
                                return True
                            elif buttons_pressed==(True,False,True):
                                if x.tile != values.index("empty"):
                                    if x.markFlag()==True:
                                        self.mines_left-=1
                                    else:
                                        self.mines_left+=1
                                    return True
                                print(f"1,3: Pressed ")
        return True
    
    def checkTilesForEnd(self):
        for y in self.field:
            for x in y:
                if x.current == x.pictures[(values.index('hidden'))]:
                    return True
        
        if self.mines_left==0:
            return False
        else:
            return True
          
    def gameInfo(self):
        loop_continue=True
        
        self.game_screen.fill((224,224,224))
        
        self.game_freefont.render_to(self.game_screen, (160, 150), "Welcome to Minesweeper game",None,)
        
        #teksti = self.game_font.render("New game", True, (0, 0, 0))
        newGame_text_area=pygame.draw.rect(self.game_screen, (200,200,200), ((245, 245), (140,34)))
        self.game_freefont.render_to(self.game_screen, (260, 250), "New game",None)
        
        exit_text_area=pygame.draw.rect(self.game_screen, (200,200,200), ((285, 295),(55,30)))
        self.game_freefont.render_to(self.game_screen,(290,300), "Exit",None)
        
        pygame.display.flip()
                
        while loop_continue==True:
            for buttonPress in pygame.event.get():    
                if buttonPress.type == pygame.QUIT:
                    exit()   
                
                if buttonPress.type == pygame.KEYDOWN:
                    if buttonPress.key == pygame.K_ESCAPE:
                        exit()
                    
                if buttonPress.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    #print(f"{mouse_position} {buttonPress.type}") 
                    if mouse_position:
                        if newGame_text_area.collidepoint(mouse_position)==True:
                            loop_continue=False
                        elif exit_text_area.collidepoint(mouse_position)==True:
                            exit()

            
    def ChooseDifficulty(self):
        
        self.game_screen.fill((220,224,224))
        
        self.game_freefont.render_to(self.game_screen, (220, 150), "Choose difficulty")
        
        #teksti = self.game_font.render("New game", True, (0, 0, 0))
        easy_text_area=pygame.draw.rect(self.game_screen, (200,200,200), ((245, 225), (140,34)))
        self.game_freefont.render_to(self.game_screen, (285, 230), "Easy")
       
        medium_text_area=pygame.draw.rect(self.game_screen, (200,200,200), ((245, 275),(140,34)))
        self.game_freefont.render_to(self.game_screen,(275,280), "Medium")
        
        hard_text_area=pygame.draw.rect(self.game_screen, (200,200,200), ((245, 325),(140,34)))
        self.game_freefont.render_to(self.game_screen,(285,330), "Hard")
        
        pygame.display.flip()
        
        while True:
            for buttonPress in pygame.event.get():    
                if buttonPress.type == pygame.QUIT:
                    #print(f"{buttonPress.type} pygame.QUIT") 
                    exit(0)    
                if buttonPress.type == pygame.KEYDOWN:
                    #print(f"{buttonPress.key} pygame.KEYDOWN") 
                    if buttonPress.key == pygame.K_ESCAPE:
                        exit()
                
                if buttonPress.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    #print(f"{mouse_position} pygame.MOUSEBUTTONDOWN") 
                    if mouse_position:
                        if easy_text_area.collidepoint(mouse_position)==True:
                            self.game_screen = pygame.display.set_mode(((9*30+10), 50+(9*30+10)))
                            return beginner
                        elif medium_text_area.collidepoint(mouse_position)==True:
                            self.game_screen = pygame.display.set_mode(((16*30+10), 50+(16*30+10)))
                            return intermediate
                        elif hard_text_area.collidepoint(mouse_position)==True:
                            self.game_screen = pygame.display.set_mode(((30*30+10), 50+(16*30+10)))
                            return expert
                        
    def randomizeMines(self):
        mines=[]
        for i in range(0,self.difficulty[0]):
            tryAgain=True
            
            while tryAgain==True:
                x=random.randint(0,self.difficulty[1]-1)
                y=random.randint(0,self.difficulty[2]-1)
                minePlace=(x,y)
                
                if minePlace not in mines:
                    mines.append(minePlace)
                    tryAgain=False
        return mines
    
    def preparefield(self):
        
        place_x = 5
        place_y = 5
            
        #mines=[(6, 0), (1, 4), (8, 1), (8, 7), (0, 5), (2, 4), (3, 4), (5, 0), (4, 5), (6, 2)]
        mines=self.randomizeMines()
            
        for y in range(0,self.difficulty[2]):
            if len(self.field)==y:
                self.field.append([])
            
            for x in range(0,self.difficulty[1]):
                temp_block=Block(x,y,place_x+x*30, 50+place_y+y*30)
                     
                if (x,y) in mines:
                    temp_block.markMine()
                                
                self.field[y].append(temp_block)
        
        #print(f"mines: {mines}")
        for y in range (0,self.difficulty[2]):
            for x in range (0,self.difficulty[1]):
                if self.field[y][x].tile!=values.index("bomb"):
                    neighbourslist=self.checkNeighbours((x,y))
                   # print(f"neighbourslist: {neighbourslist}")
                    xcounter=0
                    for neighbour in neighbourslist:
                        if neighbour in mines:
                            xcounter+=1
                    
                    self.field[y][x].value = xcounter
                   # print(f"preparefield counter:{xcounter}")
                    self.field[y][x].markNeighbours(xcounter)
                     
    def drawscreen(self):
        self.game_screen.fill((224,224,224))
        pygame.draw.rect(self.game_screen, (199,199,199), (5, 5, ((self.difficulty[1])*30), 45))  
        self.game_freefont.render_to(self.game_screen,(10,10),f"{self.mines_left}" ,(255,0,0),(139,130,109), 0, 0,40)
        
        if self.game_clock != 0:
            self.game_freefont.render_to(self.game_screen,(200,10),f"{(datetime.now()-self.game_clock).seconds:03d}" ,(255,0,0),(139,130,109), 0, 0,40)
        
        for y in self.field:
            for x in y:
                self.game_screen.blit(x.current, (x.rect.x, x.rect.y))
            
        pygame.display.flip()
    
    def openTiles(self,value:tuple):
        
        #print(f"openTiles (value):({value[0]},{value[1]})")
        #print(f"checkedTiles {self.checkedTiles}")
        neighbourslist=self.checkNeighbours((value[0],value[1]))
        #print(f"neighbourslist {neighbourslist}")
        sortedneighbours=[neighbour for neighbour in neighbourslist if (neighbour[0],neighbour[1]) not in self.checkedTiles] 
        #print(f"sortedneighbours {sortedneighbours}")
        if len(sortedneighbours)>0:
            for neighbour in sortedneighbours:
                temp_tile=self.field[neighbour[1]][neighbour[0]]
                if temp_tile.tile == values.index("empty") and temp_tile.current == temp_tile.pictures[values.index("hidden")]:
                        #print(f"openTiles2 (value):({temp_tile.index_x},{temp_tile.index_x})")
                        temp_tile.openTile()
                        self.checkedTiles.append((temp_tile.index_x,temp_tile.index_y))
                        self.openTiles(neighbour)
                elif temp_tile.tile != values.index("bomb") and temp_tile.tile != values.index("hidden") and temp_tile.current == temp_tile.pictures[values.index("hidden")]:
                        #print(f"openTiles2 (value):({temp_tile.index_x},{temp_tile.index_x})")
                        temp_tile.openTile()
                        self.checkedTiles.append((temp_tile.index_x,temp_tile.index_y))
              
        
    def checkNeighbours(self,position:tuple):
        templist=[]
        
        #print(f"checkNeighbours (value):({position[0]},{position[1]})")
        if position[0]==0:
            xstart=position[0]
        else:
            xstart=position[0]-1
            
        if position[0]==self.difficulty[1]-1:
            xend=position[0]
        else:
            xend=position[0]+1


        if position[1]==0:
            ystart=position[1]
        else:
            ystart=position[1]-1

        if position[1]==self.difficulty[2]-1:
            yend=position[1]
        else:
            yend=position[1]+1
            
        for y in range (ystart,yend+1):
            for x in range (xstart,xend+1):
                #print(f"checkNeighbours2 (value):({x},{y})")
                templist.append((x,y)) 
                
        templist.pop(templist.index(position))
                
        return templist            
                
                
                
                
if __name__ == "__main__":
    
    MinesweeperBoard()