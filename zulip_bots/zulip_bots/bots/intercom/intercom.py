# See readme.md for instructions on running this code.

from typing import Any
from intercom.client import Client

intercom = Client(personal_access_token='dG9rOjNjYWEzOTAzXzBjNDdfNDk1Zl9hY2I0XzRmY2NhZTZkYzI1YjoxOjA=')

class IntercomHandler(object):
    def usage(self) -> str:
        return '''
        This bot integrates Intercom.
        '''

    def handle_message(self, message: Dict[str, str], bot_handler: Any) -> None:
        intercom_bot_response = get_intercom_bot_response(message)
        bot_handler.send_reply(message, intercom_bot_response)

def get_intercom_bot_response(message: Dict[str, str]) -> str:
    content = message['content'].strip().split()
    command = content[0]
    if command == 'help':
        return 'Intercom bot supports these commands: ' \
               '\n\'@intercom help\' to show this help message.' \
               '\n\'@intercom create-user <email> <name>\' to create a new user.' \
               '\n\'@intercom delete-user <email> to delete a user.'
    elif command == 'create-user':
        intercom.users.create(email=content[1], name=content[2])
        return 'User created.'
    elif command == 'delete-user':
        intercom.users.delete(intercom.users.find(email=content[1]))
        return 'User created.'
    else:
        return command + ' is not a currently available command. Type \'@intercom help\' to see available commands.'

handler_class = IntercomHandler
