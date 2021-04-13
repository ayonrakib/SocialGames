import unittest
from controller.UserController import UserController
from controller.GameController import GameController
from model.Friend import Friend
from model.User import User
from model.GameTable import GameTable
import peewee

class test_GameController(unittest.TestCase):
    def test_helloWorld(self):
        assert 1 == 1


    def test_createGame(self):
        gameController = GameController()
        print(gameController.createGame('twenty-nine','1.png','twenty-nine',4))