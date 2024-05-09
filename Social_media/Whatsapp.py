import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime
global c
from Body.Listen import MicExecution

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))


def sendMessage():
    speak("Who do you want to message. Your hotlist contains: Dad, Mom, Manish, Vishesh")
    b = MicExecution().lower()
    names = {"dad": True,
             "mom": True,
             "manish": True,
             "vishesh": True,
             "sir": True
             }

    # Split the input string into individual words
    '''global c'''
    words = b.split()
    # Iterate through the words and check if they exist in the keyword dictionary
    for word in words:
        if word in names:
            c = word  # If any word matches, return True
    if c == "dad":
        speak("Whats the message")
        message = MicExecution()
        pywhatkit.sendwhatmsg("+919960455322",message,time_hour=strTime,time_min=update)
    elif c == "mom":
        speak("Whats the message")
        message = MicExecution()
        pywhatkit.sendwhatmsg("+917385459387", message, time_hour=strTime, time_min=update)
    elif c == "manish":
        speak("Whats the message")
        message = MicExecution()
        pywhatkit.sendwhatmsg("+919028992643", message, time_hour=strTime, time_min=update)
    elif c == "vishesh":
        speak("Whats the message")
        message = MicExecution()
        pywhatkit.sendwhatmsg("+917738732737", message, time_hour=strTime, time_min=update)
    elif c == "sir":
        speak("Whats the message")
        message = MicExecution()
        pywhatkit.sendwhatmsg("+919224616102", message, time_hour=strTime, time_min=update)

