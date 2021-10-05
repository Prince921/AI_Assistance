import pyttsx3
import datetime
import wikipedia
import webbrowser as wb
import psutil
import pyjokes
import pyautogui

def wishMe():
    
    
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good Morning Sir. ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir. ")
    elif hour>=18 and hour<24:
        speak("Good evening Sir. ")
    else:
        speak("It's too sir I think you should sleep now. Tell me what can I fo you.")
    speak("Welcome Back, How may I help you?")
def searchChrome():
    speak('What should I search')
    y = input('Type here')
    speak('searching for'+y+'on Chrome')
    chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    search = y.lower()
    wb.get(chromepath).open_new_tab(search+'.com')