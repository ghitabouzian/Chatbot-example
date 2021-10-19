import pyjokes
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia




listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa","")
                print(command)
    except:
        pass
    return command

def run_alexa():
    command=take_command()
    if "play" in command:
        song = command.replace("play","")
        talk("playing"+ song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p") #%H %M gives 20:01 not 08:01 pm
        print(time)
        talk("It is currently"+ time)

    elif "who is" in command:
        person = command.replace('who is',"")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "joke" in command:
        talk(pyjokes.get_joke())
    elif "i am bored" in command:
        talk('You could watch something or get work done')
    elif "am i super cool" in command:
        talk ("yes you are")
    elif "what's my favorite ice cream flavor" in command:
        talk("Pistachio and Vanilla")
    elif "mom" in command:
        talk("Fatima Zahra")
    else:
        talk("Please repeat")



while True:
    run_alexa()