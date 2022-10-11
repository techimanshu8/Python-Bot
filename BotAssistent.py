import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('rate',130)
engine.setProperty('voice', 'english')


def speak(audio):
    print(audio)
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

    speak("I am Your Assistent Sir. Please tell me how may I help you")       

def takequery():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again querylease...")  
        return "None"
    return query

def RecogniseVoice():
    speak("Press Control-c to exit any time")
    while:
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)
                print("Recognizing...")    
                query = r.recognize_google(audio, language='en-in')
                print(f" {query}\n")

        except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
        except KeyboardInterrupt:
            print("Exiting")
            return "PressExit"
        except sr.UnknownValueError:
            print("unknown error occured")
    

def OpenTTS():
    speak("Here you can type any text to speak")
    try:
        while(True):
            text = input()
            speak(text)
    except KeyboardInterrupt:
        print("Thanks For using me")
        return 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takequery().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")  

        elif ('text to speech' in query) or ("recognise text" in query ) or ("tts" in query) or ("speak text") :
            OpenTTS()

        elif("recognise voice" in query) or ("voice to text" in query) or("to text" in query) or("listen me" in query):
            RecogniseVoice() 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            os.system("code")
        
        elif ("vlcplayer" in query) or ("player" in query) or ("vlc" in query) :
            os.system("VLC")
        
        elif ("excel" in query) or ("msexcel" in query) or ("sheet" in query):
            os.system("excel")

        elif ("NOTE" in query) or ("NOTES" in query) or ("NOTEPAD" in query) or ("EDITOR" in query) or ("9" in query):
            os.system("Notepad")
        elif  ("mspowerpoint" in query) or ("ppt" in query) or ("powerpoint" in query):
            os.system("powerpnt")
 
        elif ("word" in query) or ("msword" in query):
            os.system("winword")        

        elif ("email to " in query) or ("send email " in query) or ("email" in query) :
            try:
                speak("What should I say?")
                content = takequery()

                speak("To whom you want to send")
                to = "hs696984@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email , Check username password please")   

        elif 'open ' or 'search ' in query :
            query = query.replace("open" or "search" , "")
            response = googlesearch.search(query)
            for result in response :
                webbrowser.open_new_tab(f"{result}")
                break 
        
        elif ' link ' in query :
            response = googlesearch.search(query)
            i=0 
            for result in response :
                i = i+1 
                print("Title: " + result)
                if i>=10 :
                    break 
        elif 'exit' in query :
            confirm =input("Enter command(-1 for exit)\n")
            if(confirm=="-1")
                speak("Exiting , Hope to see you again")
                break
