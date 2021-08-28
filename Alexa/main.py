from commands import _commands
from Global.print_talk import print_talk


def run_alexa():
    _commands()


while True:
    try:
        run_alexa()
    except:
        print_talk("Error")
        break
