import win32com.client as wincom

from settings import opts
import speech


voice = wincom.Dispatch('SAPI.SpVoice')


def set_voice(voice_id):
	voice.Voice = voice.GetVoices().Item(voice_id)


def say(text, error=False):
	name = 'jarvis'
	if error:
		name = 'error'

	voice.say(text)
	print(speech.log(name, text))


def error(error_msg):
	say(error_msg, error=True)


set_voice(opts['voice'])