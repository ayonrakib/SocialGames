import mysql.connector as mysql
import json, hashlib, binascii, peewee
from model.User import User
from model.Friend import Friend
from model.GameTable import GameTable
# from UserController import UserController
from controller.UserController import UserController
from library.DatabaseConnection import DatabaseConnection
import peewee, os

class GameController():
    # createGame
    # input: game title, image icon name, game path, number of players
    # return: true if created, false if not
    # method:
    #   1.  game title, image icon name, game path, number of players diye gametable e entry bananor try korbo
    #   2. jodi banaite fail kori:
    #       1. return false
    #   3. successful hoile return true
    def createGame(self, gameTitle, gameIcon, gamePath, numberOfPlayers):
        try:
            newGame = GameTable.create(gameTitle = gameTitle, gamePath = gamePath, numberOfPlayers = numberOfPlayers, gameIcon = gameIcon)
            newGame.save()
            return True
        except peewee.IntegrityError:
            return False