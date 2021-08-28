import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message, e, p):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login(e, p)
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'pip': 'rns576@gmail.com',
    'drum': 'sarojsingharnav@gmail.com',
    'pro': 'protanushsingh@gmail.com',
    'agriculture': 'agrosys.technologies@gmail.com'
}


def get_email_info(email, password):
    talk('To Whom you want to send email')
    name = get_info()
    try:
        receiver = email_list[name]
        print(receiver)
    except:
        print('I cant find the person u wanna send ur email... Please check email_list')
        talk('I cant find the person u wanna send ur email... Please check email_list')
        quit()
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    try:
        send_email(receiver, subject, message, email, password)
    except:
        print("""
    There is an error in sending ur email... Pls check:
    https://github.com/ThisIsArnav/PythonTutorials/blob/main/EmailBot/README.md#exeptions
    Make sure ur email and password are valid...
    """)
        talk("There is an error in sending ur email... Make sure ur email and password are valid...")
        quit()
    talk('Hey lazy ass. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info(email, password)
