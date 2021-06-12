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
  
""" Step 2: Web surfing.
Surf and scrape the web for stuff. I will mostly
just use wikipedia for information"""
#
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
       
