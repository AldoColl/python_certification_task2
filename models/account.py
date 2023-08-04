from peewee import Model, CharField, ForeignKeyField, DecimalField
from models.user import User

class Account(Model):
    user = ForeignKeyField(User)
    account_number = CharField(unique=True)
    balance = DecimalField(default=0)

    class Meta:
        database = db
