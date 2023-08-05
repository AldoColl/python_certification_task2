import pytest
from peewee import SqliteDatabase
from models.user import User
from models.account import Account
from models.card import Card

db = SqliteDatabase(':memory:')

@pytest.fixture
def setup_database():
    db.connect()
    db.create_tables([User, Account, Card])
    yield
    db.drop_tables([User, Account, Card])
    db.close()

def test_create_account(setup_database):
    user = User.create(nombre='Eunice')
    account = Account.create(user=user, saldo=1000)
    assert Account.select().count() == 1

def test_read_account(setup_database):
    user = User.create(nombre='Paul')
    account = Account.create(user=user, saldo=500)
    
    account_db = Account.get(Account.id == account.id)
    assert account_db.saldo == 500

def test_update_account(setup_database):
    user = User.create(nombre='Fer')
    account = Account.create(user=user, saldo=200)

    account_db = Account.get(Account.id == account.id)
    account_db.saldo = 300
    account_db.save()

    account_actualizada = Account.get(Account.id == account.id)
    assert account_actualizada.saldo == 300

def test_delete_account(setup_database):
    user = User.create(nombre='Aldo')
    account = Account.create(user=user, saldo=100)

    account.delete_instance()

    with pytest.raises(Account.DoesNotExist):
        Account.get(Account.id == account.id)

if __name__ == '__main__':
    pytest.main()
