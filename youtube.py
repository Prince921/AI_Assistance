import pyttsx3
import datetime
import wikipedia
import webbrowser as wb
import psutil
import pyjokes
import pyautogui


def youTube():
    speak('What Should I search in Youtube')
    z = input('Type Here')
    speak('searching for'+z+'on youtube')
    search_term = z.lower()
    speak('Here we go to Youtube')
    wb.open('https://www.youtube.com/results?search_query='+search_term)