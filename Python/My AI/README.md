# Making my own custom AI assistant in Python.

I've seen this done online and I want to make my own assistant. I'm using pyttsx3 for text-to-speech and using recognize_google to use Google's API  for words for the computer to recognize. This assistant will be able to open websites, look up things on Wolframalpha, turn off the computer, and in the future do stuff like send emails and be able to save notepad files.

### Voice recognition neural network.
I have an idea about programming the AI to only respond to my voice. This can be done as I've seen other projects on Github do the same thing. I will have to make python recognize pitches of my voice.

#### How it will work
I will have to write a neural network to recognize my voice. Speech recognition only recognizes words, not distinct voices, so I want to program the AI to only repsond to me. This is done through detection of certain frequencies, like how a guitar tuning app can detect frequencies of strings to know if they are in tune or not. I'll need a package to be able to recognize pitch and audio frequencies like crepe or pydub. 
I'll have to do some research to find it. If this works I can train the network to recognize my voice and only work when it detects me. This will be the greatest feature of the AI assistant.

##### New voices
I find out how to add new voices to pyttsx3. So far I only got voices that come directly from Microsoft's narrator packages.

###### Refernces used
https://towardsdatascience.com/how-to-build-your-own-ai-personal-assistant-using-python-f57247b4494b
https://www.geeksforgeeks.org/voice-assistant-using-python/
https://www.youtube.com/watch?v=n4MXCnppKOY&list=PLm4rgP2bwr1q4s_9EwAo4pHBcYxsBRPKs

