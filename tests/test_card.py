import pytest
from peewee import SqliteDatabase
from models.user import User
from models.account import Account
from models.card import Card

db = SqliteDatabase(':memory:')

def test_create_card(setup_database):
    user = User.create(nombre='Enoc')
    account = Account.create(user=user, saldo=1000)
    card = Card.create(account=account, balance=800)
    assert Card.select().count() == 1

def test_read_card(setup_database):
    user = User.create(nombre='Alex')
    account = Account.create(user=user, saldo=1500)
    card = Card.create(account=account, balance=1200)
    
    card_db = Card.get(Card.id == card.id)
    assert card_db.balance == 1200

def test_update_card(setup_database):
    user = User.create(nombre='Eunice')
    account = Account.create(user=user, saldo=2000)
    card = Card.create(account=account, balance=1800)

    card_db = Card.get(Card.id == card.id)
    card_db.balance = 2000
    card_db.save()

    card_actualizada = Card.get(Card.id == card.id)
    assert card_actualizada.balance == 2000

def test_delete_card(setup_database):
    user = User.create(nombre='Aldo')
    account = Account.create(user=user, saldo=2500)
    card = Card.create(account=account, balance=2200)

    card.delete_instance()

    with pytest.raises(Card.DoesNotExist):
        Card.get(Card.id == card.id)

if __name__ == '__main__':
    pytest.main()
