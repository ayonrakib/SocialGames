import unittest
from controller.UserController import UserController
from model.Friend import Friend
from model.User import User


class test_UserController(unittest.TestCase):
    def test_helloWorld(self):
        assert 1 == 1

    def test_GetFriendRecord(self):
        userController = UserController()
        print("\nsample message")
        print(userController.getFriendRecord(1,2).id)

# assert er baam pashe expected output, daan pashe actual output