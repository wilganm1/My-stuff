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
(a...b)  -range operator. inclusive
(a..<b)  -half-open range. excludes b


-Methods
 Methods are built-in functions using .methodName
  .isEmpty     -checks if a string is empty




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


Variables & Constants
 Variables hold data within names and are given a value. 
 Constants use let and variables use var.
 You can't change the variable type once declared, only the
 value if it's the same type
  Syntax:
      let variable_name = value_of_varialbe
      var fasl = eion
   -Declare multiple variables on the same line with , if same type
     var x = 1, y = 2, z = 3
 -You can access a varialbe within a string using:
            \(varaible)
      
-Type Annotations  
 Specify what type of data can be housed in the variable.
    Syntax:
        var variable_name: data_type
 
-Printing variables or data
 Use the print() function to print variables
    Syntax: 
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
   Syntax:
      let cat = "meow"; print(cat)    //prints 'meow'

Type Aliases
Define an alternative name for existing variable with typealias
   Syntax:
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
-------------------------------CONDITIONAL STATEMENTS---------------------------
 if, else statements. Controls flow of logic
       if something {
        //code to run }
       else {
        //code to run if if block doesn't }
  -Shorthand conditional operator.
         a : b ? c
     //if a is true, then b. If not, then c.
        

