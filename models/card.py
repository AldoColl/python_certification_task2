from peewee import Model, CharField, ForeignKeyField, DecimalField
from models.account import Account

class Card(Model):
    account = ForeignKeyField(Account)
    card_number = CharField(unique=True)
    balance = DecimalField(default=0)

    class Meta:
        database = db

    def process_deposit(self, amount):
        self.balance += amount
        self.save()

    def process_expense(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.save()
        else:
            raise ValueError("Insufficient balance")
