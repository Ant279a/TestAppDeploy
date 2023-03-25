from typing import List, Any

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
        
        self.__messages: List[int] = []  # Store message IDs instead of Message objects

    # ... (all other methods and properties remain the same)

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

    # ... (from_dict method remains the same)



    @classmethod
    def from_dict(cls, user_dict: dict) -> 'User':
        user_id = user_dict.get('user_id')
        user_name = user_dict.get('user_name')
        password = user_dict.get('password')
        return cls(user_id, user_name, password)
