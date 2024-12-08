import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import wikipedia
import subprocess
import webbrowser
import smtplib
import sys
import time
import requests
import pyautogui
import os.path
import pip 
import GoogleNews
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from newsapi.newsapi_client import NewsApiClient

# User defined names and error handling messages
new_dict = {
    1: "Sorry, I didn't catch that. Could you repeat?",
    2: "Apologies, couldn't hear clearly. Say again?",
    3: "Didn't get that. Rephrase or speak louder?",
    4: "Trouble understanding. Repeat, please?",
    5: "Issue hearing. Try again?",
    6: "What's that again?",
    7: "Say that one more time, please?",
    8: "Hard time understanding. Repeat, please?",
    9: "Didn't catch that. Rephrase, please?",
    10: "Missed that. Question again?",
    11: "Repeat question, please?",
    12: "Didn't catch that. Say again?",
    13: "Couldn't understand. Try again?",
    14: "Hard time understanding. Repeat question?",
    15: "Didn't get that. Say again?",
    16: "Trouble hearing. Say again or speak up?",
    17: "Didn't catch that. Repeat or ask differently?",
    18: "Trouble understanding. Rephrase or ask again?",
    19: "Didn't understand. Explain differently or ask again?",
    20: "Trouble hearing. Speak clearly or repeat?"
}

new_name = {1: "Hi sir!",
             2: "Hello!",
             3: "Hey, how can I help you today sir?",
             4: "Good morning! How may I assist you?",
             5: "What can I do for you? Sir!",
             6: "How can I be of service? Sir!",
             7: "Welcome! How can I support you? Sir!",
             8: "Greetings! How may I assist you today?",
             9: "Hi! What brings you here?",
             10: "Hey there! How can I make your day better?",
             11: "Well, hello! What do you need help with Sir? ",
             12: "Hi, it's great to see you! How can I be helpful today?",
             13: "Hello, good to have you here! How can I assist you?",
             14: "Hey, it's great to see you again! How can I help you today?",
             15: "Good afternoon! How can I help you?",
             16: "Hi, I'm back! What can I do for you today?",
             17: "Hello! It's been a while. How can I help you today?",
             18: "Hi, I'm back! Is there anything I can do for you today?",
             19: "Hey there! Is there anything I can help you with today?",
             20: "Good evening! Is there anything I can do for you today?",
             21: "Hello! It's nice to see you. What can I do for you today?"}


def create_engine():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[-1].id)
    engine.setProperty('rate', 210)
    return engine

def speak(engine, audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1

    with sr.Microphone() as source:
        print("listening...")
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='hindi')
        print(f"User said: {query}")

    except Exception as e:
        print(f"Exception: {e}")
        return "none"
    return query

def main():
    engine = create_engine()

    while True:
        command = take_command().lower()
        if 'hello' in command:
            speak(engine, "नमस्ते!")

if __name__ == "__main__":
    main()

def username(s1):
    try:
        speak(f"what i should to call you Sir{s1}")
        s = take_command()
        s = s.replace("call me",'')
        speak(f"hello {s1}")
        speak(s)
        with open("data of user.text","a") as e:
            st = datetime.datetime.now()
            st1 = datetime.toda()
            e.write(f"{s} use me on {st1}at{st} / n")
            e.close()
            speak(f"how can i help you{s1}")
            
    except Exception as e:
        speak(f"{s1} i dont unnderstand , What did u say , PLease sat it again Sir")
        username(s1)

def me():
    s = "YES Sir! "
    speak(s)
    speak("how can i help you !")

def increase_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(min(1.0, current_volume + 1), None)

def open_calculator():
    subprocess.Popen('calc.exe')  # Open the calculator
    time.sleep(1)  # Allowing time for the calculator to open

def open_camera():
    speak("Opening the camera. Please wait for a moment.")
    # Open the camera using opencv-python
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        # Save the captured frame to the specified location
        output_path = "C:/AiOutput"
        os.makedirs(output_path, exist_ok=True)
        file_path = os.path.join(output_path, "captured_photo.jpg")
        cv2.imwrite(file_path, frame)
        speak(f"Photo captured and saved to {file_path}.")
    else:
        speak("Failed to capture the photo. Please try again.")
    cap.release()
    cv2.destroyAllWindows()

def get_latest_news():
    # Initialize the NewsApiClient with your API key
    newsapi = NewsApiClient(api_key='6c8718c72fa14e4a8a73ccd36588c0f9')

    # Fetch the top headlines
    top_headlines = newsapi.get_top_headlines(language='en')

    if top_headlines['status'] == 'ok':
        articles = top_headlines['articles']

        if articles:
            speak("Today's Top News Headlines:")
            for index, article in enumerate(articles, start=1):
                speak(f"{index}. {article['title']}")
        else:
            print("No articles found.")
    else:
        print("Failed to fetch news.")
        
global i1
global sex
def into():
    while (1):
        try:
            s1 = take_command().lower()
            s1 = s1.replace('im','')
            if 'prince kumar'in s1 or "prince" in s1:
                sex = 'sir'
            else:
                speak("please identify your self ")
                s1  = take_command().lower()
                if 'male' in s1 or 'boy'in s1:
                    speak("please identify your name")
                    if "prince kumar" in s1 or "prince" in s1:
                        wishme()

                elif "female " in s1 or "girl" in s1:
                    sex = "MADAMM."
                else:
                    into()
                    i1 =+1
                
            if "prince" not in s1:
                username(sex)
                # print(sex)
                wishme(sex)
                break
            else:
                # print(sex)
                wishme(sex)
                break
        except Exception as e:
            i1 =+1
            into()

def stoplisting():
    speak("for how much seconds you want to stop the program Sir?")
    if "10second"in query:
        try:
            a = int(take_command())
            speak("going to sleep Sir")
            speak(a)
            time.sleep(a)
        except Exception as e:
            speak(" I could not understand What did you sat ")
            stoplisting()

def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={'Jamshedpur'}&appid={'56464fe451976bc5af28936ab4e2d5c0'}&units=metric"

    response = requests.get(complete_url)
    if response.status_code == 200:
        weather_data = response.json()

        if weather_data["cod"] == 200:
            weather_description = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']

            print(f"Weather: {weather_description}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print("City not found.")
    else:
        print("Failed to fetch weather data.")
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = '56464fe451976bc5af28936ab4e2d5c0'
    city = 'Jamshedpur'  # Replace with your city name
    get_weather(api_key, city)

def walkupme():
    strftime = datetime.datetime.now().strftime("%I:%S:%p")
    speak(f"it is {strftime} you have yo wakeup Sir.")

def minimize_active_window():
    speak("Minimizing the windows...")
    # Get the currently active window
    active_window = gw.getActiveWindow()
    if active_window:
        active_window.minimize()

def slide_window_up():
    screenWidth, screenHeight = pyautogui.size()
    slide_distance = int(screenHeight / 2)  # Adjust the slide distance as needed
    pyautogui.moveTo(screenWidth // 2, screenHeight // 2 + slide_distance, duration=0.5)
    pyautogui.dragTo(screenWidth // 2, screenHeight // 2 - slide_distance, duration=0.5, button='left')


def run(self):
    speak("wakeup avi")
    while True:
        self.query = self.take_command()
        if "wake up " in self.query or "are you there " in self.query or"hello" in self.query:
            self.take_command()

def wishme():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M:%S:%p")
    current_time = time.strftime(("'%Y-%m-%d %A'"))
    if hour >= 0 and hour <= 12:
        speak(f"Good Morning, {current_time}")

    elif hour >=12 and hour >=18:
        speak(f"Good Afternoon, {current_time}")

    else:
        speak(f"Good Evening, {current_time}")

    speak(random.choice(new_name))

if __name__ == "__main__":
    into()
    wishme()
    speak(random.choice(new_name))
    
    while True:

        query = take_command().lower()
        
        if 'hi evi' in query or 'hello evi' in query:
            speak('how can i assist you?')

        elif "sleep" in query: 
            stoplisting()

        elif "wake up evi" in query:
            speak('I am there sir' or 'yes sir' or 'yes sir i am there for you please tell me how my i help you ')

        elif "open command" in query: 
            os.system("start cmd")

        elif "minimize the windows" in query or "slide down the windows" in query or "minimize everything" in query:
            minimize_active_window()

        elif "slide up windows" in query or "slide up window" or "pick up the windows":
            slide_window_up()

        elif "volume up" in query or "increase volume" in query:
            increase_volume()

        elif "open camera " in query:
            speak(f"opening camera")
            open_camera()

        elif "wikipedia" in query:
            speak("ohk Sir. Searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2) 
            speak("according to wikipedia")
            create_engine.setProperty('rate', 180)
            speak(results)
            print(results)

        elif "todays date and time" in query:
            speak("ohk sir")
            wishme()
            
        elif "hello" in query:
            speak(random.choice(new_name))

        elif "click" in query:
            pyautogui.click()

        elif "tell me news" in query or "tell me today news" in query or "say news"in query:
            get_latest_news()

        elif " tell me today's weather" in query:
                get_weather()

        elif "open calculator" in  query:
            speak("opening calculater")
            open_calculator()

        elif 'help me' in query:
            speak(f"How can i help you Sir")
            # speak("There are 3 thing that i can do for you sir i can search for it on google, youtube or wikipedia")  
            speak(f"where i should to serach ")
            s = take_command()
            s = take_command().lower()
            print("1. Google","2 . YouTube" , "3. wikipedia" , "4.exit")
            if s == 'google':
                speak(f"opening  google!")
                webbrowser.open("www.bing.com/search?q=" + s + "=9d02b0a92caa4bc895c28ea9269d27e6&FORM=ANAB01&PC=ASTS")
            
            elif s == "youtube" or "search on youtube":
                speak(f"opening youtube sir")
                speak("what should I Search in Youtube sir?")
                s = take_command()
                webbrowser.open("www.youtube.com/results?search_query="+ s)

            elif s == "wikipedia":
                speak("what should I Search in Wikipedia sir?")
                speak

            elif s == "exit":
                speak("ok sir..")
                exit()

        elif 'i want to search' in query or 'write'in query or "search" in query:
                speak("ok sir please say what you want to write or search sir")
                s=take_command()
                pyautogui.write(s)
                time.sleep(3)
                pyautogui.press('enter')
                speak("srearching sir.")

        elif "open youtube" in query:
            speak("about what should i Search on youtube Sir?.")
            s =  take_command()
            webbrowser.open("www.youtube.com/results?search_query="+ s)

            speak("sir, what should i search on google")
            cm = take_command().lower()
            webbrowser.open(f"{cm}")

        elif " set timer" in query or "set stopwatch" in query:
            speak("for how many minutes?")
            timing = take_command()
            timing = timing.replace('minutes','')
            timing = timing.replace('minutes','')
            timing = timing.replace('for','')
            timing = float(timing)
            timing = timing * 60
            speak(f"i will remind you in {timing} seconds")
            time.sleep(timing)
            speak('your time has been finished sir?')

        elif "no thanks" in query:
            speak("tanks for using me sir,have a good day sir.")
            sys.exit()

        elif " open the hackthebox" or 'hackthebox' in query:
            s = take_command()
            s = take_command().lower()
            if s == 'hackthebox':
                speak ("opening the hackthebox")
                webbrowser.open("https://www.hackthebox.com/")
            elif s == 'open hackthebox':
                speak('sure sir'or'ohk sir'or 'opening the hacthebox')
                webbrowser.open("https://www.hackthebox.com")
            elif s == 'leave it'or 'dont open hackthebox' or 'exit':
                speak('ohk sir..')
                exit()

        elif " open the tryhackme" or 'tryhackme' in query:
            s = take_command()
            s = take_command().lower()
            if s == 'tryhackme':
                speak ("opening the tryhackme")
                webbrowser.open("https://www.tryhackme.com/")
            elif s == 'open tyhackme':
                speak('sure sir'or'ohk sir'or 'opening the tryhackme')
                webbrowser.open("https://www.tryhackme.com")
            elif s == 'leave it'or 'dont open tryhackme' or 'exit':
                speak('ohk sir..')
                exit()

        elif "close notepad" in query:
            speak("okay sir, closing notpad")
            os.system("taskkill /f /im notpad.exe")

        elif "tell me a joke" in query:
            joke = pyjoke.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif" restart the system" in query:
            os.system("shutdown /r /t 1")

        elif "sleep the system" in query:
            os.system("rundll32.exe powerprof.idl,SetSuspended 0,1,0")

        elif "what's your name" in query or "what is your name" in query:
            speak("My name is evi. Nice to meet you Sir")

        elif "can we a friend's" in query:
            speak("off course Sir!")

        elif"tell me current time and date " in query:
            speak("sure Sir! {tt} ,{current_time}")

        elif"evi" in query:
            speak("hello i am there Sir!.")

        elif"say somethings " in query or "say somethings evi" in query:
            speak("what are doing sir!")
            s = take_command().lower()
            speak("okay SIr. let's do some fun")

        elif "switch the windows" in query or "switch the tab"in query:
            speak("okay sir")
            pyautogui.hotkey('alt','tab')

        elif "stop the music" in query or 'stop music' in query:
            speak('okay')
            pyautogui.press('Space')

        elif "play the music" in query or 'play' in query:
            speak("okay")
            pyautogui.press('space')

        elif "what is the time " in query:
            now_time = datetime.datetime.now()
            speak(f"okk Sir!  current time is{now_time}")

        elif "how are you" in query or "kasise ho " in query:
            speak("i am good . tell me about u sir")

        elif "Good evi" in query:
            speak('Thanks you sir..')

        elif "exit" in query:
            if "yes":
                speak("ok Sir have a nice day!")
                exit()
            else:
                break   
       

if __name__ == "__main__":
    wishme()