-------------------------BASICS---------------------------
-Strings: text in Python. called a string. Typed with "" or ''.
     --> 'Hello World'
  -Can combine strings together with +
    -'Hello ' + 'World'   --> 'Hello World'
  -Use """ for multi-line strings
  	"""Hello
  	  World""
        
-Arithmetic operators: Math signs that manipulate data
  +     - Adds data together
  -     - Subtracts data
  *     - Multiplies data
  **	- Exponent
  /     - Divides data
  %     - Remainder after division. %f returns floats
  ==	- Is equal to.
  !=	- Not equal to.
  +=    - Adds a value to a current variable
  -=    - Subtracts value from a current variable

-Add comments with hashtag #
# This won't be read. Skipped over. 

-Floats: numbers with decimals
   - 5.0
   - 3.14
-Booleans: Sets a variable either true or false
   == TRUE
   == FALSE

-Apostrophes are made using \
 --> "That\'s gay"

-Acessing Index of a string or array: The Index starts from 0 not 1
		P Y T H O N 
		0 1 2 3 4 5
    PYTHON[3] --> H. H is the 4th letter, but 3rd index
    
 -Methods:  Built-in functions that can do things.
  -len()			 -Finds length of string
  -.lower()			 -lowercases all letters in string
  -.upper()			 -Uppercases all letters 
  -.difference(y)    -Checks if y has things that are x
  -str()			 -Turns data into strings
  -float()			 -Turns integers into floats
  -int()			 -Turns floats into integers
  -del()          -deletes by index 
 
  Example: x = "lower case"
        x.upper() --> "LOWER CASE"

******Dot notation only works on strings******
 concatenate strings conversion: "That's "  + str(gay)
         --> "That's gay"
 
-Set variables using equal sign (=)
 my_name = "Mitch"
  print my_name --> "Mitch"


-Concatenate with f strings or %s:
   name = "Mitch" ||| print "Hello {name}" --> Hello Mitch
  print "The %s who %s %s!" % ("betas", "are", "cucks")
     --> "The betas who are cucks!"
     
You can transfrom one data type into another using certain functions
 str()     -transforms into string
 int()     -transformd into whole integer
 float()   -transforms into a decimal number     
 
 -If you need to call a file from the computer or something use \\
     'C:\\Users\\WilganZMT\\...'
 


:::::::::::::::::::::::::::::::FUNCTIONS::::::::::::::::::::::::::::::::
Allow you to reuse code easily. Can be used whenever.
Format: 
    def function_name(parameter1, parameter2):    
      const = x          -optional
      print = yz          -body of code. Indented
    ****return parameter      -required****  -returns the parameter1ter

-Parameter is a variable, a placeholder. Values of parameters passed
  are called arguments
  Example:
      def square(n):        -n is the parameter here
        squared = n ** 2     
        return squared
-Call the function by simply typing it. Like square(10)
    calling a function means to write it/s parameter with it/s 
    own value
 -Example:
      square(10)                    -10 is the argument passed
       --> return squared = 10 ** 2
        --> 100

-Some functions are built-in
   -min()          -returns minimum value
   -max()          -returns maximum value  
   -abs()          -absolute value
   -type()         -returns type of data 
   -range(x)       -Creates a sequence from 0 to x. x=index
     -start()          -Where it starts from
     -stop()         -Stops at but does not include
     -step()         -Increment
   -sort()         -sorts something in ascending order
    -(reverse=True)     -sorts in descending order
   -split()       -separates string at a certain character

Website of all built in functions: 
https://docs.python.org/3/library/functions.html#abs

::::::::::::::::::::::::CONDITIONAL STATEMENTS::::::::::::::::::::::::::
If, elif, or else statements. If any of the statements = true, it runs
Used within functions or variables
-Example:
    def grade_converter(grade):		-defines function
   	 if grade >= 90:
         return "A"
     elif grade >= 80:
         return "B"					-DONT FORGET COLON
     elif grade >= 70:
         return "C"
     elif grade >= 65:
         return "D"
     else:							-runs if all others = false
         return "F"

    print grade_converter(84) 	-inserts grade number into funciton
      --> B 					 -Returns "B"

 Set multiple conditions using and, or:
 	if x > 1 and y < 5:		-both conditions must be true to run.
 		return ~~~
 	if x > 1 and y < 5:     -either 
 		return ~~~

--------------------------DATA COLLECTIONS--------------------------
A datatype that stores collection of different pieces of info. Use []
	Format:
		list_name = [item1, item2,...]
-You can access items via their index
		list_name[1] --> item2

-You can change values at will
	zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
		zoo_animals[2] = "hyena"
			-->["pangolin", "cassowary", "hyena", "tiger"]

 -Manipulate the list 
  .append()		-adds value to end of list
  .pop()		-removes value at certain index
  .removes(x)		-removes x if it's in a list'
   del(n[1])		-deletes but doesn't return anything'
  .insert(n, x)         -inserts x at index n.
  
 Take a portion of a list using slice. Includes 1st, excludes 2nd 
 value
	letters = ['a', 'b', 'c', 'd', 'e']
	slice = letters[1:3]
	 --> ['b', 'c']
  -You can even include all data before or after a certain index
     -my_list[:2]			-Includes all indices before position 2
     -my_list[3:]			-Includes everything after position 3

 -Remove data from a list using .remove
	 beatles = ["john","paul","george","ringo","stuart"]
	 beatles.remove("stuart")
		--> ["john","paul","george","ringo"]
		
		
-Dictionaries
A dictionary is similar to a list, but you access values by looking 
up a key instead of an index. A key can be any string or number.
     Uses {} 
      .get()          -retrives data from a certain location
      .keys()	      -returns list of keys
      .values()       -returns list of values
	Format:
		d = {'key1' : value1, 'key2' : value2, 'key3' : value3}
		print d['key1']
		 --> value1
	-d['new_key'] = new_value  -adds in a new value for a key
        -del d[key_name]	   -deletes keys and values

You can also count characters in dictionaries using the get method
	word='brontosaurus'			-example string
	d=dict()					   -example dictionary
	for c in word:				-for loop
		d[c]=d.get(c,0)+1		-adds 1 every time a character shows up
	print(d)					 -r, s, u, and o, appear twice

You can also use lists to find out what character appears the most
  You need to append words characters into a list, then add that list
    to a dictionary

    sent = list()					-creates list

for line in handle:					-reads through a file
    if not line.startswith("From:"): continue
    line = line.split()
    sent.append(line[1])			-puts second word into the list

counts = dict()
for word in sent:					-reads through the filled list
    counts[word] = counts.get(word,0) + 1  -counts number of times

bigcount = None
bigword = None
for word,count in counts.items(): 
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print (bigword,bigcount)	

 .items()							-returns keys and their values
 
How to save each entry in a dictionary as an index of the dictionary

dict = {}      #Have an empty dictionary

dict_list = []    #Have a list of stuff in it 
for x in dict_list:
    for i in range(len(dict_list)):
        dict[f"{i}"] = "Whatever here"
 
Calling a number for i will return the value of that keys index
  dict[2] == value3   

-----------------------------TUPLES-----------------------------
Tuples are like a hybrid of lists and strings. They dont use [] but
 they are in an order separated by a ,. They still have an index
       ****Tuples can NOT be changed. They are immutable

   x = ('Glenn', 'Sally', 'Joseph')
   print(x[2])
    --> Joseph
   print(x)
    --> ('Glenn', 'Sally', 'Joseph')

 Tuples can be used when assigning variables
 	(x, y) = (4, 'Atreus')
 	print(y)
 	 --> 'Atreus'

  using .items() on a dictioary returns tuples of keys and values

 Tuples are comparable. They look at the first value only.

   (0, 1, 5) < (4, 18, 2)
    --> True  				-0 is less than 4, so thats all it compares

:::::::::::::::::::::::::::::::LOOPS::::::::::::::::::::::::::::::::::::
Loops allow you do carry out functions continuously for every single
element in a list.

DEFINE ALL VARIABLES BEFORE YOU BEGIN. OUSIDE THE LOOP

 -******For loop******
 ******Loops through all characters in a list/object etc.********
	Format:
		for (variable) in (list_name):
			if ~~~~
		return (variable)~~~		- variable can be anything
		 
	Example:
		names = ["Adam","Alex","Mariah","Martine","Columbus"]
			for x in names:
  			print x
  			#prints all names

You can loop through dictionaries using dictionariy_name[x]
	Example:
		webster = {
  		"Aardvark" : "A star of a popular children's cartoon show.",
  		"Baa" : "The sound a goat makes.",
  		"Carpet": "Goes on the floor.",
  		"Dab": "A small amount."}
			
			for x in webster:
 			 print webster[x]

 -Loop certain values using operators.
 	Example:	numbers = [1, 3, 4, 7]
				for number in numbers: 
  					if number > 6:
    					print number
   						--> 7

 -******While loops******
  Executes the code inside of it if some condition is true. Will 
  continue to execute so long 'as' the condition is true.
  	Example:
  	count = 0
  		while count < 5:
  		  print "Hello, I am a while  - Need to increment count"
  		and count is", count"
  		  count += 1
"Condition" is the expression that decides whether the loop is going 
to continue being executed or not. 

While loops need a stop condition or they will be infinite

The break is a one-line statement that means “exit the current loop.” 
	Example:
		count = 0

		while True:
  		  print count
  		  count += 1
          if count >= 10:
            break
 -While/else:
 	while/else is similar to if/else, but there is a difference: 
 the else block will execute anytime the loop condition is 
 evaluated to False

input("Your guess: ")		-Allows raw input into console


 -Print for each character in string
    string = "fkadlf"

    for c in string:
      print c

 -enumerate - supplies corresponding index to each element passed.

 -zip - creates pairs of elements whne passed two lists, and 
 will stop at end of shorter lists

 .keys()		-returns list of dictionary's keys'
 .values()      -returns list of dictionary's values'

   d.keys()
   d.values()


:::::::::::::::::::::::::LIST COMPREHESION::::::::::::::::::::::::::::::
Short syntax for a function
	Example:
	cubes_by_four = [x ** 3 for x in range(1, 11) if
	((x ** 3) % 4) == 0]
		print cubes_by_four

l = [i ** 2 for i in range(1, 11)]


	Stride        -In lists, how much you go up by.
		Example:
			list[1,2,3,4,5,6]
				list[1:7:2]
				 --> 1, 3, 5
Reversing lists.
 		list[::-1]
::::::::::::::::::::::::::OBJECTS/CLASSES::::::::::::::::::::::::::::::::::
Objects are pieces of code that are grouped in a way to carry  
some information. Almost everything is an object, but we can actually
make spefific objects with specific functions, lists, etc.  We do this 
using classes and adding into them.

Classes can be very useful for storing complicated objects
 with their own methods and variables. Defining a 'class' is much 
 like defining a function, but we use the 'class' keyword instead.
 They are like a blank canvas or a rough draft of an object.

	Format:
		class ClassName(instance):      -creating the Class
			def function():          
			  x = Mitch                 -part of the function
			  print("My name is " x)    -prints function
c1 = ClassName()                      -sets c1 variable as the class
c1.function --> "My name is Mitch"    -the . retrieves the property of the variable

We can use classes to create new objects, which we say are
 INSTANCES of those classes. We can then assign values to 
 properties that we give classes

		newObject = ClassName()
	Example:
		class Person():
			-name: 
			-personality:    -properties that Person can have
			isSitting:
	p1.name = "Karen"
	p1.personaity = "bitch"     -sets values for properties
	p1.isSitting = False

  -dir(~)                 -returns all possible methods of the 'class'
  -type(~)                -tells what kind of thing the object is

Objects can be built then thrown away when no longer needed. We do this
by using  'constructor' and 'destructor'

Constructors just give initial values to start off, then can change.
Common name is __init__, but it can be anything
class Dog:
  kind ='canine'     -variable that all instances have

#constructors set up individual instances of objects.
 def __init__(self, name):  -self refers to this instance of class Dog
        self.name = name    # instance variable unique to each instance

  d = Dog('Fido')
  e = Dog('Buddy')
  d.kind                  # shared by all dogs
   -->'canine'
  e.kind                  # shared by all dogs
   -->'canine'
  d.name                  # unique to d
   --> 'Fido'
 e.name                  # unique to e
   --> 'Buddy'

*****Destruction happens when the variable an changes. I can change to 
anything other than PartyAnimal, and then the object is destroyed*****

You create multiple instances from the same 'class' 

 class PartyAnimal:
  x = 0
  name = ""                      -this will be changed 
  def __init__(self, z):         -z is a parameter, self is the instance
    self.name = z
    print(self.name, "constructed")

    def party(self):
      self.x = self.x + 1
      print(self.name, "party count", self.x)

s = PartyAnimal("Sally")        -Sally will replace z & will be printed
s.party() 

j = PartyAnimal("Jim")          -Jim will now be its own instance

We now have two different instances that use the same function

We can also make two differenct objects that feed off each other

 class PartyAnimal:
  x = 0
  name = ''
  def __init__(self, nam):
    self.name = nam
    print(self.name,"constructed")

  def party(self):
    self.x = self.x + 1
    print(self.name,"party count",self.x)

class FootballFan(PartyAnimal):    -#this creates a new class that adds
  points = 0                        #data to it while keeping OG data
  def touchdown(self):
    self.points = self.points + 7
    self.party()
    print(self.name,"points",self.points)


::::::::::::::::::::::::::REGULAR EXPRESSION::::::::::::::::::::::::::::
  Regular expression is a way of finding specific characters in data
   and isolating them. You use shorthand codes to express what you want
    to find. Also called 

  Need to import re before you use it
     
    ^                  -beginning of line
    $                  -end of line 
    .                  -matches any character
    *                  -matches any number of specific characters before it
     -ab*                    -aaaabbbbb, abbbbbbb, aaaaaab
    +                  -matches at least 1 character
     -ab+                    -abbb, abb, ab
    [amd]              -matches a, m, or d in a string
   #\S                 -Matches non-whitespace characters
   #\s                 -matches whitespace characters
   [a-z0-9]            -set of characters in a range                 


::::::::::::::::::::::::::::::LAMBDA::::::::::::::::::::::::::::::::::::
Lambda acts 'as' a substitue for a function
	lambda x: x (% 3 == 0)  -Function goes in ()
	def by_three(x):
  	  return x % 3 == 0

:::::::::::::::::::::::::::::::MODULE:::::::::::::::::::::::::::::::::::
   Import certain variables or functions from a given modules
	Format:
 		from module import function
 Use * to import everything form module
 		from module import *

::::::::::::::::::::::::::::::FILES:::::::::::::::::::::::::::::::::::::
Files are what python deals with the most.
open files then set a handle variable equal to it

To read files, you must assign a handle to it, then read it later

	fhand = open('~~.txt')		-Assigns the file handle name
	print(fhand)				   -prints handle, not data
****This is not the data, it is a handle****

*********To read a file, you put a for loop using the file handle.*******
   Alter the lines using methods within the for loop.
	
	for line in fhand:			-for loop that reads through the file
    	line = line.rstrip()      -removes whitespace and line height
		line = line.upper()       -changes every line to uppercase
		print(line)				 -prints the actual data

::::::::::::::::::::::::::::WEB PAGES:::::::::::::::::::::::::::::::::::
  You can take data from any webpage & read it like a file. 
       Use urllib library to read it.

  Import the library first, then save the file to a handle, then 
    decode the handle using .decode()then run a for loop to 
    read all the lines.

  import urllib.request, urllib.parse, urllib.error
  handle = urllib.request.urlopen('http://~~~~~~~~~')
  x = handle.decode()
  for line in x:
    print(line.strip())

  x.decode()                   -turns encoded data into strings

You can use BeautifulSoup to parse entire websitess into html parts

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = ('http://py4e-data.dr-chuck.net/comments_1065111.html')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
  
  You can also take specific characters from html tags using .get &
   .contents

::::::::::::::::::::::::::::::::JSON::::::::::::::::::::::::::::::::::::
 JSON is an easy, lightweight coding manipulation to store & share data
  JSON stores data within dictionaries and lists for ease of reading
 ***You need to import JSON to use it***

 To access the data, use .loads(~) to load the strings.

 import json

  Example:
 data = ''' {
  "name" : "Mitch",      
  "phone" : {
    "type" : "intl",            -This is how JSON data is stored
    "number" : +1 216 901 8097
  },
  "email" : {
    "hide" : "yes"
  }
}'''

info = json.loads(data)           -.loads() = load from string
print('Name:', info["name"])      -prints the name value, Mitch
print('Hide:', info["email"]["hide"])   -prints value of yes

 JSON can also makes lists using data
 
 input = '''[
 { "id" : "001",
   "x" : "2"},
 { "id" : "009",}]'''

 using .loads returns a list of two dictionaries. You can use a for loop
 to print out different keys and values.

::::::::::::::::::::::::::::::::SQL:::::::::::::::::::::::::::::::::::::
 Structured Query Language is a database system for uploading & editing
 data. When using python, use cur.exceute('''~~~''') to create
 or edit data.

 .cursor()  is like a file handle

 foreign key = key that links two tables together
 primary key = a number that identifies certain data 

  INSERT INTO (table name) (column 1, column 2) VALUES ('~~', '~~') ;

  DELETE FROM (table name) WHERE email = '~~~~~~~'

  UPDATE (table name) SET column 1 ='~~' WHERE column 2 = '~~~'

  ?  is a placeholder for data 

  INSERT OR IGNORE INTO Course (title) VALUES ( ? ) 
   - Ignores if any duplicates are added
You can manually create a database file using python alone using the 
following code with prepared examples

  cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

  Now if you actually want to give them values, you input code like this

      cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ? )''', 
        ( name, album_id, length, rating, count ) )
    conn.commit()

Adding the insert or ignore will prevent any errors & prevent duplicates

-------------------------API & GEOCODING----------------------------
An application programming interface (API) is an interface that defines 
interactions between multiple software applications or mixed 
hardware-software intermediaries. APIs allow data from different systems to
be transfered & received. It has it/s own syntax and structure, so we need
to know what they are in order to work with it.

--------------------------EXE CONVERSION------------------------------
Have pyinstaller installed.
Go to the main directory folder that your project is in.
In the path bar at the very top, type in cmd.
It will bring up the command line, then type the following:
     
        pyinstaller --onefile ~~name of file~~.py
Once all thats done, delete the .spec file, the build folder,
and take the exe out of the dist folder, then delete the 
dist folder. Then just run the exe.
