import pygame
import random
import astar
from item import Item
vec = pygame.math.Vector2

class Ghost(Item):
    def __init__(self, app, pos, num):
        super().__init__(app, pos)
        self.grid = self.getGrid()
        self.target = None
        self.number = num
        self.personality = self.personality()
        self.speed = self.setSpeed()
        self.startingPos = [pos.x, pos.y]

    def update(self):
        self.target = self.setTarget()
        if self.target != self.gridPos:
            self.pixPos += self.dir * self.speed
            if self.checkLegalMove():
                self.move()
            self.setGridPos()
        
    def getGrid(self):
        grid = [[0 for x in range(28)] for x in range(30)]
        for cell in self.app.walls:
            if cell.x < 28 and cell.y < 30:
                grid[int(cell.y)][int(cell.x)] = 1
        return grid
    
    def setTarget(self):
        if self.personality == "speedy" or self.personality == "slow":
            return self.app.player.gridPos
    
    def setSpeed(self):
        if self.personality in ["speedy", "scared"]:
            speed = 1.05
        else:
            speed = 0.6
        return speed

    def draw(self):
        pygame.draw.circle(self.app.screen, (255, 0, 0), (int(self.pixPos.x), int(self.pixPos.y)), 8)
    
    def move(self):
        if self.personality == "random":
            self.dir = self.getRandomDirection()
        elif self.personality == "slow":
            self.dir = self.getPathDirection(self.target)
        elif self.personality == "speedy":
            self.dir = self.getPathDirection(self.target)
        elif self.personality == "scared":
            self.dir = self.getRandomDirection()
    

    def getPathDirection(self, target):
        next_cell = self.findNextCell(target)
        xdir = next_cell[0] - self.gridPos[0]
        ydir = next_cell[1] - self.gridPos[1]
        return vec(xdir, ydir)
    
    def findNextCell(self, target):
        path = self.BFS(self.grid, [int(self.gridPos.x), int(self.gridPos.y)], [int(target.x), int(target.y)])
        return path[1]
    
    def BFS(self, grid, start, target):
        queue = [start]
        path = []
        visited = []
        while queue:
            current = queue[0]
            queue.remove(queue[0])
            visited.append(current)
            if current == target:
                break
            else:
                neighbours = [[0,-1], [1, 0], [0, 1], [-1,0]]
                for neighbour in neighbours:
                    if neighbour[0] + current[0] >= 0 and neighbour[0] + current [0] < len(grid[0]):
                        if neighbour[1] + current[1] >= 0 and neighbour[1] + current [1] < len(grid):
                            next_cell = [neighbour[0] + current[0], neighbour[1] + current[1]]
                            if next_cell not in visited:
                                if grid[next_cell[1]][next_cell[0]] != 1:
                                    queue.append(next_cell)
                                    path.append({"current": current, "next": next_cell})
        shortest = [target]
        while target != start:
            for step in path:
                if step["next"] == target:
                    target = step["current"]
                    shortest.insert(0, step["current"])
        return shortest

    def getRandomDirection(self):
        while True:
            number = random.randint(-2, 1)
            if number == -2:
                xdir, ydir = 1,0
            elif number == -1:
                xdir, ydir = 0,1
            elif number == 0:
                xdir, ydir = -1,0
            else:
                xdir, ydir = 0,-1
            nextPos = vec(self.gridPos.x + xdir, self.gridPos.y + ydir)
            if nextPos not in self.app.walls:
                break 
        return vec(xdir, ydir)
    
    def personality(self):
        if self.number == 0:
            return "speedy"
        elif self.number == 1:
            return "slow"
        elif self.number == 2:
            return "random"
        else:
            return "scared"
