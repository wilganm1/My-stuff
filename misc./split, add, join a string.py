""" Let's say you have a string and you want to add something to it, like a word. Here's how """

a_string = "What is the speed of light?"   #String I picked. Use whatever you want.

b_string = a_string.split()      #splits the string into a list of all the words --- ['What','is',...,'light?']

for i in b_string:   #loops through words in string
    if b_string.index(i)%2 == 1:   #Gets the index of the word and checks if it's odd or even. %2 == 1 means it's odd.
      b_string.insert(b_string.index(i), "#insert whatever here")   #inerts whatever you want at all the odd indices
" ".join(b_string)          #This joins all the words together. YOU MUST HAVE A SPACE BETWEEN THE "" MARKS OR THE WORDS WON'T BE SEPARATE
