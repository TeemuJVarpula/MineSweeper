import random
from datetime import datetime
from block import Block

class Field ():
    values=[]
    checkedTiles=[]
        
    def __init__(self,values:list,difficulty:tuple):
        self.values=values
        self.difficulty=difficulty
        self.fieldtable=[]
        self.mines=[]
        self.mines_left=difficulty[0]
        
        if len(Field.values)==0:
            Field.values=values
            
        self.preparefield()
        
    def preparefield(self):
        place_x = 5
        place_y = 35
            
        self.mines=self.randomizeMines()
        self.insertFieldAndMines(place_x,place_y)
        self.checkNeighbourindexes()
        
                    
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
    
    def insertFieldAndMines(self,place_x:int,place_y:int):
        for y in range(0,self.difficulty[2]):
            if len(self.fieldtable)==y:
                self.fieldtable.append([])
            
            for x in range(0,self.difficulty[1]):
                temp_block=Block(self.values,x,y,place_x+x*30, 50+place_y+y*30)
                     
                if (x,y) in self.mines:
                    temp_block.markMine()
                                
                self.fieldtable[y].append(temp_block)
    
    def checkNeighbourindexes(self):
        for y in range (0,self.difficulty[2]):
            for x in range (0,self.difficulty[1]):
                #if current tile is not a mine
                if self.fieldtable[y][x].tile!=self.values.index("mine"):
                    #Check neighbours
                    self.fieldtable[y][x].neighbours=self.checkNeighbours((x,y))
                    
                    xcounter=0
                    # Going through neighbours and counting mines
                    for neighbour in self.fieldtable[y][x].neighbours:
                        if neighbour in self.mines:
                            xcounter+=1
                    
                    # Mark tile with corresponding neighbour mines amount                     
                    self.fieldtable[y][x].markNeighbours(xcounter)
    


    def checkNeighbours(self,position:tuple):
        templist=[]
        
        # Check if x is the smallest one
        if position[0]==0:
            xstart=position[0]
        else:
            xstart=position[0]-1
            
        # Check if x is the biggest one    
        if position[0]==self.difficulty[1]-1:
            xend=position[0]
        else:
            xend=position[0]+1

        # Check if y is the smallest one
        if position[1]==0:
            ystart=position[1]
        else:
            ystart=position[1]-1
            
        # Check if x is the biggest one
        if position[1]==self.difficulty[2]-1:
            yend=position[1]
        else:
            yend=position[1]+1
            
        # Going throught all possible neighbours
        for y in range (ystart,yend+1):
            for x in range (xstart,xend+1):
                #print(f"checkNeighbours2 (value):({x},{y})")
                templist.append((x,y)) 
                
        templist.pop(templist.index(position))
                
        return templist
    
    def openTiles(self,value:tuple):
        
        neighbourslist=self.checkNeighbours((value[0],value[1]))
        sortedneighbours=[neighbour for neighbour in neighbourslist if (neighbour[0],neighbour[1]) not in Field.checkedTiles] 
        
        if len(sortedneighbours)>0:
            for neighbour in sortedneighbours:
                temp_tile=self.fieldtable[neighbour[1]][neighbour[0]]
                if temp_tile.tile == Field.values.index("empty") and temp_tile.current == temp_tile.pictures[Field.values.index("hidden")]:
                        temp_tile.openTile()
                        Field.checkedTiles.append((temp_tile.index_x,temp_tile.index_y))
                        self.openTiles(neighbour)
                elif temp_tile.tile != Field.values.index("mine") and temp_tile.tile != Field.values.index("hidden") and temp_tile.current == temp_tile.pictures[Field.values.index("hidden")]:
                        temp_tile.openTile()
                        Field.checkedTiles.append((temp_tile.index_x,temp_tile.index_y))
       
    def handleclick(self,type=str,x=int,y=int):
        cur_block=self.fieldtable[y][x]

        if type == "Left":
            cur_block.current=Block.pictures[cur_block.tile]
            if cur_block.tile == Field.values.index("mine"):
                return False
            elif cur_block.tile == Field.values.index("empty"):    
                self.openTiles((cur_block.index_x,cur_block.index_y))          
                if cur_block.tile == Field.values.index("empty"):
                    Field.checkedTiles=[]
                return True
            else: 
                return True
        elif type== "Right":
            print(f"{type},{x},{y}")
            if cur_block.markFlag()==True: # flag inserted
                self.mines_left-=1
            else:                  # Flag removed
                self.mines_left+=1
            return True
        elif type== "Both":
            if cur_block.tile != Field.values.index("empty"):
                if cur_block.markFlag()==True:
                    print("pöö")
                else:
                    print("puu")
            return True
    
    def checkTilesForEnd(self):
        for y in self.fieldtable:
            for x in y:
                if x.current == x.pictures[(Field.values.index('hidden'))]:
                    return True
        
        if self.mines_left==0:
            return False
        else:
            return True
          
                        