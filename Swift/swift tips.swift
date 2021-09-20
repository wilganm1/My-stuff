Swift is a language used for Apple producs using MacOS software. Swift is a type-safe, 
meaning it prevents you from entering in wrong data values into variables.

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


Methods
 Methods are built-in functions using .methodName
  .isEmpty     -checks if a string is empty
  .append(x)    -adds x to end of it.

Strings.
 Strings allow you to write plain text that is picked up by the editor
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


-Booleans
 true
 false
 !true == false
 !false == true

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
   -Type Annotations  
     Specify what type of data can be housed in the variable.
            var variable_name: data_type
      
Comments
 Comments exclude text from being executed.
  -Single-line //~~
      // this is ignored
  -Multiline /* ~~ */
      /*   
        This is ignored
      */ 
Type Aliases
 Define an alternative name for existing variable with typealias
      typealias VarialbeName = 0
      var secondVarialbe = VarialbeName    //secondVariable now equals 0

Tuples
You can decompose a tuple’s contents into 
separate constants or variables, which you then access as usual:
  print("Whatever data \(here)")

Swift is zero-indexed like Python. Access a tuple's index 
using .n or [n]

  t = ("a","b")
  s = a.0    //s = "a"
  q = t[1]   //q = "b"
       
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

 -guard
   Guards require that a statement be true for the statment to execute.
             guard ~~~ else {}
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

-Nesed Functions. Functions inside bodies of other functions

------------------------------------CLOSURES------------------------------------
Self-contained blocks of code that can be used anywhere. Can capture and store
references to any variables from context in which they're defined'. 
  
    let closureName:(parameter types) -> (return type) = 
       {(parameter_name:parameter_type) -> (return type) in statements}

      -What's in between the {} is the closure expression'
      -closure type syntax is the (parameter_types) -> (return type)
      -closure expression is {(parameter name:parameter type) -> return type in}

-----------------------------------ENUMERATIONS-----------------------------------
Defines common type for a group of related values. Uses cases

         enum EnumerationName {
             case x
             case y}

   -Example: four points on a compass. Can also state multiple cases per line:
         enum CompassPoint {
             case north, south, east, west }
 You can access cases in enumerations as methods and assign them to variables
       var directionToHead = CompassPoint.west
   Once it's assigned to the enumeration you can change to a different case.
           directionToHead = .east
  
 -Matching enumerations with switch
          switch EnumerationName {
           case x:
               //code
           case y:
               //code
           default:}

 -Iterating over enumeration cases. CaseIterable
          enum enumName: CaseIterable{
           case x,y,z}
     -.allCases           -calls all cases of the enumeration

 -Additional values


------------------------------STURCTURES & CLASSES-------------------------------
General purpose blocks of code that can be used anywhere and between files.
     struct StructName {
         definition here }
     class ClassName {
         definition here }

 You call classes or structs by typing their name with () after.
      struct Resolution {
        var width = 0
        var height = 0 }
    class VideoMode {
        var resolution = Resolution()    //calling the struct
        var interlaced = false
        var frameRate = 0.0
        var name: String? }

   -Access properites using dot syntax.
           Resolution.width
   -Initialize properties
         let vga = Resolution(width: 640, height: 480)


-Subscripts. shortcuts for accessing member elements of list/sequence.
         subscript(index: Int) -> Int {
          get {
             return subscript here.}
          set(newValue) {
              setting action}}

-Class inheritance.
  One class (subclass) can inherit properites and values from another (superclass)
       class SomeSubclass: SomeSuperclass {}

    -Example:
        class Vehicle {
          var currentSpeed = 0.0
          var description: String {
              return "traveling at \(currentSpeed) miles per hour"  }
          func makeNoise() {}}

        class Bicycle: Vehicle {
          var hasBasket = false}
-Overriding
  Setting a subclass's' properties instead of the superclass.
          class Train: Vehicle {
             override func makeNoise() {
                print("Choo Choo")}}

 -Type Casting. Used for instances in classes
      -is     -checks whether instance is a certain subclass type
      -as

 -Extensions. Add new functionality to existing class, enum, etc.
                ex

----------------------------------------ERRORS------------------------------------------
Receiving and handling erros in Swift. Use throw to handle errors
 Can use enums to make errors easy to find and handle.
     enum SomeEnum: Error {
      case error1
        throw throwSomething
      case error2
      case error3}

 -Do-catch statements to handle errors.
    Errors need to have a patterN that can match a catch. 
    It's like a case in a switch statement.'

      do {
         try expression
           statements
       } catch pattern 1 {
           statements
       } catch pattern 2 where condition {
           statements
       } catch pattern 3, pattern 4 where condition {
           statements
       } catch {
           statements}
        
 -Cathcing errors in functions. Uses throws 
      func getErrors() throws -> String

---------------------------------------CONCURRENCY------------------------------------------
Asynchronous code = code that can be suspended and resumed later.
paralle code = multiple pieces of code runs simultaneously.







