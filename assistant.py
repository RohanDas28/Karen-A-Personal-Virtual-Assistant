import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#Applications Path 
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
spotifypath= "C:\\Users\\YourUserName\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Spotify.lnk"
codePath = "C:\\Users\\YourUserName\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello Sir I am Karen, I am Your Personal Assistant, How Can I Help You?")       

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
            speak("opening youtube")
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'open google' in query:
            speak("opening google")
            webbrowser.get(chrome_path).open("google.com")

        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.get(chrome_path).open("stackoverflow.com")

        elif 'open facebook' in query:
            speak("opening facebook")
            webbrowser.get(chrome_path).open("facebook.com")

        elif 'open twitter' in query:
            speak("opening twitter")
            webbrowser.get(chrome_path).open("twitter.com")

        elif 'open special website' in query:
            speak("Opening! please wait!")
            webbrowser.get(chrome_path).open("rohandas28.github.io")  


        elif 'play music' in query:
            os.startfile(spotifypath)
            speak('Playing Music!')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            os.startfile(codePath)

        elif 'who made you' in query:
            speak("Rohan Das Is The Creator Of Me!, He Is a Nice Person. You Must Follow Him On Github!")
  
