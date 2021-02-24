import peewee
from library.DatabaseConnection import DatabaseConnection
from model.User import User

# gametable
# id auto increment
# gameId int
# firstPlayer int foreign key from User table id column
# secondPlayer int foreign key from User table id column
# class GameTable
class GameTable(peewee.Model):
    id = peewee.AutoField()
    firstPlayer = peewee.ForeignKeyField(User, to_field = 'id')
    secondPlayer = peewee.ForeignKeyField(User, to_field = 'id')
    class Meta:
        database = DatabaseConnection.getConnection()


    def __str__(self):
        pass


    def getId(self):
        return self.id


    def getFirstPlayer(self):
        return self.firstPlayer


    def getSecondPlayer(self):
        return self.secondPlayer