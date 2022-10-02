import pyttsx3
import datetime
import wikipedia
import webbrowser as wb
import psutil
import pyjokes
import pyautogui

def get_saving_frames_durations(cap, saving_fps):
    """A function that returns the list of durations where to save the frames"""
    s = []
    # get the clip duration by dividing number of frames by the number of frames per second
    clip_duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)
    # use np.arange() to make floating-point steps
    for i in np.arange(0, clip_duration, 1 / saving_fps):
        s.append(i)
    return s

def youTube():
    speak('What Should I search in Youtube')
    z = input('Type Here')
    speak('searching for'+z+'on youtube')
    search_term = z.lower()
    speak('Here we go to Youtube')
    wb.open('https://www.youtube.com/results?search_query='+search_term)



