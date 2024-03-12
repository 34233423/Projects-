#api_key=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
import pyttsx3
import speech_recognition as sr
import datetime
import time
import random
import os
import requests
import webbrowser
import wikipedia
import pywhatkit
import pyautogui
import sys
from openai import OpenAI
def ss():
     speak("Sir, Please tell me the name of the screenshot image")
     try:
          name = takecommand()
     except:
           speak("I can't undrestand please type that again")
           name=input("Enter the file name: ") 
     speak("I am taking screenshot")
     img = pyautogui.screenshot()
     img.save(f"{name}.png")
     speak("I am done sir.")     

def speak(audio):
     engine=pyttsx3.init('sapi5')
     voices=engine.getProperty('voices')
     print(voices[0].id)
    # Set the speaking rate to 140 words per minute
     engine.setProperty('rate', 140)
     # Set the speaking voice to a specific voice ID
     engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\MSSam')
     # Set the volume to 0.8 (80%)
     engine.setProperty('volume', 1.0)
     engine.say(audio)
     engine.runAndWait()
     print(audio)

def takecommand():
    r=sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("Adjusting for ambient noise...")
                r.adjust_for_ambient_noise(source)
                print("Listening....")
                r.pause_threshold=1
                audio = r.listen(source,timeout=10,phrase_time_limit=5)
            
                print("Recognizing")
                query=r.recognize_google(audio,language='en-in')
                print(f"User said: {query}")
                return query
        except:
                speak("Say that again Please")
                continue
    

def notepad():
    speak("Opening notepad")
    path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Notepad++"
    os.startfile(path)

def cls_notepad():
    spaek("closing notepad")
    os.system("taskkill /f /in notepad.exe")

def cmd():
    speak("opening command prompt")
    os.system("start cmd")

def ip_address():
    ip=requests.get("https://api.ipify.org").text
    speak(f"your IP address is :{ip}")

def music():
    music_dir = "D:\\mini_folder"
    songs = os.listdir(music_dir)
    rd = random.choice(songs)
    os.startfile(os.path.join(music_dir,rd))

def yt():
    speak("opening YouTube")
    webbrowser.open("www.youtube.com")

def play_yt():
    speak("What video do you need ")
    name = takecommand().lower()
    speak("playing "+ name)
    pywhatkit.playonyt(name)

def google():
    speak("What should I search on google, sir")
    qry=takecommand().lower()
    webbrowser.open(f"https://www.google.com//search?q={qry}")

def wiki():
    speak("What you want to search on wikipedia")
    qry=takecommand().lower()
    result = wikipedia.summary(qry,sentences=2)
    speak(f"According to wikipedia: {result}")
    print(result)

def whats_msg():
    speak("Enter the number")
    no = input("Enter the number with country code: ")
    speak("Tell me the message")
    msg = takecommand()
    speak("Enter specific time")
    hour = int(input("Enter the hour: "))
    minu = int(input("Enter the minutes: "))
    pywhatkit.sendwhatmsg(no,msg,hour,minu)

def wish():
    hour = int(datetime.datetime.now().hour)
    tt=time.strftime("%I %M %p")
    if (0 <= hour <12):
        a="Good Morning, Sir","Hello sir, Good Morning" 
        speak(random.choice(a)+"It is "+tt)
    elif (12 <= hour <=18):
        a="Good afternoon, Sir","Hello sir, Good afternoon"
        speak(random.choice(a)+"It is "+tt)
    else:
        a="Good Evening, Sir","Hello sir, Good Evening"
        speak(random.choice(a)+"It is "+tt)

    #speak("I am Jarvis, How may I help you")
    b="How may I help you Sir","Give me a command sir","Online and ready sir."
    speak("I am the system assistant "+random.choice(b))

def stop():
    f = "bye sir","see you again sir","as your wish, but I don't want to leave you sir"    
    speak(random.choice(f))
    sys.exit(0)

def ai():
    client = OpenAI()
    promt=takecommand()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": promt}
            ])
    response=completion.choices[0].message.content
    lines=response.splitlines()
    crt_res='\n'.join(line.strip() for line in lines)
    print(crt_res) 
    


if __name__ == '__main__':
    wish()
    # openai.api_key = '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'
    # response = openai.Completion.create(
    #     engine='text-davinci-003',
    #     prompt="Translate the following English text to French: [your text here] Hello",
    #     max_tokens=150
    #     )
    # generated_text = response.choices[0].text.strip()
    # print(generated_text)
        
    while True:
        query= takecommand().lower()  
        if "open notead" in query:
            notepad()
        elif "open cmd" in query:
            cmd()
        elif "close notepad" in query:
            cls_notepad()
        elif "ip address" in query:
            ip_address()
        elif "play music" in query:
            music()
        elif "open youtube" in query:
            yt()
        elif "open google" in query:
            google()
        elif "search on wikipedia" in query:
            wiki()
        elif "play on youtube" in query:
            play_yt()
        elif "send whatsapp message" in query:
            whats_msg()
        elif "screenshot" in query:
            ss()
        elif "stop" in query:
            stop()
        else:
            speak("I would try openai for this.")
            ai()
        speak("Do you want any other work..")
