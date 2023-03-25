from translation.adapters.memory_repository import MemoryRepository
from translation.domainmodel.User import User



class AuthManager:
    def __init__(self):
        self.__repository = MemoryRepository()
    
    def register_user(self, user_name: str, password: str) -> User:
        # Check if user with same username already exists
        existing_user = self.__repository.get_user(user_name)
        if existing_user:
            raise ValueError("User already exists")

        # Create new user object and add it to repository
        user_id = self.__repository.get_id()
        new_user = User(user_id, user_name, password)
        self.__repository.add_user(new_user)
        return new_user
    
    def authenticate_user(self, user_name: str, password: str) -> bool:
        # Check if user with given username exists
        user = self.__repository.get_user(user_name)
        if not user:
            return False

        # Check if password matches
        if user.password == password:
            return True
        
        return False
