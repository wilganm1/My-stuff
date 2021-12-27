-------------------------------------BASICS----------------------------------------------
Java is a general-purpose object-oriented programming language.

To run the java program you need the following code:

            public class Main {

              public static void main(String[] args) { 
                code in here
              }
            }

Printing things to console window:
  System.out.println(~~~);


// write single-line comments
/*
write multiline comments
*/


Data types
 int      //whole number 
 double   //decimal number. End variable with d
 char     //single-letter text. Uses ''
 boolean  //true or false value
 String   //Multi-character text. Uses ""
 
Operators
 ;    -Ends every statement like in C++.
 +    -addition
 -    -subtraction
 *    -multiplication
 /    -division
 %    -modulus. Returns remainder after division
 ++   -Increment. Increases value by 1. // ++x
 --   -Decrement. Decreases value by 1. // --x
 =    -Assignment operator. Creates variables.
 ==   -Compares two pieces of data. Returns true or false.
 !=   -"Not equal to". checks if things are not equal.
 >    -greater than.
 <    -less than
 >=   -greater than or equal to
 <=   -less than or equal to
 +=   -addition assignment
 -=   -subraction assignment
 *=   -multiplication assignment
 /=   -division assignment
 &&   -logical AND. 
 ||   -logical OR
 !    -logical NOT. changes boolean status.

Variables
    data_type identifier = value;

  You can declare variables without assigning them.
       int myVar;
       myVar = 15;
  
  -Final. Use the keyword final to make a variable immutable.
        final data_type identifier = value;
        final int myVar = 15;

Type Casing
  Converting a variable of one data type to another.
  
    -Widening casting. Automatic upon assignment.
        int myInt = 9;
        double myDouble = myInt;  //Automatic casintg: int to double

    -Narrowing casting. Manually converting with (type)
        double myDouble = 9.87d;
        int myInt = (int) myDouble; // converts double to int

Strings. 
  Strings use "" when typing. There are many methods dealing with strings.   
          String txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  txt.length().       // prints length of text variable
     .toUpperCase()   // Makes every letter upper-case
     .toLowerCase()   // makes every letter lower-case
     .indexof("~")    // finds first position of ~.
     .concat(y);      // concatenates txt with y.

  -Concatenate strings with +

  -Escape characters. If using quotes inside strings use \' or \".
      String txt = "We are the so-called \"Vikings\" from the north.";

   Adding a number and string will turn the number into a string.;

Math. Built-in class that has math functions
  .max(x,y)   //finds biggest value of x and y
  .min(x,y)
  .sqrt(x)    //Square root.
  .abs(x)     //Absolute value.
  .random()   //returns number between 0.0 and 1.0
  .exp(x)     //value of e^x
  
  
Arrays. Store multiple values in a single variable. Use [] after variable type.
  Arrays values must be only one type. Create them with {}.
  
       data_type[] arrayName = {element 1, element 2, element 3}
 
 To access values use arrayName[x] indexing. 0-indexed like Python.
 You can change any element by reassigning it.
   
                arrayName[x] = new_value
                
 -Two-dimensional arrays. 
                int[][] arraysName = { {1,2,3}, {7,8,9} };
                arraysName[1][2] // 9

------------------------------------CONDITIONALS-----------------------------------------
These control the flow of logic in the program depending if the condition is true or 
false.

-If/else/else if.
  Control what happends depending on circumstances of conditions.
  
        if (condition1) {
          // code to run if condition1 is true
        }
        else if (condition2) {
          // code to run to condition1 is false and condition2 is true
        }
        else {
          // code to run if all conditions are false.
        }
    -Ternary Operator. Shorthand for simple if/else statements
        variable = (condition) ? expressionTrue : expressionFalse;

-Switch statements.
  Basically more concise if/else statements. If the expression matches any cases
  then the code for that case is executed. Like saying if (condition == x) but shorter.
      
      switch(expression) {
        case x:
          // code to run if expression == x
          break;  // stops the switch block from running 
        case y:
          // code to run if expression == y
        default:
          //code to run if expression does not match anything  
      }

-While loops
  A block of code that will continuously run as long as a condition is met.
  Make sure that it is not an infinite loop.
  
              while (condition) {
                // code to run
              }


 -Do/While loop
  Executes the loop once, then checks if the condition is true before running loop.
    
              do {
                // code block to be executed
              }
              while (condition);
              
-For loop. Loops a certain number of times with certain statements.
  
              for (statement 1; statement 2; statement 3;) {
                // code to run
              }

        -Example:
              for (int i = 0; i <= 10; i = i = 2) {;}
  
  -For-each loop. Exclusively for arrays.
          for (int i = 0; i < arrayName.length; ++i){}
            for (data_type variable: arrayName) {;}

   -Mult-array Loop. Put a loop inside another loop.
        int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };
        for (int i = 0; i < myNumbers.length; ++i) {
          for(int j = 0; j < myNumbers[i].length; ++j) {;}}

 -Break keyword.
   Stops the loop at the current iteration.
          int i = 0;
            while (i < 10) {
              System.out.println(i);
              i++;
              if (i == 4) {
                break;}}.  //stops the loop

 -Continue keyword.
   breaks one iteration of a loop if a condition occurs and goes to next iteration.
     
        for (int i = 0; i < 10; i++) {
          if (i == 4) {
            continue;}
          System.out.println(i);};

---------------------------------------METHODS--------------------------------------------
A reusable block of code that only runs when called. Can pass parameters into it.;
They must be declared within a class. Like a function in Python.;

            public class Main {
              static void myMethod(data_type x) { //static means it belongs to class itself
                // code to be executed
              }} // void means that method does not return anything.

   -You run the function when you call it.




