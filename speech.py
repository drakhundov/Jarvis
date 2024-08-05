import datetime

from fuzzywuzzy import fuzz

import speech_recognition as sr
from settings import opts


def start_listening(listen):
    """ start listening background to recognize user commands """

    r = sr.Recognizer()
    m = sr.Microphone(device_index=opts['microphone'])

    with m as source:
        r.adjust_for_ambient_noise(source)

    listening = r.listen_in_background(m, listen)


def convert(text):
    """ get rid of extraneous words (appeal, 'say', 'tell') """

    cmd = text.split(' ')

    for alias in opts['alias']:
        while alias in cmd:
            del cmd[cmd.index(alias)]

    for tbr in opts['tbr']:
        while tbr in cmd:
            del cmd[cmd.index(tbr)]
    
    return ' '.join(cmd)


def recognize(cmd):
    """ recognize command (most close to user command) and parse arguments if needed
        
        $argv - single argument
        TODO: $*argv_list - list of arguments (maybe saparated by 'and' or comma)
    """

    data = {
        'cmd': '',
        'percent': 0,
        'argv': {}
    }

    for command, calls in opts['cmds'].items():
    	for call in calls:
            cmdv = cmd.split(' ')
            callv = call.split(' ')

            l_call = len(callv)
            l_cmd = len(cmdv)

            if l_call == l_cmd:
                for i in range(l_call):
                    if callv[i].startswith(opts['arg_indicator']):
                        cmdv[i] = callv[i]
            else:
                continue

            ratio = fuzz.token_set_ratio(
                ' '.join(cmdv),
                ' '.join(callv)
            )
            
            # more accurate command founded
            if ratio > data['percent']:
                data['cmd'] = command
                data['percent'] = ratio

                # refresh argument list
                data['argv'] = {}
                cmdv = cmd.split(' ')
                for i in range(l_call):
                    if callv[i].startswith(opts['arg_indicator']):
                        data['argv'][callv[i][1:]] = cmdv[i]
                 
    return data


def log(source, msg):
    """ create log text from given message and source """

    t = datetime.datetime.now().strftime(
        '%b %Y %p %I:%M:%S'
    )

    return f'[{t}] {source}: {msg}'
