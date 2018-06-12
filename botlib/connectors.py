# Created : 2018-06-11
#
# @author: Eric Lapouyade
"""
=================
Connectors module
=================

A connector links a source step to a destination step with a conditional test
"""


class Connector:
    def __init__(self, stepname, param):
        """
            Args:
               stepname (str): The destination step name
               param (str): A generic parameter for the conditional test
        """
        self.goto_step = stepname
        self._param = param


class IFEqualConnector(Connector):
    def matches(self,user_input):
        """Check whether the user input matches the condition

            Args:
               user_input (str): The user input to challenge

            returns:
                bool: True if matches
        """
        return self._param.lower() == user_input.lower()


class IFContainsConnector(Connector):
    def matches(self,user_input):
        """Check whether the user input matches the condition

            Args:
               user_input (str): The user input to challenge

            returns:
                bool: True if matches
        """
        return self._param.lower() in user_input.lower()