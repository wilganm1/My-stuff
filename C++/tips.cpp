------------------------------BASICS-----------------------------------------
You can import libraries like in Python.
Libraries include functions/objects that can be helpful
#include <iostream>    //input/output library
#include <cmath>     //for std::sqrt()
#include <cassert>   //for assert() true unless a bug in program
#include <vector>    //adds vector arrays
#include <cstdlib> // for std::rand() and std::srand()
#include <string_view>  //used for std::string_view
#include <algorithm>    //search, count, sort, manipulate data.
#include "random.hpp"   //include random numbers
#include <limits>       //for std::numeric_limits
#include <time.h> //time-related functions
#include <iterator>  //for getting size of array using std::size()

system("CLS")      -clears the console screens.

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
 \n\n,        -creates a blank line
 std::endl;   -starts a new line
 \t           -horizontal tab
 \?           -question mark
 //           -single-line comments. Ignored by compiler. Like # in Python.
 /* ~~ */     -multi-line comments. Like three quotes in Python.
 {}           -braces used for code in functions

-Variable Types
 int          -stores integers.
 double,float -stores decimal numbers.
 char         -stores single characters only. Uses ''
 std::string  -stores text lines. Uses "".
 bool         -True or False vales. 1= true, 0 = false

Convert one data type to another using static_cast //type conversion
     static_cast<new type>(x)
** You need to divide floats otherwise C++ will give a rounded number **
      Type cast integers into doubles when dividing
         int x{7};
         int y{4};
         std:: cout << static_cast<double>(x) / y << endl;

 -Operators
 =      -assigns values to variables
 +      -adds number or concatenates strings.
 -      -subtracts things.
 *      -multiplies values
 /      -divides values
 %      -modulus. Returnes division remainder
 ++x    -increments by 1. changes value of it.
 --x    -decrements by 1
 &&,    -AND operator. (Higher precedence than ||)
 ||     -OR operator. like in Python. (Lower precedence than &&)
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

 All comparison operators need to be in (). (~ > ~)
  When comparing floats use epsilon. These check if they are "close enough"

-------------------------------------STRINGS--------------------------------------------
#include <string>    //for strings

std::string x = "Whatever here";

-Concatenate strings.
Use + to combine different strings. Add a space at end of first string " "
or you can use .append() as the same thing.
        std::cout << "My " + "name " + "is " //notice the white space after each word

-Indexing strings []
 Can access the element at a certain posistion. 0-indexed like Python.
    std::string myString = "Hello";
    cout << myString[1];
    //Outputs e

  Get a range from a string: //range, string has element.
      std::string x = {"whatever"}
      x.substr(1,4);   -This gets indexes 1 to 4.

-Methods
  Methods are built-in functions like python.
   x.append(y)  -concatenates y to end of x
   x.length()   -gets length of x
   max(x,y,..)  -returns the largest number of x or y
   max(x,y,..)  -returns the smallest number of x or y
   .find(~)     -sees if ~ is in a string.

-std:: functions
 all_of         -checks all of an array for a condition
 size(x)        -determines size of an array

------------------------------------VARIABLES----------------------------------------
There are 4 ways to create a variable, You first
 assign a variable then you initialize it with a value.;

  data_type variable_name;  //assignment of identifier to a data_type
  data_type variable_name = value; //copy initialization
  data_type variable_name( value );  //direct initialization
  data_type variable_name { value }; //brace/list initialization *** BEST

    int myNum = 15;
    std::cout << myNum; //outputs 15

  List initialization is generally the best because any errors are addressed
  where as the other ones just auto-correct into a different value.
   ******* Use list initalization whenever possible. ********

    Doing empty braces {} results in value initialization, which is
    usually zero - called zero initialization
         int x {}   //outputs 0

 You can combine variables in one cout sentence. Make sure to add spaces
        int myName = Name;
        int myAge = 25;
        cout << "I'm " << myName << " and I'm " << myAge << " years old.";
 Add variables together:
    int x = 5;
    int y = 6;
    int sum = x + y;
    cout << sum;

 -Global variables are defined outside functions.
    use g or g_ to help define global variables

 -Static variables. These are variables who keep values if they change.
     So if it changes in a function it will saved as that value
     #include <iostream>

     int generateID()
     {static int s_id{ 0 }; //initialized as 0
     return ++s_id;}   //increments by 1

     int main()
     {std::cout << generateID() << '\n';
     std::cout << generateID() << '\n';
     std::cout << generateID() << '\n';
     //prints out 1, 2, 3, not just 1 three times.

//      If s_id wasn't static it would always print out 1.

     return 0;}

 -Constants, unchanging variables. Use const keyword
     const int myNum = 15;  -use const to make it a constant.

 -constexpr, a compile-time constant. A variable is initialized at time
    of compilation. It's a variable thats known when being built.
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

----------------------------------USER INPUTS--------------------------------------
 std::cin >>    -Use std::cin to get user input. Like input() in Python.
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

 buffer         -holds user input
 ::setw(x) >>   -limits number of elements read in x

-------------------------------------ERRORS-----------------------------------------
Errors are when something goes wrong and is handled in the code.

-Exceptions. If a problem occurrs it must be addressed & stop the flow of code
    try                //checks if there is anything to look for
    throw expression   //throws an exception if an expression is met
    catch (data)       //catches the exception and produces and error

    int main(){
        try{
            // Statements that may throw exceptions you want to handle go here
            throw -1;   //expression
        } catch (int x) {
            //An int exception thrown within the above try block gets sent here
            std::cerr << "We caught an int exception with value: " << x << '\n';}


-Manually throw an error.

    std::cerr()       -throws an error.
        if (x < 0) {
         std::cerr << "Error message";}

Or just write functions to prevent errors
double reciprocal(double x){
    if (x==0.0)        //this makes sure we don't divide by zero
        return 0.0;
    return 1.0/x;}    //standard output for function

-Fatal Erros
These are errors so bad that the program can't' continue working.
std::exit(1)           //terminates the program
        double doDivision(int x, int y){
        if (y == 0)
        {   std::cerr << "Error: Could not divide by zero\n";
            std::exit(1);}
        return static_cast<double>(x) / y;}

-Ignore extraneous inputs using std::cin.ignore()
#include <limits>       //for std::numeric_limits

std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n')
   //This ignores all the inputs until the '\n' is removed
******************************************************************************
void ignoreLine(){
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');}
  //This function is a shorthand for ignoring input

-Extraction failures. When cin input is not a valid type
.fail()     //boolean if the cin failed
.clear()      //clears the cin value
.ignore(n, '\n')  //ignores n characters and skips to next line
    while (true){         //runs a loop until condition is met
        std::cout << "Enter a double value: ";
        double x{};       //x needs to be a double value
        std::cin >> x;
//Now we have the condition if the input is a double or not
        if (std::cin.fail()){  //will catch if x is not a double
            std::cin.clear();  //will erase the cin input
            std::cin.ignore(1000, '\n');}     //removes bad input. Loop restarts
        else {
            std::cin.ignore(1000, '\n');
            return x;}}

-Assertion. An expression that is true unless something is wrong.
  Only activates if statement is false.
     #include <cassert>
       assert(statement && "Message");   -stops the program and gives an error

 Static assert. An assertion that runs at compile time if false.
    static_assert(condition, diganostic_message)

---------------------------------ARRAYS/VECTORS----------------------------------------
Store multiple values of SAME TYPE in a list.

      dataType arrayName[length of array] = {values}. //hard coding length of array is optional
      int myNum[3] = {10,20,30}  //specifying that it is three items long

 Arrays in C++ have index values just like Python, zero-indexed.
 Change the value of an element in a certain index like in python.
     cars[0] = "New value"
      //std::cout << cars[0] now prints "New value"

  -Iteration. Accessing array values from a loop
      int scores[]{ 84, 92, 76, 81, 56 };
      int numStudents{ static_cast<int>(std::size(scores)) };
      int totalScore{ 0 };
        // use a loop to calculate totalScore
      for (int student{ 0 }; student < numStudents; ++student)
          totalScore += scores[student];

  -Size of array; You must divide bytes of array by byte of the data type
        int myNumbers[5] = {10, 20, 30, 40, 50};
        int getArrayLength = myNumbers.size();

  -Swapping values
   #include <utility>
    std::swap()  -swaps two entries in an array
      int myArray[] = {2,3,5,7,8,9};
      int x = myArray[1];
      int y = myArray[5]
      std::swap(x,y)  //x will now = 9 and y will now = 3

  -Sorting values in arrays.  //sort. Ascending.
    Can sort values in ascending order
      #include <algorithm>
      int array[]{30,50,20,10,40}
      std::sort(std::begin(array), std::end(array));

  -Multidimensional arrays. an array of arrays. Like a matrix in Python
       int array[x][y]  -x-arrays with y-elements //x is optional
       int array[2][5]{   //2 arrays with 5 elements each
       {1,2,3,4,5},   //row 0
       {6,7,8,9,10}};  //row 1
    Zero-initialize arrays using empty brackets. int array[x][y]{}

     -std::array. Built-in function for array
          #include <array>
             std::array arrayName {a,b,c,d,e}
      If that doesn't work include <int, lengthOfArray>;
    -std::array myArray{a,b,c,d};
     myArray.size();

Vectors. Dynamic array functionality with own memory management
    #include <vector>          //adds in the vector library

     std::vector<data_type> vector_name = {};   -write a vector with x-number of data;

There are multiple methods/functions to alter vectors;
.front()                 -access first element of vector;
.back()                  -access last element of vector;
.begin()                 -iterator of first element;
.end()                   -iterator to final element of an array;
.insert(x, value, n)     -n-number of values at position x;
.erase(x)                -erases element at position x
.push_back(~~)           -inserts ~~ at end of array; Like .append in Python.
.pop_back()              -removes last element in vector. decreases size by 1.;
.size()                  -returns number of elements in vector;
.at(x);                  -get value at x-index
.resize(x)               -resize the vector. Gets rid of values with indices larger than x
.empty()                 -checks if its empty. If it is empty it returns true.;
.resize(x)               -resizes a vector and deletes any values that are after x elems
.find(array.begin(), array.end(), x)  -find x in an array
.find_if              -find something if it matches a condition
.count(arr.begin(),arr.end(),x)   -count occurances of x
.count_if()                       -count x if condition met
.sort()
.for_each(array.begin(), .end(),x)  -x is a list and applies to every element;
.max_size()        -max number of elements in an array;

---------------------------------CONDITIONALS-------------------------------------
-Conditional statements. These will run depending on something happening or not.
    if       -block of code is run if condition is true;
    else     -runs if same condition is false
    else if  -runs if condition before it is false
    switch   -specify many alternative blocks of code to be executed

 -If statements.

    if (condition1) {}       //block of code run if condition1 is true
    else if (condition2){}   //runs if condition1 is false and condition2 is true
    else {}                  //block of code run if all are fals

    Ternary ? operator as shortcut for if else whether it is true or false
        (condition) ? expressionTrue : expressionFalse

      std::string result = (x < 18) ? "x is illegal." : "x is legal.";

    *** When tyring to use multiple variables use && between them ***
            int xxx = 7;
            int yyy= 8;
        if (xxx == 7 && int yyy == 8){}

 -Switch statements. Basically a giant if, else layout.
    switch(expression) {    //loops through cases. MUST BE A CONSTANT. ONLY ONE EXPRESSION
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
            [fallthrough];   //goes to case y
        case y:

 -Boolean conditionals.
     bool b1;
     if (b1) //automatically evaluates to true
     if (!b1) //"not b1". Evaluates to false. "Not true."

 -Goto statements. Allows you to jump to another spot in the code.
     the jump is started at a goto statement and goes to a statement label
      Kinda like an manual restart for a loop

          double x{};

        tryAgain:  //label statement that is jumped to
            std::cin >> x;
            if (x < 0.0 )
            goto tryAgain;  //jumps to label statement
      //-in this case tryAgain would keep looping

------------------------------------LOOPS---------------------------------------
Loops are blocks of code that always restart if a certain condition is met.

-While loops. Will run forever while a condition is met.
       int i = 0;
       while (i < 5) {
         std::cout << i << "\n"; // prints out what i is equal to
         i++;}                   //increases i every time. Then restarts the loop

     If you want an infinite loop use while (true);

   Multiple conditions with OR. (this OR that)
    C++ is different than python that if you want to say (this OR that)
    you need to use the && operator because one is always set to true.
     (condition 1 && condition 2)
      Example: while x < 5 OR y < 3
  -->   while (x < 5 && y < 3)

-Do/While loop. Will run code block once, checks if condition is true, and will continue
     to loop if the condition is true.

     do {
       // code block to be executed
       }
     while (condition);  //runs if do == true


-For loop. More control over loop.
    for (starting condition; ending condition; change){}

      for (int i = 0; i < 5; i++) { //creates variable i, does something, then changes i until the condition is met
        cout << i << "\n";}

 You can combine for, if, and break to stop a loop at a condition
  for (int i = 0; i < 10; i++) {
    if (i == 4) {
      break;}     //stops the loop entirely
    std::cout << i << "\n";}

  continue. skips the current iteraion if a condition is met.
  Goes to the next iteration
     for (int i = 0; i < 10; i++) {
       if (i == 4) {
         continue;}
       std::cout << i << "\n";}

 You can loop through an arryay.
     std::string cars[4] = {"Volvo", "BMW", "Ford", "Mazda"};
     for(int i = 0; i < 4; i++) {
       std::cout << i << ": " << cars[i] << "\n";}

 Omit elements on declaration
  std::string cars[5];
  cars[0] = "Volvo";
  cars[1] = "BMW";
  ...

-For-each loops. Looping through arrays. Range-based for loops

        for (element_declaration : array) {
            statement;}

    It works like "for i in array" in Python.
        int main(){
        constexpr int fibonacci[]{ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 };
        for (for auto number : fibonacci) // iterate over array fibonacci
        {std::cout << number << ' '}; //number is the i in c++
        std::cout << '\n';
        return 0;}

    -Implement a while loop that restarts if condition not met
        while(true){
            int x{};
            std::cout << "Do something: ";
            std::cin >> x;
            if (x > 5){
                break}
            else {std::cout << "Enter value smaller than 5." << endl;}}}

-----------------------------------FUNCTIONS--------------------------------------
 Functions are blocks of code that do specific things only when called.
 They can return something specific using the return keyword. The
 function needs a data type classifier if it returns that data type.

    data_type functionName(parameters){ //declaration
    //code to run. body of function    (definition)
            return data;}

 If it returns nothing use the void keword.

    void functionName(parameter1, parameter2) {}

  To call a function you need to put it inside the main() function
     int main() {
         functionName();
         return 0;
         }

    If the returned value isn't used its discarded.
     YOU CAN ONLY HAVE ONE RETURN STATEMENT. C++ will only return the
     first return statement, and not any others.
  Functions must be DECLARED BEFORE they are called. But they have to
  be defined after the main function.

  Functions can have parameters that are variables within the function.
  They are blank variables that can be anything. Just like python

     void myFunction(std::string fname) {
      std::cout << fname << " Refsnes\n";}

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

 -Default variable, right most variable
   You can add a default variable using =. If the function has no argument
   when it's called it used the default variables.

        void myFunction(std::string country = "Norway") {
          std::cout << country << "\n";}

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
      std::cout << "Before swap: " << "\n";
      std::cout << firstNum << secondNum << "\n";
      // Call the function, which will change the values of firstNum and secondNum
      swapNums(firstNum, secondNum);
      std::cout << "After swap: " << "\n";
      std::cout << firstNum << secondNum << "\n";
      return 0;}

 ****You can dynamically change variables initialized in the main function through functions using a refernce argument****

        void refe(int& x){
            x += 5;}

        int main(){
            x = 3;
            std::cout << x << std::endl; /prints out 3
            refe(x)
            std::cout << x << std::endl;
            return 0;}

    ** x will now be changed to 8, since you added 3 **

    This is how you can change a single variable constantly throughout a program

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

  -Saving functions as variables
     //someFunction(){}
     x{ someFunction() }

      Don't use (x, ++x) as parameters because it causes error

-Recursion. A function that calls itself.
    void countDown(int count){
        std::cout << "push " << count << '\n';
        countDown(count-1);} // countDown() calls itself recursively
    if (count > 1)  -termination condition. Stops the function

-Lambdas, anonymous functions within a function
        [captureClause] (parameters) -> returnType {
             statements;}
 Capture clause and parameters don't need to be named. returnType is optional
        int main(){
           []() {}; // no captures, no parameters, and no return type
           return 0;}
****  If a function is a bool type your can print out the result by calling;
        std::cout << functionName();

-----------------------------------MEMORY----------------------------------------
-Reference operator &. Access the memory of a variable
   Access the memory address of a variable
      int x{5};
      &x       //memory of x

   Can also set it equal to another variable
      int x{};
      int& y{x};   -y is now set to the value of x

 -Indirections *&. Access value at a memory address.
      int x{5};
      std::cout << &x  //prints memory address of variable x
      std::cout << *&x  //prints the value of variable x

 -Pointer*. variable that holds memory address as a value.
      data_type* var_name{&value};
          int v{5};      //variable
          int* ptr{&v};   //pointer assigned to memory address
          std::cout << &v     //prints address of variable v
          std::cout << ptr     //prints address of ptr. = &v

   You can combine indirection and pointers
        int* ptr{&value};
        std::cout << ptr;  //prints memory address of value
        std::cout << *ptr;   //prints the actual value
    -Null pointer. A pointer that points to nothing
            data_tyep variable{nullptr}

   -indirection with arrays
      Using indirection on array points to first element
         int array[5]{9,7,5,3,1};
            *array;   //prints out 9
        //char name[]{"Jason:};
            *name      //prints out 'J'

           &array[0];  //prints address of first array element
           array  //also prints address

-Memory allocation.
   The new operator allocates memory to a variable
         pointerVariable = new dataType

    int* pointVar; // declare an int pointer
    pointVar = new int; // dynamically allocate memory using new keyword
    *pointVar = 45; // assign value to allocated memory

  delete operator deallocates memory.
       delete pointVar;

  -Memory segments. //Places where memory sit.
    -Code segment, //compiled program sits in memory
    -bss segment, //zero-initialized variables stored
    -data segment, //initialized global variables stored
    -call stack, function parameters, local variables stored.
       Works as a stack data structure, organized data to be used efficiently
       holds values like an array. You can only add or subract top of stack
          peek()       -looks at top of stack
          pop()        -takes off top (last) item of stack
          push()       -puts new item at end of stack
            stack = []
            stack.push(1); //stack = [1]
            stack.push(2);  //stack = [1,2]
            stack.pop();  //stack = [1]


    -Heap, dynamically allocated variables
       int *ptr = new int;  //4 bytes assigned to heap

  -Linkage.
    Internal linkage is when an identifier can be seen and used within a
    single file, but not accessible from other files.
    Global variables with interanl inkage are called internal variables.
     Use static to make non-const global variable
        static int g_x;

------------------------------CLASSES & OBJECTS-----------------------------------
A class is a blueprint of objects in which all objects have some or all
attributes of the class. Think of a class as a car and object as Volvo.
 You can create multiple objects from a single class.

     class ClassName {
      public:   //access specifier. How methods can be accessed.
          data_tye x{};    //attribute
          data_type y{};
          data_type z{};
          ClassName (data_type ax, data_type ay, data_type az){ //constructor
          x = ax //the a in front just means "argument"
          y = ay  //argument y
          z = az //argument z
          }};

        Access modifiers describe what code can access class attributes.
        public       //can be accessed outside class
        private      //Can only be accessed by other members of class. DEFAULT
        protected    //like private but can be accessed by derived classes.


  -Constructors.
    Special functions that are called whenever an object is created from a class.
    They take in arguments like normal functions. Think "self" like in Python.
    They have the same name as the class name.

   Create an object of Car class by calling the class name and
   giving the instance a name. Pass in arguments for the constructor.

    int main() {
        Car Honda("Honda", "Accord", 2000);
        //Now the object Honda will have these attributes.
        //cout << Honda.brand to test
      return 0;}

      To change the value of an attribute use dot notation.
           Car.age {x}

     -Methods. methods are functions that belong to classes. Must be public to use outside
        class MyClass {        // The class
          public:              // Access specifier.
            void myMethod() {  // Method/function defined inside the class
              cout << "Hello World!";}};
            To call the method use dot notation.

        int main() {
          MyClass myObj;     // Create an object of MyClass
          myObj.myMethod();  // Call the method function
          return 0;}

     -You can call a function outside a class using :: and add arguments
          void MyClass::functionName(argument){
          std::cout << "Hello World!";}
         int Car::speed(int maxSpeed){
              return maxSpeed; }

         int main() {
          Car myObj; // Create an object of Car
          std::cout << myObj.speed(200); // Call the method with an argument
          return 0;}

    -Access function retrives or change value of a private member variable
        -Setters
           Functions that set value of a class variable. You use these so that
           specific private variables are unchanged or only set to things you
           want them set to.

        class Movie {
            private:
                string rating;
            void setRating(string aRating){
                if (aRating == "G" || aRating == "PG") {
                rating = aRating}
                else {
                        return rating;}}};
        -Getters
           Functions that return value of class variable.
           string getRating(){
           return rating;};

     -Member initialization list. Method to initialize class members.
       Starts with constructor name then a : after

       class Something
        {
        private:
            int m_value1{};
            double m_value2{};
            char m_value3{};
        public:
            Something() : m_value1{ 1 }, m_value2{ 2.2 }, m_value3{ 'c' } // Initialize our member variables
       {}
       void print()
       {
           std::cout << "Something(" << m_value1 << ", " << m_value2 << ", " << m_value3 << ")\n";
       }};

   int main()
   {
       Something something{};
       something.print();
       return 0;
   }

    -Delegating constructors. Calling other constructors from same class
        Just call the first constructor as a member initialization of the second

        class Foo {
        private:

        public:
            Foo()   //default constructor
            {
                //code to do A
            }

            Foo(int value) : Foo{}  //calls default constructor to do A
            {
                //code to do B
            }};

    You can call constructors outside of classes with ClassName::Constructor

        class abc {
        public:
            abc(x,y,z)};
    abc::abc(1,2,3)    //this call the constructor outside the class

    -Destructors. Help with clean up of code.
        Uses ~ before name of constructor

        class ClassName {
        private:
            int m_length{};
        public:
            ClassName(int length) {  //constructor
                m_length = length}

            ~ClassName() {
                delete[] //stuff here
            }};

-------------------FOUR PILLARS OF OBJECT ORIENTED PROGRAMMING----------------------

 -Inheritance. One class takes on the attributes of another.
       class derived-class: access-specifier base-class

        class BaseClass{
        //code for this class here
        };
    //Now the derived/child class
        class DerivedClass: public BaseClass{
        };

    -Multilevel inheritance.
        class MyClass;
        class MyChild: pblic MyClass;
        class MyGrandChild: public MyChild;

    -Multiple inheritance.
        class MyChildClass: public MyClass, public MyOtherClass;

 -Encapsulation. Hiding information away from user.
      This usually takes the form of accessing values of a class through functions called
      access functions

        #include <iostream>

        class Something
        {private:    //This is private so it doesn't get changed from outside
              int m_value[3]; // note: we changed the implementation of this class!
         public:
              // We have to update any member functions to reflect the new implementation
              void setValue1(int value) { m_value[0] = value;}
              int getValue1() { return m_value[0]; }
    };

          int main()
          {// But our program still works just fine!
              Something something;
              something.setValue1(5);
              std::cout << something.getValue1() << '\n';};

 -Polymorphism. Use methods from derived classes to perform different tasks.

        class Animal {    //base class
          public:c++
            void animalSound(){
            std::cout << "The animal makes a sound \n"}};

        class Dog : public Animal {   //derived class
          public:
            void animalSound() {   //Same method as Animal Class
            std::cout << "The dog says: bow wow \n";}};

    When we call .animalSound from each class we will get the corresponding

 -Abstraction. Only display essential info and hide the rest.



-------------------------------------STRUCTS-----------------------------------------
  -Struct. group of data elements together under one name.
     Like a class but simplified and public as default.

      struct nameOfStruct {
        int x;
        double y;}
    You can then call objects with attributes of the structure.
      nameOfStruct obj;
        obj.x = 20  //sets the attribute of obj struct

    Create an array of from struct
        struct Rectangle {
            int length{};
            int width{};};

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
  //To set a derived class you need a : to classify it.
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

---------------------------------OBJECT COMPOSITION-----------------------------------
Object composition deconstructs complex objects into smaller parts.;
"Has-a" relationship. A car "has-a" transmission. Computer "has-a" project;
Complex object = whole, parent.
Simpler object = part, child, component.

To qualify as a composition, an object and a part must have the
 following relationship:
    The part:
        is part of the object (class).
        can only belong to one object (class) at a time.
        has its existence managed by the object (class).
        does not know about the existence of the object (class).

---------------------------------HEADER FILES-----------------------------------------
Files that have functions that you can forward declare.;
 These files are at top of the file. May have a .h or .hpp extension.
    #include <iostream>        //pre-defined c++ header
    #incldue "file_here.h"     //manually-created header file

  -Guards. Stop duplicating same function from different sources
     #ifndef FILE_NAME_HERE
     #define FILE_NAME_HERE
       //declarations
     #endif

  -Logging. Logging is sending debugging information to a file that
  records events in software called a log file.
        #include <plog/Log.h>
        #include <plog.Initializers/RollingFileInitializer.h>

------------------------------------FILES-------------------------------------------
You can modify delete or create new files with c++
#include <iostream>    //Need this
#include <fstream>     //Need this too.

 -Write files with ofstream.

    int main() {
       ofstream MyFile("filename.txt"); //create and open A NEW file
       MyFile << "blah blah whatever the fuck"; //write file
       MyFile.close();}  //close file

 -Read files with ifstream.

    string myText;   //create text string
    ifstream MyReadFile("filename.txt");  //read text file
 // Use a while loop together with the getline() function to read each line
    while (getline (MyReadFile, myText)) { // Output the text from the file
      cout << myText;}
     MyReadFile.close();   // Close the file

---------------------------STANDARD TEMPLATE LIBRARY---------------------------------
A collection of classes that provide templated containers,  algorithms, iterators

Containers

 -Deque class. Double-ended queue class that can grow from both ends;
 #include <deque>

------------------------------------RAII----------------------------------------------

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

 #include "random.hpp" //add a linker in Project -> Build Option -> Linker Options
 using Random = effolkronium::random_static;
 int main(){
 	 std::cout << Random::get(1, 6) << '\n';
 	 std::cout << Random::get(1, 10) << '\n';
 	 std::cout << Random::get(1, 20) << '\n';
 	 return 0;}
