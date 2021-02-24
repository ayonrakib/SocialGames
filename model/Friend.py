import peewee
from library.DatabaseConnection import DatabaseConnection
from model.User import User

class Friend(peewee.Model):
    id = peewee.AutoField()
    user = peewee.ForeignKeyField(User, to_field = 'id')
    friend = peewee.ForeignKeyField(User, to_field = 'id')
    status = peewee.CharField()
    isBlocked = peewee.BooleanField(default=False)
    class Meta:
        database = DatabaseConnection.getConnection()


# friends na, friends mane list of friend, so friend hobe
# userId er naam hobe user. 
# ei duita field e actual user object pabo, id pabo na.