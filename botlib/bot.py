# Created : 2018-06-11
#
# @author: Eric Lapouyade
"""
==========
Bot module
==========

The Bot class is initialized with an interface to interact with.
It loops for detecting an intent. If found, the bound story is run,
otherwise the fallback is triggered.
"""
from .actions import SendMessageAction

class Bot:
    fallback_message = "Please say something I understand (aide: hello, bonjour, bye, au revoir)"
    """Fallback message to display when no intent has been detected"""

    def __init__(self, interface):
        """
            Args:
               interface (Interface): the interface to interact with
        """
        self.interface = interface
        self.intents = []

    def add_intent(self, intent):
        """Add an intent to the bot

            Args:
               intent (Intent): the intent to add
        """
        self.intents.append(intent)

    def detect_intent(self, user_input):
        """Use user input to find the relevant intent

            Args:
                user_input (str) : User input

            Returns :
               Intent: the detected intent or None
        """
        for intent in self.intents:
            if intent.matches(user_input):
                return intent
        return None

    def fallback(self):
        """run fallback action(s)"""
        action = SendMessageAction(self.fallback_message)
        action.run(self.interface)

    def run(self):
        """Loop to get the revelant intent and run the bound story"""
        while True:
            user_input = self.interface.read()
            intent = self.detect_intent(user_input)
            if intent:
                story = intent.story
                story.reset()
                story.run(self.interface)
            else:
                self.fallback()