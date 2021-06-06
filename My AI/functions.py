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
#
def get_wiki():
    query = listen.lower()
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
    quer = query.split()   #takes the query and splits it
    for word in quer:   #loops through words in query
        if quer.index(word)%2 == 1: 
            quer.insert(quer.index(word), "+")   #adds in + sign in every odd index
    quer = ''.join(quer)
    webbrowser.open('https://www.google.com/' + quer)

#Get information from wikipedia

def wikinfo():
    if 'what is' in query:
        query = query.split()
        em = ""
        for words in query[query.index('is')+1]:
            em += str(words)
        wikipedia.summary(em, sentences = 3)
        
#Play video on youtube
    
def play_vid():
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
    
def greet():
    if 6 >= datetime.now().hour > 9:
        speak('Good morning sir.')
        speak(random.choice(greetings))
    elif 9 >= datetime.now().hour > 14:
        speak('Good day sir.')
        speak(random.choice(greetings))
    if 14 >= datetime.now().hour > 18:
        speak('Good afternoon sir.')
        speak(random.choice(greetings))
    elif 18 >= datetime.now().hour > 24:
        speak('Good evening sir.')
        speak(random.choice(greetings))
