# Created : 2018-06-11
#
# @author: Eric Lapouyade
"""
================
Interface module
================

Defines classes to interact with a console or an API
"""


class Interface:
    pass


class ConsoleInterface(Interface):
    def __init__(self, in_prompt='Me> ', out_prompt='Bot> '):
        """
            Args:
                in_prompt (str): Prompt for the end-user
                out_prompt (str): Prompt for the bot
        """
        self._in_prompt = in_prompt
        self._out_prompt = out_prompt

    def read(self):
        """Read keyboard"""
        return input(self._in_prompt)

    def write(self, message):
        """Write a message to the console

            Args:
                message (str): message to display on console
        """
        print('{}{}'.format(self._out_prompt,message))


class APIInterface(Interface):
    def __init__(self,url, user=None, password=None, in_prompt='Me> '):
        """
            Args:
                url (str): API url
                user (str): API user
                password (str): API password
                in_prompt (str): Prompt for the end-user
        """
        self._in_prompt = in_prompt
        self._url = url
        self._user = user
        self._password = password

    def read(self):
        """Read keyboard"""
        return input(self._in_prompt)

    def write(self, message):
        """Simulate API usage

            Args:
                message (str): message to send to the API
        """
        print("requests.post('{url}',data={{'msg':'{msg}'}},auth=('{user}','{passwd}'))"
              .format(url=self._url,
                      user=self._user,
                      passwd=self._password,
                      msg=message))
