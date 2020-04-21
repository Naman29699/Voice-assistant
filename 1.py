import os 
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from random import randint
import webbrowser
import subprocess
import datetime

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(':', '-')+"-note.txt"
    with open(file_name, 'w') as f:
        f.write(text)
    subprocess.Popen(['notepad.exe', file_name])


def speak(text):
    tts = gTTS(text= text, lang='en')
    filename = '{}{}{}.mp3'.format(randint(0, 9), randint(0, 9), randint(0, 9))
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=3, timeout = 9)
        said = ''
        try:
            said = r.recognize_google(audio)
            print(said.lower())
        except Exception:
            print("Try speaking again, I did not catch that.")
    return said.lower()
    
    
def get_wake_audio():
    r = sr.Recognizer()    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ''
        try:
            said = r.recognize_google(audio)
            print(said.lower())
            if 'hey bro' in said:
                breakpoint
        except Exception:
            print("Try speaking again, I did not catch that.")
    return said.lower()

GREETINGS = ['hello', 'hi', 'what up', 'hey', 'yo' ]
NOTE_STRS = ['make a note', 'write this down', 'remember this']
WAKE = 'hey bro'


speak("How can I help you")
text = get_audio()

for greeting in GREETINGS:
    if greeting in text:
        speak("how are you doing")
if "what is your name" in text:
    speak("my name is Cool Assistant")
if "youtube" in text:
    webbrowser.open('https://www.youtube.com/')
if 'spotify' in text: 
    subprocess.call([r"C:\Users\naman\AppData\Roaming\Spotify\Spotify.exe"])
for phrase in NOTE_STRS:
    if phrase in text:
        speak('What would you like me to write down?')
        note_text = get_audio()
        note(note_text)
        speak('I have made a note of that')

