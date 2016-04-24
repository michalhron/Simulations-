#PERCOLATION MODEL
#MICHAL HRON
#April 24, 2016

import random
import pylab
import numpy

class Grid(object):
    def __init__(self,X,Y,P):
        self.X = X
        self.Y = Y
        self.P = P
        
        tempGrid = {}
        for x in range(self.getX()):
            for y in range(self.getY()):
                value = random.random()
                if value <= P:
                    value = True
                else:
                    value = False
                tempGrid[(x,y)]= (value,False)
        self.grid = tempGrid

    def getX(self):
        return self.X
        
    def getY(self):
        return self.Y
    
    def getGrid(self):
        return self.grid
        
    def getTiles(self):
        return self.grid.keys()
        
    def isValidTile(self,tile):
        if tile in self.getTiles():
            return True
        return False
        
    def getNextTiles(self,tile):
        nextOnes = []
        #is it a valid tile?
        if not self.isValidTile(tile):
            raise ValueError("Tile not in grid")
        x = tile[0]
        y = tile [1]
        
        #right under
        right_under = (x,y+1)
        if self.isTileLeakable(right_under):
            nextOnes.append(right_under)
        
        #right diagonal
        right_diag = (x+1,y+1)
        if self.isValidTile(right_diag) and self.isTileLeakable(right_diag):
            nextOnes.append(right_diag)
        
        #left diagonal
        left_diag = (x-1,y+1)
        if self.isValidTile(left_diag) and self.isTileLeakable(left_diag):
            nextOnes.append(left_diag)
        return nextOnes
        
    def isTileWet(self,tile):
        if not self.isValidTile(tile):
            raise ValueError("not valid tile")
        return self.getGrid()[tile][1]
        
        
    def isTileLeakable(self,tile):
        if not self.isValidTile(tile):
            return None
            
        return self.getGrid()[tile][0]
        
        
    def getWetPercentage(self):
        WetPercentage = 0.0
        for tile in self.getTiles():
            WetPercentage += int(self.isTileWet(tile))
        WetPercentage = WetPercentage / float(len(self.getGrid().values()))
        return WetPercentage
        
    def getLeakabilitypercentage(self):
        LeakabilityPercentage = 0.0
        for tile in self.getTiles():
            LeakabilityPercentage += int(self.isTileLeakable(tile))
        LeakabilityPercentage = LeakabilityPercentage / float(len(self.getGrid().values()))
        return LeakabilityPercentage

    def __str__(self):
        toPrint = "==GRID=="
        toPrint += "\n" + "Dimensions: " + str(self.getX())+" times " + str(self.getY()) +"\n"
        toPrint +=  "Simulated Leakability: " + str(self.getLeakabilitypercentage()) + " (Theoretical: " + str(self.P) +")" + "\n"
        if len(self.getTiles()) > 60:
            return toPrint
        for tile in self.getTiles():
            toPrint += '\n' +"POINT " + str(tile) +": Leaks: " + str(self.getGrid()[tile][0]) + ", Wet: " + str(self.getGrid()[tile][1])
        return toPrint
        
    def makeWet(self,tile):
        if not self.isValidTile(tile):
            pass
        tile_values = self.getGrid()[tile]
        if tile_values[0] == True and tile_values[1] == False:
            self.grid[tile] = (True,True)
            
    def Propagate(self,tile):
        if not self.isTileWet(tile):
            self.makeWet(tile)
        for t in self.getNextTiles(tile):
            self.makeWet(t)
            self.Propagate(t)
        
    def lastRowWet(self):
        wet_tiles = 0
        x_total = self.getX()
        y = self.getY() -1
        
        for x in range(x_total):
            this_tile = (x,y)
            if self.isTileWet(this_tile):
                wet_tiles +=1
        return wet_tiles > 0
        #return float(wet_tiles)/x_total
        
        
    def letItRain(self):
        #first row will be turned always
        y = 0
        for x in range(self.getX()):
            this_tile = (x,y)
            self.Propagate(this_tile)
            
            if self.isTileLeakable(this_tile):
                self.Propagate(this_tile)
                
        return self.lastRowWet()


    
def runSimulation(N,gridX,gridY,gridP):
    """
    takes Grid object, lets water propagate through from top to bottom
    returns list of results (number of ) 
    """
    
    results = []
    for take in range(N):
        grid = Grid(gridX,gridY,gridP)
        results.append(grid.letItRain())
    
    return sum(results)/float(len(results))
    
    
def multiSim(N,gridX,gridY,start,finish):
        results = []
        x_values = numpy.linspace(start,finish)
        for gridP in x_values:
            results.append(runSimulation(N,gridX,gridY,gridP))
        
        pylab.scatter(x_values,results)
        return results

