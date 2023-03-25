from User import User

class Message:
    def __init__(self, sender: User, recipient: User, content: str):
        self.sender = sender
        self.recipient = recipient
        self.content = content

    def __str__(self):
        return f"{self.sender.user_name} -> {self.recipient.user_name}: {self.content}"
