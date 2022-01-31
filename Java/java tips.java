--------------------------------------BASICS-----------------------------------------------
Java is a general-purpose object-oriented programming language.;

Packages. Importing classes and functions that do stuff.;

import package.name.Class ;   //import a single class of the package
import package.name.*   ;     //imports whole package

import java.time.* ;     //dates and times
                   
To run the java program you need the following code:

            public class Main {

              public static void main(String[] args) { 
                code in here
                }}

Printing things to console window:
  System.out.println("~~~");

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

Variables. Assign data to names to be referenced later.
      data_type identifier = value;

      int myAge = 26;

  You can declare variables without assigning them.
       int myVar;
       myVar = 15;
  
  -Final. Use the keyword final to make a variable immutable.
        final data_type identifier = value;
        final int myVar = 15;

 -Scope. Variables assigned between {} are only available in those braces.

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
  txt.length().         // prints length of text variable
     .toUpperCase()     // Makes every letter upper-case
     .toLowerCase()     // makes every letter lower-case
     .indexof("~")      // finds first position of ~.
     .concat(y)         // concatenates txt with y.
     .charAt(n)         //returns character at index n.;
     .startswith("~")   //checks if string starts with ~
     .endswidth("~")    //checks if string ends with ~
     .split()           //splits string into set of substrings
     .trim()            //removes whitespace from both ends
  

  -Concatenate strings with +

  -Escape characters. If using quotes inside strings use \' or \". " '
      String txt = "We are the so-called \"Vikings\" from the north.";

   Adding a number and string will turn the number into a string.;

Math. Built-in class that has math functions
  .max(x,y)   //finds biggest value of x and y
  .min(x,y)
  .sqrt(x)    //Square root.
  .abs(x)     //Absolute value.
  .random()   //returns number between 0.0 and 1.0
  .exp(x)     //value of e^x
  .floor(x)   //rounds x down to nearest integer
;

Wrapper. Use primitive data types as objects. More functionality.;
          Wrapper    data type
          Integer     -int
          Float       -float
          Double      -double
          Boolean     -boolean
          Character   -char
  
   -Convert Integer to String.;  .toString();
                Integer myInt = 100;
                String myString = myInt.toString();
                
   -Convert String to Integer; .valueOf();
                String str = "25";
                Integer number = Integer.valueOf(str);
  
User input. Directly type stuff into the console window/terminal.;
            import java.util.Scanner; //import Scanner class
  //.in is the input method of Scanner
            class Main {
              public static void main(String[] args) {
                Scanner scanner = new Scanner(System.in); //create Scanner object
                System.out.println("enter username");
      
                String userName = scanner.nextLine();  // This line reads user input
                System.out.println("Username is: " + userName); //output user input
              }}

                x = scanner.nextInt();  //reads integers
                y = scanner.nextInt();  //reads second integer

  The scanner object can be used for any & all data types. You just need to call
  the object with the specific 

  For each data type you need a different method from the scanner Class;
      boolean     nextBoolean();
      double      nextDouble();
      int         nextInt();  //reads integers. Call for as many things you want to read.
      String      nextLine();

 PROBLEM. When you do nextInt() or nextDouble() Java automatically adds a \n 
 which creates a new line. The problem is that it doesn't' go away if you do 
 a nextLine() method call.; To fix that just call nextLine() with no arguments.;
 
            // String input
            String name = scanner.nextLine();

            // Numerical input
            int age = scanner.nextInt();
            double salary = scanner.nextDouble();

------------------------------------COLLECTIONS-------------------------------------------
  
Arrays. Store multiple values in a single variable. Use [] after variable type.
  Arrays values must be only one type. Create them with {}. IMMUTABLE.
  
       data_type[] arrayName = {element 1, element 2, element 3}
 
 To access values use arrayName[x] indexing. 0-indexed like Python.
 You can change any element by reassigning it.
   
                arrayName[n] = new_value
                
 -Two-dimensional arrays. 
                int[][] arraysName = { {1,2,3}, {7,8,9} };
                arraysName[1][2] // 9;
                  
 -ArrayList. Resizable array.
                  import java.util.ArrayList;
                  ArrayList<data_type> arraylistObj = new ArrayList<data_type>();
     Methods for arrayList
                  .add();    //adds in items
                  .get(n);   //access element at index n
                  .set(n, ~)  //change value at index n to ~
                  .remove(n)  //removes element of index n
                  .clear()    //deletes all elements in list.
                  .size()       //find size of array. Like len() in python
                  
 -LinkedList. Manipulate data in a list. Almost identical to ArrayList.;
              addFirst()
              addLast()
              removeFirst()
              removeLast()
              getFirst()
              getLast()
                
-HashMap. Store elements in key/value pairs. Just like dictionaries in Python.
                import java.util.HashMap 
                
 HashMap<key_data_type, value_data_type> hashmap_name = new HashMap<key_data_type, value_data_type>();

          .put(~)       -adds items.
          .get(key)     -access a value through its key.
          .remove(~)    -remove item ~
          .clear()      -removes all items.
          .size()       -returns how many items. like len in Python.;

 HashSet. List with UNIQUE items.
              import java.util.HashSet;

       HashSet<Wrapper> obj = new HashSet<Wrapper>();

        .add(~)       -add ~ to set.
        .contains(~)  -checks if x is in list
        .remove(~)    -removes an item
        .clear()      -removes all items.
        .size()       -how many items there are;

Iterator. Object to loop through ArrayList and HashSet.
                import java.util.ArrayList;
                import java.util.Iterator;

             ArrayList<Wrapper> obj = new ArrayList<Wrapper>();

                    //get the iterator
                    Iterator<Wrapper> it = obj.iterator();

                    // print first item
                    System.out.println(it.next());

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
              static return_type myMethod(data_type parameter) {
                // code to be executed
              }} 

    static means it belongs to a class itself;
    If your method does not return anyting use void;
    
   -You run the function when you call it.;
             public static void main(String[] args) {
                myMethod("argument");};
  -Overloading. Same name with different parameters.
       int myMethod(int x);
       float myMethod(float x);
       double myMethod(double x, double y);
;

Lambdas. short block of code. Takes in a parameter and returns a value.;
    
                        parameter -> expression
                        
                 (parameter1, parameter2) -> { code block }

-----------------------------------CLASSES & OBJECTS-----------------------------------------
Objects containe data and methods that can be called at any time.;
Classes are like blueprint for objects. They have attributes and methods. Some 
can be shared with all objects or each object can have their own traits.;

               public class ClassName {
                           //code
               };
 To create a new object:
              public static void main(String[] args) {
                ClassName objName1 = new Main(); //Create new object called objName
                ClassName objName2 = new Main(); //2nd object of class.
                System.out.println(myObj.x);}}


-Attributes. You access attributes of callses using dot syntax ( . );
             public class Main {
               int x = 5;

               public static void main(String[] args) {
                 Main myObj = new Main(); 
                 System.out.println(myObj.x);}}
          // prints out 5

  Access methods of a class using .methodName()

    Static vs Non-static;
        static = accessed without creating an object of a class
        public = need to create an object.;

 -Constructors. Special methods to initialize objects. Sets initial values 
 of object attributes.;
   The constructor must have the same name as the class;

            public class Main {
              int x;
              String y
              public Main(parameter1, parameter2) { // CONSTRUCTOR
                x = parameter1;
                y = parameter2;}
            };

 -Access Modifiers. Clearence level for classes & attributes;
            public  -accessible for all classes
            private  -only within declared class
            protected  -same package and subclasses.
                        
 -Setters & getters;
            public class Person {
              private String name; // private = restricted access

              // Getter
              public String getName() {
                return name;}

              // Setter
              public void setName(String newName) {
                this.name = newName;}}

    The get method returns the value of the variable name.
    The set method takes a parameter (newName) and assigns it to the name variable. 
    The this keyword is used to refer to the current object.;

-Inheritance. Passing attributes from one class to another. Uses extends keyword
               class Vehicle {
                  protected String brand = "Ford";        // Vehicle attribute
                  public void honk() {                    // Vehicle method
                    System.out.println("Tuut, tuut!");}}

                class Car extends Vehicle {
                  private String modelName = "Mustang";    // Car attribute
                  public static void main(String[] args) {}};

-Polymorphism. Using inherited methods to perform different tasks. Methods with same name.
  This invovles chaning the methods from parent class.;

                  class Animal {
                    public void animalSound() {
                      System.out.println("The animal makes a sound");}}

                  class Pig extends Animal {
                    public void animalSound() {
                      System.out.println("The pig says: wee wee");}}

                  class Dog extends Animal {
                    public void animalSound() {
                      System.out.println("The dog says: bow wow");}}

                  class Main {
                    public static void main(String[] args) {
                      Animal myAnimal = new Animal();  // Create a Animal object
                      Animal myPig = new Pig();  // Create a Pig object
                      Animal myDog = new Dog();  // Create a Dog object
                      myAnimal.animalSound();
                      myPig.animalSound();
                      myDog.animalSound();}}

-Nested Classes. You can group classes that belong together. Create an object of 
an outer class then make an object of the inner class.;

              class OuterClass {
                int x = 10;

                class InnerClass { //This class is nested.
                  int y = 5;
                }}
              
              public class Main {
                public static void main(String[] args) {
                  OuterClass myOuter = new OuterClass(); //creating an object
                  OuterClass.InnerClass myInner = myOuter.new InnerClass(); //object of inner class
                  System.out.println(myInner.y + myOuter.x);}}

-Abstraction. Hiding certain details and showing only essential information to user.;
      abstract keyword is a non-access modifier.
        -abstract class: restricted class than cannot create objects. Must be inherited
        -abstract method: only used in abstract class. body provided by subclass.;
                
           // Abstract class
          abstract class Animal {
            // Abstract method (does not have a body)
            public abstract void animalSound();
            // Regular method
            public void sleep() {
              System.out.println("Zzz");}}
            
          // Subclass (inherit from Animal)
          class Pig extends Animal {
            public void animalSound() {
              // The body of animalSound() is provided here
              System.out.println("The pig says: wee wee");}};
          
-Interfaces. completely abstract class to group related methods with empty bodies.;
  You must implement interfaces to access them. 
    Use the interface keyword to create and interface and implements to extend it
          // interface
          interface Animal {
            public void animalSound(); // interface method (does not have a body)
            public void run(); // interface method (does not have a body)
          }
          
          // Pig "implements" the Animal interface
          class Pig implements Animal {
            public void animalSound() {
              // The body of animalSound() is provided here
              System.out.println("The pig says: wee wee");};}

-Enums. Special "class" that represents a group of constants (unchangeable variables)
     You can access consants with dot notation..;
            
          enum LEVEL {
            LOW,
            MEDIUM,
            HIGH;};          
            
 -Making packages. 
               package mypack;
               class MyPackageClass {
                 public static void main(String[] args) {
                   System.out.println("This is my package!");
                 }};

-----------------------------------ERRORS & EXCEPTIONS------------------------------------
Exceptions occurr when there are erros in the code that prevent it from running.;
  
try/catch/finally. Test a code block and if it matches an error you handle it.;

                  try {
                    //  Block of code to try
                  }
                  catch(Exception e) {
                    //  Block of code to handle errors
                  }
                  finally {
                    // this block runs no matter what
                  }

throw. Create a custom error for whatever you want. You can match an existing error.;

              throw new Exception("Message");
                             
-----------------------------------REGULAR EXPRESSIONS------------------------------------
Sequence of characters that forms a search pattern.;

              import java.util.regex;
                                    .Pattern  -defines a pattern
                                    .Matcher  -used to search for pattern;

       Pattern pattern = Pattern.compile("pattern", Pattern.CASE_INSENSITIVE);
       Matcher matcher = pattern.matcher("~~~~~~");
       boolean matchFound = matcher.find();

 "pattern" is searched for in "~~~~~~" 

        Compile patterns;
              [abc]     -find one character from option between brackets
              [^abc]    -find one character NOT between brackets
              [0-9]     -find a single character from range 0 to 9;

        Metacharacters
              |       -find a match of any patterns separated by |: a|b|c;
              .       -find ONLY ONE instance of any character
              ^       -match at beginning of string: ^Hello
              $       -match at end of strings as in: World$
              \d      -digit
              \s      -whitespace character
              \b      -match at beginning or end: \bWORD, WORD\b
              
        Quantifiers
              n+      -match string with AT LEAST ONE n
              n*      -contains >= 0 occurances of n
              n?      -contains 0 or 1 occurrences of n
              n{x}    -sequence of X n's'
              n{x,y}  -sequence of X to Y n's'
              n{x,}   -sequence of at least X n's'.;

-------------------------------------THREADING--------------------------------------------
Threads allow a program to operate ore efficiently by doing multiple things at once.;

            public class Main extends Thread { //extend Thread class
              public static void main(String[] args) {
                Main thread = new Main();
                thread.start();
                System.out.println("This code is outside of the thread");
              }
              public void run() {
                System.out.println("This code is running in a thread");}}

------------------------------------FILE HANDLING------------------------------------------
Java can open, rewrite, read, and delete files dynamically.
    
                  import java.io.File  //File class
              
                  File myObj = new File("filename.txt") //specify the filename
                  
     -Methods for File class:
              canRead()          -whether file readable or not
              canWrite()         -whther file writable or not
              createNewFile()    -creates empty file
              delete()           -deletes a file
              exists()           -tests whether file exists
              getName()          -return of the name of file
              getAbsolutePath()  -returns aboslute pathname
              length()           -size of file in bytes
              list()             -arrays of files in directory
              mkdir()            -creates a directory
              
              
          import java.io.File;  // Import the File class
          import java.io.IOException;  // Import the IOException class to handle errors

  -Creating new file. Use a try/catch block to handle IOException error. .createNewFile will return
    true if a new file is created and false if that file already exists.

          public class CreateFile {
            public static void main(String[] args) {
              try {
                File myObj = new File("filename.txt");
                if (myObj.createNewFile()) {
                  System.out.println("File created: " + myObj.getName());
                } else {
                  System.out.println("File already exists.");
                }
              } catch (IOException e) {
                System.out.println("An error occurred.");
                e.printStackTrace();}}}

      To specify path of file and use \\ for Windows and / for Mac and Linux.
               File myObj = new File("C:\\Users\\MyName\\filename.tx");
   
  -Write to file. Use FileWrite with .write() method to write to a file. Use .close() when done.
                      import java.io.FileWriter;
                      import java.io.IOException;

            public class WriteToFile {
              public static void main(String[] args) {
                try {
                  FileWriter myWriter = new FileWriter("filename.txt");
                  myWriter.write("~~~~~~"); // writing text to some existing file
                  myWriter.close();  //closes the file.
                  System.out.println("Successfully wrote to the file.");
                } catch (IOException e) {
                  System.out.println("An error occurred.");
                  e.printStackTrace();}}}

  -Read a file. Import Scanner class to read contents of text file.;

              import java.io.File;  // Import the File class
              import java.io.FileNotFoundException;  // Import this class to handle errors
              import java.util.Scanner; // Import the Scanner class to read text files

              public class ReadFile {
                public static void main(String[] args) {
                  try {
                    File myObj = new File("filename.txt");
                    Scanner myReader = new Scanner(myObj);
                    while (myReader.hasNextLine()) {
                      String data = myReader.nextLine();
                      System.out.println(data);
                    }
                    myReader.close();
                  } catch (FileNotFoundException e) {
                    System.out.println("An error occurred.");
                    e.printStackTrace();}}}

            
