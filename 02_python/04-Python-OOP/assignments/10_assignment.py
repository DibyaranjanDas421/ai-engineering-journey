
from datetime import datetime


# 1. User class
class User:
    def __init__(self, username):
        self.username = username

    def send_message(self, chatroom, content):
        chatroom.send_message(self, content)

    def join_chatroom(self, chatroom):
        chatroom.join(self)

    def leave_chatroom(self, chatroom):
        chatroom.leave(self)


# 2. Message class
class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.timestamp = datetime.now()

    def display(self):
        print(
            f"[{self.timestamp.strftime('%H:%M:%S')}] "
            f"{self.sender.username}: {self.content}"
        )


# 3. ChatRoom class
class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []

    def join(self, user):
        if user not in self.users:
            self.users.append(user)
            print(f"{user.username} joined {self.room_name}")
        else:
            print(f"{user.username} is already in the room")

    def leave(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"{user.username} left {self.room_name}")
        else:
            print(f"{user.username} is not in the room")

    def send_message(self, user, content):
        if user in self.users:
            message = Message(user, content)
            self.messages.append(message)
            message.display()
        else:
            print(f"{user.username} must join the room first")

    def view_history(self):
        print(f"\nChat history of {self.room_name}:")

        if not self.messages:
            print("No messages yet")
            return

        for message in self.messages:
            message.display()


# Creating users
user1 = User("Dibya")
user2 = User("Rahul")

# Creating a chatroom
room = ChatRoom("Python Group")

# Users joining the chatroom
user1.join_chatroom(room)
user2.join_chatroom(room)

# Sending messages
user1.send_message(room, "Hello everyone!")
user2.send_message(room, "Hi Dibya!")

# Viewing chat history
room.view_history()

# User leaving the chatroom
user2.leave_chatroom(room)

# Trying to send a message after leaving
user2.send_message(room, "One more message")