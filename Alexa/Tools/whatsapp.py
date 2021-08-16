import pywhatkit
from Global.speech_recognize import _take_command
from Global.print_talk import print_talk
import datetime
from datetime import timedelta

phone_list = {
    'papa': "+919740710041",
    'drum': '+919916100384',
}


def send_msg():
    print_talk("To whom u wanna sent whatsapp message")
    num = _take_command()
    receiver = phone_list[num]
    print(receiver)
    print_talk("Whats ur whatsapp message")
    msg = _take_command()
    print(msg)
    time_h = datetime.datetime.now().hour
    time_m = datetime.datetime.strptime(str(datetime.datetime.now()), '%d/%m/%Y %H:%M') + timedelta(minutes=1)
    print(time_m)

    #pywhatkit.sendwhatmsg(receiver, msg, time_h, int(time_m))


send_msg()
