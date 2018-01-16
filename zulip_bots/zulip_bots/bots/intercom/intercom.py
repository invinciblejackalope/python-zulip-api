# See readme.md for instructions on running this code.

from typing import Any
from intercom.client import Client

intercom = Client(personal_access_token='dG9rOjNjYWEzOTAzXzBjNDdfNDk1Zl9hY2I0XzRmY2NhZTZkYzI1YjoxOjA=')

class IntercomHandler(object):
    def usage(self) -> str:
        return '''
        This bot integrates Intercom.
        '''

    def handle_message(self, message: Any, bot_handler: Any) -> None:
        content = 'beep boop' # type: str
        bot_handler.send_reply(message, content)

handler_class = IntercomHandler
