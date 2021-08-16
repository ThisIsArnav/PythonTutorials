from googletrans import Translator
import speech_recognition as sr
import gtts
import playsound
from Global.speech_recognize import _take_command
from Global.print_talk import print_talk

recognizer = sr.Recognizer()
translator = Translator()
dest = "../data/trans/trans.wav"

# http://www.lingoes.net/en/translator/langcode.htm


def run():

    input_lang = "hi"
    output_lang = 'en'

    print_talk("In which language u want to speak")

    i = input("Language (enter language code): ")
    if i.lower() == "hindi":
        i = "hi"

    print_talk("In which language u want to translate")
    print("Need help go to this url http://www.lingoes.net/en/translator/langcode.htm")
    o = input("Language (enter language code): ")
    if o.lower() == "english":
        o = "en"

    elif o.lower() == "hindi":
        o = "hi"

    if i == "":
        i = "hi"
    if o == "":
        o = "en"
    if i != "":
        input_lang = i
    if o != "":
        output_lang = o

    try:
        with sr.Microphone() as source:
            print('Speak Now')
            voice = recognizer.listen(source)
            print('processing')
            text = recognizer.recognize_google(voice, language=input_lang)
            print(text)
    except:
        print('error')

    translated = translator.translate(text, dest=output_lang)
    print(translated.text)
    print("Playing audio")
    converted_audio = gtts.gTTS(translated.text, lang=output_lang)
    converted_audio.save(dest)
    playsound.playsound(dest)
