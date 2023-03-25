from typing import List

from .repository import AbstractRepository
from ..domainmodel.User import User

class MemoryRepository(AbstractRepository):
    def __init__(self):
        self._users: List[User] = []
        self._next_id = 1

    def add_user(self, user: User) -> None:
        user.id = self._next_id
        self._users.append(user)
        self._next_id += 1
    
    def get_user(self, user_name: str) -> User:
        return next((user for user in self._users if user.user_name == user_name), None)
    
    def get_id(self) -> int:
        next_id = self._next_id
        self._next_id += 1
        return next_id
