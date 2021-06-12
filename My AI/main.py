""" I want to make my own AI assistant and maybe 
add in a synthesized voice or the OG Aku from 
Samurai Jack (rip Mako). To get the trained voice
I can find something online or use Microsoft's Azure
program to train a custom voice.

I need this AI to be able to listen to me through
my microphone, recognize speech, and return the 
results I want. I'll have to give it funcitonality
to surf the web and get information. Wikipedia 
and Wolfram Alpha will help.

I could also make an Excel sheet of possible 
answers/responses to my question/orders.
"""

""" Step 1: Speech recognition & text-to-speech
Write function that will listen to my voice 
and recognize speech. Then have it respond."""

import random
import speech_recognition as sr
import pyttsx3
import os
import wolframalpha
import wikipedia
import webbrowser
from datetime import datetime

global responses
responses = ['Yes sir.', 'As you wish.', 'Of course sir.',
             'Just one moment.' 'Right away sir.',
             'As you command.', 'Please wait.']

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 185)
global r
r = sr.Recognizer()
global mic
mic = sr.Microphone()

""" Now do text to speech """
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def greet():
    greetings = ['Welcome back.', 'How are you today?', 
             'I\'ve missed you.']
    if datetime.now().hour >= 6 and datetime.now().hour < 9:
        speak('Good morning sir.')
        speak(random.choice(greetings))
    elif datetime.now().hour >= 9 and datetime.now().hour < 14:
        speak('Good day sir.')
        speak(random.choice(greetings))
    elif datetime.now().hour >= 14 and datetime.now().hour < 18:
        speak('Good afternoon sir.')
        speak(random.choice(greetings))
    elif datetime.now().hour >= 18 and datetime.now().hour < 21:
        speak('Good evening sir.')
        speak(random.choice(greetings))
             

""" Make a recognizer function to start when 
you say certain words """    
keywords = [("Jarvis"), ('hey Jarvis') ('yo Jarvis')]


def rise():
    calls = ['Yes sir?', 'You called sir?', 'What can I help you with?', 'What do you need?', 'Listening sir']
    while True:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
            r.recognize_sphinx(audio)
            for keyword in keywords:
                if keyword in r.recognize_sphinx(audio):
                    try:
                        speak(random.choice(calls))
                        break
                        takeCommand()
                    except sr.UnknownValueError:
                        print("Sphinx could not understand audio")
                        continue
                    except sr.RequestError as e:
                        print("Sphinx error; {0}".formate(e))
                        continue
                else:
                    print('Keyword not heard, try again')
                    continue
def takeCommand():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        r.recognize_sphinx(audio)
    try:
        print("Recognizing...")   
        query = r.recognize_sphinx(audio, language ='en-in')
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".formate(e))
    return query

""" Step 2: Web surfing. """
#Open wikipedia page on something
def get_wiki(query):
    speak(random.choice(responses))
    split = query.split()
    the_index = -2
    while True:
        if split[the_index] != 'for' or 'on' or 'about':
            the_index -= 1
            continue
        elif split[the_index] == 'for' or 'on' or 'about':
            query = split[the_index+1:]
            break
    for i in range(len(query)):
        query[i] = query[i].capitalize()
    for word in query:   #loops through words in query
        if query.index(word)%2 == 1: 
            query.insert(query.index(word), "_") 
    query = "".join(query)
    webbrowser.open("https://en.wikipedia.org/wiki/" + str(query))
    
def get_google(query):
    speak(random.choice(responses))
    quer = query.split()   #takes the query and splits it
    for word in quer:   #loops through words in query
        if quer.index(word)%2 == 1: 
            quer.insert(quer.index(word), "+")   #adds in + sign in every odd index
    quer = ''.join(quer)   #joins all words without any spaces
    webbrowser.open('https://www.google.com/' + quer)
    
#Open the YouTube search for a video            
def play_vid(query):
    speak(random.choice(responses))    
    quer = query.split()
    quer.remove('play')
    quer.remove('by')
    for word in quer:   #loops through words in query
        if quer.index(word)%2 == 1: 
            quer.insert(query.index(word), "+")   #adds in + sign in every odd index
    "".join(quer)
    webbrowser.open('https://www.youtube.com/results?search_query=' + quer)
    
#Directs to weather.com - 10-day forecast
def get_weather():
    speak(random.choice(responses))
    webbrowser.open("https://weather.com/weather/tenday/l/c277dae335f9538e22909aaa3e887daa822dbde134f4379a25f368167c04bbfe")

#Search WolframAlpha for answers to questions  
def wolf(query):
    speak(random.choice(responses))
    question = query
    app_id = 'AQV4H4-8LWH8GRXWG'
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    answer = next(res.results).text
    speak(answer)
    print(answer)            

def open_site(site):
    speak("Opening " + str(site))
    webbrowser.open(Websites[str(site)])

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    greet()
    inquiries = ['who', 'what', 'where', 'when', 'why', 'how']
    Websites = {'youtube' : 'https://www.youtube.com/',
    'google' : 'https://www.google.com/',
    'reddit' : 'https://www.reddit.com/',
    'td ameritrade' : 'https://www.tdameritrade.com/home.html',
    'gmail' : 'https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin',
    'ncbi' : 'https://www.ncbi.nlm.nih.gov/',
    'indeed' : 'https://www.indeed.com/',
    'github' : 'https://github.com/'}
    
    while True:
        rise()
        query = takeCommand().lower()
        for site in Websites:
            if site in query:
                open_site(site)
                
        for inquiry in inquiries:
            if inquiry == query.split[0]:
                wolf(query)
                
        if 'wikipedia' in query:
            get_wiki(query)
              
        elif "play" in query and 'by' in query: #Play a video on youtube. Format: 'Play {What you want to play here}
            play_vid(query)                     #by {artist or uploader}
  
        elif 'weather' in query:
            get_weather()
                    
