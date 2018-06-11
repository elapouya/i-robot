# Created : 2018-06-11
#
# @author: Eric Lapouyade


class Step:
    def __init__(self, name):
        self.name = name
        self._connectors = []
        self._actions = []

    def add_connector(self, connector):
        self._connectors.append(connector)

    def get_connectors(self):
        return self._connectors

    def add_action(self, action):
        self._actions.append(action)

    def get_actions(self):
        return self._actions