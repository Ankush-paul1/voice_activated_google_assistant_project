import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
engine=pyttsx3.init('sapi5')
engine.setProperty('rate',150)
engine.setProperty('volume',1.0)

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<=12:
        speak("good morning!")
    elif hour>12 and hour<=18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    speak("I am jarvis, tell me how may i help you")

def take_command():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("listening.....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("recognizing.....")
        querry=r.recognize_google(audio,language='in-en')
        print(f"you said: {querry}")

    except Exception as e:
        print("say that again please.....")
        return "None"
    return querry


if __name__=="__main__":
    wish_me()
    if 1:
        querry=take_command().lower()

        if "wikipedia" in querry:
            print("searching wikipedia.....")
            querry=querry.replace("wikipedia","")
            results=wikipedia.summary(querry,sentences=3)
            speak("according to wikipedia...")
            print(results)
            speak(results)

        elif "open youtube" in querry:
            webbrowser.open("youtube.com")
        
        elif "open google" in querry:
            webbrowser.open("google.com")
        
        elif "open stack overflow" in querry:
            webbrowser.open("stackoverflow.com")
        
        elif "the time" in querry:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            speak(time)

        elif "play song" in querry:
            music_dir="C:\\Users\\ANKUSH\\Desktop\\songs"
            songs=os.listdir(music_dir)
            len=len(songs)
            random_song=random.randint(0,len)
            os.startfile(os.path.join(music_dir,songs[random_song]))
