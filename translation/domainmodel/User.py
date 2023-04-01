from __future__ import annotations
from typing import List, Any


class User:
    def __init__(self, user_id: Optional[int], username: str, password: str):
        if user_id is not None:
            assert isinstance(user_id, int) and user_id >= 0, "User ID should be a non-negative integer."
        self.__user_id = user_id

        if isinstance(username, str):
            self.__username = username.lower().strip()
        else:
            self.__username = None

        if isinstance(password, str) and len(password) >= 7:
            self.__password = password
        else:
            self.__password = None

        self.__friends = []
        self.__preferred_language = "English"
        self.sent_messages = []
        self.received_messages = []
        self._messages = []
    

    @property
    def user_id(self) -> int:
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @property
    def username(self) -> str:
        return self.__username

    @property
    def password(self) -> str:
        return self.__password
    
    @property
    def preferred_language(self) -> str:
        return self.__preferred_language
    
    @preferred_language.setter
    def preferred_language(self, language: str):
        self.__preferred_language = language

    def send_message(self, recipient: 'User', content: str) -> None:
        message_id = len(self.__messages)
        self.__messages.append(message_id)
        recipient.__messages.append(message_id)

    def view_messages(self, all_messages: List[Any]) -> None:
        for message_id in self.__messages:
            print(all_messages[message_id])

    def view_messages_with(self, user: 'User', all_messages: List[Any]) -> List[Any]:
        messages = []
        for message_id in self.__messages:
            message = all_messages[message_id]
            if message.sender_id == user.user_id or message.recipient_id == user.user_id:
                messages.append(message)
        return messages

    @property
    def friends(self) -> List[User]:
        return self.__friends

    def add_friend(self, user: User):
        if user not in self.__friends:
            self.__friends.append(user)

    def remove_friend(self, user: User):
        if user in self.__friends:
            self.__friends.remove(user)
    
    def get_messages_with_friend(self, friend: User) -> List[Message]:
        messages = []
        for message in self._messages:
            if message.sender_id == self.id and message.recipient_id == friend.id:
                messages.append(message)
            elif message.sender_id == friend.id and message.recipient_id == self.id:
                messages.append(message)
        return messages

    @classmethod
    def from_dict(cls, user_dict: dict) -> 'User':
        user_id = user_dict.get('user_id')
        username = user_dict.get('username')
        password = user_dict.get('password')
        return cls(user_id, username, password)
