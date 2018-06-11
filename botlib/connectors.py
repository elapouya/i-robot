# Created : 2018-06-11
#
# @author: Eric Lapouyade


class Connector:
    def __init__(self, stepname, param):
        self.goto_step = stepname
        self._param = param


class IFEqualConnector(Connector):
    def matches(self,user_input):
        return self._param.lower() == user_input.lower()


class IFContainsConnector(Connector):
    def matches(self,user_input):
        return self._param.lower() in user_input.lower()