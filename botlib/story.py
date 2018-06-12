# Created : 2018-06-11
#
# @author: Eric Lapouyade
"""
============
Story module
============

A story has got several steps linked together by connectors.
When the story runs a step bound actions are run first,
a user input is asked and then the first matching connector is taken to
go to the next step.
"""

from .actions import SendMessageAction

class Story:
    fallback_message = "Try something else..."
    """Fallback message to display when no connector is matching"""

    def __init__(self, first_step):
        """
            Args:
               first_step (str): The first step name
        """
        self._first_step = first_step
        self._current_step = first_step
        self._steps = {}
        self._finished = False

    def set_finished(self):
        """Sets story as finished"""
        self._finished = True

    def is_finished(self):
        """Tells story as finished"""
        return self._finished

    def run(self, interface):
        """Runs the story against an interface

            Args:
                interface (Interface): interface to use
        """
        while True:
            step = self.get_step(self._current_step)
            for action in step.get_actions():
                action.run(interface, self)
            if self.is_finished():
                return
            user_input = interface.read()
            for connector in step.get_connectors():
                if connector.matches(user_input):
                    self._current_step = connector.goto_step
                    break
            else:
                self.fallback(interface)

    def fallback(self, interface):
        """Runs fallback actions

            Args:
                interface (Interface): interface to use
        """
        action = SendMessageAction(self.fallback_message)
        action.run(interface, self)

    def add_step(self, step):
        """Add a step in the story

            Args:
                step (Step): step to add
        """
        self._steps[step.name] = step

    def get_step(self, stepname):
        """Gets step object from its name

            Args:
                stepname (str): step name

            Returns:
                Step: requested step
        """
        return self._steps[stepname]

    def reset(self):
        """Restarts the story"""
        self._finished = False
        self._current_step = self._first_step

