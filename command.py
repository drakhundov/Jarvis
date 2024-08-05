import datetime
import random

import assistant
import apps
from settings import opts


def execute(cmd, argv, percent):
    """ run command with given arguments """

    if cmd == 'ctime':
        time = datetime.datetime.now()
        assistant.say('It is ' + str(time.hour) + ':' + str(time.minute))
    elif cmd == 'stupid1':
        joke = random.choice(opts['jokes'])
        assistant.say(joke)
    elif cmd == 'weather':
        assistant.say(apps.weather(argv['place']))
    elif cmd == 'password':
        length = 10

        if argv.get('length'):
            length = int(argv['length'])

        assistant.say(apps.password.generate(length))
    elif cmd in ['addition', 'subtraction', 'division', 'multiplication']:
        n1, n2 = [int(i) for i in argv.values()]
        op = opts['op'][cmd]

        assistant.say(eval(f'{n1} {op} {n2}'))
