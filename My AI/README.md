# Making my own custom AI assistant in Python.

I've seen this been done online and I want to make my own assistant. I'm using pyttsx3 for text-to-speech and using recognize_google to use Google's API  for words for the computer to recognize. This assistant will be able to open websites, look up things on Wolframalpha, turn off the computer, and in the future do stuff like send emails and be able to save notepad files.

### Voice recognition neural network.
I have an idea about programming the AI to only respond to my voice. This can be done as I've seen other projects on Github do the same thing. I will have to make python
recognize pitches of my voice.

#### How it will work
I will have to write a neural network to recognize my voice. This is done through detection of certain frequencies, like how a guitar tuning app and detect frequencies
of strings to know if they are in tune or not. What I do is I record myself speaking for about 3-7 seconds, then have Python read this wav file and print out the
array of values that it produces. I'll have to use scipy.io.wavefile and numpy to do this. What I can do then is I can convert it to a time-frequency spectrogram to 
visualize my voice. I can then convert the wav file to a list of frequencies or just leave it as is. The neural network will be a perceptron with 1 output neuron. I
don't think I would need a hidden layer. The perceptron will be a classification neural network with a binary output, 1 being my voice, and 0 being not my voice.
I will need as many weights as there are inputs, and just one bias. The final activation function will be a sigmoid function, and the loss function will be 
cross-entropy function. I will just have to find the partial derivatives of the sigmoid, weights, and bias, then train the neural network with batch gradient descent.
If this works I can train the network to recognize my voice and only work when it detects me. This will be the greatest feature of the AI assistant.

##### New voices
I find out how to add new voices to pyttsx3. So far I only got voices that come directly from Microsoft's narrator packages.

###### Refernces used
https://towardsdatascience.com/how-to-build-your-own-ai-personal-assistant-using-python-f57247b4494b
https://www.geeksforgeeks.org/voice-assistant-using-python/
https://www.youtube.com/watch?v=n4MXCnppKOY&list=PLm4rgP2bwr1q4s_9EwAo4pHBcYxsBRPKs

