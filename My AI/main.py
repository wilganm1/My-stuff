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
and recognize speech. Then have it play back."""

import random
import time
import speech_recognition as sr
import pyttsx3
import os
import wolframalpha
import wikipedia
import twilio
import json
import subprocess
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup 
import re
import webbrowser
import pocketsphinx
from datetime import *

greetings = ['Welcome back.', 'How are you today?', 
             'I\'ve missed you.']
responses = ['Yes sir.', 'As you wish.', 'Of course sir.',
             'Just one moment.' 'Right away sir.',
             'As you command.', 'Please wait.']

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
global r
r = sr.Recognizer()
global mic
mic = sr.Microphone()

""" Now do text to speech """
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
     
""" Make a recognizer function to start when 
you say certain words """    
keywords = [("aku", 1), ('hey aku', 1), ('yo aku',1),]

""" Make a dictionary of different websites with
their names as keys and  urls as the values 
"""
Websites = {'youtube' : 'https://www.youtube.com/',
    'google' : 'https://www.google.com/',
    'reddit' : 'https://www.reddit.com/',
    'td ameritrade' : 'https://www.tdameritrade.com/home.html',
    'gmail' : 'https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin',
    'ncbi' : 'https://www.ncbi.nlm.nih.gov/',
    'indeed' : 'https://www.indeed.com/',
    'github' : 'https://github.com/'}


def callback(recognizer, audio):
    try:
        speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries=keywords) #Uses Sphinx to recognise speech
        print(speech_as_text) #prints what was said on the screen
        if "jarvis" in speech_as_text or "hey jarvis": #starter names
            speak("Yes sir?") #Calls 'Speak' and acknowledges user
    except sr.UnknownValueError: #if there is nothing understood
        print("Oops! Didn't catch that") #prints to screen error message

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

print("Loading your AI personal assistant G-One")
speak("Loading your AI personal assistant G-One")
wishMe()  


""" Step 2: Web surfing.
Surf and scrape the web for stuff. I will mostly
just use wikipedia for information Used to open
up different websites."""

def get_wiki():
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
    
def get_google():
    speak(random.choice(responses))
    quer = query.split()   #takes the query and splits it
    for word in quer:   #loops through words in query
        if quer.index(word)%2 == 1: 
            quer.insert(quer.index(word), "+")   #adds in + sign in every odd index
    quer = ''.join(quer)
    webbrowser.open('https://www.google.com/' + quer)
            
def play_vid():
    query = takeCommand().lower
    query = query.split()
    query.remove('play')
    query.remove('by')
    for word in query:   #loops through words in query
        if query.index(word)%2 == 1: 
            query.insert(query.index(word), "+")   #adds in + sign in every odd index
    "".join(query)
    webbrowser.open('https://www.youtube.com/results?search_query=' + query)

def get_weather():
    webbrowser.open("https://weather.com/weather/tenday/l/c277dae335f9538e22909aaa3e887daa822dbde134f4379a25f368167c04bbfe")

    
def wolf():
    question = takeCommand()
    app_id = 'AQV4H4-8LWH8GRXWG'
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    answer = next(res.results).text
    speak(answer)
    print(answer)            

inquiries = ['who', 'what', 'where', 'when',
            'why', 'how']

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    while True:
        query = takeCommand().lower()
        for site in Websites:
            if site in query:
                webbrowser.open(Websites[site])
        speak("Opening " + str(site))
  #Search WolframAlpha for answers to questions
        for inquiry in inquiries:
            if inquiry in query:
                wolf()
  #Open wikipedia page on something
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            get_wiki()
  #Open the YouTube search for a video  
        elif "play" in query and 'by' in query: #Play a video on youtube. Format: 'Play {What you want to play here}
            play_vid()                     #by {artist or uploader}
  #Directs to weather.com - 10-day forecast
        elif 'weather' in query:
            get_weather()
                   
