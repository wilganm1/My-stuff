------------------------------BASICS------------------------------
Python is a general puprose high-level interpreted programming language. 

Data Types.
 int     -Integers. Whole numbers. -9, 3045
 str     -strings. Text in Python. Uses "" or ''.
 float   -decimal numbers. 3.14, 0.2134 
 bool    -Boolean. true or false
        
-Operators: Signs that manipulate data
  =     - Creates variables.
  +     - Adds data together
  -     - Subtracts data
  *     - Multiplies data
  **	- Exponent
  /     - Divides data
 //     - Divides data then rounds to nearest smallest number
  %     - Remainder after division. %f returns floats
  ==	- Is equal to.
  !=	- Not equal to.
  +=    - Adds a value to a current variable
  -=    - Subtracts value from a current variable

-Acessing Index of a string or array: The Index starts from 0 not 1
		P Y T H O N 
		0 1 2 3 4 5
    PYTHON[3] --> H. H is the 4th letter, but 3rd index

 Check if a variable is a certain data type. isinstance
	  isintance(variable, data_type)
    
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
 

-------------------------------FUNCTIONS-------------------------------
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

--------------------------CONDITIONAL STATEMENTS--------------------------
If, elif, or else statements. If any of the statements = true, it runs
Used within functions or variables
-Example:
    def grade_converter(grade):	
   	 if grade >= 90:
             return "A"
   	 elif grade >= 80:
             return "B"		
         elif grade >= 70:
             return "C"
         elif grade >= 65:
             return "D"
         else:		 -runs if all else fails					
             return "F"

 Set multiple conditions using and, or:
 	if x > 1 and y < 5:	-both conditions must be true to run.
 	    return ~~~
 	if x > 1 and y < 5:     -either 
 	    return ~~~

--------------------------DATA COLLECTIONS--------------------------
List. A datatype that stores collection of different pieces of info. Use []
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
			
Dictionaries. A dictionary is similar to a list, but you access values
by looking up a key instead of an index. A key can be any string or number.
      	Format:
		d = {'key1' : value1, 'key2' : value2, 'key3' : value3}
		print d['key1']
		 --> value1
	.get()          -retrives data from a certain location
        .keys()	      -returns list of keys
        .values()       -returns list of values
	d['new_key'] =   new_value  -adds in a new value for a key
        del d[key_name]	   -deletes keys and values
	.items()	-returns keys and their values

 You can also count characters in dictionaries using the get method
	word='brontosaurus'	-example string
	d=dict()		-example dictionary
	for c in word:		   -for loop
		d[c]=d.get(c,0)+1  -adds 1 every time a character shows up
	print(d)		   -r, s, u, and o, appear twice

How to save each entry in a dictionary as an index of the dictionary

dict = {}      #Have an empty dictionary

dict_list = []    #Have a list of stuff in it 
for x in dict_list:
    for i in range(len(dict_list)):
        dict[f"{i}"] = "Whatever here"
 
Calling a number for i will return the value of that keys index
  dict[2] == value3   

Tuples. Like a hybrid of lists and strings. They dont use [] but
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

-----------------------------LOOPS-----------------------------
Loops allow you do carry out functions continuously for every single
element in a list.

DEFINE ALL VARIABLES BEFORE YOU BEGIN. OUSIDE THE LOOP

 -For loop. Loops through all characters in a list/object etc.
	Format:
		for variable in object: -variable can be anything
			#code here	 
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

While loops
  Executes the code inside of it if some condition is true. Will 
  continue to execute so long 'as' the condition is true.
  	Example:
  	count = 0
  		while count < 5:
  		  print "Hello, I am a while  - Need to increment count"
  		  count += 1
	While loops need a stop condition or they will be infinite
	
-Stopping the loop with break
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

-----------------------------LIST COMPREHESION-----------------------------
Short syntax for a list creation.
  General format:
	  [what_you_want_to_do for x in whatever]
	
    Example, adding 3 to every number in a range:
	[x+3 for x in range(1,5]
           --> [4,5,6,7,8,9]
     -Stride        -In lists, how much you go up by.
	Example:
	   list[1,2,3,4,5,6]
		list[1:7:2]
		--> 1, 3, 5
Reversing lists.
 		list[::-1]
-------------------------------OBJECTS/CLASSES-------------------------------
Class are like blueprints to create new things called objects. Think of classes
as car and object like Volvo. All cars have simialr features, but Volvo has specific
differences. 

	Format:
	    class ClassName(instance):      -creating the Class
		    x = "~"             -attribute of class. All objects have this
			
		    def __init__(self, y):  -constructor.
			    self.y = y
	
  -Constructors. 
    Constructors are special funtions that are always called each time a new object is created. 
	It works just like a regular function but the parameters you pass become the attributes
        of the new object. The self keyword bind the attribute to the object.
	
 -Creating an object. Just create a new variable and assign it the the class name with arguments for the
constructor.
     obj1 = ClassName(x)
 
 -Get attributes using dot notation.
	obj1.y = y

----------------------------REGULAR EXPRESSION----------------------------
 Shorthand codes to find certain patterns.

import re
   ^                  -any character to its right at beginning of line
   $                  -matches any character to its left at end of line
   .                  -matches any character
   *                  -matches any number of specific characters before it
    -ab*                    -aaaabbbbb, abbbbbbb, aaaaaab
   +                  -matches at least 1 character
    -ab+                    -abbb, abb, ab
  [amd]               -matches a, m, or d in a string
  #\S                 -Matches non-whitespace characters
  #\s                 -matches whitespace characters
  [a-z0-9]            -set of characters in a range                 


---------------------------------LAMBDA---------------------------------
Lambda acts 'as' a substitue for a function
	lambda x: x (% 3 == 0)  -Function goes in ()
	def by_three(x):
  	  return x % 3 == 0

---------------------------------MODULE---------------------------------
   Import certain variables or functions from a given modules
	Format:
 		from module import function
 Use * to import everything form module
 		from module import *

----------------------------------FILES----------------------------------
Python can open, read, save, copy, delete, and move files around.
Python opens files by locating their directory (aka folder) and 
changing what to do with those files.

On Windows, use raw string literals when accessing files with \
		r'path\file'

 -Accessing files. Use with open pattern to load files and do stuff
	with open (r'folder\file.txt', '~') as x:
		#do stuff
		
   -Reading files
	 with open(r'folder\file', 'r') as x:
	       	 data = x.read()
			
   -Writing files
	 with open(r'folder\file', 'w') as x:
		data = "text~~~~~~"
		x.write(data)
		
		Lines = ['daf', 'eta']
		x.writelines(Lines)  -writes all list items on new lines
		
  -Append to existing file. a+ lets you read and write.
	 with open(r'folder\file', 'a+') as x:
		x.read('\n~~')  -\n to start a new line
		x.write("~~"). -

Pathlib. Package to use paths and work with files more easily

import pathlib

  pathlib.Path.cwd(). -print out current directory
    .read_text().    -reads data as string 
    .resolve().      -finds full path of file

-------------------------------WEB PAGES---------------------------------
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

---------------------------------JSON---------------------------------
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

--------------------------------SQL--------------------------------
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
