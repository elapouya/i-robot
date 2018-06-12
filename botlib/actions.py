# Created : 2018-06-11
#
# @author: Eric Lapouyade


class Action:
    pass


class SendMessageAction(Action):
    def __init__(self, message):
        """
           Args:
               message (str): message to send
        """
        self.message = message

    def run(self, interface, story=None):
        """Send the message to the interface

           Args:
               interface (Interface): the interface to write
               story (Story): Story that triggered the action
        """
        interface.write(self.message)


class SendImageAction(Action):
    image_url_template = '<img src="{url}">'
    """Image url template to generate HTML code for the image"""

    def __init__(self, url):
        """
           Args:
               url (str): image url
        """
        self.image_url = url

    def run(self, interface, story=None):
        """Send an image to the interface

           Args:
               interface (Interface): the interface to write
               story (Story): Story that triggered the action
        """
        interface.write(self.image_url_template.format(url=self.image_url))


class EndStoryAction(Action):
    def run(self, interface, story=None):
        """Ends the story, go back to the intent detector

           Args:
               interface (Interface): the interface to write
               story (Story): Story that triggered the action
        """
        assert story, 'story must be specified'
        story.set_finished()


class ExitMessageAction(Action):
    def __init__(self, message):
        """
           Args:
               message (str): message to send
        """
        self.message = message

    def run(self, interface, story=None):
        """Exit the bot with a message

           Args:
               interface (Interface): the interface to write
               story (Story): Story that triggered the action
        """
        interface.write(self.message)
        exit(0)
