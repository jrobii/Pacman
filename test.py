import unittest
import app
import player
import ghost
from pygame.math import Vector2 as vec

class TestApp(unittest.TestCase):
    def test_state(self):
        state = 2
        newState = app.App.setState(self, state)
        currentState = app.App.getState(self)
        self.assertEqual(currentState, 2)
    
    def test_score(self):
        newScore = 1000.00
        score = app.App.setScore(self, newScore)
        currentScore = app.App.getScore(self)
        self.assertEqual(currentScore, 1000.00)

    def test_player_dir(self):
        direction = vec(0, 1)
        dir = player.Player.setDir(self, direction)
        currentDir = player.Player.getDir(self)
        self.assertEqual(currentDir, vec(0, 1))
    
    def test_player_lifes(self):
        newLifes = 10
        lifes = player.Player.setLifes(self, newLifes)
        currentLifes = player.Player.getLifes(self)
        self.assertEqual(currentLifes, 10)
    
    def test_ghost_dir(self):
        direction = vec(0, 1)
        dir = ghost.Ghost.setDir(self, direction)
        currentDir = ghost.Ghost.getDir(self)
        self.assertEqual(currentDir, vec(0, 1))

if __name__ == '__main__':
    unittest.main()