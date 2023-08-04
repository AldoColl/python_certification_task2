from peewee import Model, CharField, AutoField

class User(Model):
    id = AutoField()
    name = CharField()
    email = CharField(unique=True)
    phone = CharField(null=True)

    class Meta:
        database = db
