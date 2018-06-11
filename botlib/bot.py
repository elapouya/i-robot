# Created : 2018-06-11
#
# @author: Eric Lapouyade

from .actions import SendMessageAction

class Bot:
    fallback_message = "Please say something I understand"

    def __init__(self, interface):
        self.interface = interface
        self.intents = []

    def add_intent(self, intent):
        self.intents.append(intent)

    def detect_intent(self, user_input):
        for intent in sorted(self.intents, key=lambda i:i.priority):
            if intent.matches(user_input):
                return intent
        return None

    def fallback(self):
        action = SendMessageAction(self.fallback_message)
        action.run(self.interface)

    def run(self):
        while True:
            user_input = self.interface.read()
            intent = self.detect_intent(user_input)
            if intent:
                story = intent.story
                story.reset()
                story.run(self.interface)
            else:
                self.fallback()