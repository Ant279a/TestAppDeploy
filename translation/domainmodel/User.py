from typing import List

from Message import Message

class User:
    def __init__(self, user_id: int, user_name: str, password: str):
        assert isinstance(user_id, int) and user_id >= 0, "User ID should be a non-negative integer."
        self.__user_id = user_id

        if isinstance(user_name, str):
            self.__user_name = user_name.lower().strip()
        else:
            self.__user_name = None

        if isinstance(password, str) and len(password) >= 7:
            self.__password = password
        else:
            self.__password = None
        
        self.__messages: List[Message] = []

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password

    def __repr__(self):
        return f'<User {self.__user_name}, user id = {self.__user_id}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__user_id == other.user_id

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return self.__user_id < other.user_id

    def __hash__(self):
        return hash(self.__user_id)

    def send_message(self, recipient: 'User', content: str) -> None:
        message = Message(self, recipient, content)
        self.__messages.append(message)
        recipient.__messages.append(message)

    def view_messages(self) -> None:
        for message in self.__messages:
            print(message)

    def view_messages_with(self, user: 'User') -> List[Message]:
        messages = []
        for message in self.__messages:
            if message.sender == user or message.recipient == user:
                messages.append(message)
        return messages

    @classmethod
    def from_dict(cls, user_dict: dict) -> 'User':
        user_id = user_dict.get('user_id')
        user_name = user_dict.get('user_name')
        password = user_dict.get('password')
        return cls(user_id, user_name, password)
