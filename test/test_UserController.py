import unittest
from controller.UserController import UserController
from model.Friend import Friend
from model.User import User
import peewee


class test_UserController(unittest.TestCase):
    def test_helloWorld(self):
        assert 1 == 1

    def test_GetFriendRecord(self):
        userController = UserController()
        print("\nsample message")
        print(userController.getFriendRecord(1,2).id)

# assert er baam pashe expected output, daan pashe actual output

    def test_SetUserAsAdmin(self):
        user = User.get(User.email == "eva@gmail.com")
        user.role = "admin"
        user.save()


    def test_IsMyRoleAdmin(self):
        userController = UserController()
        isUserAdmin = userController.isMyRoleAdmin("b''n0\xfa\xdd\xceHT\xce\xaf\xbe\xee\xcc\xff\x9e\x10\xc5x|\xb2\xed''")
        print(isUserAdmin)

    
    def test_validateCurrentSession(self):
        try:
            user = User.get(User.currentSession == 'b''G\xea\xda\xee\xf6\xf4\xfbJ\xb0n\r}\xba\x05+6\xc5\xb8U\xfb''')
            print("user is",user.id)
            return True
        except peewee.DoesNotExist:
            return False