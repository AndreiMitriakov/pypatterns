#!/usr/bin/env python3
# coding: utf-8

from datetime import datetime

class ChatRoom:

    def show_message(self, usr, msg):
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        sender = usr.get_name()
        print('{} : {} : {}'.format(time, sender, msg))

class User:
    def __init__(self, name, chat_mediator):
        self.name = name
        self.chat_mediator = chat_mediator

    def get_name(self):
        return self.name

    def send(self, msg):
        self.chat_mediator.show_message(self, msg)


if __name__ == '__main__':
    mediator = ChatRoom();
    john = User('John Doe', mediator)
    jane = User('Jane Doe', mediator)
    john.send('Hi there!')
    jane.send('Hey!')

