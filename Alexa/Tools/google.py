import wikipedia
import webbrowser
from Global.talk import talk
from Global.print_talk import print_talk


def search(q):
    webbrowser.open('https://google.com/search?q=' + q)


def wiki(q):
    try:
        info = wikipedia.summary(q, 1)
        print(info)
        talk(info)
    except:
        print_talk("Can't Find what u want :(")
