# Created : 2018-06-11
#
# @author: Eric Lapouyade

from .actions import SendMessageAction

class Story:
    fallback_message = "Try something else..."

    def __init__(self, first_step):
        self._first_step = first_step
        self._current_step = first_step
        self._steps = {}
        self._finished = False

    def set_finished(self):
        self._finished = True

    def is_finished(self):
        return self._finished

    def run(self, interface):
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
        action = SendMessageAction(self.fallback_message)
        action.run(interface, self)

    def add_step(self, step):
        self._steps[step.name] = step

    def get_step(self, stepname):
        return self._steps[stepname]

    def reset(self):
        self._finished = False
        self._current_step = self._first_step

