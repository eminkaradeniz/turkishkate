import os
import time
import playsound
import speech_recognition  as sr
from gtts import gTTS
import webbrowser
import pyfiglet
import sys

print("-" * 63)
banner=pyfiglet.figlet_format('Turkish Kate')
print(banner)
print(" " * 42 + 'By Emin Karadeniz')
print("-" * 63)


########   TEXT ---->> SPEACH ##########
def speak(text):
    tts=gTTS(text=text, lang='en', tld='co.uk')
    filename='voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        said="" 

        try:
            said=r.recognize_google(audio)
            print(said)

        except Exception as e:
            speak('i am sorry,i did not get what you say')

    return said


while True:
    text=get_audio()

    if 'hello' in text:
        speak('Hello, how are you')

    if 'what is your name' in text:
        speak('My name is kate')

    if 'who made you' in text:
        speak('Emin Karadeniz is my creator , he is smart and handsome ,i want him so much')

    if 'physical therapist' in text:
        speak('i am also created as a physical therapist whats wrong with you')

    if 'Google' in text:
        speak('Opening Google')
        webbrowser.open('https:/google.com.tr', new=2)

    if 'thank you' in text:
        speak('You are welcome ,I am always here for you')

    if 'goodbye' in text:
        speak('Why you are going off did i made a bad think')

