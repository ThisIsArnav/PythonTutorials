import webbrowser
from Global.print_talk import print_talk
from Global.speech_recognize import _take_command


def map_():
    print_talk("Where u want to go?")
    cmd = _take_command()
    print(cmd)
    print_talk("Going to " + cmd)
    q = cmd
    try:
        webbrowser.open('https://google.com/maps?q=' + q)
        print_talk("Hope it helps")
    except:
        print_talk("Can't Find the place u want :(")

