import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import sys
import os
import time
from googlesearch import search



engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
engine.setProperty("voice", voice[0].id)
# print(voice[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak('All the the servers working fine in the backend')
    speak("Ace   got   online successfully ")
    print("Ace got online successfully")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Mr.Kumar how are you")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Mr.Kumar  how are you")
    else:
        speak("Good Evening Mr.Kumar how are you")


def takeCommand(c):
    """Takes microphone input from the user and returns string output"""

    R = sr.Recognizer()
    R.energy_threshold = 4000
    with sr.Microphone() as source:
        print("Listening...")
        R.pause_threshold = 1
        audio = R.listen(source)

    try:
        print("Recognizing...")
        query = R.recognize(
            audio
        )  # Here we are recognizing the audio which is given as an input.
        print(f"Command:{query}\n")

    except Exception as e:
        print(e)
        speak(c)
        print("Say that again")
        return "None"
    return query


if __name__ == "__main__":

    wishMe()
    while True:
        c = "this is meop"
        query = takeCommand(c).lower()

        # Logic for executing task. 
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
       
        elif 'open youtube' in query:
            chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'
            c = webbrowser.get(chrome_path).open('youtube.com')
        elif 'facebook' in query:
            chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'
            c = webbrowser.get(chrome_path).open('facebook.com')
            
        elif 'google' in query:
            m = "Take This"
            variable = takeCommand(m)
            chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'
            c = webbrowser.get(chrome_path)
            c.open_new_tab(f'{variable}')
            

            
        
        # Don't jave songs right now.        
        # elif 'play music' in query:
        #     music_dir = 'D:\\Songs'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir,songs[0]))


        elif 'time' in query:
            curr_time = time.strftime("%H:%M:%S", time.localtime())
            print(curr_time)
            speak(curr_time)
        


            
        elif "introduce" in query:
            speak("Hi everyone there I'm ace ")
            speak('Archit\'s artificial intelligence system. I was made and was commenced by Mr.Kumar on 3 December 2021 .Since then we are working together on several projects.And today is my first birthday,that\'s why I\'m here talking to you. Wish me Happy Birthday.THank You')

        elif 'open code' in query:
            codePath = "C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code.exe"
            os.startfile(codePath)

  
                        
        elif 'shutdown' in query:
            speak('All the servers are shutting and ace is going offline.')
            speak('Have a good day Mr.Kumar.')
            quit()
            
        elif 'email' in query:
            try:
                speak("To whom you want to send the email")
                a = "This is for the inconvinence"
                n = takeCommand(a)
                email = "architkumar1550@gmail.com"
                b = "Can't understand say it again"
                content = takeCommand(b)
                # sendEmail(email,content)
                speak("Email has been sent")
                    
            except Exception as e:
                print(e)
                speak("Invalid Task")
            
