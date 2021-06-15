import pyttsx3
import speech_recognition as sr 
import time 
from datetime import datetime
import random
import os
import wolframalpha
import wikipedia
import sys
import webbrowser

"Make the program a class"
class AI:
    def __init__(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        self.responses = ['Yes sir.', 'As you wish.', 'Of course sir.',
             'Just one moment.' 'Right away sir.',
             'As you command.', 'Please wait.', 'One moment please.']
        self.inquiries = ['who', 'what', 'where', 'when', 'why', 'how']
        self.Websites = {'youtube' : 'https://www.youtube.com/',
        'google' : 'https://www.google.com/',
        'reddit' : 'https://www.reddit.com/',
        'td ameritrade' : 'https://www.tdameritrade.com/home.html',
        'gmail' : 'https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin',
        'ncbi' : 'https://www.ncbi.nlm.nih.gov/',
        'indeed' : 'https://www.indeed.com/',
        'github' : 'https://github.com/'}

 
    def speak(self, audio):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        self.engine.setProperty('rate', 190)
        self.engine.say(audio) #tells Python to self.speak variable 'text'
        self.engine.runAndWait() #waits for speech to finish and then continues with program
  
    def greet(self):
        greetings = ['Welcome back.', 'How are you today?', 
             'I\'ve missed you.']
        while True:
            if datetime.now().hour >= 6 and datetime.now().hour < 9:
                self.speak('Good morning sir.')
                self.speak(random.choice(greetings))
            elif datetime.now().hour >= 9 and datetime.now().hour < 14:
                self.speak('Good day sir.')
                self.speak(random.choice(greetings))
            elif datetime.now().hour >= 14 and datetime.now().hour < 18:
                self.speak('Good afternoon sir.')
                self.speak(random.choice(greetings))
            elif datetime.now().hour >= 18 and datetime.now().hour < 21:
                self.speak('Good evening sir.')
                self.speak(random.choice(greetings))
            elif datetime.now().hour >= 21 and datetime.now().hour < 24:
                self.speak('It\'s getting late sir.')
                self.speak(random.choice(greetings))
            break
    
    def takeCommand(self): #Main reply call function
        self.query = ""
        while True:
            with self.mic as source: #sets microphone
                self.r.adjust_for_ambient_noise(source)
                print("Waiting for command...") #prints to screen
                self.r.pause_threshold = 1
                audio = self.r.listen(source) #sets variable 'audio'
                self.r.recognize_sphinx(audio)
            try:
                self.query = self.r.recognize_sphinx(audio).lower() #now uses Google speech recognition
                break
            except sr.UnknownValueError:
                print("Sphinx could not understand audio")
                continue
            except sr.RequestError as e:
                print("Sphinx error; {0}".formate(e))
                continue
        return self.query
    
    def get_wiki(self):     #Opens the wikipedia page for something.  Format: "Open the wikipedia page
        self.speak(random.choice(self.responses))                       # 'For/on/about {what ever}
        split = self.query.split()                                              
        the_index = -1
        while True:
            if split[the_index] != 'for' or split[the_index] != 'on' or split[the_index] != 'about':
                the_index -= 1
                continue
            elif split[the_index] == 'for' or 'on' or 'about':
                self.query = split[the_index+1:]
                break
        for i in range(len(self.query)):
            self.query[i] = self.query[i].capitalize()
        for word in self.query:   #loops through words in self.query
            if self.query.index(word)%2 == 1: 
                self.query.insert(self.query.index(word), "_") 
        self.query = "".join(self.query)
        webbrowser.open("https://en.wikipedia.org/wiki/" + self.query)
      
    #Searches Google     
    def get_google(self):
        self.speak(random.choice(self.responses))
        quer = self.query.split()   #takes the self.query and splits it
        for word in quer:   #loops through words in self.query
            if quer.index(word)%2 == 1: 
                quer.insert(quer.index(word), "+")   #adds in + sign in every odd index
        quer = ''.join(quer)   #joins all words without any spaces
        webbrowser.open('https://www.google.com/' + quer)
        
    #Opens YouTube to search for a video by search word. Format: "Play {video} by {artist}      
    def play_vid(self):
        self.speak(random.choice(self.responses))    
        quer = self.query.split()
        quer.remove('play')
        quer.remove('by')
        for word in quer:   #loops through words in self.query
            if quer.index(word)%2 == 1: 
                quer.insert(self.query.index(word), "+")   #adds in + sign in every odd index
        "".join(quer)
        webbrowser.open('https://www.youtube.com/results?search_self.query=' + quer)
        
    #Directs to weather.com - 10-day forecast
    def get_weather(self):
        self.speak(random.choice(self.responses))
        webbrowser.open("https://weather.com/weather/tenday/l/c277dae335f9538e22909aaa3e887daa822dbde134f4379a25f368167c04bbfe")
    
    #Search WolframAlpha for answers to questions  
    def wolf(self):
        self.speak(random.choice(self.responses))
        question = self.query
        app_id = 'AQV4H4-8LWH8GRXWG'
        client = wolframalpha.Client(app_id)
        res = client.self.query(question)
        answer = next(res.results).text
        self.speak(answer)
        print(answer)            
    
    def open_site(self):
        self.speak(random.choice(self.responses))
        for site in self.Websites:    #checks if a pre-determined site is in query
            if site in self.query:    
                self.speak('Opening ' + str(site))
                webbrowser.open(self.Websites[str(site)])
        extensions = ['.com', '.org', '.gov']
        for x in extensions:
            if x in self.query:
                extension = x
                self.query = self.query.replace(x, "")
        quer = self.query.split()   
        if 'open up' in self.query:
            quer.remove('open')
            quer.remove('up')
        elif 'open' in quer:
            quer.remove('open')
        elif 'go to' in self.query:
            quer.remove('go')
            quer.remove('to')
        quer = "".join(quer)
        self.speak("Opening " + quer)
        webbrowser.open("https://www." + quer + str(extension))        
        
        
"""Main program"""
if __name__ == '__main__':
    AI = AI()
    try:
        AI.greet()
        while True:            #This will always keep it running.
            AI.takeCommand() #Since this resets query every time it's called, it will last forever.
          #Open specific wikipedia page
            if 'wikipedia' in AI.query:
                AI.get_wiki()
                continue
          #Play YouTube video
            elif "play" in AI.query and 'by' in AI.takeCommand(): #Play a video on youtube. Format: 'Play {What you want to play here}
                AI.play_vid()                    #by {artist or uploader}
                continue
          #Opens weather.com for my location
            elif 'weather' in AI.query:
                AI.get_weather()
                continue
          #Opens a website
            elif 'open' in AI.query or 'go to' in AI.query:
                AI.open_site()
                continue
            
          #Stops the program
            elif "terminate" in AI.query:
                break
          #Shuts down the computer
            elif "shut down" in AI.query:
                AI.speak("Shutting down, good bye sir.")
                break
                os.sytem("shutdown /s /t 1")
                      
          #Searches wolframalpha for answers to questions        
            for inquiry in AI.inquiries:
                if inquiry == AI.split[0]:
                    AI.wolf()
                    continue
    except KeyboardInterrupt:
        print("Interrupted")
        try: 
            sys.exit(0)
        except SystemExit:
            os._exit(0)