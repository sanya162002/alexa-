import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
import smtplib
def speak(text):
     engine =pyttsx3.init('sapi5')
     voices=engine.getProperty('voices')
     engine.setProperty('voice',voices[1].id)
     engine.say(text)
 def wishMe():
     hour=int(datetime.datetime.now().hour)
      if hour>=0 and hour<12:
          speak("good morning")
      elif hour >=12 and hour<18:
           speak("good afternoon")
        else:
        speak ("good evening")

    speak("hi there I am alexa. how I can help u")
    def takenCommand():
         r=sr.Recognizer()
         with sr.Microphone() as source:
            print("Listening.......")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("recognizing......")     
        query=r.recognize_google(audio,language='en-in')
        print("User said::",query)
   
    except  Exception as e:
        print("Come again please")
        return "None"
    
    return query
     def sendEmail(to,content):
        sever=smtplib.SMTP("smpt.gmail.com",587)
        sever.ehlo()
        sever.starttls()
        to=input("please enter an email address to send an email to: ")
        sever.login("sanya.bhatia990@gmail.com", "mymotherisbest")
        sever.sendmail("sanya.bhatia990l@gmail.com",to,content)

        sever.close()



   wishMe()
   while True:
       query=takenCommand().lower()
     if "wikipedia" in query:
        speak("searching in wikipedia")
        query=query.replace("wikipedia","")
        result=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(result)
        speak(result) 

    elif "open youtube"in query:
        webbrowser.open("youtube.com")
    elif "open facebook"in query:
        webbrowser.open("facebook.com")
    elif "open instagram"in query:
        webbrowser.open("instagram.com")
    elif "open google"in query:
        webbrowser.open("google.com")
    elif "open gmail"in query:
        webbrowser.open("mail.google.com") 
    elif "open news"in query:
        webbrowser.open("news.google.com")
    elif "open amazon"in query:
        webbrowser.open("www.amazon.in")


    elif "play music" in query:
        Music=("C:\\music")
        songs=os.listdir(Music)
        print(songs)
        os.startfile(os.path.join(Music,songs[0]))
    elif "the time" in query:
        e = datetime.datetime.now()
        speak ("The time is now %s:%s:%s" % (e.hour, e.minute, e.second))
    elif "open spotify" in query:
        codePath=("C:\\Users\\hp\\AppData\\Roaming\\Spotify\\Spotify.exe")
        os.startfile(codePath)

    elif "open whatapp" in query:
        codePath=("C:\\Users\\hp\\AppData\\Roaming\\whatapp\\whatpp.exe")
        os.startfile(codePath)
    elif "open telegram" in query:
        codePath=("C:\\Users\\hp\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
        os.startfile(codePath)
    elif "open  discord" in query:
        codePath=("C:\\Users\\hp\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")
        os.startfile(codePath)
    elif "open zoom" in query:
        codePath=("C:\\Users\\hp\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
        os.startfile(codePath)
    elif "open vs code"in query:
        codePath=("C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS \\Code.exe")
        os.startfile(codePath)
    elif "open power point" in query:
        codePath=("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")  
        os.startfile(codePath)
    elif "open excel" in query:
        codePath=("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
        os.startfile(codePath)
    elif "open word " in query:
        codePath=("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
        os.startfile(codePath)
    elif "open google chrome"in query:
        codePath=("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        os.startfile(codePath)
    elif "email to sanya"in query:
        try :
            speak("what i should i say?")
            content=takenCommand()
            to="sanya.bhatia990@gmail.com"
            sendEmail=(to,content)
            speak("please tell me what speak to them")
        except Exception as e:
            print("e")
            peak("sorry mam")

    elif "bye"in query:
        sys.exit()
    elif "shutdown" in query:
        shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")
        if shutdown == 'no':
            exit()
        else:
            yos.system("shutdown /s /t 1")
    elif "logout"in query:
        logout = input("Do you wish to log out your computer ? (yes / no): ")
        if logout == 'no':
            exit()
        else:
            os.system("shutdown -l")
    elif "restart" in query:
        restart = input("Do you wish to restart your computer ? (yes / no): ")
        if restart == 'no':
            exit()
        else:
            os.system("shutdown /r /t 1")
    
    
    
    else:
        try:
            from googlesearch import search 
        except ImportError: 
	        print("No module named 'google' found") 
        for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
            speak(f'opning {j}\n')
            webbrowser.open(j)
    
    
    

    
        




     


    








  



         
        




     


    








  