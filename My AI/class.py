import pyttsx3
import speech_recognition as sr 
from datetime import datetime
import random
import os
import wolframalpha
import webbrowser
import subprocess


"""The key to writing a bunch of functions and not have the program get confused is to be hyper-specifc.
Like, if 'how' == query.split()[4] and ~~~~."""

"Make the program a class"
class AI:
    def __init__(self):            #Main properties of the class.
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        self.term = ''  #!!! Enter sir/ma'am/master/mistress/my lord/whatever you want the AI to address you as. Then delete the ! marks.
        self.name = ''  #!!! Enter the name that you will call the AI. "Jarivs", "Karen", "Fuck face" etc.
        self.keywords = [f'hey {self.name}', f'{self.name}', f'yo {self.name}', f'excuse me {self.name}']
        self.responses = [f'Yes {self.term}.', 'As you wish.', f'Of course {self.term}.',
                          'Just one moment.' f'Right away {self.term}.', 'As you command.', 
                          'One moment please.', 'Please wait.', 'One moment please.']       #Responses so I know it's doing what I ask
        self.inquiries = ['who', 'what', 'where', 'when', 'why', 'which','what\'s','whose','when\'s',]   #For wolfram to answer questions
        self.Websites = {'youtube' : 'https://www.youtube.com/',
                         'google' : 'https://www.google.com/',
                         'reddit' : 'https://www.reddit.com/',      #List of websites I've pre-programmed to open when I ask for it.
                         'td ameritrade' : 'https://www.tdameritrade.com/home.html',   
                         'gmail' : 'https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin',
                         'ncbi' : 'https://www.ncbi.nlm.nih.gov/',
                         'indeed' : 'https://www.indeed.com/',
                         'github' : 'https://github.com/'}
        self.Programs = {"Fret finder": 'C:\\Users\\WilganZMT\\Desktop\\Fret Finder.exe', #!!! Add in your own programs
                         "Audacity": "C:\\Program Files (x86)\\Audacity\\audacity.exe",  
                         "Krita": "C:\\Program Files\\Krita (x64)\\bin\\krita.exe",
                         "iTunes": "C:\\Program Files\\iTunes\\iTunes.exe",
                         'tux guitar': "C:\\Program Files (x86)\\tuxguitar-1.1\\tuxguitar.exe"}
    
   #Function that converts text to speech.
    def speak(self, audio):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        self.engine.setProperty('rate', 190)    #How fast the voice speaks.
        self.engine.say(audio) #tells Python to self.speak variable 'text'
        self.engine.runAndWait() #waits for speech to finish and then continues with program
        return
    
   #Greets me whenever I start the program after stopping it. Greeting is based on the hour of the day.
    def greet(self):
        greetings = ['Welcome back.', 'How are you today?', ]
        while True:
            if datetime.now().hour >= 6 and datetime.now().hour < 9:
                self.speak(f'Good morning {self.term}' )
                self.speak(random.choice(greetings))
            elif datetime.now().hour >= 9 and datetime.now().hour < 14:
                self.speak(f'Good day {self.term}')
                self.speak(random.choice(greetings))
            elif datetime.now().hour >= 14 and datetime.now().hour < 18:
                self.speak(f'Good afternoon {self.term}')
                self.speak(random.choice(greetings))
            elif datetime.now().hour >= 18 and datetime.now().hour < 21:
                self.speak(f'Good evening {self.term}.')
                self.speak(random.choice(greetings))
            elif datetime.now().hour >= 21 and datetime.now().hour < 24:
                self.speak(f'It\'s getting late {self.term}, you should consider sleeping.')
                self.speak(random.choice(greetings))
            break
        return
    
   #This will activate the AI only when you speak a keyword. This way it won't run if people are speaking in the background or whatever
   
   #This is the main function of the entire script. This will listen to what you say and assign it 
   #to the query variable. It is set in a loop if it ever fails. The query resets every time it's called
   #So it will always be fresh and new.
    def takeCommand(self):   #Main reply call function
        with self.mic as source:      #sets microphone as source
            self.r.adjust_for_ambient_noise(source)   #Cancels out ambient noise
            print("Waiting for command...")        #Let's me know it's waiting
            self.r.pause_threshold = 1         #Waits a minute.
            audio = self.r.listen(source)      #sets variable 'audio'
        try:
            query = self.r.recognize_sphinx(audio)      #Sphinx recognizes what I said.
        except sr.UnknownValueError:          
            print("Sphinx could not understand audio. Please try again")
            self.speak("I'm sorry, I didn't catch that.")
        except sr.RequestError as e:
            print("Sphinx error; {0}".formate(e))
            self.speak('something has goine wrong.')
        return query

   #Opens the wikipedia page for something. Format: "Open (the) wikipedia (page) for/on/about {what ever}"
    def get_wiki(self,query):     
        self.speak(random.choice(self.responses))    
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
    
   #Opens YouTube to search for a video by search word. Format: "Play {video} by {uploader/artist}"   
    def play_vid(self,query):
        self.speak(random.choice(self.responses))    
        quer = query.split()
        quer.remove('play')
        quer.remove('by')
        for word in quer:   #loops through words quer
            if quer.index(word)%2 == 1: 
                quer.insert(quer.index(word), "+")   #adds in + sign in every odd index
        "".join(quer)
        webbrowser.open('https://www.youtube.com/results?search_self.query=' + quer)
        return
    
   #Directs to weather.com - 10-day forecast
    def get_weather(self):
        self.speak(random.choice(self.responses))
        webbrowser.open("https://weather.com/weather/tenday/l/c277dae335f9538e22909aaa3e887daa822dbde134f4379a25f368167c04bbfe")
        return
    
   #Search WolframAlpha for answers to questions  
    def wolf(self, query):
        self.speak(random.choice(self.responses))
        question = query              #I got this code from geeksforgeeks. If it doesn't work
        app_id = 'AQV4H4-8LWH8GRXWG'             #use wikipedia.summary to get what you want
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        self.speak(answer)
        print(answer)  
        return
        
   #Opens a specific site. Could be one in the dictionary or another one.   
    def open_site(self, query):
        self.speak(random.choice(self.responses))
        for site in self.Websites:    #checks if a pre-determined site is in query
            if site in query:    
                self.speak('Opening ' + site) 
                webbrowser.open(self.Websites[site])  #opens up the website
        extensions = ['.com', '.org', '.gov']   #Checks for extensions.
        for x in extensions:
            if x in query:
                extension = x    #Save this for later use in webbrowser
                query = query.replace(x, "")  #gets rid of the extension.
        quer = query.split()           #Splits the query into separate words
        if 'open' == quer[0]:  #Following code just removes words if they're in the query
            quer.remove('open')
        elif 'open' == query.split()[0] or 'go' == query.split()[0] and 'to' == query.split()[1]:
            quer.remove('go')
            quer.remove('to')
        quer = "".join(quer)           #Combines all the words into one string without spaces.
        self.speak("Opening " + quer)
        print('Opening ' + quer)
        webbrowser.open("https://www." + quer + str(extension))    #opens the website in browser   
        return
    
   #Opens a program on the computer. 
    def open_program(self, program):
        subprocess.call(self.Programs[program])
        return
    
   #Opens a YouTube video on how to do something. Format: "Show me how to....", "How do you...", etc.
    def instruction_vid(self,query):
        self.speak(random.choice(self.responses))
        instructions = ["show me how to", "look up how to", "How do you"]
        if instructions[0] in query or instructions[1] in query:
            quer = query.split
            quer.remove(query[0])
            quer.remove(quer[0])
            for word in quer:   #loops through words in query
                if quer.index(word)%2 == 1: 
                    quer.insert(quer.index(word), "+")   #adds in + sign in every odd index
            "".join(quer)
            webbrowser.open('https://www.youtube.com/results?search_self.query=' + quer)
            return
        elif instructions[2] in query:
            quer = query.split
            quer.remove("do")
            quer.remove("you")
            quer.insert(quer.index('how')+1, 'to')
            for word in quer:   #loops through words in query
                if quer.index(word)%2 == 1: 
                    quer.insert(quer.index(word), "+")   #adds in + sign in every odd index
            "".join(quer)
            webbrowser.open('https://www.youtube.com/results?search_self.query=' + quer)
            return
 
"""Main program"""
if __name__ == '__main__':
    try:
        AI = AI()   #Sets the AI class.
        AI.greet()   
        while True:           #This loop will always keep it running. It will only stop when an error occurs or you stop it manually
            query = AI.takeCommand().lower
            if query ==0:
                continue
            for inquiry in AI.inquiries:
                if inquiry == query.split[0]:
                    AI.wolf(query)
                    continue
            for program in AI.Programs:
                if 'open' == query.split()[0] and program in query:
                    AI.open_program(program)
                    continue
            for instruct in AI.instructions:
                if instruct in query:
                    AI.instruction.vid(query)
                    continue              
            if 'wikipedia' in query:
                AI.get_wiki(query)
                continue
            elif 'how' == query.split()[0] and 'many' == query.split()[1] or 'much' == query.split()[1]:
                AI.wolf(query)
                continue
            elif "play" == query.split()[0] and 'by' in query:  #Format: "Play {video} by {uploader/artist}
                AI.play_vid(query)
                continue
            elif 'the weather' in query:   #As long as "the weather" is in query it doesn't matter.
                AI.get_weather(query,)
                continue
            elif 'open' == query.split()[0] or 'go' == query.split()[0] and 'to' == query.split()[1]:
                AI.open_site(query)     #Format: "Go to/Open up/Open {site}. If not in self.Websites say .com/.org/.gov
                continue
            elif 'how' == query.split()[2] and 'to' == query.split()[3] or 'how' == query.split()[0] and 'do' == query.split()[1] and 'you' == query.split()[2]:
                AI.instruction_vid(query,)             #Format: "Look up how to/Show me how to/How do you
                continue
            elif "terminate" in query and "program" in query:
                break            
            elif "shut down computer" in query:
                AI.speak(f"Shutting down, good bye {AI.term}")
                break
                os.sytem("shutdown /s /t 1")
            elif 'kill yourself' in query:
                os._exit(0)
        if KeyboardInterrupt:
            raise 
    except RuntimeError:
        try:
            raise
        except:
            os._exit(0)
