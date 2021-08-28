import pywhatkit
from Global.speech_recognize import _take_command
from Global.print_talk import print_talk
import datetime

num = ""
receiver = ""
err = 0

phone_list = {
    'papa': "+919740710041",
    'drum': '+919916100384',
}


def take_info():
    global num

    num = _take_command()

    global receiver
    receiver = phone_list[num]
    print(receiver)

    return receiver


def send_msg():
    print_talk("To whom u wanna sent whatsapp message")
    try:
        take_info()
    except:
        print_talk(f"I couldn't find {num} u wanna send message")
        print_talk("Pls try again")

        global err
        err = 1
        while err != 4:
            take_info()
            if err == err:
                break
            else:
                err = err + 1

    print_talk("Whats ur whatsapp message")
    msg = _take_command()
    print(msg)
    time_h = datetime.datetime.now().hour
    time_m = datetime.datetime.now().minute
    print(f"Current time {str(time_h)}:{str(time_m)}")

    print_talk("The message will be sent within 20 secs")
    pywhatkit.sendwhatmsg_instantly(receiver, msg)

