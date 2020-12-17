import speech_recognition as sr
import pyttsx3
import pyaudio
import pywhatkit
import wikipedia
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_comand():
    try:
        with sr.Microphone() as source:
            print("Listening.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            ##print(command)
            #talk(command)

    except:
        pass
    return command

def run_alexa():
    command = take_comand()

    if 'play' in command:
        command = command.replace('play', '')
        print(command)
        talk("playing "+command)
        pywhatkit.playonyt(command)
    if 'time' in command:
        time= datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+time)
    elif 'date' in command:
        talk('sorry, I have a boyfriend.')
    elif 'are you single' in command:
        talk('sorry, I am in a relationship. please do not waste your time.')
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)


run_alexa()
# if __name__ == '__main__':


