# Created : 2018-06-11
#
# @author: Eric Lapouyade


class Interface:
    pass


class ConsoleInterface(Interface):
    def __init__(self, in_prompt='Me> ', out_prompt='Bot> '):
        self._in_prompt = in_prompt
        self._out_prompt = out_prompt

    def read(self):
        return input(self._in_prompt)

    def write(self, message):
        print('{}{}'.format(self._out_prompt,message))


class APIInterface(Interface):
    def __init__(self,url, user=None, password=None, in_prompt='Me> '):
        self._in_prompt = in_prompt
        self._url = url
        self._user = user
        self._password = password

    def read(self):
        return input(self._in_prompt)

    def write(self, message):
        print("requests.post('{url}',data={{'msg':'{msg}'}},auth=('{user}','{passwd}'))"
              .format(url=self._url,
                      user=self._user,
                      passwd=self._password,
                      msg=message))
