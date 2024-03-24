import pygame

class Block():
    pictures=[]
    values=[]
    
    def __init__(self,values,x:int,y:int,coord_x:int,coord_y:int):
        pygame.sprite.Sprite.__init__(self)
        self.tile=values.index("hidden")
        self.neighbours=[]
        
        if len(Block.values)==0:
            Block.values=values
            for name in Block.values:
                Block.pictures.append(pygame.image.load(name + ".png")) 
                
        
        self.current=self.pictures[values.index("hidden")]
        self.rect = self.current.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y
        self.index_x=x
        self.index_y=y
    
    # Mark block as mine    
    def markMine(self):
        self.tile=Block.values.index("mine")
        
    # Mark block with amount of neighbour mines
    def markNeighbours(self,value:int):
        self.tile=value
    
    
    
    
    # Mark block as possible mine with flag or take flag away return True if Flag marked
    def markFlag(self):
        if self.current == Block.pictures[Block.values.index("hidden")]:
            self.current = Block.pictures[Block.values.index("flag")]
            return True
        elif self.current == Block.pictures[Block.values.index("flag")]:
            self.current = Block.pictures[Block.values.index("hidden")]
            return False
        else:
            return False
       
    def openTile(self):
        self.current=Block.pictures[self.tile]
        
    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):   
            return True
        return False
    
    def state(self):
        return self.tile