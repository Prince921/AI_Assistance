import pyttsx3
import datetime
import wikipedia
import webbrowser as wb
import psutil
import pyjokes
import pyautogui
from speak immport speak


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def Google():
    speak('What should I search in Google?')
    x = input('Type here')
    speak('searching for'+x+'on Google')
    search_Term = x.lower()
    speak('Searching')
    speak('Here we go to Google')
    wb.open('http://www.google.com/search?q='+search_Term)
def CPU():
    usage = str(psutil.cpu_percent())
    speak('Cpu is at')
    speak(usage)
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent) 
