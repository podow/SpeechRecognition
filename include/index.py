import os
import sys
import webbrowser
import speech_recognition as sr


def talk(words):
    print(words)
    os.system("say " + words)


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        words = r.recognize_google(audio).lower()
        print("Command is: " + words)
    except sr.UnknownValueError:
        talk("I'm understand")
        words = command()

    return words


def makeSomething(command):
    if "open website" in command:
        talk("Open website")
        url = 'http://localhost:8080/home/index'
        webbrowser.open(url)
    elif "stop" in command:
        talk("Stop program")
        sys.exit()


while True:
    makeSomething(command())
