import Tk as Tk
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
from FBLogin import fblogin
from EmailAttachment import emailattach
from EmailMessage import sendMessageEmail
import subprocess
import wolframalpha
import requests
import pyjokes
from requests import get
#from twilio.rest import Client
#from ecapture import ecapture as ec
#import ecapture as ec
from tkinter import *
import cv2
#import Image
import PIL.Image, PIL.ImageTk
import random
import smtplib
import roman
# from Class1 import Student
# import pytesseract
from PIL import Image

numbers = {'hundred':100, 'thousand':1000, 'lakh':100000}
a = {'name':'your email'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning sir!!")
    elif 12 <= hour < 18:
        speak("Good Afternoon sir!!")
    else:
        speak("Good Evening,sir!!")
    #speak("what can i help you with...")
    speak("We hope you are safe, lets begin the presentation")


def takecommand():
    """it takes input from user"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 500
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        queryy = r.recognize_google(audio, language='en-US')
        print(f"User : {queryy}\n")
    except Exception as ee:
        print("can't recognize say that again...")
        print(ee)
        return "None"
    return queryy


if __name__ == "__main__":
    greet()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "who i am" in query:
            speak("If you talk then definately your human.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'open youtube' in query:
            chromePath = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
            webbrowser.get('chrome').open("youtube.com")
        elif 'open google' in query:
            chromePath = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
            webbrowser.get('chrome').open("google.com")
        elif 'open stack overflow' in query:
            chromePath = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
            webbrowser.get('chrome').open("stackoverflow.com")

        elif 'play songs' in query:
            music_dir = "E:\\Project\\Assistant - Copy\\songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{strTime}")

        elif 'news' in query:
            chromePath = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
            webbrowser.get('chrome').open("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')

        elif "weather" in query:
            # Google Open weather website
            # to get API of Open weather
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takecommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'open pycharm' in query:
            appPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.3\\bin\\pycharm64.exe"
            os.startfile(appPath)

        elif 'open word' in query:
            appPath = "C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.EXE"
            os.startfile(appPath)

        elif 'open powerpoint' in query:
            appPath = "C:\\Program Files\\Microsoft Office\\Office16\\POWERPNT.EXE"
            os.startfile(appPath)

        # elif "send message " in query:
        #     # You need to create an account on Twilio to use this service
        #     account_sid = 'Account Sid key'
        #     auth_token = 'Auth token'
        #     client = Client(account_sid, auth_token)
        #
        #     message = client.messages \
        #         .create(
        #         body=takecommand(),
        #         from_='Sender No',
        #         to='Receiver No'
        #     )
        #
        #     print(message.sid)

        elif 'email' in query:
            speak("what you want to do?")
            workToDo = takecommand().lower()
            try:
                if 'file' in workToDo:
                    emailattach()
                    speak("Email has been sent !")
                    print("Email has been sent !")
                elif 'message' in workToDo:
                    speak("what should i sent???")
                    content = takecommand()
                    to = "18it122@charusat.edu.in"
                    sendMessageEmail(to, content)
                    speak("Email has been sent !")
                    print("Email has been sent !")
            except Exception as e:
                print(e)
                speak("Sorry ,i am not able to send this email!")

        elif 'facebook' in query:
            speak('enter your username and password ')
            fblogin()
            speak("logging in...")

        elif 'question' in query:
            speak('Ask any computational or geographical question')
            question = takecommand()
            app_id = "75T4VE-U49LKHAVJJ"
            client = wolframalpha.Client('75T4VE-U49LKHAVJJ')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "log off" in query or "sign out" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif 'exit' in query:
            speak("Thank you sir!")
            print("Thank you sir!")
            exit()

        else:
            search = 'https://www.google.com/search?q=' + query
            webbrowser.open(search)

def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('JARVIS')

label = Label(window, width = 500, height = 500)
label.pack()
window.after(0, update, 0)

btn0 = Button(text = 'WISH ME',width = 20, command = wishme, bg = '#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text = 'PLAY',width = 20,command = play, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()


window.mainloop()