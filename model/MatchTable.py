# class MatchTable
# id auto increment
# gameId foreign key field refer gametable id
# firstPlayer foreign key field refer user id
# secondPlayer foreign key field refer user id
# firstPlayerMove string
# secondPlayerMove string
import peewee
from library.DatabaseConnection import DatabaseConnection
from model.User import User
from model.GameTable import GameTable


class MatchTable(peewee.Model):
    id = peewee.AutoField()
    firstPlayer = peewee.ForeignKeyField(User, to_field="id")
    secondPlayer = peewee.ForeignKeyField(User, to_field="id")
    thirdPlayer = peewee.ForeignKeyField(User, to_field="id")
    fourthPlayer = peewee.ForeignKeyField(User, to_field="id")
    matchNumber = peewee.IntegerField()
    class Meta:
        database = DatabaseConnection.getConnection()