from translation.adapters.memory_repository import MemoryRepository
from translation.domainmodel.User import User


class AuthManager:
    def __init__(self):
        self.__repository = MemoryRepository()
    
    def get_repository(self) -> MemoryRepository:
        return self.__repository
    
    def register_user(self, user_name: str, password: str) -> User:
        # Check if user with same username already exists
        existing_user = self.__repository.get_user(user_name)
        if existing_user:
            raise ValueError("User already exists")

        # Create new user object and add it to repository
        new_user = User(None, user_name, password)
        if user_name == "b":
            new_user.language = "korean"
        self.__repository.add_user(new_user)
        return new_user
    
    def authenticate_user(self, user_name: str, password: str) -> bool:

        user = self.__repository.get_user(user_name)

        if not user:
            return (False, None)

        # Check if password matches
        if user.password == password:
            return (True, user.id)
        
        return (False, None)
