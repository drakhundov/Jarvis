# samuel v1.0

import sys
import time

import speech_recognition as sr
import assistant, speech, command
from settings import opts


argv = sys.argv


def implement(cmd):
    """ check, recognize, and execute command """

    # delete appeal to jarvis, and words like 'say', 'tell', 'please'
    cmd = speech.convert(cmd)

    print(speech.log('usr', cmd))

    # parse arguments
    data = speech.recognize(cmd)

    if '--info' in argv:
        for k, v in data.items():
            print(k, v)

    if not '--debug' in argv:
        command.execute(**data)


def listen(recognizer, audio):
    """ keep track of user's speech, and implement given command if user appealed to jarvis """

    try:
        text = recognizer.recognize_google(audio, language='en-EN').lower()

        # appeal to jarvis
        if text.startswith(tuple(opts['alias'])):
            implement(text)

    except sr.UnknownValueError:
        assistant.error('Unknown vote!')

    except sr.RequestError as e:
        assistant.error('Unknown error!')


if '-cmd' in argv:
    while True:
        try:
            cmd = input('command: ')
            implement(cmd)
        except:
            sys.exit()

else:
    assistant.say('Hi!')

    speech.start_listening(listen)

    while True:
        try:
            time.sleep(opts['interval'])
        except:
            sys.exit()
