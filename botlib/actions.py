# Created : 2018-06-11
#
# @author: Eric Lapouyade


class Action:
    pass


class SendMessageAction(Action):
    def __init__(self, message):
        self.message = message

    def run(self, interface, story=None):
        interface.write(self.message)


class SendImageAction(Action):
    image_url_template = '<img src="{url}">'

    def __init__(self, url):
        self.image_url = url

    def run(self, interface, story=None):
        interface.write(self.image_url_template.format(url=self.image_url))


class EndStoryAction(Action):
    def run(self, interface, story=None):
        assert story, 'story must be specified'
        story.set_finished()


class ExitMessageAction(Action):
    def __init__(self, message):
        self.message = message

    def run(self, interface, story=None):
        interface.write(self.message)
        exit(0)
