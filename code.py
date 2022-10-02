import pyttsx3
import datetime
import wikipedia
import webbrowser as wb
import psutil
import pyjokes
import pyautogui
from speak immport speak
from wish import wishMe
from date import date_
from time import time
from youtube import youTube

engine = pyttsx3.init()

def Next_Locate():
    speak('What should I find?')
    x = input('Type here')
    speak('You asked to find'+x)
    wb.open_new_tab('http://www.google.com/maps/place/'+x)
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
def Jokes():
    speak(pyjokes.get_joke())
def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/Shanu srivastava/PicturesScreenshots')
def Say():
    speak('What do you want me to say?')
    x = input('Type here')
    speak(x)
def Locate():
    speak('What should I find?')
    x = input('Type here')
    speak('You asked to find'+x)
    wb.open_new_tab('http://www.google.com/maps/place/'+x)
def apicall():
    speak('What should I search in Google?')
    x = input('Type here')
    speak('searching for'+x+'on Google')
    search_Term = x.lower()
    speak('Searching')
    speak('Here we go to Google')
    wb.open('http://www.google.com/search?q='+search_Term)
def wheather():
    usage = str(psutil.cpu_percent())
    speak('Cpu is at')
    speak(usage)
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent) 
def Temp_convert():
    speak('Welcome to this Temperature Conversion Porgram')
    speak('Enter 1 if you want to convert from Celsius')
    speak('Enter 2 if you want to convert from Fahrenheit')
    speak('Enter 3 if you want to convert from Kelvin')
    while True:
        speak('Enter your choice')
        x = input('Enter your choice.. : ')
        y=int(x)
        # Logic to convert when Celsius is Given
        if y==1:
            speak('Enter the temperature in Celcius')
            temp = input('Given temperature in Celsius: ')
            temp_c=int(temp)
            temp_f = (9/5*temp_c)+32
            temp_k = temp_c + 273.15
            temp_f = round(temp_f, 4)
            temp_c = round(temp_c, 4)
            temp_k = round(temp_k, 4)
            speak('\nDegrees Celsius:\t\t'+str(temp_c))
            speak('Degrees Fahrenheit:\t\t'+str(temp_f))
            speak('Degrees Kelvin:\t\t\t'+str(temp_k))
        #Logic to solve when Fahrenheit is Given
        elif y==2:
            speak('Enter the Temperature in Fahrenheit')
            temp = input('Given temperature in Fahrenheit: ')
            temp_f = int(temp)
            temp_c = (5/9)*(temp_f-32)
            temp_k = temp_c+273.15
            temp_f = round(temp_f, 4)
            temp_c = round(temp_c, 4)
            temp_k = round(temp_k, 4)
            speak('\nDegrees Fehrenheit:\t\t'+str(temp_f))
            speak('Degrees Celsius:\t\t'+str(temp_c))
            speak('Degrees Kelvin:\t\t\t'+str(temp_k))
        #Logic to solve when Kelvin is Given
        elif y==3:
            speak('Enter the Temperature in Kelvin')
            temp = input('Given temperature in Kelvin: ')
            temp_k = int(temp)
            temp_c = temp_k-273.15
            temp_f = (9/5*temp_c)+32
    
            temp_f = round(temp_f, 4)
            temp_c = round(temp_c, 4)
            temp_k = round(temp_k, 4)
            speak('\nDegrees Kelvin:\t\t\t' + str(temp_k))
            speak('Degrees Celsius:\t\t' + str(temp_c))
            speak('Degrees Fahrenheit:\t\t' + str(temp_f))
        for_quit = input('Enter y to quit')
        if for_quit == 'y':
            quit()
        else:
            continue
def Speed_con():
    speak('Welcome to this Speed Conversion Porgram')
    #taking name
    #Asking What type of conversion
    speak('\nEnter 1 to convert Miles/hour to Meter/seconds')
    speak('\nEnter 2 to convert meter/second to miles/hours')
    while True:
        speak('Enter your Choice')
        x = input('Enter your section')
        y = int(x)   #taking input in interger form only
        # Logic for Mph to Mps
        if y==1:
            speak('Enter speed in Miles per hour')
            mph = float(input('\nEnter speed in Miles/hour :'))
            mps = mph*0.4474
            mps = round(mps,2)
            speak('\nYour speed in Meter per second is '+str(mps)+' mps.')
        # Logic for Mps to Mph
        elif y==2:
            speak('Enter speed in meters per second')
            mps = float(input('\nEnter speed in Meters/second :'))
            mph = mps / 0.4474
            mph = round(mph, 2)
            speak('\nYour speed in Miles per hour is ' + str(mph) + ' mph.')
    
        else:
            print("\nEnter a valid Selection")
        for_quit = input('Enter y to quit')
        if for_quit == 'y':
            quit()
        else:
            continue
    else:
        print('Incorrect value')


if __name__ == "__main__":
    
    
    speak('Hi I am Jarvis')
    speak('I am personal assistance of Mister Prince')
    wishMe()
    speak('To know what I can do..type feature')
    while True:
        x = input('What should I do')
        
        if 'time' in x:
            speak(x)
            time_()
        elif 'date' in x:
            speak(x)
            date_()
        elif 'wikipedia' in x:
            speak(x)
            speak('Searching')
            x=x.replace('wikipedia','')
            result=wikipedia.summary(x,sentences=3)
            speak('According to wikipedia')
            print(result)
            speak(result)
        elif 'search' in x:
            speak(x)
            searchChrome()
        elif 'youtube' in x:
            speak(x)
            youTube()
        elif 'google' in x:
            Google()
        elif 'cpu' in x:
            speak(x)
            CPU()
        elif 'joke' in x:
            speak(x)
            Jokes()
        elif 'screenshot' in x:
            speak(x)
            try:
                screenshot()
            except:
                speak('Sorry Sir cannot take screen shot')
        elif 'say' in x:
            Say()
        elif 'convert' in x:
            speak("Press 1 to convert temperature and 2 to convert Speed")
            y = input("Enter choice : ")
            if y=='1':
                Temp_convert()
            elif y=='2':
                Speed_con()
        elif 'find' in x:
            Locate()
        
        elif 'sleep' in x:
            speak(x)
            speak('Okay sir.')
            quit()
        elif 'feature' in x:
            speak('I can do many things')
            speak('I can tell you current time and date')
            speak('I can search anything on Google, Youtube, or on wikipedia')
            speak("I can even Tell you joke..but if you don't laugh thats not my problem")
            speak("I can find any location you want me to find")
            speak('I can even speak whatever you want me to speak')
            speak('I can tell you status of Battery of this device')
            speak('I am made my Mister Prince Srivastava and I hope he will make me do more thing.')

        else:
            print('what next?')

 
