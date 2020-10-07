import pygame
import random
from item import Item
vec = pygame.math.Vector2

class Ghost(Item):
    def __init__(self, app, pos):
        super().__init__(app, pos)

    def update(self):
        self.pixPos += self.dir
        if self.checkLegalMove():
            self.move()
        self.setGridPos()
        

    def draw(self):
        pygame.draw.circle(self.app.screen, (255, 0, 0), (int(self.pixPos.x), int(self.pixPos.y)), 8)
    
    def move(self):
        self.dir = self.getRandomDirection()
        #self.dir = self.getPathDirection()
    

    def getPathDirection(self):
        next_cell = self.findNextCell()
        xdir = next_cell[0] - self.gridPos[0]
        ydir = next_cell[1] - self.gridPos[1]
        return vec(xdir, ydir)
    
    def findNextCell(self):
        path = self.BFS([int(self.gridPos.x), int(self.gridPos.y)], [int(self.app.player.gridPos.x), int(self.app.player.gridPos.y)])
        return path[1]
    
    def BFS(self, start, target):
        grid = [[0 for x in range(40)] for x in range(32)]
        for cell in self.app.walls:
            if cell.x < 40 and cell.y < 32:
                grid[int(cell.y)][int(cell.x)] = 1
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
