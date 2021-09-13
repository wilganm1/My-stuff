Swift is a language used for Apple producs using MacOS software. Swift is a type-safe, meaning it prevents you from 
entering in wrong data values into variables.

------------------------------------BASICS-------------------------------------
Data types
 Int()        -integer. Whole number. (1)
 Float()      -number with decimal points. 32-bit (3.14)
  X.XXeY()      -scientific notation 
 Double()     -number with decimal points. 64-bit
 Bool()       -true or false
 String()     -plain text. Uses "" ("Hello World"). 
    """ for multiline strings """
 Character  -Single character string.  ("H")
 Optional   -can either hold a value or not hold a value
 Tuple      -group multiple values in single compound value 
   (a,b)

Operators 
 +    -adds values together
 -    -subtracts numbers. Can also make values negative.
 *    -multiplies numbers
 /    -divides numbers
 %    -remainder operator. Returns a whole number of what's left over 
  b % a    - reaminder of a going into b.
 =    -assignment operator
 ==   -"is equal to"
 !=   -"not equal to"
 >    -greater than
 <    -less than
 +=   -adds to a prexisting variable and saves it.
 &&   -logical AND operator. If one false all false.
 ||   -logical OR operator. If one true expression is true
 !    -logical NOT operator
 _    -wildcard. 
(a...b)  -range operator. inclusive
(a..<b)  -half-open range. excludes b


-Methods
 Methods are built-in functions using .methodName
  .isEmpty     -checks if a string is empty
  .append(x)    -adds x to end of it.

Strings.
 Strings allow you to write plain text that is picked up by the editor
   """ """     -multiline comments
   Use \ at end of line of string to exclude white space in value
      Indents ignore white spaces in """ """.
  -Special characters
     \0     -null character
     \\     -backlash
     \t     -horizontal tab
     \n     -line feed
     \r     -carriage return
     \u{n}  -Unicode scalar value
  You can initialize an empty string in two ways.
        var emptyString = ""
        var emptyString = String()
  Concatenate strings using + or +=
      var variableString = "Horse"
      varableString += " and carriage"

   -Use count to get a count of characters in a string
      var word = "cafe"
      print("the number of characters in \(word) is \(word.count)")

 -Modifying strings
     .insert(_:at:x)    -inserts _ at index-x
     .remove(_:at:x)    -removes _ at index-x
     .removeSubrange(_) -removes range of         
     .hasPrefix(_)       -checks if a string starts with _. Like .startswith() in Python.
     .hasSuffix(_)       -checks if a string ends with _


Variables & Constants
 Variables hold data within names and are given a value. 
 Constants use let and variables use var.
 You can't change the variable type once declared, only the
 value if it's the same type.

      let variable_name = value_of_varialbe
      var fasl = eion

   -Declare multiple variables on the same line with , if same type
     var x = 1, y = 2, z = 3
 -You can access a varialbe within a string using:
            \(varaible)
      
Type Annotations  
 Specify what type of data can be housed in the variable.
        var variable_name: data_type
 
Printing variables or data
 Use the print() function to print variables
      print(variable)
      print("String")      -prints String
      print(1)             -prints 1
      
Comments
 Comments exclude text from being executed.
  -Single-line //~~
      // this is ignored
  -Multiline /* ~~ */
      /*   
        This is ignored
      */ 
      
Semicolons ;
 Semicolons are used to write separate statements
 on a single line.
      let cat = "meow"; print(cat)    //prints 'meow'

Type Aliases
 Define an alternative name for existing variable with typealias
      typealias VarialbeName = 0
      var secondVarialbe = VarialbeName    //secondVariable now equals 0

-Booleans
 true
 false
 !true == false
 !false == true

Tuples
You can decompose a tuple’s contents into 
separate constants or variables, which you then access as usual:
  print("Whatever data \(here)")

 Swift is zero-indexed like Python. Access a tuple's index 
   using .n

  t = (a,b)
  s = a.0
            
------------------------------COLLECTION TYPES--------------------------------
-Arrays. store values of the same type in an ordered list.
     var array: [Element] = []
     var array = [value1, value2]
  Set default values 
        threeDoubles = Array(repeating: x, count: y)

-Sets. stores distinct values of same type with no defined order.
     Sets must be hashable (int object same for all objects)
             var set = Set<Characters>()
     .intersection(_)         -create new set with common values
     .symmetricDifference(_)  -excludes shared values
     .union(_)                -includes all values
     .subtracting(_)          -values not specified
  
            
-Dictionaries.
 Allow you to store data in a sequence in key-value pairs.
     let dictionary = ["key1": "value1", "key2": "value2"]
 Dictionaries are unordered
-----------------------------CONDITIONAL STATEMENTS---------------------------
 if, else statements. Controls flow of logic
       if something {
        //code to run 
       } else if {
        //code to run if irst is wrong
       } else {
        //code to run if if block doesn't 
       }
  -Shorthand conditional operator.
         a : b ? c
     //if a is true, then b. If not, then c.
Switch. Uses cases instead of if, else. If value of case matches switch, case runs
    switch value {
    case value1:
        respond to value 1
    case value 2,
         value 3:
        responds to value 2 or 3
     default:
        runs if nothing matches}
 -You can use tuples in switches and use underscore as a case and a where.
   Can also declare variables within cases, and use compound cases
        switch (x,y) {
         case (_,y) where y == z:
             whatever
         case let (a,b) where c == d:
             whatever
         case "a", "b", "c":
             whatever
             fallthrough
         default:
              whatever} 
  -fallthrough
      keeps a switch going even after a case is met
-----------------------------------LOOPS--------------------------------------
For-in loops. Iterate over a sequence. Exaclty like for loops in Python
        var sequence = [1,2,3,4]
        for seq in sequences {
         //code to run}
   -Loop through ranges
         for index in 1...5 {
              print("\(index) times 5 is \(index * 5)")}

 You can loop through dictionaries with (key, value) 
        let dictionary = ["key1": "value1", "key2": "value2"]
        for (keys, values) in dictionary {
         print("\(keys), ~~ \(values)~~"}
  You can set the how numbers are looped by with stride(from:to:by:)
        let minuteInterval = 5
        let minutes = 60
        for tickMark in stride(from: 0, to: minutes, by: minuteInterval) {
           // render the tick mark every 5 minutes (0, 5, 10, 15 ... 45, 50, 55)}
   -Add in through: to have it stride up to max range.
 
While loops
 Performs statement until a condition becomes false.
         while condition {
          statements}
 -repeat-while loop. Loops once to check condition. Then loops until false.
         repeat {
          statements 
         } while condition}
        }}
 -Labeled statements. Name a loop to make it stand out
        label name: while condition {
           statements }

----------------------------------FUNCTIONS-----------------------------------
Have a type depending on parameter type and return type.
       func name(parameter: parameterType) -> returnType{
          return code}
 You must give arguments labels when you call them if they are defined.

 -Omit argument labels with _ for a parameter
       func ion(_){}

 The return type is the overall data type the function gives back.
 You do not need a return type.

-Call functions by typing the name and parameter(s) of the function
            print(name(parameter: "whatever")) 

-Variadic parameters. Accept zero or more values of a specific type  
 Uses ... after parameter type's name.
        func adslf(numbers: Double...) ->

-In-out parameters. Can change the parameter's value within the function.
     func fad(_ a: inout Int, _ b: inout Int) {
    let temporaryA = a
    a = b
    b = temporaryA}


 
        
        
