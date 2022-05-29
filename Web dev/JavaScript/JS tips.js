--------------------------------Basics--------------------------------
 **Code typed in camelCase. Every word after first is capitalized**

To use JavaScript code in an HTML file it needs to be within
    <script>
     ~~~~~~~~~~~~
    </script>/

Statements. Statements are lines of code that are read.
They must end with a semicolon.;

Syntax:
;           -ends a statement
//          -single-line comments
/**/        -multi-line comments
()          -specify parameters or conditions
{}          -code block for closed off code

Data types:
"String"			-read as words. Requires "" or ''
Numeric			-number values
Boolean   		-whether something is true or not.
objects      -like dictionaries in Python

typeof        -returns what type of data a piece of code is

Type converstion:
Number(x)      -converts x to a number
  Number(false)  -returns 0;
  Number(true)   -returns 1;
String(x)      -turns x into a string
 x.toString()  

Arithmatic operators:
 +       -Adds two variables
 -       -Subtracts
 /       -Divides variables
 *       -multiplies
 >=	 -Greater than or equal too
 <=	 -Less than or equal
 !=	 -not equal to
 ==      -Is equal to. Causes coercion. Makes strings numbers
 ===	 -Is equal to. Does not cause coercion
 !       -Is not.
 %	 -Remainder Whats left over after one number goes into 
	   another number fully. Example: 7 % 3 = 1.
           3 goes into 7 two times with a left-over of 1.
 +=	 -Adds values to a variable
 ++	 -Increases value of variable by 1
 --	 -Decreases value of variable by 1 
 &&      -logical AND operator 
 ||      -logical OR operator
 
  Add a comment with //.   //This is ignored by machine

console.log();         -Prints data onto console
document.write()       -writes characters onto document
.getElementById("~~")   -can grab an HTML element by its Id name

console.log('Go Fu ' + 'ck Yourself');
--> Go Fuck Yourself

-Numbers
 Nan         -not a number. 
 Infinity    -infinity value

--------------------------------Variables--------------------------------
Variables allow us to save any data to a name to access later

Use words var, let, and const 

 var variableName = whatever    //assings whatever to variable
     var myName = "Mitch"       //Sets a variable.
     console.log(myName);
       --> "Mitch"                 //prints out myName variable

  You can redeclare a variable assigned using var
  Chaning variables using var changes it in all scopes
     var x = 10;           //here it's 10
     {var x = 2;}          //here x is 2
     console.log(x)         //prints 2

 let variableName = whatever    //stops from redeclaring varable
    let meal = 'pizza'            //unless use let again
      --> 'pizza'
    let meal = 'fries'
      --> 'fries'
    Using let prevents variables chaning across scopes
    Cannot redeclare variables within the same block using let

 const variableName = whatever  //A variable that cant be changed.
    Object.freeze(myName)         //prevents myName from being altered

String interpolation using template literals.
Can be used to log strings together with a const variable
  Set a const, then use `__${variable}`****
    Example:
      const myPet = 'Dragon';
      console.log(`I own a pet ${myPet}.`)
        --> 'I own a pet Dragon'

--------------------------------Arrays--------------------------------
Arrays are created using []. They are used to make lists like in Python.
Lists are ordered by index starting at 0.
   const variable = [0,1,2,3,4,5,6,7,8]   //9 numbers 

Example:
    let list = ['A','B','C','E'];  //indicies are 0,1,2,3
    list[1] --> 'B';    

Array methods:
.shift()        -removes first element
.unshift(x)     -inserts x to front of array
.push(x)        -adds x to end of array 
.pop()          -removes last element of array

Can change a list by chaning, adding, or removing elements.
    list[3] = 'D';
     --> ['A','B','C','D'];   //changes 'E' to 'D';
   -.push()            -adds items to the end of array.
  list.push('F','G');
   -->['A','B','C','D','F','G']
   -.pop()             -Removes last item in an array.
                   -logging the pop only returns what was removed.;
 -.splice(index,n,x)  -removes index positions. n= # to delete. X adds in
 -.slice(i1, i2)      -copies data to new array. starts at i1, ends at i2+1

Nested Arrays.         -Have a list inside a bigger list.
const nestedArr = [[x], [y,z]];  -Nested array. Can have separate
  nestedArr[1] --> [y, z]     arrays that take up an index space
  nestedArr[1][0] --> y       You need an array index for every nested array

Spread operator [...~~~]      -Copies an entire array
  Example:
    const arr12 = [316, 420];
    const arr2 = [...arr12]
  console.log(arr2) --> ['316, 420'];


-------------------------------Methods------------------------------------
Methods are built-in fucntions. Use by adding a . after a variable/instance

Format:   methodName(argument) {
	property(argument)}

	addNew(new) {this._new.push(new)}
	
Example:
	console.log('hello'.toUpperCase());  -Uppcase every letter
		--> 'HELLO'

 .toUpperCase()      -Uppercases all letters
 .toLowerCase()      -lowercases all letters
 .random() 		   	   -generates random number.
 .length()		   	   -How long a list/array is.
 .indexOf("")        -find the index of a variable or string
 .replace(X, Y)      -replaces X with Y
 .pop()              -removes last position of an array
 .splice(index,n,x)  -removes index positions. n= # to delete. X adds in
 .slice(i1, i2)      -returns a new array. starts at i1, ends at i2-1
 .substr(x,n)        -returns new array from x, n is length extracted part.
 .map()              -makes new array for every array element of function
 .sort(desc())       -sorts array ascending or descending. asc is default

---------------------------------DATE-------------------------------------
How to get the date.;

 var d = new Date();  //can add in "month day, year hour:min:sec:millisec"
  .getDay()           -gets day of date (0 to 6)
  .getFullYear()      -gets full year
  .getMonth()         -gets current month.
  .getHours()         -gets current hours of date
  .getMilliseconds(); -returns millisecond

-------------------------CONDITIONAL STATEMENTS--------------------------
Checks a specific condition & performs a task based on condition

If, else if, else statements 		//if something happens, do something.

	if(condition) {code to run};    //prints out the code if true               
	 else if (condition){code to run};	//runs if this condition true   
	 else {code to run;}  //runs if all else fails

	  -If the if or else if condition = true, the code runs   
	  -If the first if condition = false, the else if code runs.       
     - If else if = false, the else runs.                  
       - Stops when any condition = true;                        

    Example:  let hunger = 7
    		  if(hunger > 7) {console.log('Time to eat!')}
    		   else {console.log('We can eat later!')};
    		      //'We can eat later!'

Operators.  Can add additional conditions
 &&	-This AND that are true
 ||	-This is true OR that is true
 !	-NOT.
 !=     -not equal to.
 
    Example:  let day = 'Saturday';
    			if(day === 'Saturday' || day === 'Sunday'){
    			console.log('Enjoy the weekend!');
    			} else {console.log('Do some work.');}
    		   --> Enjoy the weekend;

    		  let excited = true;
    		  console.log(!excited);
    		   --> false

-break statement. Use to jump out of a loop;
  for (let i = 0; i < 10; i++) {
    if (i === 3) { break; }
    text += "The number is " + i + "<br>";}
      //prints out numbers 0 to 2

continue statement.;     breaks current iteration of loop. Like C++;
  for (let i = 0; i < 10; i++) {
    if (i === 3) { continue; }
    text += "The number is " + i + "<br>";} 
        //will not print out "The number is 3"

Ternary operator ? Acts as a shorthand for if else.
	 Format:  var ? if true code : else false code
      Example:
        let PMarks = 40  
        let result = (PMarks > 39)?  
            console.log("Pass":"Fail");   //this will print fail.

Switch statements. Acts like a big if else statment with cases. There is a 
condition that is checked for.;
  switch(condition){
    case x:              //if condition == x this will run
      //code to run;
      break;
    case y:              //
      //code to run;
      break;
    default:           //if nothing meets condition this runs.
      //code to run}

--------------------------------FUNCTIONS--------------------------------
Functions are blocks of code we create to do stuff. They can have certain
parameters that are passed called arguments. Whatever you pass into the
parameters will be used

Syntax:
  function functionName(parameter1, parameter2) {
    return whatever }    //return stops the function
	  
You run a function by calling it or assigning it to a variable

  Example:
    function myFunction(a,b){
      return a + b}

    let x = myFunction(4,3);
    console.log(x)    //prints out 4 + 3


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

-Return call
Use return to call the function;
    function x(y,z) {const area = y * z;
    return area;}
     --> returns the area of y and z;

//ES6 syntax
Use let = () => {return } to shortcut function command;

Use const = xyz;
  xyz(() => {}); to shortcut function command;
  parameters inside the ( ) and then add an arrow => that points to the 
  function body surrounded in { } like this:;
    const rectangleArea = (width, height) => {
     let area = width * height;
        return area;};

--------------------------------LOOPS--------------------------------
Loops repeat a command over and over under conditions

-For loops             //iterate through a condition until told to stop
    for (initialization; stopping condition; iteration statement){
      //code block to be run;}

     Example:
        var = i;
        for(i = 0; i < x; i++){          //x can be anything
          console.log(i)}
      As each loop passes, i gets bigger by 1 until x is reached.

          i++ can also be written as i = i + 1;
   
      Example:
      	for (let counter = 0; counter < 4; counter++) {
      		console.log(counter);}
      	-->0
      	   1
      	   2
      	   3

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

-For..in         -will execute a given block of code 
    for (variable in object){
      code to be executed;}
      Example:                 for each property in an object. 
        let x = [1,3,5,6,7];
        for (number in x) {x + 1;}



-while loops. A loop that always runs until told to stop
  let counterTwo = 1;
  while (counterTwo < 4) {
    console.log(counterTwo);
    counterTwo++;   //increments counterTwo

Iteration methods  - methods to perform loops 
 - .forEach()			 - Loops every element in an array.;
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


--------------------------------ERRORS--------------------------------
Errors are when things go wrong. You can manually try for them.;
    try      -test a block of code for errors;
    catch    -lets you handle erros that are found in try block.;
    throw    -create custom errors.;
    finally  -executes some code regardless of result;

    try {Block of code to try};
    catch(err) {block of code to handle errors;}
    throw "message";    //can be text or a number

Can add throw in with if statements.;
    try {
      if (x == "") throw "empty";}

JavaScript creates an Error object with a name and message
 To print out either just type it as a method:
   err.name;     //prints out error type
   err.message;   //prints out preset error message

   -EvalError       -eval() function
   -RangeError      -use number outside range of legal values
   -ReferenceError  -used a referenced variable that is not declared yet
   -SyntaxError     -syntax error in code
   -TypeError       -value outside range of expected types
   -URIError        -illegal characters in URI function.;

--------------------------------OBJECTS--------------------------------
Objects are containers storing related data and functionality.
Use  {} to create an object literal. Has a value for a key.
Like a dictionary in Python.;

		let obj = {key1: 'value1', 
               key2: 'value2', ....};

-Access an objects value by using obj.key or obj['propertyName']
    Example:
     let spaceship = {
      homePlanet: 'Earth',
      color: 'silver'};
    spaceship.homePlanet; // Returns 'Earth',
    spaceship.color; // Returns 'silver',

   	let spaceship = {
      'Fuel Type': 'Turbo Fuel',
      'Active Duty': true,
      homePlanet: 'Earth',
      numCrew: 5};
     spaceship['Active Duty'];   // Returns true
     spaceship['Fuel Type'];   // Returns 'Turbo Fuel'
     spaceship.numCrew;   // Returns 5
     spaceship['!!'];   // Returns undefined 

-this keyword.            -refers to owner object.;
  const person = {
  firstName: "John",
  lastName : "Doe",
  fullName : function() {
    return this.firstName + " " + this.lastName;}};
        //this.firstName refers to the firstName key of person object

-new keyword. Assign variable as an object
 
   delete operator to delete a value from an object
   delete spaceship.mission
   delete spaceship['Secret Mission']

 -Nested objects.
   Use dot notation like so:
   		variable.object1.subobject['String']
  Arrays look like this:
  	passengers : [{name: 'Space Dog'}],


 -By Reference
  -When changing a value that is part of an object, its positioning
  stays the same but the value Changes
    Example;
     const spaceship = {
       homePlanet : 'Earth',
       color : 'silver'
     };let paintIt = obj => {			-/*function*/
       obj.color = 'glorious gold'
     };paintIt(spaceship);
     spaceship.color // Returns 'glorious gold' 

     - in property          -checks if an object has a specific property
        'Alan' in user;
          //returns true

 -Constructors         -create new objects called instances. Capitalized
      function Dog(){
         this.name = "Albert"}  //Dog.name = "Albert"
 //  You can set a new variable equal to a new object using the new element
        let hound = new Dog(); 
      //   hound now has all the properites of Dog 
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

--------------------------------EVENTS--------------------------------
Events are things that happend to HTML elements when something happens
   -page finished loading
   -input field changed
   -button was clicked
Events are pieces of JavaScript code that change HTML

Syntax:
  <element event="some JavaScript">

You can also use functions as events.
    <button onclick="functionName()">HTML text</button>/

Common HTML events:
  onchange      An HTML element has been changed
  onclick       Click an HTML element
  onmousedown   Hold down the mouse click
  onmouseover   Move the mouse over an HTML element
  onmouseout    Move the mouse away from an HTML element
  onkeydown     The user pushes a keyboard key
  onload        The browser has finished loading the page
  onsubmit      When a submit button is pressed
  onfocus       Input field is foucsed/clicked on

--------------------------------CLASSES--------------------------------
Classes are templates for objects

Syntax:
 	class ClassName {
 		constructor(value1, value2) {  //parameters like in functions
 			this.property1 = value1;        //the x value of ClassName is property1
 			this.property2 = value2;
      method(parameter){};}}

  You use classes to create objects using the new keyword. Called instances.;
  Pass in parameters to create new properties for the class values
    let variable = new ClassName("1", 2) /*Creates a new Class instance*/
        variable.property1 = "1"
        variable.property2 = 2

  Add methods for greater specificity and control.;
      age(z){
        return z - this.property1;}

-Inheritance. Can make subclasses that take properties and methods 
 from their parent.; Use extends keyword. Use the parent property 
 with super keyword;

 Syntax: 
  class ParentClass {            //Parent class
    constructor(parentProperty){
      this.value1 = property;}}

  class ChildClass extends ParentClass{  //subclass
    constructor(parentProperty, childProperty){
      super(parentProperty);
      this.value2 = subclassProperty;}}

 -static methods: methods that any object can call
 	static methodName() {
    const names = ['Angel', 'Spike', 'Buffy', 'Willow', 'Tara'];
    const randomNumber = Math.floor(Math.random()*5);
    return names[randomNumber];} 

    myVar = new

--------------------------------MODULES--------------------------------
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
 
--------------------------------PROMISES--------------------------------
Promises are objects that represent the eventual outcome on an
 asynchronous operation. They will or won't do it'. Declare a constant, 
 then use new to create a promise.;

Syntax:
  const myPromise = new Promise((resolve, reject) => {});   

3 types of promises:
 -Pending     -operation has not completed yet. Default state
 -Fulfilled   -operation has completed and promise is resolved
 -Rejected    -Opertion has failed and promise has a reason for failure
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

 promise.then((resolvedValue) => {
     console.log(resolvedValue);
   })

 promise.catch((rejectionReason) => {
     console.log(rejectionReason);
   });

------------------------JAVASCRIPT OBJECT NOTATION-----------------------
JSON is a format of storing and transporting data to external sources.
Since JSON is just text it can be parsed into objects or parsed from objects
into text. All words have quotes around them
   -parse()       -Parses JSON string into a JavaScript object
       var myObj = JSON.parse(myJSON);
   -stringify()   -Converts a JavaScript object into a JSON string
       var myJSON = JSON.stringify(myObj);

Vaules cannot be: function, date, undefined

You can also add a function to parsed objects.;
  const text = '{"name":"John", "birth":"1986-12-14", "city":"New York"}';
  const obj = JSON.parse(text, function (key, value) { //add function word
    if (key == "birth") {
      return new Date(value);        
    } else {
      return value;}});

---------------------------REGULAR EXPRESSIONS---------------------------
Regular expressions, also called "regex" help find specific characters in 
a string. Works like Contorl + F but shorthand. Case-sensitive;

~ will be used to represent any & all non-important text;

Syntax:
  /pattern/modifiers;

Methods:
 .search(text)            -searches for match and returns starting index.;
    let text = "Visit W3Schools!";
    let n = text.search(/w3schools/i);
          //returns 6

 .replace(text, replacement)       -replaces text with replacement
    let text = "Visit Microsoft!";
    let result = text.replace(/microsoft/i, "W3Schools");   
          //Visit W3Schools        

 .test(text)                  -checks if something is in something else;
    let testStr = "freeCodeCamp";    -string that has characters
    let testRegex = /Code/;           -character being serached for
     testRegex.test(testStr);       -Returns true if in or false if not;
       -tests the regex to the string

 .match()            -Extracts match from a string
   let ourStr = "Regular expressions"; -The string we made
   let ourRegex = /expressions/;       -Word being searched for
    ourStr.match(ourRegex);              -returns the search word
      -tests the string to the testRegex . does string have regex?

Modifiers:
 /~~~/i                -i at end ignores case-sensitivity;
 /~~~/g                -g for the same word multiple times;
 /~~~/m                -multiline matching;
 /~.~/                 -wild-card variable. /hu./ = "hut" & "hug";
 /yes|no|maybe/        -OR | operator for mulitple searches;
 /~[xyz]~/             -define group of characters to match;         
 /~[a-e]~/                  -defines a range of characters. Inclusive.;
 /~[a-e2-5]~/               -combines different ranges together;
 /[^~~^~]/                  -^. Dont want to match. Negated;
                            -Can also find start of a string     
 -/~+/                      -a characters that is repeated side-by-side
 -/~*/                      -* allows at character to not show up
    -let word = "gut"
     let regex = /go*/        -returns "g";
 /~?~/                      -returns smallest possible match.;
 /~~$/                      -Searches end of strings;
 /^~~/                       -Starts search at beginning of string;
 /\w/                       -Shorthand for the entire alphabet;
 /\W/                       -Same as /^\w/.;
 /\d/                       -Shorthand for [0-9];
 /\D/                       -Same as /^\d/;
 /\s/                       -Searches for whitespace;
 /~{x,y}/                   -x-to-y times ~ appears in a string.;
 /{x,}/                     -X is the lowest repition searched for;
 /{x}/                      -only if string has a character x times;
 /?/                        -checks if a character might exist.;
 /(?=~)/                    -positive lookahead. sees if ~ is there;
 /(?!~)/                    -negative lookahead. Sees if ~ is not there;
              Neiter lookaheads match or return query;
 -/~(abc|xyz)#/              -Can see if any words that begin with ~ and
  Example: /P(engu|umpk)in/   end with # have abc or xyz in them
 -/(~)\1/                    -Sees if ~ repeats and matches it.
 -.replace('x', 'y')         -replaces x with y
   Example:
    let wrongText = "The sky is silver.";
    let silverRegex = /silver/;
    wrongText.replace(silverRegex, "blue"); // Returns "The sky is blue.
-$n $o....                   -captures words that are searched for

-----------------------DOCUMENT OBJECT MODEL---------------------------
The DOM is a model of the webpage that separates elements in a tree.;

                             Document
                                |
                           Root Element:
                              <html>
        ________________________|_____________________
        |                                            |
     Element:                                     Element:
      <head>                                       <body>
        |                                      ______|______     
     Element:                                  |           |
     <title>              Attribute:________Element:    Element:        
        |                   "href"            <a>        <h1>
      Text:                                    |           |
    "My title"                               Text:       Text:
                                           "My link"  "My header"

With the DOM JavaScript can dynamically change HTML elements
DOM methods are actions to perform on HTML elements;
DOM properties are values of HTML elements that you can change;

Finding HTML Elements;
 document.getElementBy{}  //element is plural if not Id
  -Id("")              -singular element of specific Id;
  -ClassName("")       -All elements with a specific class;
  -TagName("")         -All tags like <div> or <img>

Changing HTML Elements;
 .innerHTML = "new HTML";   //changes what the html tag shows
  element                      
  .{attribute} = new value      -change attribute of HTML element
  .style.{property} = new style  -change CSS style of HTML element
  .setAttribute(attribute,value) -change attribute value
  .addEventListener("event", property)  -adds event;
  .removeEventListener()

Adding & Deleting Elements;
 document              -calls the document 
  .createElement("tag")     -creates HTML element;
  .removeChild(element)     -removes HTML element
  .createTextNode('text')   -creates node with text;
  .appendChild(element)     -Add an HTML element
  .replaceChild(new, old)   -replace element;
  .write(text)              -Adds a new div where <script> is with text;
  .getElementById('p1').remove()          

Adding event handlers in code;
   element.addEventListener(event, function(), useCapture, param1);
 This is a shortcut to adding an event. You don't need' to write a 
 function out if you include an action as a parameter;
                           OR
  document.getElementById("").event = ('function(){code}');

  https://www.w3schools.com/jsref/dom_obj_event.asp 

  Or you can make a function then call it in the event;
     <script>
       function myFunction(){code to execute;}</script>/
           <tag onlick = myFunction()>

 You can assign a varialbe to finding elements then change HTML.;
    const element = document.getElementsByTagName("");
      element.innerHTML = ''      //changes the html elements


Event Bubbling & Event Capturing
 What is the order of events? If you have a <p> inside a <div> and 
 you do a "click" event which element is affected first?
       This uses the useCapture argument in addEventListener

-bubbling. Inner-to-outer event handling. useCapture = false. default
       <div onclick=>          //second
         <p onclick=></p>/     //first
       </div>/

-capturing. Outer-to-inner handling.  useCapture = true
       <div onclick=>     //first
         <p onclick =></p>/   //second
       </div>/

Accessing Nodes of the DOM tree.;
 Each element is a node, and they can have children nodes;
    .firstChild.nodeValue      -get value of a particular node
    .childNodes[0].nodeValue;  

 Access full document
  document.body;             -show all of <body> of page
  document.documentElement

 .nodeName property         -returns the tag name of the node;
 .nodeValue property        -

HTML Collection Objects. Return a list of tags or classes;
 When you call getElementsByTagName() it returns an HTMLCollection 
 object which is an array of HTML elements.;
    <div>
      <p id ="p1"></p>/
      <p id ="p2"></p>/
    </div>/

  const myCollection = document.getElementsByTagName("p");
 -This returns an array with 2 elements in it.;
    .length         -returns length of myCollection;
