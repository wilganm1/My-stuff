------------------------------BASICS-----------------------------------------
You can import libraries like in Python.
Libraries include functions/objects that can be helpful
#include <iostream>    //input/output library
#include <cmath>     //for std::sqrt()
#include <cstdint>
#include <cassert>   //for assert() true unless a bug in program
#include <vector>    //for vector
#include <cstdlib> // for std::rand() and std::srand()

To add external libraries, download them, click on Settings up top,
click on Compiler, click on Linker Settings and add the path.
#include "library.h"

  -Namespaces, make your own functions. Use :: operator
      namespace abc {   //creating the namespace abc
         int func(param1, param2) {}}  //function within namespace
     call the func function by using the namespace and ::
            abc::func
     calling :: within a namespace calls the global function

  -Nested namespaces
   You can shorthand a namespace inside another namespace
       namespace foo::goo {} with is the same as
         namespace foo{
          namespace goo{int func(){}}}
   -Namespace aliases let you save a namespace variable as a namespace
       namespace active = foo::goo;   //
         active::func();    //calling the foo:goo function

-Basic syntax
;            -ends statements in C++. Need these in every statement
\n           -inserts a new line.
\n\n, endl   -creates a blank line
\t           -horizontal tab
\?           -question mark
//           -single-line comments. Ignored by compiler. Like # in Python.
/* ~~ */     -multi-line comments. Like triple quotes in Python.
{}           -braces used for code in functions


-Variable Types
int          -stores integers.
double,float -stores decimal numbers.
char         -stores single characters only. Uses ''
string       -stores text lines. Uses "".
bool         -True or False vales. 1= true, 0 = false

Convert one type to another using static_cast
     static_cast<new type>(x)
** You need to divide floats otherwise C++ will give a rounded number **
      Type cast integers into doubles when dividing
         int x{7};
         int y{4};
         std:: cout << static_cast<double>(x) / y << endl;

-Concatenate strings.
Use + to combine different strings. Add a space at end of first string " "
or you can use .append() as the same thing.
        std::cout << "My " + "name " + "is "

-Indexing strings []
 Can access the element at a certain posistiom. 0-indexed like Python.
    string myString = "Hello";
    cout << myString[1];
    //Outputs e
-Methods
   Methods are built-in functions like python.
    x.append(y)  -concatenates y to end of x
    x.length()   -gets length of x
    max(x,y,..)  -returns the largest number of x or y
    max(x,y,..)  -returns the smallest number of x or y
    .find(~)     -sees if ~ is in a string.

-Operators
=      -assigns values to variables
+      -adds numbers. Concatenates strings.
-      -subtracts things.
*      -multiplies values
/      -divides values
%      -modulus. Returnes division remainder
++x    -increments by 1. changes value of it.
--x    -decrements by 1
&&,    -and operator. (Higher precedence than ||)
||     -or operator. like in Python. (Lower precedence than &&)
!      -logical not
::     -scope resolution operator
>      -greater than. Returns true or false
<      -less than.
>=     -greater than or equal to.
<=     -less than or equal to.
==     -is equal to
!=     -not equal to
+=     -adds value to a variables
-=     -subtracts from a variables
*=     -multiplies a variable
&=     -reference equals
std::pow(x,y)  -Exponential. #include<cmath> to use. Equals x^y.

 -funciton for exponentiation.
     #include <cstdint>
    std::int_fast64_t pow(int base, int exp){
        std::int_fast64_t result{ 1 };
        while (exp){
            if (exp & 1)
                result *= base;
            exp >>= 1;
            base *= base;}
        return result;}

-Arrays/lists. Uses {} braces
   dataType arrayName[x]. x = how long it is. Need to be same data type
   int myNum[3] = {10,20,30}
 Change the value of an elem in a certain index the same way in python.
   cars[0] = "New value"

All comparison operators need to be in (). (~ > ~)
  When comparing floats use epsilon. These check if they are "close enough"

----------------------------USER INPUTS--------------------------------------
 cin >>    -Use std::cin to get user input. Like input() in Python.
   int x;
   std::cout << "Type a number: ";
   std::cin >> x;  //Gets user input from keyboard.
   std::cout << "Your number is: " << x;

.ignore   -ignores everything up to break line.

 getline(std::cin, std::ws, x).  -input strings of text.
  -ws      -ignores leading whitespace
      std::string fullName;
      std::cout << "Type your full name: ";
      std::getline (cin, fullName);
      std::cout << "Your name is: " << fullName;

 buffer   -holds user input

 Errors. Have an error pass if a condition is not met.
  std::cerr       -throws an error.
    if (x < 0) {
     std::cerr << "Error";}

 Assertion. Something is true unless something is wrong.
   #include <cassert>
     assert(gravity > 0.0)   -stops the program and gives an error

 Static assert. An assertion that runs at compile time if false.
    static_assert(condition, diganostic_message)

-------------------------------VARIABLES-------------------------------------
There are 4 ways to create a variable, You first
 assign a variable then you initialize it with a value.;
  data_type identifier;  //assignment of identifier to a data_type
  data_type identifier = value; //copy initialization
  data_type identifier( value );  //direct initialization
  data_type identifier { value }; //brace/list initialization ***
    int myNum = 15;
    cout << myNum; //outputs 15
  List initialization is generally the best because any errors are addressed
  where as the othere ones just auto-correct into a different value.
   ******* Use list initalization whenever possible. ********

    Doing empty braces {} results in value initialization, which is
    usually zero - called zero initialization
         int x {}   //outputs 0

 You can combine variables in one cout sentence. Make sure to add space
        int myName = Mitch;
        int myAge = 25;
        cout << "I'm " << myName << " and I'm " << myAge << " years old.";
 Add variables together:
    int x = 5;
    int y = 6;
    int sum = x + y;
    cout << sum;

 -Global variables are defined outside functions.
    use g or g_ to help define global variables

 -Type cast. Converting one data type to another.
      static_cast<new_data_type>(expression)

 -Constants, unchanging variables
     const int myNum = 15;  -use const to make it a constant.

 -constexpr, a compile-time constant. A variable is initialized at time
    of compilation. It's a variable that's known when being built.
   constexpr double gravity {9.8}  //this doesn't change and is known before

 -Auto, have the computer assign variable type automatically.
        auto variable = value;
     Auto variables must be initialized or it returns an error

 -Signed and unsigned numbers.
    -unsigned   -Can only hold positve numbers. > 0
    -signed     -can be negative or positive.


 -Aliases. Set a name equal to a data_type
     using name_of_alias = data_type;
       using distance_t = double
    distance_t milesToDestination{ 3.4 } //a double variable

 -Typedef. same as aliases with using keyword
     typedef data_type variable_name;
       typedef long miles_t;

 -Enumerated types
     Enumerated types are data types the user can create
        enum enumName {
            enumerator1,  //values called enumerator
            enumerator2,
            ...};
     Different enum can't have the same enumerator names.
   Each enumerator is auto-assigned an integer value based on position.
       enum enumName {
            enumerator1,   //assigned 0
            enumerator2};  //assigned 1
       enumName varName{enumerator1};
       std::cout << x //outputs 0

   Inputting enumerators. Use type casting
        int inputColor{};
        std::cin >> inputColor;
        Color color { static_cast<Color>(inputColor)};

   Printing enumerator's values
     enum Color {
        color_black};
     Color color{};
     std::cout <<

 -Use e to represent powers of 10 for numbers
    float f1 = 35e3;

 -Reference operator. &
   you can create another variable with the same value as another variable
      string food = "Pizza";
      string &meal = food;

      cout << food << "\n";  // Outputs Pizza
      cout << meal << "\n";  // Outputs Pizza

 -Memory address &. references a variable itself to get it's memory address
  string food = "Pizza";
  cout << &food; // Outputs 0x6dfed4

 -Pointer. stores memory address as its value. Needs a & in its value
   string food = "Pizza";  // A food variable of type string
   string* ptr = &food;   //NEED TO HAVE & SYMBOL
  Use *ptr to print out the OG value that is being referenced to. Without
  the * symbol it just prints out the memory of the referenced variable
    cout << ptr << endl;  //outputs 0x61fde0
    cout << *ptr;    //outputs Pizza

 -Saving functions as variables
     //someFunction(){}
     x{ someFunction() }

      Don't use (x, ++x) as parameters because it causes error.

-Memory allocation. You need to manually deallocate memory in C++.
  The new operator allocates memory to a variable
   Syntax: pointerVariable = new dataType

    int* pointVar; // declare an int pointer
    pointVar = new int; // dynamically allocate memory using new keyword
    *pointVar = 45; // assign value to allocated memory
   the output of *pointVar = 45

  delete operator deallocates memory.
     delete pointerVariable

  -Linkage.
    Internal linkage is when an identifier can be seen and used within a
    single file, but not accessible from other files.
    Global variables with interanl inkage are called internal variables.
     Use static to make non-const global variable
        static int g_x;

----------------------------CONDITIONALS-------------------------------------
-Conditional statements.
    if       -block of code is run if condition is true
    else     -runs if same condition is false
    else if  -runs if first condition is false
    switch   -specify many alternative blocks of code to be executed

    if (condition1) {//block of code run if true
    } else if (condition2){//block of code if condition1 is false
    } else {} //block of code run if all are false

    Ternary ? operator as shortcut for if else
        (condition) ? expressionTrue : expressionFalse
      string result = (x < 18) ? "x is illegal." : "x is legal.";

  -Switch syntax. Basically a giant if, else layout.
    switch(expression) {    //loops through cases
      case x:
        // code block if x == expression
        break;   //stops the loop
      case y:
        // code block if y == expression
        break;
      default:}
        // code block if nothing == expression
    switch will evaluate an expression and will run the case that mathces it.

    -Fallthroughs. Starting at one case and going until told to stop.
        case x:
            [[fallthrough];   //goes to case y
        case y:

 -Boolean conditionals.
     bool b1;
     if (b1) automatically evaluates to true
     if (!b1) "not b1". Evaluates to false. "Not true."

 -Goto statements. Allows you to jump to another spot in the code
     the jump is started at a goto statement and goes to a statement label
      Kinda like an manual restart for a loop
          int main(){
          double x{};
        tryAgain:  //label statement that is jumped to
            std:: cin >> x;
            if (x < 0.0 )
            goto tryAgain;}  //jumps to label statement

    -Implement a while loop that restarts if condition not met
        while(1){
            int x{};
            std::cout << "Do something: ";
            std::cin >> x;
            if (x > 5){
                break}
            else {std::cout << "Enter value smaller than 5." << endl;}}}

---------------------------------LOOPS---------------------------------------
-Loops, for and while
 While loops will run forever unless a condition is met.
   int i = 0;
   while (i < 5) {
     cout << i << "\n";
     i++;}   //increases i every time. Then restarts the loop

   Multiple conditions with OR. (this OR that)
    C++ is different than python that if you want to say (this OR that)
    you need to use the && operator because one is always set to true.
     (condition 1 && condition 2)
      Example: while x < 5 OR y < 3
  -->   while (x < 5 && y < 3)

 Do/While loop
     will run code block once, checks if condition is true, and will continue
     to loop if the condition is true.
     do {
       // code block to be executed
       }
     while (condition);  //runs if do == true

    If you want an infinite loop use while (true)

-For loop. More control over loop. (starting; while condition; change)
  for (int i = 0; i < 5; i++) {
    cout << i << "\n";}

 You can combine for, if, and break to stop a loop at a condition
  for (int i = 0; i < 10; i++) {
    if (i == 4) {
      break;     //stops the loop entirely
    }
    cout << i << "\n";}

  continue. skips the current iteraion if a condition is met.
  Goes to the next iteration
     for (int i = 0; i < 10; i++) {
       if (i == 4) {
         continue;}
       cout << i << "\n";}

 you can loop through an arryay.
 string cars[4] = {"Volvo", "BMW", "Ford", "Mazda"};
 for(int i = 0; i < 4; i++) {
   cout << i << ": " << cars[i] << "\n";}

 Omit elements on declaration
  string cars[5];
  cars[0] = "Volvo";
  cars[1] = "BMW";
  ...

----------------------------FUNCTIONS--------------------------------------
 Functions are blocks of code that do specific things. Only when called.
 They can return something specific using the return keyword. The
 function needs a data type classifier if it returns that data type.
    data_type functionName(parameters){ //declaration
    //code to run. body of function    (definition)
            return data;}

 If it returns nothing use the void keword.
    void functionName(parameter1, parameter2) {
  To call a function you need to put it inside main() function
     int main() {
     functionName();
     return 0;}

    if the returned value isn't used it's discarded.
     YOU CAN ONLY HAVE ONE RETURN STATEMENT. C++ will only return the
     first return statement, and not any others.
  functions must be DECLARED BEFORE they are called. But they have to
  be defined after the main function.

  Functions can have parameters that are variables within the function.
  They are blank variables that can be anything. Just like python

     void myFunction(string fname) {
      cout << fname << " Refsnes\n";}

    int main() {
      myFunction("Liam"); //function will output "Liam"
      return 0;}

  **********YOU CANNOT DO NESTED FUNCTION IN C++************
       int f1(){int f2(){}}  //Not allowed

   If you want to return a functions value inside main(){} you need to
    set a variable to the function itself, then print out that variable

    int getValueFromUser(){  //function to get an input
        std::cout << "Enter an integer: ";
        int input{};
        std::cin >> input;  //input a number
        return input;}  //prints out the input
    int main(){
        int num {getValueFromUser()};  //This sets num equal to input
        std::cout << num << " doubled is: " << num * 2 << '\n';
        return 0;}
  -Local scope
  Local scope refers to variables defined inside a function. If x is
  defined in a function it has no value outside it.

   -Default variable, rightmost variable
   You can add a default variable using =. If the function has no argument
   when it's' called it used the default variables.
        void myFunction(string country = "Norway") {
          cout << country << "\n";}

        int main() {
          myFunction("Sweden"); //outputs Sweden
          myFunction();    //outputs Norway
          return 0;}
   -Forward declaration. You can declare a function but define it later.
        int add(int x, int y); //declared but not defined
        int main(){
            std::cout << "The sum of 3 and 4 is: " << add(3, 4) << '\n'; // this works because we forward declared add() above
            return 0;}
        int add(int x, int y){  //defining the add function
            return x + y;}

  -Naming collisions. When functions in multiple files have same name.
   Say you have the function myFunc in two separate file both with int
   as a data type. Linking them would give an error.

  -Reference. You can swap variables using references sign &
      void swapNums(int &x, int &y) {
      int z = x;
      x = y;
      y = z;}
    int main() {
      int firstNum = 10;
      int secondNum = 20;
      cout << "Before swap: " << "\n";
      cout << firstNum << secondNum << "\n";
      // Call the function, which will change the values of firstNum and secondNum
      swapNums(firstNum, secondNum);
      cout << "After swap: " << "\n";
      cout << firstNum << secondNum << "\n";
      return 0;}

  -Function overloading
    Multiple functions can have the same name with different parameters.
       int plusFunc(int x, int y){
         return x + y;}
       double plusFunc(double x, double y){
         return x + y;}

  -Templates. Build functions using a specific form
          template <typename T> //template parameter declaration
          T funcName(T x, T y) {} //use T,U,V,...etc to name template types
     Calling a function from the template is called function template
     instantiation.
           funcName<int>(x,y)  //instantiation of function
     The function instantiated looks like this:
         int max<int>(in x, int y) //generated from max<int>(int, int)

-------------------------CLASSES & OBJECTS----------------------------------
 A class is a blueprint of objects. Think class as car and object as Volvo
 You can create multiple objects
     class Car {        // The class
          public:          // Access specifier
            string brand;  // Attribute
            string model;  // Attribute
            int year;      // Attribute
            Car(string x, string y, int z) {  // Constructor with parameters
              brand = x;  //plug in stuff like a function into constructor.
              model = y;  //Each object will have all the same attributes
              year = z;}};  //but with what is entered as parameters.
      
/*The constructor is a special function that is run when an object of a class is created.
You can set up arguments in constructors and set attributes of the class equal to
these arguments. Think of it like self in Python.
*/
        int main() {
          // Create Car objects and call the constructor with different values
          Car carObj1("BMW", "X5", 1999);
          Car carObj2("Ford", "Mustang", 1969);
          // Print values
          cout << carObj1.brand << " " << carObj1.model << " " << carObj1.year << "\n";
          cout << carObj2.brand << " " << carObj2.model << " " << carObj2.year << "\n";
          return 0;}
      
    You can also define constructor outside of class using ::
      Car::Car(string x, string y, int z) {
        brand = x;
        model = y;
        year = z;}
        
 -Methods. methods are functions that belong to classes
    class MyClass {        // The class
      public:              // Access specifier
        void myMethod() {  // Method/function defined inside the class
          cout << "Hello World!";}};
    int main() {
      
      MyClass myObj;     // Create an object of MyClass
      myObj.myMethod();  // Call the method
      
      return 0;}

   You can call a function outside a class using ::
       void MyClass::myMethod(){
       cout << "Hello World!";}
   Can also add parameters
      int Car:: speed(int maxSpeed) { return maxSpeed}

      int main() {
       Car myObj; // Create an object of Car
       cout << myObj.speed(200); // Call the method with an argument
       return 0;}
       
 
  -Struct. group of data elements together under one name.
     Like a class but simplified and public as default.
      struct nameOfStruct {
        int x;
        double y;}
    You can then call objects with attributes of the structure.
      nameOfStruct a;
        a.x = 20

-Access specifiers.
How member of a class can be accessed.
 -public    -members accessible from outside class
 -private   -members cannot be accessed from outside class.    Default.
 -protected -cannot be accessed outside class, but can be in inherited classes

    class MyClass {
      public:    // Public access specifier
        int x;   // Public attribute
      private:   // Private access specifier
        int y;};   // Private attribute

    int main() {
      MyClass myObj;
      myObj.x = 25;  // Allowed (public)
      myObj.y = 50;  // Not allowed (private)
      return 0;}

-Encapsulation. Make "sensitive" data hidden from users
Set class to private, and use get and set methods to modify private values
    class Employee {
      private:
        int salary;
      public:  //makes both functions public.
        // Setter
        void setSalary(int s) {
          salary = s;}
        // Getter
        int getSalary() {
          return salary;}};

-Inheritance. Two categories of inheritance
  derived class (child)  -inherits from another class
  base class (parnet)    -the class being inherited from
    class Vehicle {   //parent class
        public:
  To set a derived class you need a : to classify it.
    // Derived class
    class Car: public Vehicle {  //need public to reference the parent class
      public:
        string model = "Mustang";};}
 //You can also inherit multiple times
    class Model: public Car {};  //inherited from Car class.

  Inheritance from multiple parent classes using ,
    class SomeClass{public:};   //Base class 1
    class SomeOtherClass{public:};  //Base class 2
    class InheritClass: public SomeClass, public SomeOtherClass

  the protected specifier can be accessed in inherited classes.

-Polymorphisms. Use the same inherited methods to do different things
      class Pig : public Animal {
        public:
          void animalSound() {    //
          cout << "The pig says: wee wee \n" ;}};
      class Dog : public Animal {
        public:
          void animalSound() {
          cout << "The dog says: bow wow \n" ;}};

-Files
Use fstream library to work with files
#include <iostream>
#include <fstream>

 -Write files with ofstream and <<.
    int main() {
   ofstream MyFile("filename.txt"); //create and open file
   MyFile << "Files can be tricky, but it is fun enough!"; //write file
   MyFile.close();}  //close file
 -Read files with ifstream
    string myText;   //create text string
    ifstream MyReadFile("filename.txt");  //read text file
 // Use a while loop together with the getline() function to read each line
    while (getline (MyReadFile, myText)) { // Output the text from the file
      cout << myText;}
     MyReadFile.close();   // Close the file

-RAII

-Preprocessors, includes, macros.
 Preprocessors manipulate the text in each code file. Use a # directive
 When you include a file you actually import the contents of the file.
 You use #include nameOfFile like when you do #include <iostream> to
 be able to use cout and cin.

  -Macros. A rule that defines how input text is converted into replacement
  output text. They are shortcuts.
    #define identifier

  -Conditional compilation. specify if something will compile. They
    They are ifdef and ifndef. They both end in endif
       int main() {
         #ifdef X //if X is defined, the code is compiled
           //code to run
         #endif
         return 0;}
       int main() {
         #ifndef Y //if Y is NOT defined, code runs
           //code to run
         #endif
         return 0;}
    Also use if 0 to stop things from compiling
         #if 0
           //whatever code
         #endif
-Header files. forward declaring functions
 These files are at top of file May have a .h or .hpp extension.
    #incldue "file_here.h"

       *****USE "" FOR FILES YOU WRITE YOURSELF*****

 You can write your own headers in two parts, a guard and the content
  If you pair a header file with a code file use the same base name:
      add.h & add.cpp (add)

   -Guards. Stop duplicating same function from different sources
      #ifndef file_name
      #define file_name
        //declarations
      #endif

  -Logging. Logging is sending debugging information to a file that
  records events in software called a log file.
        #include <plog/Log.h>
        #include <plog.Initializers/RollingFileInitializer.h>

-Bits and bytes. All data has memory, a combination of 1's and 0's called
 bits. 8 bits = 1 byte.
     -sizeof operator to see how large some data types are.
 signed integers. 4 types of integers
   short s;
   int i;
   long l;
   long long ll;

 Floating point numbers. 3 different types.
    float f = 4 bytes
    double d = 8 bytes
    long double ld = 8 bytes

 Inf. Used for infinity. NaN, stands for Not a Number
    double posinf // positive infinity
    double neginf // negative infinity
    double nan

 -Boolean prints 0 for false or 1 for ture. Use std::boolalpha to
    print out either true or false.
    std::cout << std::boolalpha
  You can assign an integer to a bool variable. Setting it equal to 0
   prints out false, and other numbers evaluate to true.

  To input a bool as true or false use std::boolalpha
   bool b{}
   std::cin >> std:: boolalpha;
   std:: cin >> b;

-Halts.
Halts will stop the program entirely.
 exit() will explicitly end the program.
   int main(){
       std::exit(0);} //terminates the program at that point.
       //rest of code
 atexit() will specify a function to be called when program is exited.
   int main(){
       std::atexit(cleanup());}

 abort() aborts abnormally do to unusual error like dividing by 0
    std::abort();

-Random number generation
 a pseudo-random number generator (PRNG) takes a starting number (seed)
 and does math to it to get a new different number. Then repeats the math.
 Use a third-party library for random numbers

 #include "random.hpp"
 using Random = effolkronium::random_static;
 int main(){
 	 std::cout << Random::get(1, 6) << '\n';
 	 std::cout << Random::get(1, 10) << '\n';
 	 std::cout << Random::get(1, 20) << '\n';
 	 return 0;}
