
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyautogui
from playsound import playsound
import webbrowser
import os
import time
from plyer import notification
# import main



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate' , 170)
# engine.setProperty('pitch' , 2000)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)   
    if hour>=0 and hour<12 :
        print("Good Morning Sir")
        speak("good morning Sir!")
    elif hour>=12 and hour<15:
        print("Good Noon Sir!")
        speak("good noon  Sir!")
    elif hour>=15 and hour<18:
        print("Good Afternoon Sir")
        speak("good afternoon Sir!")
    else:
        print("Good Evening Sir!")
        speak("good evening sir!")

def takecommand():
    '''
    take command takes input from the microphone and returns string output.
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("I am listening sir...")
        r.pause_threshold = 1
        r.energy_threshold = 1700
        audio = r.listen(source)

    try:
        '''
        we use try when there is a posibility of getting error 
        '''
        print("recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print("you said: ", query)

    except Exception  :
        
        print("sorry sir say that again please...")
        return "none"
    return query

def writecommand():
    '''
    this command helps you to write through voice input.
    It can also open a blank page, go to next line, can increase and decrease the size of the text(if allowed), can use bold italic underline functions
    also select a line(not sentence) either from start or from end. REMEMBER THIS IS AN INFINITE LOOP. SO TO EXIT THE LOOP TELL FRIDAY "EXIT"
    '''
    speak("alright sir, writing mode activated!")
    while True:
        abc = takecommand().lower()
        
        if 'type' in abc:
            speak("okay sir!")
            write = takecommand()
            pyautogui.typewrite(write)
        elif 'open a blank page' in abc:
            speak("alright sir!")
            pyautogui.hotkey('enter')
        elif 'next line' in abc:
            speak("right sir!")
            pyautogui.hotkey('enter')
        elif 'enter' in abc:
            speak("yes sir!")
            pyautogui.hotkey('enter')
        elif 'select the line' in abc:
            speak("yes sir!")
            pyautogui.hotkey('shift','home')
        elif 'exit' in abc:
            speak("yes sir!writing mode is now disabled!")
            break
                
#Paths for apllications.........
browser = webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s")
notepad_path = "C:\\WINDOWS\\system32\\notepad.exe"           
msword_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe"
msexcel_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.exe"
poweront_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.exe"
chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

if __name__ == "__main__":
    
    speak("Checking all system applications!")
    speak("installing all the drivers")
    speak("calibrating and examining all the core processes")
    playsound('D:\\Frost\\activating sound.mp3')
    notification.notify(title = "F_R_I_D_A_Y", message = "Welcome Back Sir!", app_icon = 'D:\\Frost\\circleknot.ico', timeout = 30)
    wishme()
    speak("welcome back")
    speak("please have a seat, i am ready for your command")
    while True :
        query = takecommand().lower()

        if 'who are you' in query:
            print("my name is friday, i am a voice assistant.")
            speak("my name is friday, i am a voice assistant.")

        elif 'what can you do' in query or 'how can you help me' in query:
            print("i am still in development, but i can play music, search wikipedia, open any website")
            speak("i am still in development, but i can play music, search wikipedia, open any website")

        elif 'hello friday' in query or 'hello' in query or 'hi' in query:
            print("hello sir! how can I help you?")
            speak("hello sir! how can I help you?")

        elif 'are you there' in query:
            print("yes sir!")
            speak("yes sir!")

        elif 'time to sleep' in query:
            print("okay sir! good night! see you next time")
            speak("okay sir! good night! see you next time") 

        elif 'good morning' in query:
            print("thank you sir ! hope you have a nice day!")
            speak("thank you sir ! hope you have a nice day!")

        elif 'good night' in query :
            hour = int(datetime.datetime.now().hour)
            if hour>= 0 and hour<=12:
                print("Sir! Its already morning!")
                speak("sir! its already morning!")
            elif hour > 12 and hour <=17 :
                print("Its noon sir!")
                speak("its noon sir!")
            elif hour >17 and hour <= 21 :
                print("Its not an usual time for good night!")
                speak("Its not an usual style for good night!")
            else :
                print("thank you sir")
                speak("thank you sir")

        elif 'thank you' in query:
            print("it's my pleasure sir!!!")
            speak("it's my pleasure sir!!!") 

        elif 'owner' in query:
            print("My owner is Bidyut Kumar Das.")
            speak("My owner is Bidyut Kumar Das.")

        elif 'open youtube' in query:
            speak("alright sir! opening youtube!")
            browser.open("youtube.com")

        elif 'open google' in query:
            browser.open("google.com")

        elif 'open gmail' in query:
            speak("yes sir! opening your gmail inbox!")
            browser.open("mail.google.com")
            speak("gmail opened sir")

        elif 'open notepad' in query:
            speak("yes sir! opening notepad")
            os.startfile(notepad_path)

        elif 'open microsoft word' in query:
            speak("Yes sir! Opening microsoft word!")
            os.startfile(msword_path)
            time.sleep(4)
            speak("Do you want me to type for you?") 
            msword = takecommand().lower()               
            if 'yes' in msword:
                writecommand()
            elif 'no' in msword:
                speak("okay sir! no problem!")
            else:
                break

        elif 'open excel'in query:
            speak("on the way of opening excel sir!")
            os.startfile(msexcel_path)
        elif 'activate writing mode' in query:
            writecommand()
        
        elif 'launch chrome' in query:
            os.startfile(chrome_path)
            
        elif 'open new tab' in query:
            pyautogui.hotkey('ctrl','t')

        elif 'open start menu' in query:
            pyautogui.press('winleft')

        elif 'close start menu'in query:
            pyautogui.press('winleft')

        elif 'minimise' in query:
            pyautogui.hotkey('winleft','down','down')
        elif 'auto kill' in query:
            time.sleep(5)
            while true:
                pyautogui.click()
                time.sleep(0.7)
        else:
            continue
                
         
            
        