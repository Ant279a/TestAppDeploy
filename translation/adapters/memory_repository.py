from typing import List

from .repository import AbstractRepository
from ..domainmodel.User import User
from ..domainmodel.Message import Message
from flask import jsonify
from translation.services.translation import translate_text


class MemoryRepository(AbstractRepository):
    def __init__(self):
        self._users: List[User] = []
        self._messages: List[Message] = []
        self._next_id = 1

    def add_user(self, user: User) -> None:
        user.id = self._next_id
        user.user_id = user.id
        self._users.append(user)
        self._next_id += 1
        print(self._users)
    
    def get_user(self, username: str) -> User:
        return next((user for user in self._users if user.username == username), None)

    def get_id(self) -> int:
        next_id = self._next_id
        self._next_id += 1
        return next_id
    
    def get_user_by_id(self, user_id: int) -> User:
        return next((user for user in self._users if user.user_id == user_id), None)
    
    def add_friend(self, user: User, friend: User):
        user.add_friend(friend)
        friend.add_friend(user)
    
    def remove_friend(self, user: User, friend: User):
        user.remove_friend(friend)
        friend.remove_friend(user)
    
    def get_user_by_username(self, username: str) -> User:
        for user in self._users:
            if user.username == username:
                return user
        return None
    
    def update_user(self, updated_user: User) -> None:
        for index, user in enumerate(self._users):
            if user.user_id == updated_user.user_id:
                self._users[index] = updated_user
                break

    def send_message(self, sender_id: int, recipient_id: int, content: str, sender_lang: str, recipient_lang: str):
        # Store the original message
        print(f"Senders language: {sender_lang} and recipient: {recipient_lang}")
        original_message = Message(sender_id, recipient_id, content, language=sender_lang)
        self._messages.append(original_message)

        # If the sender and recipient have different languages, store the translated message as well
        if sender_lang != recipient_lang:
            translated_content = translate_text(content, sender_lang, recipient_lang)
            translated_message = Message(sender_id, recipient_id, translated_content, language=recipient_lang)
            self._messages.append(translated_message)


    def fetch_messages(self, sender_id: int, recipient_id: int, preferred_language: str) -> List[Message]:
        messages = []
        for message in self._messages:
            if (message.sender_id == sender_id and message.recipient_id == recipient_id) or \
            (message.sender_id == recipient_id and message.recipient_id == sender_id):
            
                # Check the message's language
                if message.language == preferred_language:
                    messages.append(message)
                    
        return messages

