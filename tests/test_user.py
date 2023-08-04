from main import add_user, delete_user
from models.user import User
import pytest

# Test add_user function
def test_add_user():
    add_user()
    user = User.get_or_none(User.name == 'Alice')
    assert user is not None

# Test delete_user function
def test_delete_user():
    # Add a user first for testing
    user = User.create(name='Test User', email='test@example.com')
    user_id = user.id

    delete_user()
    user = User.get_or_none(User.id == user_id)
    assert user is None
