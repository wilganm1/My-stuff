import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import os
import subprocess
import wolframalpha
import random

global term
term = 'sir'
global name
name = "jarvis"
global keywords
keywords = ["Hey Jarvis", "Yo Jarivs", "Jarvis"]
global calls
calls = [f'yes {term}?', 'The fuck do you want now?', 'You called?', 'You rang?', 'shut your whore mouth', 'Yes masta?']
global responses
responses = [f'Yes {term}.', 'As you wish.', f'Of course {term}.',
          'Just one moment.', f'Right away {term}.', 'As you command.', 
          'One moment please.', 'Please wait.', 'One moment please.']       #Responses so I know it's doing what I ask
global inquiries
inquiries = ['who', 'what', 'where', 'when', 'why', 'which','what\'s','whose','when\'s',]   #For wolfram to answer questions
global Websites
Websites = {'youtube' : 'https://www.youtube.com/',
            'google' : 'https://www.google.com/',
            'reddit' : 'https://www.reddit.com/',      #List of websites I've pre-programmed to open when I ask for it.
            'td ameritrade' : 'https://www.tdameritrade.com/home.html',   
            'gmail' : 'https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin',
            'ncbi' : 'https://www.ncbi.nlm.nih.gov/',
            'indeed' : 'https://www.indeed.com/',
            'github' : 'https://github.com/'}
global Programs
Programs = {"Fret finder": 'C:\\Users\\WilganZMT\\Desktop\\Fret Finder.exe', 
                 "Audacity": "C:\\Program Files (x86)\\Audacity\\audacity.exe",  
                 "Krita": "C:\\Program Files\\Krita (x64)\\bin\\krita.exe",
                 "iTunes": "C:\\Program Files\\iTunes\\iTunes.exe",
                 'tux guitar': "C:\\Program Files (x86)\\tuxguitar-1.1\\tuxguitar.exe"}
global instructions
instructions = ["show me how to", "look up how to", "How do you"]

def speak(text):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 1.5)
    engine.say(text)
    engine.runAndWait()
    

def greet():
        greetings = ['Welcome back.']
        while True:
            if datetime.now().hour >= 6 and datetime.now().hour < 9:
                speak(f'Good morning {term}' )
                speak(random.choice(greetings))
            elif datetime.now().hour >= 9 and datetime.now().hour < 14:
                speak(f'Good day {term}')
                speak(random.choice(greetings))
            elif datetime.now().hour >= 14 and datetime.now().hour < 18:
                speak(f'Good afternoon {term}')
                speak(random.choice(greetings))
            elif datetime.now().hour >= 18 and datetime.now().hour < 21:
                speak(f'Good evening {term}.')
                speak(random.choice(greetings))
            elif datetime.now().hour >= 21 and datetime.now().hour < 24:
                speak(f'It\'s getting late {term}, you should consider sleeping.')
                speak(random.choice(greetings))
            break      
def activate():
    while 1:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Awaiting request...")
            audio=r.listen(source)
            try:
                spoken = r.recognize_google(audio,language='en-in')
                if f"{name}" in spoken.lower():
                    break
            except Exception as e:
                speak("Pardon me, please say that again")
                continue                   
def takeCommand():
    while True:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            speak(random.choice(calls))
            print("Listening...")
            audio=r.listen(source)
            try:
                query=r.recognize_google(audio,language='en-in')
                print(f"user said: {query}\n")
                return query
                break
            except Exception as e:
                speak("Pardon me, please say that again")
                continue
def open_site(query):
        speak(random.choice(responses))
        for site in Websites:    #checks if a pre-determined site is in query
            if site in query:    
                speak('Opening ' + site) 
                webbrowser.open(Websites[site])  #opens up the website
        extensions = ['.com', '.org', '.gov']   #Checks for extensions.
        for x in extensions:
            if x in query:
                extension = x    #Save this for later use in webbrowser
                query = query.replace(x, "")  #gets rid of the extension.
        quer = query.split()           #Splits the query into separate words
        if 'open' == quer[0]:  #Following code just removes words if they're in the query
            quer.remove('open')
        elif 'open' == xyz[0] or 'go' == xyz[0] and 'to' == xyz[1]:
            quer.remove('go')
            quer.remove('to')
        quer = "".join(quer)           #Combines all the words into one string without spaces.
        speak("Opening " + quer)
        print('Opening ' + quer)
        webbrowser.open("https://www." + quer + str(extension))    #opens the website in browser   
        return
def instruction_vid1(query):
    speak(random.choice(responses))
    if instructions[0] in query or instructions[1] in query:
        quer = query.split()
        quer.remove(quer[0])
        quer.remove(quer[0])
        for word in quer:   #loops through words in query
            if quer.index(word)%2 == 1: 
                quer.insert(quer.index(word), "+")   #adds in + sign in every odd index
        quer="".join(quer)
        webbrowser.open('https://www.youtube.com/results?search_query=' + quer)      
def instruction_vid2(query):
    speak(random.choice(responses))
    quer = query.split()
    quer.remove("do")
    quer.remove("you")
    quer.insert(quer.index('how')+1, 'to')
    for word in quer:   #loops through words in query
        if quer.index(word)%2 == 1: 
            quer.insert(quer.index(word), "+")   #adds in + sign in every odd index
    quer ="".join(quer)
    webbrowser.open('https://www.youtube.com/results?search_query=' + quer)
    return
def open_program(program):
    subprocess.call(Programs[program])
    return
def wolf(query):
        speak("Checking")
        app_id = 'AQV4H4-8LWH8GRXWG'             
        client = wolframalpha.Client(app_id)
        res = client.query(query)
        answer = next(res.results).text
        if 'what is the' in query:
            quer = query.split()[2::]
            quer.append('is ')
            quer = " ".join(quer)
            print(answer)
            speak(quer + answer)
        elif 'how many' in query or 'how much':
            quer = query.split()[-3::]
            quer = " ".join(quer)
            print(answer)  
            speak("There are " + answer + " " + quer)
        return
def get_weather():
        speak(random.choice(responses))
        webbrowser.open("https://weather.com/weather/tenday/l/c277dae335f9538e22909aaa3e887daa822dbde134f4379a25f368167c04bbfe")
        return
def get_wiki(query):     
        speak(random.choice(responses))    
        split = query.split()                                              
        the_index = -1
        while True:
            if split[the_index] != 'for' or split[the_index] != 'on' or split[the_index] != 'about':
                the_index -= 1
                continue
            elif split[the_index] == 'for' or split[the_index] == 'on' or split[the_index] == 'about':
                query = split[the_index+1:]
                break
        for i in range(len(query)):
            query[i] = query[i].capitalize()
        for word in query:   #loops through words in query
            if query.index(word)%2 == 1: 
                query.insert(query.index(word), "_") 
        query = "".join(query)
        webbrowser.open("https://en.wikipedia.org/wiki/" + query)
        return
def play_vid(query):
        speak(random.choice(responses))    
        quer = query.split()
        quer.remove('play')
        quer.remove('by')
        for word in quer:   #loops through words quer
            if quer.index(word)%2 == 1: 
                quer.insert(quer.index(word), "+")   #adds in + sign in every odd index
        quer = "".join(quer)
        webbrowser.open('https://www.youtube.com/results?search_query=' + quer)
        return
if __name__=='__main__':   
    greet()
    try:
        while 1:
            activate()
            query = takeCommand().lower()
            xyz = query.split()
            for inquiry in inquiries:
                if inquiry == xyz[0]:
                    wolf(query)
                    continue
            for program in Programs:
                if 'open' == xyz[0] and program in xyz:
                    open_program(program)
                    continue
            if 'wikipedia' in query:
                get_wiki(query)
                continue
            elif 'the weather' in query:   #As long as "the weather" is in query it doesn't matter.
                get_weather()
                continue
            elif '.com' in query or '.org' in query or '.gov' in query and 'open' == xyz[0] or 'go' == xyz[0] and 'to' == xyz[1]:
                open_site(query)     #Format: "Go to/Open up/Open {site}. If not in Websites say .com/.org/.gov
                continue
            elif'how' == xyz[0] and 'do' == xyz[1] and 'you' == xyz[2]:
                instruction_vid2(query)
                continue
            elif 'how' == xyz[2] and 'to' == xyz[3]:
                instruction_vid1(query)             #Format: "Look up how to/Show me how to/How do you
                continue
            elif 'how many' in query or 'how much' in query:
                wolf(query)
                continue
            elif "play" == xyz[0] and 'by' in query:  #Format: "Play {video} by {uploader/artist}
                play_vid(query)
                continue       
            elif "end program" in query:
                speak("Alright the. Goodbye.")
                break
    except RuntimeError:
        os._exit(0)
