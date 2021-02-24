from library.DatabaseConnection import DatabaseConnection
from model.User import User
from controller.UserController import UserController
from model.Friend import Friend
from model.GameTable import GameTable
from model.MatchTable import MatchTable
import os
from playhouse.migrate import *

databaseConnection = DatabaseConnection.getConnection()
userController = UserController()

# userController.findUsersWithEmail('ayo')

# jokhon table banabo, create_tables function er input hobe list of Class objects
# databaseConnection.create_tables([User, Friends, GameTable, MatchTable])
# databaseConnection.create_tables([Friend])
# salt = str(os.urandom(20))
# currentSession = str(os.urandom(20))

# Adding users one by one:
    # user1 = User.create(email = 'ayon@gmail.com', firstName = "Rakib", lastName = "Ayon", salt = salt, password = userController.hashPassword("password", salt), currentSession = "")
    # user1.save()

    # user2 = User.create(email = 'eva@gmail.com', firstName = "Fahmida", lastName = "Mahjabin", salt = salt, password = userController.hashPassword("password", salt), currentSession = "")
    # user2.save()

    # user3 = User.create(email = 'golam@gmail.com', firstName = "Golam", lastName = "Muktadir",salt = salt, password = userController.hashPassword("password", salt), currentSession = "")
    # user3.save()

    # user4 = User.create(email = 'saad@gmail.com', firstName = "Saad", lastName = "Manzur",salt = salt, password = userController.hashPassword("password", salt), currentSession = "")
    # user4.save()

    # user5 = User.create(email = 'ayonrakib@gmail.com', firstName = "Rakib Hasan", lastName = "Ayon", salt = salt, password = userController.hashPassword("password", salt), currentSession = "")
    # user5.save()

# modifying table with columns
role = enumerate(default=False)
database = MySQLDatabase("socialgames",host = "localhost", user = "root", password = "Hahaha01670", port = 3306)
migrator = MySQLMigrator(database)

# migrate(
#     migrator.add_column('Friends','isBlocked', isBlocked)
# )

# migrate(
#     migrator.drop_column('User','isBlocked')
# )

# status = Friend.get(Friend.user_id == 1 and Friend.friend_id == 55)
# print(status)

# existingRequest = Friend.get(Friend.user_id == 2 and Friend.friend_id == 1)
# print(existingRequest.id)
# existingRequest.status = "requested"
# existingRequest.save()

migrate(
    migrator.add_column()
)