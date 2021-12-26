Run scala on browser here:
https://scalafiddle.io
----------------------------------BASICS-------------------------------------
Data Types
 byte       - -128 to 127
 boolean    - true or false
 Char       - single-letter text. Uses ''
 String     - Normal text. Uses ""
 Short      
 Int        - Whole numbers.
 Long       - Really big numbers
 Float      - Decimal numbers
 Double.    - Big decimal numbers
 
Write comments with //. Multiline with /* */

print to command line with println(~~~)
  
- s-string. Print variables within strings. Like f-strings in Python.
  Declare variables, then precede string with s and use $ for variables
 val x = "John"
 val y = 'C'
 val z = "Doe"
          println(s"Name: $x $y $z") // "Name: John C Doe"
 Or use 

Variables. Assign data names.
  Two types of variables, mutable - var - and immutable - val.
      
      val identifier: data_type = data. // immutable. Cannot be changed
      var identifier: data_type = data. // mutable. Can be changed.
      
 The data_type is not requried and can be inferred but best if explicitly 
 stated
  val x = 1

-Lists
  val ints = List(1,2,3,4,5)


-Blocks. Uses {}
  println({val x = 1 + 1
  x +1})
 
----------------------------FUNCTIONS & METHODS-------------------------------
-Functions. 
  Expressions that have parameters and take arguments. 
  To run a function call it with parameters during the call.

         (parameter1: data_type, parameter2: data_type) => // code

 You can name functions.
       val name = (identifier: data_type) => // code
       
-Methods. 
  Like functions but with def, a return_type, and a body
  
     def name(parameter1: data_type): return_data_type = //body

  Methods can also take multiple parameter lists.
    def name(parameter1: Int, parameter2: Int)(parameter3: Int): Int //code

----------------------------CONTROL STRUCTURES-------------------------------
These are things that control the flow of logic of the program.

-if/else. Conditional that does something if an expression matches.

           if expression1 then  //if expression1 is a match
              //code to run
           else if expression2 then
              //code to run
           else               //runs if nothing else matches
              //code to run

-For loop.
 Runs a loop based on generators. Generators are usually written as i <- data.
 
            for i <- data do //code
   Example:        
    val ints = List(1,2,3,4,5)
    
    for i <- ints do println(i)
    //prints 1,2,3,4,5
    
-Guards. if expressions in a for loop
  for
    i <- ints
    if i > 2.  //guard
  do
    println(i)

