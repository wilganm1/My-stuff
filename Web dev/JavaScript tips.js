::::::::::::::::::::::::::::::::Basics::::::::::::::::::::::::::::::::::
 **Code typed in camelCase. Every word after first is capitalized**

console.log();         -Prints data onto console
document.write()       -writes characters onto document
	-"String"			-read as words. Requires ""
	-Numeric			-number values
	-Boolean   		-wheter a function is true or not.


.innerHTML="~~"    -Change the text of an element 


.getElementById("~~")   -can grab an HTML element by its Id name

console.log('Go Fu ' + 'ck Yourself');
--> Go Fuck Yourself

Arithmatic operators
	+					-Adds two variables
	/					-Divides variables
	-					-Subtracts
	>=					-Greater than or equal too
	<=					-Less than or equal
	!=					-not equal to
  ==          -Is equal to. Causes coercion. Makes strings numbers
	===					-Is equal to. Does not cause coercion
	*					-multiplies
	%					-Remainder Whats left over after one number goes into 
						 another number fully. Example: 7 % 3 = 1.
             3 goes into 7 two times with a left-over of 1.
	+=				-Adds values to a variable
	++				-Increases value of variable by 1
	--				-Decreases value of variable by 1 
  Add a comment with //

:::::::::::::::::::::::::::::::VARIABLES:::::::::::::::::::::::::::::::::
Variables allow us to save any type of data as a name to access later
 -var myName = "Mitch"       -Sets a variable.
  console.log(myName);
   --> "Mitch"

 -let meal = 'pizza'     -Can be assigned to a different value
  --> 'pizza'
  -let meal = 'fries'
   --> 'fries'

-const nyName = 'Deepthroat' -A variable that cant be changed.
Object.freeze(myName)     -prevents myName from being altered

****String interpolation**** using template literals.
Can be used to log strings together with a const variable
****Set a const, then use `__${variable}`****
Example:
const myPet = 'Dragon';
console.log(`I own a pet ${myPet}.`)
  --> 'I own a pet Dragon'

Append methods to find attributes of variables
 -xyz.length
 -.

::::::::::::::::::::::::::::::::Methods:::::::::::::::::::::::::::::::::::
Methods are built-in fucntions.
*******Use by adding a . after a variable/instance********

Format:   methodName(argument) {
	property(argument)}

	addNew(new) {this._new.push(new)}
	
Example:
	console.log('hello'.toUpperCase());  -Uppcase every letter
		--> 'HELLO'

 new Date()           -creates a new date
 -.getFullYear()
 -.getMonth()         -gets current month.
 -.toUpperCase()      -Uppercases all letters
 -.toLowerCase()      -lowercases all letters
 -.random() 		   	  -generates random number.
 -.length()		   	    -How long a list/array is.
 -.indexOf("")        -find the index of a variable or string
 -.replace(X, Y)      -replaces X with Y
 -.pop()              -removes last position of an array
 -.splice(index,n,x)  -removes index positions. n= # to delete. X adds in
 -.slice(i1, i2)      -copies data to new array. starts at i1, ends at i2+1
 -.map()              -makes new array for every array element of function
 -.sort(desc())       -sorts array ascending or descending. asc is default
 -document.getElementBy
  -Id()               -get id of elements
  -ClassName()
 -.innerHTML="~"      -Changes content of an element

::::::::::::::::::::::::::CONDITIONAL STATEMENTS::::::::::::::::::::::::
Checks a specific condition & performs a task based on condition
**************************************************************
*- if statements 		-if something happens, do something      *
*	if(condition that evaluates to true ){                      *
*		console.log('code that runs');                          *
*	 } else if (condition){console.log('this code runs');	   *
*	 } else {console.log('this code runs')}                    *
*	  -If the if or else if condition = true, the code runs    *
*	  -If the condition = false, the else if code runs.        *
*     - If else if = false, the else runs.                   *
*       - Stops when else if = true;                         *
**************************************************************
LAST else DOES NOT HAVE A CONDITION

Example:  let hunger = 7
		  if(hunger > 7) {console.log('Time to eat!')}
		   else {console.log('We can eat later!')};
		--> 'We can eat later!'

	-Operators 
	  - &&			-Check if two things are true
	  - ||			-Check if at least one thing is true
	  - !			-Checks if it's not equal to'
Example:  let day = 'Saturday'
			if(day === 'Saturday' || day === 'Sunday') 
			{console.log('Enjoy the weekend!');
		  } else {console.log('Do some work.');}
		   --> Enjoy the weekend

		  let excited = true;
		  console.log(!excited);
		   --> false
****Can use ? to create a ternary operator****
	  Format:  var  ?  if true code  :  else code
    let PMarks = 40  
    let result = (PMarks > 39)?  
        "Pass":"Fail";

isNightTime ? console.log('Turn on the lights!') :
console.log('Turn off the lights!');

**Use switch to replace if and case to replace else. Use break to stop**
switch(groceryItem){
	case 'tomato': 
	  console.log('tomatoes are $0.49');
	break;								  -exits block
	case 'lime':
.................
  default:
    console.log(xyz);
    break;

  If you have a variable, you need to include it in case

  var answer = ""
    case 1:
      answer = "~~";
      break;

::::::::::::::::::::::::::::::::FUNCTIONS:::::::::::::::::::::::::::::::::
***We can make our own functions with following format***

  function functionName(parameters) {command code(parameters)}
/*The word function is an inherent command to create
a function. functionName is the name of the function with 
parameters and the command code. Parameters are treated as 
variables.*/

********Here is how functions work********
EXample:  const xyz = [1,2,44,621,77,3]
	    const abc = xyz(VEGETABLE => {return ~~~});
  ****Making NUMBERS a parameter, it names all the elements in the 
  xyz array as a VEGETABLE; It does this because we have already
  made xyz as  function identifier. *****It treats everything in 
  the xyz array as a VEGETABLE!!!!!*********************;

 Putting somehting in the parantheses makes it follow the 
 command code.;

const rectWidth = 10;
const rectHeight = 6;
 function calculateArea(rectWidth, rectHeight) 
 			console.log(rectHeight * rectWidth

 Example:  function sayThanks(name)
 			{console.log('Thanks ' + name + '.')}
 			sayThanks('Cole');
 			 --> Thanks Cole; 

*default parameters*
 function list(item1 = 'eggs', item2 = 'milk') {
 	console.log(`Buy ${item1}`);
 	console.log(`Buy ${item2}`);}

**Return call**
Use return to call the function;

function x(y,z) {const area = y * z;
	return area;}
	 --> returns the area of y and z;

/Function expression/
const plantNeedsWater = function(day){if(day ===
	'Wednesday'){return true;} else{return fals;}};
		plantNeedsWater('Tuesday');
		console.log(plantNeedsWater('Tuesday'));
		 --> false;

Use let = () => {} to shortcut function command;

::::::::::::::::::::::::::::::::ARRAYS:::::::::::::::::::::::::::::::::
Arrays are created using []. They are used to make lists 
in functions.;Lists are ordered by index starting at 0, not 1.
	***[0,1,2,3,4,5,6,7,8]***
Example:
		let list = ['A','B','C','E'];
		list[1] --> 'B';
Can update a list.
		list[3] = 'D';
		 --> ['A','B','C','D'];
   -.push() 					 -adds items to the end of array.
  list.push('F','G');
   -->['A','B','C','D','F','G']
   -.pop()						 -Removes last item in an array.
    							 -logging the pop only returns what was removed.;
 -.splice(index,n,x)  -removes index positions. n= # to delete. X adds in
 -.slice(i1, i2)      -copies data to new array. starts at i1, ends at i2+1

const nestedArr = [[1], [2,3]];  -Nested array. Can have separate
  nestedArr[1] --> [2, 3]		  arrays that take up an index space
  nestedArr[1][0] --> 2       You need an array index for every nested array

Spread operator ([...~~~])       -Copies an entire array 
  Example:
    const arr12 = [316, 420];
    const arr2 = [...arr12]
  console.log(arr2) --> ['316, 420'];

::::::::::::::::::::::::::::::LOOPS:::::::::::::::::::::::::::::::::::::::
Loops functions repeat a command over and over under conditions

For loops
 Example:
    var = i;
    for(i = 0; i < x; i++){
      console.log(i)
    }
  as each loop passes, i gets bigger by 1 until x is reached.

      i++ can also be written as i = i + 1;

  Example: looping from 0 to 9
    for (i=0; i < 10; i++)

Use const = xyz;
	xyz(x => {}); to shortcut function command;
	parameters inside the ( ) and then add an arrow => that points to the 
	function body surrounded in { } like this:;
		const rectangleArea = (width, height) => {
 		 let area = width * height;
  			return area;};

*Repeats a set of instructions until a specified condition is met.*
	Loops typically used as or in functions
   for (initialization; stopping condition; iteration statement){};
Example:;
	for (let counter = 0; counter < 4; counter++) {
		console.log(counter);}
	-->0
	   1
	   2
	   3
Do it in reverse;
	for(let counter = 3; counter >= 0; counter--) {
		console.log(counter);}

Arrays have zero-based indexing, which means the last 
index of the array is length - 1 

Use .length to make loops easier
Example:;
	const letters = ['A','B','C','D'];
 for(let i = 0; i < letters.length; i++) {
 	console.log('I know the letter ' + letters[i]);}
 	--> 'I know the letter A'
 		'I know the letter B'
  		'I know the letter C'
 		'I know the letter D'

Nested loops
	const myArray = [6, 19, 20];
	const yourArray = [19, 81, 2];
	  for (let i = 0; i < myArray.length; i++) {
  	   for (let j = 0; j < yourArray.length; j++) {
    	 if (myArray[i] === yourArray[j]) {
      console.log('Both loops have the number: ' + yourArray[j])}};

While loops make loops with a different format;
  let counterTwo = 1;
while (counterTwo < 4) {
  console.log(counterTwo);
  counterTwo++;

Iteration methods - methods to perform loops 
 - .forEach()			- Loops every element in an array.;
  Example:
   const fruits = ['mango', 'papaya', 'pineapple', 'apple'];
   			// Iterate over fruits below
fruits.forEach(fruit => console.log(`I want to eat a ${fruit}.`));

 - .map()				- takes an argument & returns a new array;
  Example:
    const numbers = [1, 2, 3, 4, 5]; 

const bigNumbers = numbers.map(number => {   -number defines elements
  return number * 10;});					  in the array as a parameters

 - .filter()			- filters out certain elements from array;
 Example:
  const randomNumbers = [375, 200, 3.14, 7, 13, 852];
const smallNumbers = randomNumbers.filter(num => 
	{return num < 250});
     --> [200, 3.14, 7, 13];

 - .forIndex() 			- Find location of an element in array.
 Example:				  Returns first value that = true
  const jumbledNums = [123, 25, 78, 5, 9]; 
   const lessThanTen = jumbledNums.findIndex(num => {
     return num < 10;});
      --> 3

  - .reduce()			- Reduces an array after each iteration.
 Example:
 	const numbers = [1, 2, 4, 10];
	 const summedNums = numbers.reduce((accumulator, currentValue)
	  => {return accumulator + currentValue});
			console.log(summedNums) // Output: 17

::::::::::::::::::::::::::::::::OBJECTS:::::::::::::::::::::::::::::::::::
*Objects are containers storing related data and functionality.*
Use  {} to create an object literals. Has a value for a key
		let xyz = {'key1': 'value1', 
               'key2': 'value2', ....};

 -Access an objects value by using Dot . notation with its key
Example:
 let spaceship = {
  homePlanet: 'Earth',
  color: 'silver'};
spaceship.homePlanet; // Returns 'Earth',
spaceship.color; // Returns 'silver',

 - Bracket [] notation		- Accesses keys that have spaces. works like dot
 Example:
 	let spaceship = {
  'Fuel Type': 'Turbo Fuel',
  'Active Duty': true,
  homePlanet: 'Earth',
  numCrew: 5};
spaceship['Active Duty'];   // Returns true
spaceship['Fuel Type'];   // Returns  'Turbo Fuel'
spaceship['numCrew'];   // Returns 5
spaceship['!!'];   // Returns undefined 

 - property assingment =	   - Can assign new values using =
 Example: 					  
 const spaceship = {type: 'shuttle'};
spaceship = {type: 'alien'}; // TypeError: Assignment to constant variable.
spaceship.type = 'alien'; // Changes the value of the type property
spaceship.speed = 'Mach 5'; // Creates a new key of 'speed' with a value of 'Mach 5'
  *****Use dot notation for key and use [] notation for value*****
 - delete operator to delete a value from an object
   delete spaceship.mission
   delete spaceship['Secret Mission']

  - methods 			     	- default functions that are in Objects
     key is the method name. value is method function
   const alienShip = {invade: fucntion () {console.log('he')}};
   --> invade () {console.log('he')};

  - Nested objects.
   Use dot notation like so:
   		variable.object1.subobject['String']
  Arrays look like this:
  	passengers : [{name: 'Space Dog'}],


 - By Reference
- When changing a value that is part of an object, its positioning
stays the same but the value Changes
Example;
 const spaceship = {
   homePlanet : 'Earth',
   color : 'silver'
 };let paintIt = obj => {			-/*function*/
   obj.color = 'glorious gold'
 };paintIt(spaceship);
 spaceship.color // Returns 'glorious gold' 

 -.hasOwnProperty(~~)    -checks if a property is in an object

 - in property          -checks if an object has a specific property
    'Alan' in user;
      //returns true

 - for..in 					   - will execute a given block of code 
Example:						     for each property in an object. 
  for (let crewMember in spaceship.crew) {
  console.log(`${crewMember}: ${spaceship.crew[crewMember].name}`)};

  -Constructors         -create new objects called instances. Capitalized
      function Dog(){
         this.name = "Albert"}
 //  You can set a new variable equal to a new object using the new element
        let hound = new Dog(); 
          -hound now has all the properites of Dog 
//   You can also make constructors flexible makning them easier to use
      -Pass parameters into the function before calling a new object;
        function Bird(name, color) {
          this.name = name;
          this.color = color;
          this.numLegs = 2;}
      -Then pass in your own names and colors into the new object.
        let hawk = new Bird("Hawk", "Brown")
            hawk.name --> //Hawk
            hawk.color --> //Brown
            hawk.numLegs --> //2

    -X instaceof Y        -Can check if X is was created by Y. true or 
        let hawk instanceof Bird; // => true
        let qoee innstaceof Bird; // => false

    -own       -own properites are properites directly defined on objects
      Every new instance of a constructor has their own propeirties if 
      the parent object has a parameter in it
         function Bird(name) {
         this.name  = name;
         this.numLegs = 2;}
            let duck = new Bird("Donald");
    -.hasOwnProperty    -checks if an instance has a property
      you can add the properites to a new array
        let ownProps = [];

        for (let property in duck) {
        if(duck.hasOwnProperty(property)) {
        ownProps.push(property);}}
console.log(ownProps); // prints [ "name", "numLegs" ]

    -~~.prototype.~~        -shares a property among ALL instances
        Bird.prototype.numLegs = 2;   -numLegs will always be 2

    -~~.constructor === ~   -checks if its true or false
        function joinBirdFraternity(candidate) {
          if (candidate.constructor === Bird) {
           return true;
         } else {
           return false;}}
//     You can add all properties into a prototype:
             Bird.prototype = {
              constructor: Bird,     -need to add constructor
              numLegs: 2, 
              eat: function() {
               console.log("nom nom nom");},
              describe: function() {
               console.log("My name is " + this.name);}};
    -~~.isPrototypeOf       -checks if a prototype is from a constructor
         function Bird(name) {
              this.name = name}
                let duck = new Bird("Donald");
          Bird.prototype.isPrototypeOf(duck); // returns true
    -Object.prototype      -prototypes that have their own prototypes
       Object.prototype.isPrototypeOf(Bird.prototype); // returns true
       Object.prototype.isPrototypeOf(Bird.prototype); // returns true

    -supertype of object      -Allows code not to be repeated   
          Bird.prototype = {
            constructor: Bird,
            describe: function() {
            console.log("My name is " + this.name);}};

          Dog.prototype = {
            constructor: Dog,
            describe: function() {
            console.log("My name is " + this.name);}};
/*   Both instances have the describe function. supertypes store describe
      in one separate "placeholder" object so it doesn't have to be
      repeated */

      -Object.create(~.prototype)   -set a new object prototype equal to
                                     a supertype prototype
        Bird.prototype = Object.create(Animal.prototype);
          let duck = new Bird("Donald");
          duck.eat(); // prints "nom nom nom"
      -prototype.constructor        -manually set where an instance 
                                     takes its constructor from  
   - this. 					   -set properties of new object. refers to new 
  Example:   					  object inside the constructor.
const goat = {***dietType***: 'herbivore',
     diet() {console.log(this.***dietType***);}};
		goat.diet(); 
		//****Output: herbivore******
		return `I am ${this.dietType}`;


 - Privacy :the idea that only certain properties
 	 should be mutable or able to change in value.

 - Getters: get and return the internal properties of an object.
 Example:
 	const person = {
  _firstName: 'John',
  _lastName: 'Doe',
  **get fullName() {if (this._firstName && this._lastName){**
      return `${this._firstName} ${this._lastName}`;
    } else {return 'Missing a first name or a last name.';}}}
	// To call the getter method: 
	  person.fullName; // 'John Doe'

 - setters: reassign values of existing properties within an object
 Example:
 const person = {_age: 37, set age(newAge){
 	if (typeof newAge === 'number'){
      this._age = newAge;
    } else {console.log('You must assign a number to age');}}};

  - Factory functions: make many instances of objects quickly.
Example
  const monsterFactory = (name, age, energySource, catchPhrase) => {
  return {name: name,
  	age: age,
    energySource: energySource,
    scare() {
      console.log(catchPhrase);}}};
   -***This creates an object template that will be filled with
   other constants****
  const ghost = monsterFactory('Ghouly', 251, 'ectoplasm', 'BOO!');
	ghost.scare();
			-Calling monsterFactory() sets the values to the object
If parameter is same as object key, just type in key,

  Ojbect property shorthand     -easy way to write object literals
    -Old method
      const obj = (x, y) => ({x: x, y: y});
    This is can be shortened.
    -Shorthand method
      const obj = (x, y) => ({ x, y });

::::::::::::::::::::::::::CLASSES::::::::::::::::::::::::::::::::::
JS is an Ojbect-Oriented Programming (OOP) language
********Classes create templates for objects*********

 - destructured assignment : shorthand for a particular parameter
 	  const residence = vampire.residence; 
	console.log(residence); // Prints 'Transylvania' 

 - Constructor class
 It’s called the constructor method. JavaScript calls 
   the constructor() method every time it creates a new 
   instance of a class. 

 Format of class: 
 	class Class {
 		constructor(property1, property2) {
 			this.property1 = property1;
 			this.property2 = ~~~;}}
 - Creating an instance: object that contains the 
     property names and methods of a class
 
 To create an instance, make a new constant and set it equal to 
    = new Class('new parameter1 call') /*Creates a new Class instance*/

 - Inheritance: A super class whose properties are shared among
 			many other classes. Create a parent class.

 	extends: makes methods of parent clas available to subclass
 	super(argument1): passes argument of subclass to constructor
 	 of the parent class.
Example:
 	 class Cat extends Animal {
  constructor(name, usesLitter) {
    super(name);
    this._usesLitter = usesLitter;}}

 - static methods: methods that any object can call
 	static generateName() {
    const names = ['Angel', 'Spike', 'Buffy', 'Willow', 'Tara'];
    const randomNumber = Math.floor(Math.random()*5);
    return names[randomNumber];} 

:::::::::::::::::::::::::::MODULES::::::::::::::::::::::::::::::::
Reusable pieces of code that can be exported from one 
 program and imported for use in another program
 		Export and import files
  Write in HTML within the <script> tag
    <script type="module" scr="~~~~~.js"><script>

Exporting:
const add = (x, y) => {           
  return x + y;}
const subtract = (a, b) => {         -functions defined then exported
  return a - b;}                      at the same time

export { add, subtract };

Importing:
 import { ~~, ~~, ~~ } from './math_functions.js';
  -if multiple functions are in same file, 

Use import * as ~~ to import everything from a file.


Format:
	object = {}
	object.property = value;

  let Xyz = {}; 		    -Object that represents module
  Xyz.abc = 'dfask';    -property of Xyz module = value in property

  module.exports = Xyz;	-variable that represents module

 - import
 	const obj = require('./file_name.js');

 - export default:      -Easier way to export data.
Format: let Xyz = {};
        export default Xyz;

 - import Xyz from './file_name'   -import command shortcut
 
 ::::::::::::::::::::::::::PROMISES::::::::::::::::::::::::::::::::
 Promises are objects that represent the eventual outcome on a
 asynchronous operation. They will or won't do it'

  declare a constant, then use new to create a promise
 Format:
  const myPromise = new Promise((resolve, reject) => {});   

3 types of promises:
 -Pending     -operation has not completed yet. Default state
 -Fulfilled   -operation has completed successfl and promise is
              resolved
 -Rejected    -Opertion has failed and prome has a reason for failure
      - end in error

const executorFunction = (resolve, reject) => {};
const myFirstPromise = new Promise(executorFunction);
  -resolved()      - changes promise's status from pending to resolved'
  -reject()        - changes promise status from pending to rejected;

setTimeout(callbackFunction, delayinMilliseconds)

When promise is resolved, use .then() to state what will happen after.
When promise is reject, use .catch()
  Has two arguments called "handlers"

const makeServerRequest = new Promise((resolve, reject) => {

 prom
   .then((resolvedValue) => {
     console.log(resolvedValue);
   })
   .catch((rejectionReason) => {
     console.log(rejectionReason);
   });

:::::::::::::::::::::::::REGULAR EXPRESSIONS::::::::::::::::::::::::::::::
Regular expressions, also called "regex" help find specific characters in 
a string. Works like Contorl + F. Case-sensitive

 -.test() & /~~~/                -checks if something is in something else.
  let testStr = "freeCodeCamp";   -string that has characters
  let testRegex = /Code/;           -character being serached for
   testRegex.test(testStr);       -Returns true if in or false if not;
     -tests the regex to the string

 -.match()                       -Extracts match from a string
  let ourStr = "Regular expressions"; -The string we made
  let ourRegex = /expressions/;       -Word being searched for
   ourStr.match(ourRegex);              -returns the search word
     -tests the string to the testRegex . does string have regex?

        Every sign can be applied to every character

 -/yes|no|maybe/             -OR | operator for mulitple searches
 -/~~~/i                     -i at end ignores case-sensitivity
 -/~~~/g                     -g for the same word multiple times
 -/~.~/                      -. variable character. /hu./ = "hut" & "hug"  
 -/~[xyz]~/                  -define group of characters you want to match         
    let bigStr = "big";
    let bagStr = "bag";
    let bugStr = "bug";
    let bogStr = "bog";
    let bgRegex = /b[aiu]g/; -[aiu] is what you search for between b & g
      bigStr.match(bgRegex); // Returns ["big"]
      bagStr.match(bgRegex); // Returns ["bag"]
      bugStr.match(bgRegex); // Returns ["bug"]
      bogStr.match(bgRegex); // Returns null
 -/~[a-e]~/                  -defines a range of characters. Inclusive.
 -/~[a-e2-5]~/               -combines different ranges together
 -/[^~~^~]/                   -^. Dont want to match. Negated
                             -Can also find start of a string     
 -/~+/                       -a characters that is repeated side-by-side
 -/~*/                       -* allows at character to not show up
    -let word = "gut"
     let regex = /go*/        -returns "g"

 -/~?~/                      -returns smallest possible match.
 -/~~$/                      -Searches end of strings
-/^~~/                       -Starts search at beginning of string
 -/\w/                       -Shorthand for the entire alphabet
 -/\W/                       -Same as /^\w/.
 -/\d/                       -Shorthand for [0-9]
 -/\D/                       -Same as /^\d/ 
 -/\s/                       -Searches for whitespace
 -/~{x,y}/                   -x-to-y times ~ appears in a string.
 -/{x,}/                     -X is the lowest repition searched for 
 -/{x}/                      -only if string has a character x times
 -/?/                        -checks if a character might exist.
 -/(?=~)/                    -positive lookahead. sees if ~ is there
 -/(?!~)/                    -negative lookahead. Sees if ~ is not there
              Neiter lookaheads match or return query
 -/~(abc|xyz)#/              -Can see if any words that begin with ~ and
  Example: /P(engu|umpk)in/   end with # have abc or xyz in them
 -/(~)\1/                    -Sees if ~ repeats and matches it.
 -.replace('x', 'y')         -replaces x with y
   Example:
    let wrongText = "The sky is silver.";
    let silverRegex = /silver/;
    wrongText.replace(silverRegex, "blue"); // Returns "The sky is blue.
-$n $o....                   -captures words that are searched for



:::::::::::::::::::::CREATE AN AUTOMATIC SLIDESHOW::::::::::::::::::::::
  //Create a slideshow. Needs a looping function. Make in HTML

  /*First, make a div that contains the slideshow itself, 
    then make separate divs that hold every single image
     Give them all the same class "mySlides" or anything*/

<div class="slideshow-container">

<div class="mySlides fade">
  <div class="numbertext">1 / 3</div>
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">2 / 3</div>
  <img src="img_snow_wide.jpg" style="width:100%">
  <div class="text">Caption Two</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">3 / 3</div>
  <img src="img_mountains_wide.jpg" style="width:100%">
  <div class="text">Caption Three</div>
</div>
    ///All divs have the same class. Can add a caption if you want

</div>
<br>

///You can add dots underneath slideshow using the following.
<div style="text-align:center">
  <span class="dot"></span> 
  <span class="dot"></span> 
  <span class="dot"></span> 
</div>

//Using script to create the JavaScript needed to make the slideshow
<script>
  //create variables that will be used in the function
  //set an index variable to zero to start 
var slideIndex = 0;
showSlides();

function showSlides() {
  var i;        //index variable
  var slides = document.getElementsByClassName("   ");
      /*this syntax retrives the images within the same document. 
        The images need the same class */
  var dots = document.getElementsByClassName("    ");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";}
    /* This is the looping function that tells the function showSlides
       to move onto the next index within the images array */
  slideIndex++;  //This causes the next image to actually show.

  if (slideIndex > slides.length) {slideIndex = 1}
      /*This tells the function showSlides to reset to the first image
            once the last image is shown */
    for (i = 0; i < dots.length: i++) {
      dots[i].className = dots[i].className.replace(" active", "");
 }
 slides[slideIndex-1].style.display = "block";
 dots[slideIndex-1].className += " active";
 setTimeout(showSlides, 2000); //change image every 2 seconds
}                            //1000 = 1 second

 </script> /

::::::::::::::::::::::::::::MATCH EMAILS::::::::::::::::::::::::::::::::::
/*This will make sure two emails are the same when in a form.
Have two different email inputs, with the latter one having an event
called onchange="~~". The ~~ will be the JavaScript function that sees
if both emails are the same. Make sure they have different ids*/

<input type = "email" name="email2" onchange="check()">

function check(){
  var email1 = document.getElementById('email_addr');
  var email2 = document.getElementById('email_repeat');
  if ( email1.value != email2.value ) {
    alert("The two emails must match.");
    return false;
  }
}

/*Call the function when on the submit button*/
<input type ='submit' value="Confirm Email" 
onclick ='return check();'
