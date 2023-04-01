# tests/test_memory_repo.py
import pytest
from translation.adapters.memory_repository import MemoryRepository
from translation.domainmodel.User import User


def test_memory_repo_add_user(memory_repo):
    user = User(0, 'test_user', 'test_password')
    memory_repo.add_user(user)
    assert len(memory_repo._users) == 1
    assert memory_repo._users[0].id == 1
    assert memory_repo._users[0].username == 'test_user'

def test_memory_repo_get_user(memory_repo):
    user = User(0, 'test_user', 'test_password')
    memory_repo.add_user(user)
    found_user = memory_repo.get_user('test_user')
    assert found_user is not None
    assert found_user.username == 'test_user'
    assert found_user.password == 'test_password'

def test_memory_repo_get_id(memory_repo):
    user_id = memory_repo.get_id()
    assert user_id == 1
    user_id = memory_repo.get_id()
    assert user_id == 2

def test_get_user_by_username():
    # Create a memory repository instance
    memory_repo = MemoryRepository()

    # Create a user
    user = User(1, "test_user", "password")

    # Add the user to the memory repo
    memory_repo.add_user(user)

    # Retrieve the user from the memory repo using their username
    retrieved_user = memory_repo.get_user_by_username("test_user")

    # Check if the retrieved user's username matches the original user's username
    assert retrieved_user.username == "test_user", "Usernames do not match"

def test_get_user_by_id():
    memory_repo = MemoryRepository()

    user = User(1, "test_user", "password")

    memory_repo.add_user(user)

    retrieved_user = memory_repo.get_user_by_id(user.user_id)

    assert retrieved_user.user_id == user.user_id, "User IDs do not match"

def test_add_friend():
    memory_repo = MemoryRepository()

    user = User(1, "test_user", "password")
    friend = User(2, "friend", "password")

    memory_repo.add_user(user)
    memory_repo.add_user(friend)

    memory_repo.add_friend(user, friend)

    assert user in friend.friends, "Friend not added to user's friends"

def test_remove_friend():
    memory_repo = MemoryRepository()

    user = User(1, "test_user", "password")
    friend = User(2, "friend", "password")

    memory_repo.add_user(user)
    memory_repo.add_user(friend)

    memory_repo.add_friend(user, friend)

    memory_repo.remove_friend(user, friend)

    assert friend not in user.friends, "Friend not removed from user's friends"
