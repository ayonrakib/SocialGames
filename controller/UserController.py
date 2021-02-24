import mysql.connector as mysql
import json, hashlib, binascii, peewee
from model.User import User
from model.Friend import Friend
from library.DatabaseConnection import DatabaseConnection
import peewee, os
# import logging
# logger = logging.getLogger('peewee')
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)

class UserController():
    # def __init__(self):
    #     self.databaseConnection = DatabaseConnection.getConnection()
    def getUserSalt(self, email):
        return User.get(User.email == email).getSalt()


    def hashPassword(self, password, salt):
        if not isinstance(password, str):
            raise Exception("Password should be a string")
        password = salt + password
        encodedPassword = hashlib.sha512(password.encode('utf-16',errors='strict'))
        hashedPassword = encodedPassword.hexdigest()
        return hashedPassword


    def authenticateUser(self, email, password):
        if not isinstance(email, str):
            raise Exception("email has to be string")
        if not isinstance(password, str):
            raise Exception("password has to be str.")
        userSalt = self.getUserSalt(email)
        password = self.hashPassword(password, userSalt)
        try:
            if User.get(User.email == email) and User.get(User.password == password):
                return True
        except:
            return False

# user jei data pathay sob string, so email str kina check dorkar nai.
    def findUserByEmail(self, email):
        # if not isinstance(email, str):
        #     raise Exception("Email is not a string")
# bivinno exception khaite paare: db down, busy, user paay nai, fail korse db te.
# user related kaaj gula show korbo, baki sob log korbo.
        try: 
            if User.get(User.email == email):
                return "User found"
        except peewee.DoesNotExist:
            return "User Not found"


    # getUserWithSessionId
    # input: sessionId
    # return: id of the found user, None if not
    # method:
    #   return user er id jeitar currentSession == sessionId
    def getUserWithSessionId(self, sessionId):
        user = User.get(User.currentSession == sessionId)
        return user.id


    def createUserFromRegistrationForm(self, email, password, firstName, lastName):
        salt = str(os.urandom(20))
        currentSession = str(os.urandom(20))
        user = User.create(email = email, firstName = firstName, lastName = lastName, password = self.hashPassword(password, salt), salt = salt, currentSession = currentSession)
        return user


    # findUsersWithEmail
    # input: friendName, sessionid
    # return: friends list except logged in user
    # method:
    #   1. userModels hobe User table er sob user jader email e friendName substring thake
    #   2. curentUser hobe jei user er currentSession= sessionId
    #   3. users er 0 index hobe currentuser er email
    #   4. userNameAndId dic with keys name and id
    #   5. userModels er sob user er jonno:
    #       1. jodi user.email and currentUser.email soman na hoy:
    #           1. fullName = user.firstName + " " + user.lastName
    #           2. userNameAndId name key er value fullname
    #           3. userNameAndId email key er value user.email
    #           4. users e append userNameAndId
    #   6. return users
    def findUsersWithEmail(self, email, currentSession):
        userModels = User.select().where(User.email.contains(email))
        currentUser = User.get(User.currentSession == currentSession)
        users = [currentUser.id]
        for user in userModels:
            if user.email != currentUser.email:
                userNameAndId = {"name": "", "id": "", "status": ""}
                fullName = user.firstName + " " + user.lastName
                try:
                    friend = self.getFriendRecord(currentUser.id, user.id)
                except peewee.DoesNotExist:
                    friend = None
                userNameAndId["name"] = fullName
                userNameAndId["id"] = user.id
                if friend is not None:
                    userNameAndId["status"] = friend.status
                else:
                    userNameAndId["status"] = ""
                users.append(userNameAndId)
        return users


    # for user in userModes:
    # 1. user = eva@gmail.com object
    #   1. if user.email != currentUser.email:
    #   2. if 'eva@gmail.com' != currentUser.email:
    #   3. if 'eva@gmail.com' != 'ayon@gmail.com':
    #   4. if true:
    #       1. fullName = user.firstName + " " + user.lastName
    #       2. fullName = "Fahmida" + " " + user.lastName
    #       3. fullName = "Fahmida" + " " + "Mahjabin"
    #       4. fullName = "Fahmida Mahjabin"
    #       5. userNameAndId["name"] = fullName
    #       6. userNameAndId["name"] = "Fahmida Mahjabin"
    #       7. x12345["name"] = "Fahmida Mahjabin"
    #       8. userNameAndId["email"] = email
    #       9. userNameAndId["email"] = "eva@gmail.com"
    #       10. x12345["email"] = "eva@gmail.com"
    #       10. userNameAndId = {"name": "Fahmida Mahjabin", "email" : "eva@gmail.com"}
    #       11. users.append(userNameAndId)
    #       12. users.append(x12345)
    #       12. users = [x12345]
    # 2. user = golam@gmail.com object
    #   1. if user.email != currentUser.email:
    #   2. if 'golam@gmail.com' != currentUser.email:
    #   3. if 'golam@gmail.com' != 'ayon@gmail.com':
    #   4. if true:
    #       1. fullName = user.firstName + " " + user.lastName
    #       2. fullName = "Golam" + " " + user.lastName
    #       3. fullName = "Golam" + " " + "Muktadir"
    #       4. fullName = "Golam Muktadir"
    #       5. userNameAndId["name"] = fullName
    #       6. userNameAndId["name"] = "Golam Muktadir"
    #       7. x12345["name"] = "Golam Muktadir"
    #       7. userNameAndId["email"] = email
    #       8. userNameAndId["email"] = "golam@gmail.com"
    #       10. x12345["email"] = "golam@gmail.com"
    #       9. userNameAndId = {"name": "Golam Muktadir", "email" : "golam@gmail.com"}
    #       10. users.append(userNameAndId)
    #       12. users.append(x12345)
    #       11. users = [x12345, x12345]

    # for user in users:
    #   print(user)

    # loop1:
    #   1. user = x12345
    #   2. print(user)
    #   3. print(x12345)
    #   4. print({"name": "Golam Muktadir", "email" : "golam@gmail.com"})



    # getUser
    # input: sessionid
    # return: found user object
    # method:
    #   return User.get(User.currentSession == currentSession)
    def getUser(self, currentSession):
        return User.get(User.currentSession == currentSession)

    # addFriend
    # input: currentuser, friend_id
    # return: "", just add the request on the db
    # method:
    #   1. getFriendRequest theke return nibo with 2 inputs
    #   2. jodi record none na hoy:
    #       1. jodi record.status requested hoy:
    #           1. status accepted
    #           2. return true
    #   3. notn entry banabo friend table e, user = userid, frien = friendid, status = requested
    #   4. return truea
    def addFriend(self, user_id, friend_id):
        print("came here")
        existingRequest = self.getFriendRecord(user_id, friend_id)
        if existingRequest is not None:
            print(existingRequest.status)
            if existingRequest.status == "requested":
                existingRequest.status = "accepted"
                existingRequest.save()
                return True
        friendRequest = Friend.create(user = user_id, friend = friend_id, status = "requested")
        friendRequest.save()
        return "Successfully sent friend request" 


    # acceptFrienRequest
    # input: currentUserId, requesterId
    # return: true if accepted,false if not
    # method:
    #   1. getFriendRecord theke record nibo with userid and friendid
    #   2. jodi entry none na hoy:
    #       2. jodi entry.status == "requested" hoy:
    #           1. entry.status = "accepted"
    #           2. entry.save()
    #   3. return true
    def acceptFrienRequest(self, currentUserId, requesterId):
        friendRequest = self.getFriendRecord(currentUserId, requesterId)
        print(currentUserId, requesterId, friendRequest.id)
        if friendRequest is not None:
            if friendRequest.status == "requested":
                friendRequest.status = "accepted"
                friendRequest.save()
                return True


    # getUserNameWithId
    # input: id
    # return: user full name as string
    # method:
    #   1. user = User.get(User.id == id)
    #   2. return user er firstName + user er lastName
    def getUserNameWithId(self, id):
        user = User.get(User.id == id)
        return user.firstName + " " + user.lastName


    # getpendingrequests
    # input: currentsession, to get current logged in user
    # return: the pending friend request object from friend table
    # method:
    #   1. currentsession diye current user khuje ber korbo
    #   2. existingRequests hobe friend.select jeikhane friend table er user == currentuser , status == requested
    #   3. existtingrequests er sob user er jonno:
    #       3. print(user.friendid)
    def getPendingRequests(self, currentSession):
        currentUser = User.get(User.currentSession == currentSession)
        existingRequests = Friend.select().where(((Friend.friend_id == currentUser.id) | (Friend.user_id == currentUser.id)) , Friend.status == "requested")
        friendsRequested = []
        for user in existingRequests:
            # print(user.status)
            if user.status == "requested":
                userNameAndId = {"name": "", "id": "", "status": ""}
                if user.user_id == currentUser.id:
                    userNameAndId["id"] = user.friend_id
                    name = self.getUserNameWithId(user.friend_id)
                else:
                    userNameAndId["id"] = user.user_id
                    name = self.getUserNameWithId(user.user_id)
                userNameAndId["name"] = name
                userNameAndId["status"] = user.status
                friendsRequested.append(userNameAndId)
        return friendsRequested 


# getMyFriends
# input: user_id
# return: list of my friends
# method:
#   1. myFriends = []
#   2. table theke record bair korbo jeikhane userid == input or friendid == input
#   3. jodi record none hoy:
#       1. return []
#   4. record er sob entry er jonno:
#       1. jodi entry.id not equal to userid hoy and entry.status = "accepted" hoy:
    #       1. userNameAndId = {"name": "", "id": ""}
    #       2. userNameAndId er name key hobe getUserNameWithId(entry.id)
    #       3. userNameAndId er id hobe entry.id
    #       4. myFriends e append userNameAndId
#   5. return myFriends

    def getMyFriends(self, user_id):
        myFriends = []
        friends = Friend.select().where((Friend.user_id == user_id) | (Friend.friend_id == user_id))
        if friends is None:
            print("returned none")
            return []
        for friend in friends:
            if friend.id != user_id and friend.status == "accepted":
                userNameAndId = {"name": "", "id": ""}
                if friend.user_id == user_id:
                    friendId = friend.friend_id
                else:
                    friendId = friend.user_id
                userNameAndId["name"] = self.getUserNameWithId(friendId)
                userNameAndId["id"] = friendId
                myFriends.append(userNameAndId)
        return myFriends

# userController = UserController()
# print(userController.authenticateUser("rakib@gmail.com","password"))
# databaseConnection.create_tables([User])

# create 2 users
# user1 = User(email = "ayon@gmail.com", password = userController.hashPassword("password"))
# print(user1.save())
# user2 = User(email = "golam@gmail.com", password = userController.hashPassword("password"))
# print(user2.save())

# emails are unique, so this user will throw errors
#   user3 = User(email = "golam@gmail.com", password = user.hashPassword("password"))
#   print(user3.save())

# update user email field
#   user1 = User.get(User.id == 1)
#   user1.email = "ayon@gmail.com"
#   print(user1.save())

# update user password field with hash
#   user1 = User.get(User.id == 1)
#   user1.password = user.hashPassword("password")
#   print(user1.save())

# update current session
#   user1 = User.get(User.id == 1)
#   user1.currentSession = ""


# duijon user friend kina? duita id dewa ase
# getFriendRecord
# input: userId1, userId2
# return: record if found, none if not
# method:
#   1. record khujbo jeikhane userid == userId1 and friendid == userId2
#   2. paile record return, na paile pass
#   3. record khujbo jeikhane userid == userId2 and friendid == userId1
#   4. paile record return, na paile pass
#   5. return None 
    def getFriendRecord(self, userId1, userId2):
        try:
            record = Friend.get(Friend.user_id == userId1 , Friend.friend_id == userId2)
            # print("first record")
            return record
        except peewee.DoesNotExist:
            pass
        try:
            record = Friend.get(Friend.user_id == userId2 , Friend.friend_id == userId1)
            # print("second record")
            return record
        except peewee.DoesNotExist:
            pass
        return None

    # removefriend
    # input: current user id, friend id
    # return: true if removed, false if not
    # method:
    #   1. getFriendRecord function call kore return value save korbo jekhane input = current user id, friend id
    #   2. jodi record none na hoy:
    #       1. record delete korbo
    #       2. return true
    #   3. return false
    def removefriend(self, currentUserId, friend_id):
        record = self.getFriendRecord(currentUserId, friend_id)
        if record is not None:
            record.delete_instance()
            record.save()
            return True
        return True


    # blockFriend
    # input: user_id, friend_id
    # return: true if block, false if not
    # method:
    #   1. getFriendRecord theke record nibo with parameters user_id, friend_id
    #   2. jodi record none hoy:
    #       1. Friend table e record create korbo with user_id = user_id, friend_id = friend_id, status = "blocked" and isBlocked = true
    #       2. return true
    #   3. record.status = "blocked"
    #   4. record.isBlocked = true
    #   5. return true
    def blockFriend(self, user_id, friend_id):
        record = self.getFriendRecord(user_id, friend_id)
        if record is None:
            newEntry = Friend.create(user = user_id, friend = friend_id, status = "blocked", isBlocked = True)
            newEntry.save()
            return True
        record.status = "blocked"
        record.isBlocked = True
        record.save()
        return True

    # unblockFriend
    # input: user_id, friend_id
    # return: true if unblocked, false if not
    # method:
    #   1. getFriendRecord theke record nibo with parameters user_id, friend_id
    #   2. jodi record none hoy:
    #       1. return false
    #   3. record delete korbo
    #   4. return true
    def unblockFriend(self, user_id, friend_id):
        record = self.getFriendRecord(user_id, friend_id)
        if record is None:
            return False
        record.delete_instance()
        record.save()
        return True