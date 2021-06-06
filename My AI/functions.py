def speak(audio):
    engine.say(audio)
    engine.runAndWait()
     
""" Make a recognizer function to start when 
you say certain words """    

keywords = [("aku", 1), ('hey aku', 1), ('yo aku',1),]

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

"""Opens up the wikipedia page of what you ask for. We do this by splitting the query into separate words, and extract the last words.
You can't just extract the last because it might be wrong. Example: The Big Bang. If you just take Bang, you won't get the correct results.

This follows a forumula that's on main.py.   If you mention wikipedia, you need to say the words 'for', 'on', or 'about', before saying what you 
want to go on Wikipedia for.  So if you want to open the wiki page for the 
"""
def get_wiki():
    query = listen.lower()
    split = query.split()
    the_index = -1
    while True:
        if split[the_index] == 'for' or 'on' or 'about':
            query = split[the_index+1:]
            mn = ""
            for x in query:
              mn += str(x)
            break
        elif split[the_index] != 'for' or 'on' or 'about':
            the_index -= 1
            continue
    webbrowswer.open("https://en.wikipedia.org/wiki/" + str(mn))
    print(results)
    speak(results)
    
#If sphinx recognizes ? marks then this will work, if not I'll have to readjust this.
#This automatically opens up a google tab with what you asked for
def get_google():
    qu = query.replace("?","")  #gets rid of ?
    quer = qu.split()   #takes the query and splits it
    for word in quer:   #loops through words in query
        if quer.index(word)%2 == 1: 
            quer.insert(quer.index(word), "+")   #adds in + sign in every odd index
    ask = ""    #This will be added to the google URL
    for q in quer:
        ask += str(q)
    webbrowser.open('https://www.google.com/' + str(ask))

#Get information from wikipedia
def wikinfo():
    if 'what is' in query:
        query = query.split()
        em = ""
        for words in query[query.index('is')+1]:
            em += str(words)
        wikipedia.summary(em, sentences = 3)
        
        
