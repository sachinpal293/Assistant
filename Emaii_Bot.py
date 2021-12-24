import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listner = sr.Recognizer()

engine = pyttsx3.init()
# engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listner.listen(source)
            info = listner.recognize_google(voice)
            print(info)
            return info.lower()

    except:
        pass

def send_email(reciver, subject,message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('srani1998p@gmail.com', 'abcdefghijklmnopqrstuvwxyz841238')
    email = EmailMessage()
    email['From'] = 'srani1998p@gmail.com'
    email['To'] = reciver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list={
    'shubham bhai':'shubhampal2698@gmail.com',
    'sachin': 'palsachin209@gmail.com',
    'ankit pal' : 'ankitpal1906@gmail.com',
    'poonam didi' : 'poonamrani1463@gmail.com',
    'manika': "manikagarg19@gmail.com",
    'lalita': "ly7379180@gmail.com",
    'karishma': "kadhitomar48@gmail.com",
    'muskan': "muskanposwal706@gmail.com",
    'shivani': "shivani2297@gmail.com",


}

def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    reciver = email_list[name]
    print(reciver)
    talk("What is the subject of your email?")
    subject = get_info()
    talk('tell me text in your email')
    message = get_info()
    send_email(reciver,subject,message)
    talk('Hey lazy ass.your email is sent')
    talk('Do you want to send more email?')
    send_more=get_info()
    if 'yes' in send_more:
        get_email_info()

if __name__ == '__main__':
    get_email_info()


