from main import add_user, delete_user
from models.user import User
import pytest

db = SqliteDatabase(':memory:')

@pytest.fixture
def setup_database():
    db.connect()
    db.create_tables([User, Account, Card])
    yield
    db.drop_tables([User, Account, Card])
    db.close()

def test_create_user(setup_database):
    user = User.create(nombre='David')
    assert User.select().count() == 1

def test_read_user(setup_database):
    user = User.create(nombre='Alex')
    
    user_db = User.get(User.id == user.id)
    assert user_db.nombre == 'Alex'

def test_update_user(setup_database):
    user = User.create(nombre='Aldo')

    user_db = User.get(User.id == user.id)
    user_db.nombre = 'Aldo Updated'
    user_db.save()

    user_actualizado = User.get(User.id == user.id)
    assert user_actualizado.nombre == 'Aldo Updated'

def test_delete_user(setup_database):
    user = User.create(nombre='Eunice')

    user.delete_instance()

    with pytest.raises(User.DoesNotExist):
        User.get(User.id == user.id)

if __name__ == '__main__':
    pytest.main()

