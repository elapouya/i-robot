# Created : 2018-06-11
#
# @author: Eric Lapouyade
"""
=============
Intent module
=============

An intent links a pattern to match to a story to run.
Intents are detected at bot level.
"""


import re

class Intent:
    def __init__(self, pattern, story):
        """
            Args:
                pattern (str): The regex to search
                story (Story): The story to run
        """
        self.pattern = pattern
        self.story = story

    def matches(self, user_input):
        """Check whether the user input matches the intent

            Args:
                user_input (str): The user input to challenge

            returns:
                bool: True if matches
        """
        return re.search(self.pattern, user_input, flags=re.I)
