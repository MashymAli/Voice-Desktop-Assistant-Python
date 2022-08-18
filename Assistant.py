import pyttsx3, datetime, webbrowser, pyjokes,os,random,requests
import speech_recognition as sr
from time import strftime
from datetime import date
import pyautogui
import winshell, wikipedia
from requests import *


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):   #will say anyting you want
    engine.say(audio)
    engine.runAndWait()

def greetings():  #greet me when program is started according to time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello I am Alexa. How can i assist you?")
    print("Hello I am Alexa. How can i assist you?")

def listen():  #listen to me and recongnize it
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("User said ",query)
        print("\n") 
    except Exception as e:
        print("Sorry can you repeat that again please")
        speak("Sorry Can you repeat that again please")
        print("\n")
        return "None"
    return query

def weather():
    city = "your_city_name"
    appid= "your_api_id"
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}&units=metric").json()
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    humidity = res["main"]["humidity"]
    return f"{temperature}℃", f"{feels_like}℃", f"{humidity}%"
   
if __name__ == "__main__":
    
    greetings()
    counter=0   #to save screenshot as a new filenamae each time

    paths = {'chrome_path': 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s',
        'notepad':'C:\\Windows\\notepad',
        'music_dir':'C:\\Users\\Music',
        'vscode':'C:\\Users\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe',
        'netbeans':'C:\\Program Files\\NetBeans-12.5\\netbeans\\bin\\netbeans64.exe',
        }  #change paths according to your desktop

    while True:
        
        query = listen().lower()

        if 'open chrome' in query or 'open google' in query:
            speak("Opening Google Chrome.")
            webbrowser.get(paths.get('chrome_path')).open('google.com')

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.get(paths.get('chrome_path')).open('youtube.com')

        elif 'open wikipedia' in query:
            speak("Opening Wikipedia")
            webbrowser.get(paths.get('chrome_path')).open('wikipedia.com')

        elif 'open stackoverflow' in query:
            speak("Opening Stackoverflow")
            webbrowser.get(paths.get('chrome_path')).open('stackoverflow.com')

        elif 'open whatsapp' in query:
            speak("Opening Whatsapp")
            webbrowser.get(paths.get('chrome_path')).open('web.whatsapp.com')

        elif 'open notepad' in query:
            speak("Opening Notepad")
            notepad=paths.get('notepad')
            os.startfile(notepad)

        elif 'open cmd' in query or 'command prompt' in query:
            speak("Opening command prompt")
            os.system("start cmd")

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak("Your IP Address is "+ip)
            print(ip)

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)

        elif 'play music' in query or 'play song' in query:
            speak("Playing Song")
            music_dir = paths.get('music_dir')
            songs = os.listdir(music_dir) 
            songs.remove('desktop.ini')
            total_files = len(songs)  
            os.startfile(os.path.join(music_dir, songs[random.randint(0,total_files-1) ]))

        elif 'alexa' in query:
            speak("What can I do for you?") 

        elif 'time' in query:
            time = strftime('%I:%M %p')
            speak(time)

        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open("https://google.com/search?q=%s" % query)

        elif 'made you' in query or 'create you' in query:
            speak("I am created by Mashym")

        elif 'are you' in query:
            speak("I am alexa, mashym's dektop assistant")

        elif 'how are you' in query:
            speak("I am doing good after listening to you. What about you?")
            reply = listen().lower()
            if('am fine' in reply):
                speak("I am glad to hear that")
            else:
                speak("I am sorry to hear that.")

        elif 'date' in query:
            date = date.today()
            speak(date)

        elif 'screenshot' in query:
            speak("Taking Screenshot")
            Screenshot = pyautogui.screenshot()
            Screenshot.save(rf'C:\\Users\\Pictures\\Img{counter}.png') 
            counter+=1

        elif 'empty recycle bin' in query:
            speak("Emptying the recycle bin")
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)

        elif 'open code' in query:
            speak("Opening VS Code")
            vscode = paths.get('vscode')
            os.startfile(vscode)

        elif 'open netbeans' in query:
            speak("Opening Netbeans")
            netbeans = paths.get('netbeans') 
            os.startfile(netbeans)

        elif 'weather' in query:
            temperature, feels_like, humidity = weather()
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}, and humidity is {humidity} ")
            print(f"Temperature: {temperature}\nFeels like: {feels_like}\nHumidity: {humidity}")

        elif 'can you do' in query:
            speak("I can perform everyday tasks for you like emptying recycle bin, open youtube or google and also stackoverflow. As well as open netbeans and vscode for you or if you want me to screenshot something i can do that also. What can i do for you?")
    
        elif 'stop' in query or 'exit' in query or 'get lost' in query or 'bye' in query or 'shut up' in query:
            speak("Goodbye! I hope we will talk soon")
            exit()

            
            
  
