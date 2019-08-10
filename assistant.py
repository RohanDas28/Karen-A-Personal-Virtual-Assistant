import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

#For Some Normal Talk With Karen
def KarenSpeak():
    karen_there = ["Always at your service sir", "Yes Sir", "Always!", "Yes Sir, I Love Seeing you work"]
    karen_there_speak = random.choice(karen_there)
    speak(karen_there_speak)

def KarenLoveYou():
    karen_love = ["I Love You 3000 Sir", "I Love you too!", "yeah Sir Love You Too!"]
    karen_love_speak = random.choice(karen_love)
    speak(karen_love_speak)

#Applications Path
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
spotifypath= "C:\\Users\\User\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Spotify.lnk"
codePath = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")   

    else:
        speak("Good Evening Sir!")  

    speak("Hello Sir Karen's Here to Help You!")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except:   
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'shutdown' in query:
            quit(speak ('Shutting Down.... Good Bye Sir'))

        elif 'open youtube' in query:
            try:
                speak("opening youtube")
                webbrowser.get(chrome_path).open("youtube.com")
            except:
                speak("opening youtube")
                webbrowser.open("youtube.com")

        elif 'open google' in query:
            try:
                speak("opening google")
                webbrowser.get(chrome_path).open("google.com")
            except:
                speak('opening Google')
                webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            try:
                speak("opening stackoverflow")
                webbrowser.get(chrome_path).open("stackoverflow.com")
            except:
                speak('opening stackoverflow')
                webbrowser.open("stackoverflow.com")

        elif 'open facebook' in query:
            try:
                speak("opening facebook")
                webbrowser.get(chrome_path).open("facebook.com")
            except:
                speak("opening facebook")
                webbrowser.open("facebook.com")

        elif 'open twitter' in query:
            try:
                speak("opening twitter")
                webbrowser.get(chrome_path).open("twitter.com")
            except:
                speak("opening Twitter")
                webbrowser.open("twitter.com")

        elif 'open special website' in query:
            try:
                speak("Opening! please wait!")
                webbrowser.get(chrome_path).open("rohandas28.github.io")  
            except:
                speak("Opening Special Website!")
                webbrowser.open("rohandas28.github.io")

        elif 'play music' in query:
            try:
                os.startfile(spotifypath)
                speak('Playing Music!')
            except:
                speak("Sir Please Install Sptify First!")
                webbrowser.open("https://www.spotify.com/in/")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            try:
                os.startfile(codePath)
            except:
                speak("Please Install VSCode First!")
                webbrowser.open("https://code.visualstudio.com/")

        elif 'who made you' in query:
            speak("Rohan Das Is The Creator Of Me! I Love him 3000!")
        
        elif 'you there' in query:
            KarenSpeak()
        
        elif 'love you' in query:
            KarenLoveYou()