#!/usr/bin/env python
#
# Created : 2018-06-11
#
# @author: Eric Lapouyade

import argparse
from botlib.bot import Bot
from botlib.actions import *
from botlib.connectors import *
from botlib.intent import Intent
from botlib.step import Step
from botlib.story import Story
from botlib.interfaces import *

# Get CLI options
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--api", action="store_true", help="Use REST API")
args = parser.parse_args()

# Select the right interface:
if args.api:
    interface = APIInterface('http://api.facebook.com',
                             user='clustaar',
                             password='seemybot')
else:
    interface = ConsoleInterface()

# Define the first Intent/Story (English version)
story1 = Story(first_step='first_step')

step = Step('first_step')
step.add_action(SendMessageAction('Hi, how are you ? (tips: fine or sad)'))
step.add_connector(IFContainsConnector('fine_step','fine'))
step.add_connector(IFContainsConnector('sad_step','sad'))
story1.add_step(step)

step = Step('fine_step')
step.add_action(SendMessageAction('Cool'))
step.add_action(EndStoryAction())
story1.add_step(step)

step = Step('sad_step')
step.add_action(SendMessageAction('Why ? (tips: bad day)'))
step.add_connector(IFContainsConnector('bad_day_step','day'))
story1.add_step(step)

step = Step('bad_day_step')
step.add_action(SendMessageAction('Here is something to brighten your day :'))
step.add_action(SendImageAction('https://i.imgur.com/4QvA1xc.gif'))
step.add_action(EndStoryAction())
story1.add_step(step)

intent1 = Intent('hello', story1)


# Define a 2nd Intent/Story (French version)
story2 = Story(first_step='first_step')
step = Step('first_step')
step.add_action(SendMessageAction('Salut, comment ça va? (aide: roule ou triste)'))
step.add_connector(IFContainsConnector('fine_step','roule'))  # ex : ca roule
step.add_connector(IFContainsConnector('sad_step','triste'))
story2.add_step(step)

step = Step('fine_step')
step.add_action(SendMessageAction('Super !'))
step.add_action(EndStoryAction())
story2.add_step(step)

step = Step('sad_step')
step.add_action(SendMessageAction("Mais qu'est-ce qui ne va pas ? (aide: pas mon jour)"))
step.add_connector(IFContainsConnector('bad_day_step','jour'))  # ex : c pas mon jour
story2.add_step(step)

step = Step('bad_day_step')
step.add_action(SendMessageAction('Voici de quoi remonter le moral :'))
step.add_action(SendImageAction('https://i.imgur.com/4QvA1xc.gif'))
step.add_action(EndStoryAction())
story2.add_step(step)

intent2 = Intent('Bonjour', story2)


# Define a 3rd Intent/Story (To exit the bot)
story3 = Story(first_step='exit_step')
exit_step = Step('exit_step')
exit_step.add_action(ExitMessageAction('Bye bye.'))
story3.add_step(exit_step)

intent3 = Intent('bye|revoir', story3)


# Instantiate a bot
irobot = Bot(interface)

# add intents
irobot.add_intent(intent1)
irobot.add_intent(intent2)
irobot.add_intent(intent3)

# run the bot.
try:
    irobot.run()
except (KeyboardInterrupt, EOFError):
    print('\n\nI Robot has been stopped, have a nice day.\n\n')

