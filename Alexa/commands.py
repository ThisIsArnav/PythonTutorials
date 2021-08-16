import speech_recognition as sr
import pyttsx3
from Global.print_talk import print_talk

# ################# For Commands #############################

import os
try:
    import pywhatkit
except:
    pass
import datetime
import pyjokes
from Tools.google import search
from Tools.google import wiki
from Tools.email_bot import get_email_info as email_
from Tools.Selfie.main import start as selfie
from Tools.translator import run as trans
from Tools.map import map_

# ###########################################################

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def _take_command():
    try:
        with sr.Microphone() as source:
            print_talk('listening...')
            voice = listener.listen(source)
            print("Processing")
            command = ""
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        print('some error')
    return command


def _commands():
    command = _take_command()
    print(command)
    if 'play' in command:
        vid = command.replace('play', '')
        talk('playing ' + vid)
        pywhatkit.playonyt(vid)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print_talk('Current time is ' + time)
    elif any(item.lower() == command.lower() for item in ["what is", "how"]):
        print_talk("Results for " + command)
        q = command.replace('what is', '')
        pywhatkit.search(q)
    elif 'lol' in command:
        talk('lol')
    elif 'idiot' in command:
        print_talk('u are a idiot?')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'security' in command:
        from Tools.security_cam.security_cam import run
        run()
    elif 'hack' in command:
        os.startfile("C:/Users/Tanush/Personal/Other-Stuff/lol.bat")
    elif 'email' in command:
        e = input('what ur email: ')
        if e == '':
            e = "protanushsingh@gmail.com"
        print(e)
        p = input('Whats ur password: ')
        print(p)
        email_(e, p)
    elif any(item.lower() == command.lower() for item in ["word", "note", "book", "wordpad"]):
        from Tools.word.word import Word
        Word()
    elif 'define' in command:
        try:
            q = command.replace('define', '')
            wiki(q)
        except:
            print_talk("Results for " + command)
            q = command.replace('define', '')
            search(q)
    elif any(item.lower() == command.lower() for item in ["quit", "stop", "shut up"]):
        quit()
    elif "selfie" in command:
        selfie()
    elif any(item.lower() == command.lower() for item in ["translate", "covert", "say"]):
        trans()
    elif any(item.lower() == command.lower() for item in ["map", "go to", "navigate", "maps", "place"]):
        map_()
    elif any(item.lower() == command.lower() for item in ["whatsapp", "message", "send", "chat"]):
        pywhatkit.sendwhatmsg("+919740710041", "Yo sent from whatsapp bot", 00, 5)
    else:
        if command != "":
            print_talk("Results for " + command)
            search(command)
        else:
            print_talk("Please say the command again")
