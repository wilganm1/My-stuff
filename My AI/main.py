import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import os
import subprocess
import wolframalpha
import random
import ctypes
from os import walk        #!!!! Have the names of your images something that is easy to read. dog/space station/grass field/Earth, etc.


global term      #!!! What you want the AI to address you as.
term = 'sir'
global responses      #Responses to what I say so I know it's doing what I ask.
responses = [f'Yes {term}', 'As you wish', f'Of course {term}',
          'Just one moment', f'Right away {term}', 'As you command', 
          'One moment please', 'Please wait']       
global Websites    #Preset websites that the computer will open for you.
Websites = {'youtube' : 'https://www.youtube.com/',
            'google' : 'https://www.google.com/',
            'reddit' : 'https://www.reddit.com/',      #List of websites I've pre-programmed to open when I ask for it.
            'td ameritrade' : 'https://www.tdameritrade.com/home.html',   
            'ncbi' : 'https://www.ncbi.nlm.nih.gov/',
            'indeed' : 'https://www.indeed.com/',
            'github' : 'https://github.com/'}
global Programs        #Programs on your computer that you can preset. 
Programs = {"Fret finder": 'C:\\Users\\WilganZMT\\Desktop\\Fret Finder.exe', 
            "Audacity": "C:\\Program Files (x86)\\Audacity\\audacity.exe",  
            "Krita": "C:\\Program Files\\Krita (x64)\\bin\\krita.exe",
            "iTunes": "C:\\Program Files\\iTunes\\iTunes.exe",
            'tux guitar': "C:\\Program Files (x86)\\tuxguitar-1.1\\tuxguitar.exe"}
global instructions   #Used to look up a video on how to do something. Used for function
instructions = ["show me how to", "look up how to", "How do you"]

def password():    #Has you enter a password to begin. Uncomment below to activate
    password = "shrubbery"     #Monty Python reference
    while 1:
        if input("Please enter password: ") == password:
            speak("Welcome back sir")
        else:
            speak("Invalid password.")
            continue
def speak(text):         #speaks what is typed in
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[3].id)   #Defaults are 2 voices. It possible to add more. I've done it.
    engine.setProperty('rate', 160)    #How fast the voice speaks.
    engine.setProperty('volume', 1.5)  #how loud the voice is.
    engine.say(text)
    engine.runAndWait()
def greet():       #Says hello to you. Based on time of day
        greetings = ['Welcome back.', "I hope you're well.", 'Good to see you again']
        while 1:
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
def activate():  #Name of the AI. Change this to whatever you want. 
    name = "jarvis"   #!!!!!! Change to whatever you want.
    while 1:       #loop so it stays in this function forever until condition met.
        r=sr.Recognizer()
        with sr.Microphone() as source:  #sets your default microphone as the source
            r.adjust_for_ambient_noise(source)   #checks for ambient noise. Only works when it hears you
            r.pause_threshold = 1      #waits a bit.
            print("Awaiting request...")   #Prints to the screen so you know it's listening
            audio=r.listen(source)
            try:
                spoken = r.recognize_google(audio,language='en-in')   #What it hears and transcribes. 
                if f"{name}" in spoken.lower():  #Checks if the AI's name is in spoken.
                    break    #stops the loop,
            except Exception as e:
                speak("Pardon me, please say that again")
                continue                   
def takeCommand():       #Main function of the AI. listens to you speak and will pass it along.
    calls = [f'yes {term}?', 'You called?', 'You rang?', 'What can I help you with?']
    while 1:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 1
            speak(random.choice(calls))
            print("Listening...")    #waiting for a command
            audio=r.listen(source)
            try:
                query=r.recognize_google(audio,language='en-in')
                print(f"user said: {query}\n")
                return query
                break
            except Exception as e:
                speak("Pardon me, please say that again")  #Error if it doesn't understand what you said.
                continue
def open_site(query):        #opens a website based on what you said. #Format: "Go to/Open {site}. If not in Websites say .com/.org/.gov
        speak(random.choice(responses))     #random response so you know it's working
        for site in Websites:    
            if site in query:    #checks if a preset site is in query  
                speak(" ".join(['Opening', site])) 
                webbrowser.open(Websites[site])  #opens up the website
        extensions = ['.com', '.org', '.gov']   #Checks for extensions.
        for x in extensions:
            if x in query:
                extension = x    #Save this for later use in webbrowser
                query = query.replace(x, "")    #gets rid of the extension.
        quer = query.split()             #Splits the query into separate words
        if 'open' == quer[0]:     #Following code just removes words if they're in the query
            quer.remove('open')
        elif 'open' == xyz[0] or 'go' == xyz[0] and 'to' == xyz[1]:
            quer.remove('go')
            quer.remove('to')
        quer = "".join(quer)           #Combines all the words into one string without spaces.
        speak(" ".join(["Opening", quer]))
        print(" ".join(['Opening' + quer]))
        webbrowser.open("".join(["https://www.",quer, str(extension)]))    #opens the website in browser   
        return
def instruction_vid1(query):   #Opens a youtube video on how to do something: "(Show me/look up) How to use a chainsaw"
    speak(random.choice(responses))
    if instructions[0] in query or instructions[1] in query:
        quer = query.split()     #['Look','up','how','to] / ['show','me','how','to']
        quer.remove(quer[0])  #removes "look up/show me"
        quer.remove(quer[0])
        for word in quer:    #loops through words in query
            if quer.index(word)%2 == 1:      #checks if the index is odd.
                quer.insert(quer.index(word), "+")   #adds in + sign in every odd index
        quer="".join(quer)
        webbrowser.open("".join(['https://www.youtube.com/results?search_query=', quer]))   #Opens youtube search for query  
def instruction_vid2(query):      #Same thing as previous function.  Format: "How do you {whatever}
    speak(random.choice(responses))
    quer = query.split()           #['How', 'do', 'you', ~~~~~~~~~~]
    quer.remove("do")
    quer.remove("you")
    quer.insert(quer.index('how')+1, 'to')   #adds 'to' to the list after 'how'.
    for word in quer:   #loops through words in query
        if quer.index(word)%2 == 1: 
            quer.insert(quer.index(word), "+")   
    quer ="".join(quer)  
    webbrowser.open("".join(['https://www.youtube.com/results?search_query=',quer]))
    return
def open_program(program):         #Opens program on your computer that's in the Programs dictionary
    subprocess.call(Programs[program])
    return
def wolf(query):    #Checks wolframalpha for a answers to a question. Wolframalpha is a search engine. 
        speak("Checking")
        app_id = ''      #!!! You need to create an account and get your own app_id. type in wolfram alpha in google and make an account there.       
        client = wolframalpha.Client(app_id)
        res = client.query(query)
        answer = next(res.results).text
        if 'what is the' in query:
            quer = query.split()[2::]
            quer.append('is ')
            quer = " ".join(quer)
            print(answer)
            speak("".join([quer, answer]))
        elif 'how many' in query or 'how much':
            quer = query.split()[-3::]
            quer = " ".join(quer)
            print(answer)  
            speak(" ".join(["There are", "answer", "quer"]))

        return
def get_weather():      #Opens weather.com for your location. Add link of your location.
        speak(random.choice(responses))
        webbrowser.open("https://weather.com")
        return
def get_wiki(query):     #Opens wikipedia page for something. Format: "(Open/Search/~~) wikipedia {for/on/about} (whatever)"
        speak(random.choice(responses))    
        split = query.split()                                              
        the_index = -1           #Starts at the last index .
        while 1:     
            if split[the_index] != 'for' or split[the_index] != 'on' or split[the_index] != 'about':
                the_index -= 1   #Checks the split for certain words that need to bethere. If they are not the index goes back one.
                continue
            elif split[the_index] == 'for' or split[the_index] == 'on' or split[the_index] == 'about':
                quer = split[the_index+1:]  #This returns only what's after for/on/about. Exmaple: for the big bang
                break       
        for i in range(len(quer)):
            quer[i] = quer[i].capitalize()    #The Big Bang
        for word in quer:      #loops through words in query
            if quer.index(word)%2 == 1:  #chekcs for odd indices
                quer.insert(quer.index(word), "_")   #inserts _ for the url
        quer = "".join(quer)     #The_Big_Bang
        webbrowser.open("".join(["https://en.wikipedia.org/wiki/", quer]))   #opens the wikipedia page for query
        return
def play_vid(query):       #Searches youtube for a video
        speak(random.choice(responses))    
        quer = query.split()   # "Play {video} by {uploader/artist}"
        quer.remove('play')
        quer.remove('by')
        for word in quer:   
            if quer.index(word)%2 == 1: 
                quer.insert(quer.index(word), "+")
        quer = "".join(quer)
        webbrowser.open("".join(['https://www.youtube.com/results?search_query=',quer]))
        return
def change_wallpaper():  #Changes wallpaper. You need a folder that has pics you want to choose from.  
    while 1:       #loop so it stays in this function forever until condition met.
        r=sr.Recognizer()
        mypath = "C:\\Users\\WilganZMT\\Pictures\\Wallpaper pics"  #!!! Insert the folder that has the images you want to choose from
        from os import listdir
        from os.path import isfile, join
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for x in onlyfiles:
            x = x.replace('.jpg', "")
            print(x)
        with sr.Microphone() as source:  
            print("Choose wallpaper...")   #Prints to the screen so you know it's listening
            speak("Please speak desired image")
            audio=r.listen(source)
            try:
                wallpaper = r.recognize_google(audio,language='en-in')   
                print(f"user said: {wallpaper}\n")
                for x in onlyfiles:    
                    x = x.replace('.jpg', "")  #Gets rid of .jpg/.png/whatever.
                    if x == wallpaper:
                        ctypes.windll.user32.SystemParametersInfoW(20,0, "".join([mypath,"\\", str(x), ".jpg"]), 0)     #This is used for windows.                      
                        break    #stops the loop
            except Exception as e:
                speak("Pardon me, please say that again")
                continue  
        return                 

if __name__=='__main__':   
    inquiries = ['who', 'what', 'where', 'when', 'why', 'which','what\'s','whose','when\'s',]    #For wolfram to answer questions
    #password()       #uncomment to activate
    greet()            
    while 1:           #Starts a loop that will keep the script running unless it's told to end
        activate()       
        query = takeCommand().lower()     
        xyz = query.split()        #splits the query to check for certain words. Used for later.
        for inquiry in inquiries:     
            if inquiry == xyz[0]:     #Checks if a word in inquiries is the first word of the query
                wolf(query)       
                continue     #This loops back to the start of the loop. 
        for program in Programs:
            if 'open' == xyz[0] and program in xyz:
                open_program(program)
                continue
        if 'wikipedia' in query: 
            get_wiki(query)
            continue
        elif 'the weather' in query:   
            get_weather()
            continue
        elif '.com' in query or '.org' in query or '.gov' in query and 'open' == xyz[0] or 'go' == xyz[0] and 'to' == xyz[1]:
            open_site(query)     
            continue          
        elif 'how' in query and xyz.index('to') == xyz.index('how')+1:  
            instruction_vid1(query)    
            continue
        elif'how' == xyz[0] and 'do' == xyz[1] and 'you' == xyz[2]:
            instruction_vid2(query)     
            continue
        elif 'how many' in query or 'how much' in query:
            wolf(query)
            continue
        elif "play" == xyz[0] and 'by' in query:  
            play_vid(query)  
            continue       
        elif 'wallpaper' in query:
            change_wallpaper()
            continue
        elif "end script" in query or "end program" in query or 'and script' in query or 'and program' in query or 'kill yourself' in query:
            speak("Alright then. Goodbye.")  #Causes the program to end
            break
        elif RuntimeError:
            os._exit(0)
        else:
            break
    if RuntimeError:
        os._exit(0)
