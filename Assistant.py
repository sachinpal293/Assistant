import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import Emaii_Bot
import downloader
import webbrowser

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning i am Jarves")
    elif hour>=12 and hour<18:
        talk("Good Afternoon i am jarves ")
    else:
        talk("Good Evening i am jarves")
def takecammand():
    try:

        with sr.Microphone() as source:
            print("Listening....")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'hey google'  in command:
                command = command.replace('hey google','')

    except Exception as e:
        pass
    return command

def run():
   try:
       command = takecammand()
       print(command)
       if 'play' in command:
           song = command.replace('play', '')
           talk("Playing " + song)
           a = pywhatkit.playonyt(song)
           print(a)
       elif 'time' in command:
           time = datetime.datetime.now().strftime('%I:%M %p')
           print(time)
           talk('current time is ' + time)
   #
       elif 'wikipedia' in command:
           person = command.replace('wikipedia', '')
           info = wikipedia.summary(person, sentences=2)
           print(info)
           talk(info)
   #
       elif 'search' in command:
           topic = command.replace('search', '')
           talk('seacrhing ' + topic)
           info = pywhatkit.search(topic)

       elif 'send mail' in command:
           Emaii_Bot.get_email_info()

       elif 'download' in command:
           inp = command.replace('download', '')
           a = pywhatkit.playonyt(inp)
           downloader.takedata(a)

       elif 'open youtube' in command:
           webbrowser.open('www.youtube.com')

       elif 'open Google' in command:
           webbrowser.open('www.google.com')


       elif 'open geeksforgeek' in command:
           webbrowser.open('www.geeksforgeek.com')

       elif 'open gmail' in command:
           webbrowser.open('https://mail.google.com/mail/u/0/#inbox/FMfcgzGlksCTJQTCwdzwxpRzQNtgDNfj')

   except Exception as e:
        pass

if __name__ == '__main__':
    wishme()
    run()


