import pyttsx3
from pyttsx3 import engine
import speech_recognition as sr
import wikipedia
import webbrowser
from pyfirmata import Arduino,util
from pyfirmata import OUTPUT
import time
import os

engine = pyttsx3.init('sapi5')

board = Arduino('COM1')

board.digital[10].mode = OUTPUT
board.digital[11].mode = OUTPUT
board.digital[12].mode = OUTPUT
board.digital[2].mode = OUTPUT
board.digital[3].mode = OUTPUT
board.digital[4].mode = OUTPUT
board.digital[5].mode = OUTPUT

def greenled():
    board.digital[2].write(0)
    board.digital[3].write(1)
    board.digital[4].write(0)
    board.digital[5].write(0)


def blueled():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(1)
    board.digital[5].write(0)


def yellowled():
    board.digital[2].write(0)
    board.digital[3].write(0)
    board.digital[4].write(0)
    board.digital[5].write(1)

board.digital[10].write(1)
board.digital[11].write(1)
board.digital[12].write(1)
time.sleep(20)

def speech(audio):
    engine.say(audio)
    engine.runAndWait()


def listen():
    voice = sr.Recognizer()
    mic = sr.Microphone.list_microphone_names()
    # print(mic)

    mic = sr.Microphone(device_index=1)
    # print(mic)

    with mic as source:
        print("listening..")
        board.digital[2].write(1)
        board.digital[3].write(0)
        board.digital[4].write(0)
        board.digital[5].write(0)

        voice.pause_threshold = 0.8
        audio = voice.listen(source)
        print(audio)

    try:
        print("Recognizing")
        greenled()
        query = voice.recognize_google(audio,language="en-in")
        print("Harshit said",query)

    except Exception as e:
        print(e)
        print("say that again")
        blueled()
        time.sleep(3)

        return "None"

    return query

speech('Hello Harshit')
speech('Welcome to voice control system')
speech('Now you can control your iot devices by voice and command me to fetch anything via internet')
time.sleep(3)
speech('now command me')



while True:
    query = listen().lower()
    if'who is' in query:
        speech('wait let me search ')
        yellowled()
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speech(results)

    elif'play music' in query:
        speech('ok, here is your music')
        yellowled()
        codepath = 'C:\\Users\\Music'
        Music = os.listdir(codepath)
        os.startfile(os.path.join(codepath,Music[0]))
        time.sleep(3)

    elif'google' in query:
        speech("wait let me google it")
        yellowled()
        webbrowser.open(query)
        time.sleep(3)

    elif'red light off' in query:
        speech('turning red light off')
        yellowled()
        board.digital[10].write('0'.encode('ascii'))
        time.sleep(3)

    elif'red light on' in query:
        yellowled()
        speech('turning red light on')
        board.digital[10].write('1'.encode('ascii'))
        time.sleep(3)

    elif'orange light off' in query:
        yellowled()
        speech('turning orange light off')
        board.digital[11].write('0'.encode('ascii'))
        time.sleep(3)

    elif'orange light on' in query:
        yellowled()
        speech('turning orange light on')
        board.digital[11].write('1'.encode('ascii'))
        time.sleep(3)

    elif'pink light off' in query:
        yellowled()  
        speech('turning pink light off')
        board.digital[12].write('0'.encode('ascii'))
        time.sleep(3)

    elif'pink light on' in query:
        yellowled()
        speech('turning pink light on')
        board.digital[12].write('1'.encode('ascii'))
        time.sleep(3)