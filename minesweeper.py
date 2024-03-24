import pygame
import pygame.freetype
import pygame.sprite
from datetime import datetime
from field import Field

beginner,intermediate,expert = (10,9,9),(40,16,16),(99,30,16)
values=["empty", "1","2","3","4","5","6","7","8","mine","flag","hidden"]
            
class MinesweeperBoard():
        
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("MineSweeper")

        self.game_font = pygame.font.SysFont("Comic Sans MS", 24)
        self.game_freefont = pygame.freetype.SysFont("Comic Sans MS", 24)

        self.init_2(beginner)
            
    def init_2(self,difficulty):
        self.difficulty=difficulty
        self.game_screen = pygame.display.set_mode((difficulty[1]*30+10, 80+difficulty[2]*30+10))
        self.game_screen.fill((224,224,224))

        self.beginner_text_area=pygame.draw.rect(self.game_screen, (0,0,0), (0,0,0,0)) 
        self.intermediate_text_area=pygame.draw.rect(self.game_screen, (0,0,0), (0,0,0,0)) 
        self.expert_text_area=pygame.draw.rect(self.game_screen, (0,0,0), (0,0,0,0)) 
        
        self.game_clock = datetime.now()
        self.clock_start = datetime.now()
        
        self.field= Field(values,self.difficulty)

        self.gameLoop()
        
    # This is the game loop which controlls the whole game
    def gameLoop(self):
        end="Tie"
        game_on=False
        
        while True:
            if game_on == True:
                self.game_clock = datetime.now()
                        
            for buttonPress in pygame.event.get():    
                if buttonPress.type == pygame.QUIT:
                    exit()   
                
                if buttonPress.type == pygame.KEYDOWN:
                    if buttonPress.key == pygame.K_ESCAPE:
                        exit()
                    
                if buttonPress.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    buttons_pressed=pygame.mouse.get_pressed()
                    
                    # Check if game size if modified
                    if mouse_position:
                        if self.beginner_text_area.collidepoint(mouse_position)==True:
                            self.init_2(beginner)
                        elif self.intermediate_text_area.collidepoint(mouse_position)==True:
                            self.init_2(intermediate)
                        elif self.expert_text_area.collidepoint(mouse_position)==True:
                            self.init_2(expert)
                                  
                    #if game area is clicked
                    if game_on == True or ((game_on == False) and (end=="Tie")):
                        
                        for y in range(0,len(self.field.fieldtable)):
                            for x in range(0,len(self.field.fieldtable[y])):
                                # Check from block if it is clicked
                                value=self.field.fieldtable[y][x].check_click(mouse_position)
                                if value==True:
                                    if game_on == False:
                                        self.clock_start=datetime.now()
                                        end="Lose"
                                        game_on = True
                                        
                                    print(f"value : {value}")  
                                    if buttons_pressed==(True,False,False):
                                        game_on=self.field.handleclick("Left",x,y)
                                    elif buttons_pressed==(False,False,True):
                                        game_on=self.field.handleclick("Right",x,y)
                                    elif buttons_pressed==(True,False,True):
                                        game_on=self.field.handleclick("Both",x,y)
            
                        #check clicks and game state
                        if game_on==False:
                            end="Lose"
                            print("clicks")
                            break
                        
                        if self.field.checkTilesForEnd()==False:
                            end="Win"
                            print("tiles")
                            game_on=False
                            break
            
            #draw screen
            self.drawscreen() 
        
        if end=="Win":
            print("Onneksi olkeoon löysit pommit")
        else:
            print("peli loppui pommin räjähdykseen")

    #draw actual game screen
    def drawscreen(self):
        
        self.game_screen.fill((224,224,224))
        self.beginner_text_area=pygame.draw.rect(self.game_screen, (199,199,199), (5, 5, 70, 20))  
        self.game_freefont.render_to(self.game_screen,(10,10),"Beginner" ,(0,0,0),size=15)
        self.intermediate_text_area=pygame.draw.rect(self.game_screen, (199,199,199), (90, 5, 105, 20)) 
        self.game_freefont.render_to(self.game_screen,(95,10),"Intermediate" ,(0,0,0),size=15)
        self.expert_text_area=pygame.draw.rect(self.game_screen, (199,199,199), (210, 5, 60, 20)) 
        self.game_freefont.render_to(self.game_screen,(215,10),"Expert" ,(0,0,0),size=15)
        
        
        pygame.draw.rect(self.game_screen, (199,199,199), (10, 32, 60, 45))  
        self.game_freefont.render_to(self.game_screen,(20,40),f"{self.field.mines_left}" ,(255,0,0),size=40)
        
        pygame.draw.rect(self.game_screen, (199,199,199), (((self.difficulty[1]*30-80), 32, 80, 45)) )
        if self.game_clock != 0:
            self.game_freefont.render_to(self.game_screen,((self.difficulty[1]*30-75),40),f"{(self.game_clock-self.clock_start).seconds:03d}" ,(255,0,0),(139,130,109), 0, 0,40)
        else:
            self.game_freefont.render_to(self.game_screen,((self.difficulty[1]*30-75),40),"000" ,(255,0,0),(139,130,109), 0, 0,40)
        
        for y in self.field.fieldtable:
            for x in y:
                self.game_screen.blit(x.current, (x.rect.x, x.rect.y))
            
        pygame.display.flip()
       
if __name__ == "__main__":
    
    MinesweeperBoard()