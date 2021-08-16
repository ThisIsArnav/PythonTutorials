import speech_recognition as sr
from Global.print_talk import print_talk


listener = sr.Recognizer()


def _take_command():
    try:
        with sr.Microphone() as source:
            print_talk('listening...')
            voice = listener.listen(source)
            print("Processing")
            command = ""
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        print('some error')
    return command
