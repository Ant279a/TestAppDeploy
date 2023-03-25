import abc
from typing import List
from datetime import date

from ..domainmodel.Message import Message
from ..domainmodel.User import User

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add_user(self, user: User):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_user(self, user_name: str) -> User:
        raise NotImplementedError