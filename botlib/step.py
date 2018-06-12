# Created : 2018-06-11
#
# @author: Eric Lapouyade
"""
===========
Step module
===========

A step can have many actions and connectors.
When a step is triggered, bound actions are run,
a user input is asked and then the first matching connector is taken to
go to the next step.
"""


class Step:
    def __init__(self, name):
        """
            Args:
               name (str): The step name
        """
        self.name = name
        self._connectors = []
        self._actions = []

    def add_connector(self, connector):
        """Add a connector to the step

            Args:
                connector (Connector): a connector to add
        """
        self._connectors.append(connector)

    def get_connectors(self):
        """Get connectors

            Returns:
                list: bound connectors
        """
        return self._connectors

    def add_action(self, action):
        """Add an action to the step

            Args:
                action (Action): a action to add
        """
        self._actions.append(action)

    def get_actions(self):
        """Get actions

            Returns:
                list: bound actions
        """
        return self._actions