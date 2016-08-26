from random import randint
from collections import namedtuple, defaultdict
from time import sleep

    
class Board():
    
    def __init__(self, dim, pop):
        self.dim = dim
        self.alive = self.createPopulation(pop)

    def createPopulation(self, pop):
        alive = set()
        for i in range(0, pop):
            alive.add(Cell(x = randint(0,self.dim + 1), y = randint(0,self.dim + 1)))
        return alive
    
    def draw(self):
        #print(len(self.alive)) 
        xs = []     
        for cell in self.alive:
            xs.append(cell.x)
        ys = []
        for cell in self.alive:
            ys.append(cell.y)
        board_string = ""
        for y in range(min(ys), max(ys) +1 ):
            for x in range(min(xs), max(xs) + 1):
                board_string +="x" if Cell(x,y) in self.alive else " "
            board_string += "\n"
        print(board_string)

    def neighbours_dict(self, alive):
        neighbours_count = defaultdict(int)
        for cell in alive:
            for neighbour in cell.getNeighbours():
                neighbours_count[neighbour] += 1
       # print(len(neighbours_count))        
        return neighbours_count
        
    def evolution(self):            
        next_round_alive = set()
        for cell, count in self.neighbours_dict(self.alive).items():
            if count == 3:
                next_round_alive.add(cell)
            elif count == 2 and cell in alive:
                next_round_alive.add(cell)
                
        self.alive = next_round_alive 

    
class Cell():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getNeighbours(self):
        neighbours = []
        for row in range(self.x - 1, self.x + 2):
            for col in range(self.y -1, self.y + 2):
                if Cell(row,col) != self:
                    neighbours.append(Cell(row,col))
        return neighbours

if __name__ == "__main__":

    dim = int(input("Dimension: "))
    pop = int(input("Population: "))
    itr = int(input("Iterationen: "))
    
    playground = Board(dim, pop)

    for _ in range(itr):
        playground.evolution()
        playground.draw()
        sleep(0.1)
