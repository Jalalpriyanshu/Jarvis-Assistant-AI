import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "4220c2d810394d9db5802fdc0d7f28ad"

def speak(text):
    engine.say(text)
    engine.runAndWait()
def processcammand(c):
   if "open google" in c.lower():
      webbrowser.open("https://google.com")
   elif  "open instagram" in c.lower():
      webbrowser.open("https://instagram.com")
   elif "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")
   elif c.lower().startswith("play"):
      song = c.lower().split(" ")[1]
      link = musiclibrary.music[song]
      webbrowser.open(link)

   elif "news" in c.lower():
      r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
      if r.status_code==200:
         
         data = r.json()
         articles = data.get('articles',[])

         for article in articles:
            speak(article['title'])
   

if __name__== "__main__":
    speak("initializing jarvis...")
    while True:
        # listen for the wake world "jarvis"
        #obtain audio from the microphone

        r=sr.Recognizer()
        
        
        print("recognizing...")
        try:
            with sr.Microphone() as source:
             print("listening...")
             audio = r.listen(source, timeout=10, phrase_time_limit=10)
             word = r.recognize_google(audio)
             if(word.lower()=="jarvis"):
                 speak("ya")
                 # listen for cammand
                 with sr.Microphone() as source:
                   print("jarvis active...")
                   audio = r.listen(source)
                   command = r.recognize_google(audio)

                   processcammand(command)
        except Exception as e:
            print("error; {0}".format(e))
