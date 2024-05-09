import threading
from time import sleep

import speech_recognition as sr
from googletrans import Translator
from playsound import playsound as play_audio


def Speech_ON():
    sound_path = 'Body/Sounds/Speech_On.wav'
    play_audio(sound_path)


def Speech_OFF():
    sound_path = 'Body/Sounds/Speech_Off.wav'
    play_audio(sound_path)


def Error():
    sound_path = 'Body/Sounds/Error.wav'
    play_audio(sound_path)


def Listen():
    threading.Thread(target=Speech_ON).start()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 0)
        try:
            print("Recognizing...")
            sentences = r.recognize_google(audio, language='en-in')
            threading.Thread(target=Speech_OFF).start()
        except sr.UnknownValueError:
            threading.Thread(target=Error).start()
        except Exception as e:
            print(e)
            return ""
        return sentences


def ToEnglish(audio):
    if len(audio) > 3:
        Translate = Translator()
        Sent = Translate.translate(audio)
        text = Sent.text
        return text
    elif "None" in audio:
        print("Could not Understand")
    else:
        pass


def MicExecution():
    try:

        sentences = Listen()
        sentence = ToEnglish(sentences)
        print(f">> You : {sentences}")
        return sentence
    except UnboundLocalError:
        return 'Error'


