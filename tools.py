import speech_recognition as sr
import assistant


def voices():
	return assistant.voice.GetVoices()


def description(voice_id):
	return assistant.voice.GetVoices().Item(voice_id).GetDescription()


def mic_index():
	for index, name in enumerate(sr.Microphone.list_microphone_names()):
		print('Name: \"{1}\"\nIndex: {0}'.format(index, name))