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
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup 
import re
from datetime import date
import webbrowser
import pocketsphinx

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
r = sr.Recognizer()
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
    
#Open different websites
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
            listen() #Runs the function recognize_main
    except sr.UnknownValueError: #if there is nothing understood
        print("Oops! Didn't catch that") #prints to screen error message

def listen():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        r.recognize_sphinx(audio)
    try:
        print("Recognizing...")   
        global query
        query = r.recognize_sphinx(audio, language ='en-in')
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".formate(e))
    return query
  
""" Step 2: Web surfing.
Surf and scrape the web for stuff. I will mostly
just use wikipedia for information"""

def get_wiki():
    query = listen.lower()
    split = query.split()
    the_index = -2
    while True:
        if split[the_index] == 'for' or 'on' or 'about':
            query = split[the_index+1:]
            break
        elif split[the_index] != 'for' or 'on' or 'about':
            the_index -= 1
            continue
    results = wikipedia.summary(str(query))
    print(results)
    speak(results)
    
def get_google():
    quer = query.split()   #takes the query and splits it
    for word in quer:   #loops through words in query
        if quer.index(word)%2 == 1: 
            quer.insert(quer.index(word), "+")   #adds in + sign in every odd index
    ask = ""    #This will be added to the google URL
    for q in quer:
        ask += str(q)
    webbrowser.open('https://www.google.com/search?q=' + str(ask))
    
def wikinfo():
        query = query.split()
        em = ""
        for words in query[query.index('is')+1]:
            em += str(words)
        wikipedia.summary(em, sentences = 3)
        
if __name__ == '__main__':
    clear = lambda: os.system('cls')
    while True:
        listen()
        for site in Websites:
            if site in query:
                webbrowser.open(Websites[site])
        speak("Opening " + str(site))

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            get_wiki()
            
        elif 'what is' in query:
            wikinfo()

        """ Make a dictionary for questions that
        Google may have answers to. Example:
        If query has 'How big is', or 'What is the
        most' then ask google. """
        

