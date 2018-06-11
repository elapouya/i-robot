# Created : 2018-06-11
#
# @author: Eric Lapouyade
import re

class Intent:
    def __init__(self, pattern, story, priority=10):
        self.pattern = pattern
        self.story = story
        self.priority = priority

    def matches(self, user_input):
        return re.search(self.pattern, user_input, flags=re.I)
