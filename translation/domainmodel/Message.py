class Message:
    def __init__(self, sender_id: int, recipient_id: int, content: str):
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.content = content

    def __str__(self):
        return f"{self.sender_id} -> {self.recipient_id}: {self.content}"
