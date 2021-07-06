C++ tips:
You can import librarys like in Python.
#include <iostream>
using namespace std
#include <string>
#include <cmath>     //include cmath library

-Variables
int          -stores integers.
double,float -stores decimal numbers.
char         -stores single characters only. Uses ''
string       -stores text lines. Uses "". Need to #include <string> library
bool         -True or False vales. 1= true, 0 = false


-Operators
=          -assigns values to variables
+          -adds numbers. Concatenates strings.
-          -subtracts things.
*          -multiplies values
/          -divides values
%          -modulus. Returnes division remainder
++         -increases values by 1
--         -decreases values by 1
&&         -and operator. compares things. Like and in Python
||         -or operator. like in Python.
!          -logical not
::         -scope resolution operator
>          -greater than. Returns true or false
<          -less than.
>=         -greater than or equal to.
<=         -less than or equal to.
==         -is equal to
!=         -not equal to
+=         -adds value to a variables
-=         -subtracts from a variables
*=         -multiplies a variable
&=         -reference equals
|=
^=
>>=
<<=

All comparison operators need to be in (). (~ > ~)

-Syntax
cout <<      -outputs values. works like print() in Python.
return 0;    -Ends the function
<<           -"See out". Output
>>           -"see in". Input
;            -ends statements in C++
\n           -inserts a new line.
\n\n, endl   -creates a blank line
//           -single-line comments. Ignored by compiler. Like # in Python.
/* ~~ */     -multi-line comments. Like """ in Python.
std::        -can bypass the namespace.

-Variable creation
  type identifier = value;
    int myNum = 15;
    cout << myNum;
You can combine variables in one cout sentence
        int myAge = 35;
        cout << "I am " << myAge << " years old.";
Add variables together:
    int x = 5;
    int x = 6;
    int sum = x + y;
    cout << sum;

Declare multiple variables of the dame type.
    int x = 4, y = 5, z = 20;
    cout << x+y+z;

Constants, unchanging variables
    const int myNum = 15;  -use const to make it a constant.

Use e to represent powers of 10 for numbers
    float f1 = 35e3;

Reference operator. &
you can create another variable with the same value as another variable
    string food = "Pizza";
    string &meal = food;

    cout << food << "\n";  // Outputs Pizza
    cout << meal << "\n";  // Outputs Pizza

 Memory addres
  string food = "Pizza";

  cout << &food; // Outputs 0x6dfed4
*************************************************
 Pointer. stores memory address as its value
  string food = "Pizza";  // A food variable of type string
  string* ptr = &food;
 Use *ptr to print out the OG value that is being pointed to.
    *ptr -> 'Pizza'

-User inputs
cin >>   -Use cin to get user input. Like input() in Python.
 int x;
 cout << "Type a number: ";
 cin >> x;  //Gets user input from keyboard
 cout << "Your number is: " << x;
If you want to save a line of text to cin use getline(cin, x)
    string fullName;
    cout << "Type your full name: ";
    getline (cin, fullName);
    cout << "Your name is: " << fullName;

Concatenate strings.
Use + to combine different strings. Add a space at end of first string " "
or you can use .appen() as the same thing.

-Indexing strings []
Can access the element at a certain posistio. 0-indexed like Python.
   string myString = "Hello";
   cout << myString[1];
   //Outputs e
-Methods
Methods are built-in functions like python.
x.append(y)  -concatenates y to end of x
x.length()   -gets length of x
max(x,y,..)  -returns the largest number of x or y
max(x,y,..)  -returns the smallest number of x or y

-Conditional statements
if       -block of code is run if condition is true
else     -runs if same condition is false
else if  -runs if first condition is false
switch   -specify many alternative blocks of code to be executed

if (condition1) {//block of code run if true
} else if (condition2){//block of code if condition1 is false
} else { //block of code run if all are false
}
Ternary ? operator as shortcut for if else
    (condition) ? expressionTrue : expressionFalse
  string result = (x < 18) ? "x is illegal." : "x is legal.";
Switch syntax
switch(parameter) {    //loops through cases
  case x:
    // code block if x == parameter
    break;   //stops the loop
  case y:
    // code block if y == parameter
    break;
  default:
    // code block if nothing == parameter
}
switch will evaluate an expression and will run the case that mathces it.

-Loops, for and while
While loops will run forever unless a condition is met.
int i = 0;
while (i < 5) {
  cout << i << "\n";
  i++;   //increases i every time. Then restarts the loop
}

Do/While loop
will run code block once, checks if condition is true, and will continue
to loop if the condition is true.
do {
  // code block to be executed
}
while (condition);  //runs if do == true

For loop. More control over loop. (starting; while condition; change)
for (int i = 0; i < 5; i++) {
  cout << i << "\n";
}

You can combine for, if, and break to stop a loop at a condition
for (int i = 0; i < 10; i++) {
  if (i == 4) {
    break;     //stops the loop entirely
  }
  cout << i << "\n";
}
continue. skips the iteraion if a condition is met. goes to the next iteration
for (int i = 0; i < 10; i++) {
  if (i == 4) {
    continue;
  }
  cout << i << "\n";
}

-Arrays/lists. Uses {}
create arrays using [x]. x = how long it is. Need to be the same elem type.
int myNum[3] = {10,20,30}
change the value of an elem in a certain index the same way in python.
cars[0] = "New value"

you can loop through an arryay.
string cars[4] = {"Volvo", "BMW", "Ford", "Mazda"};
for(int i = 0; i < 4; i++) {
  cout << i << ": " << cars[i] << "\n";}

Omit elements on declaration
string cars[5];
cars[0] = "Volvo";
cars[1] = "BMW";
...

-Functions
functions are blocks of code that do specific things. Only when called.
    void functionName(parameter1, parameter2) { //declaration
    //code to run. body of funtion    (definition)
    }   //void returns nothing
  To call a function you need to put it inside main() function
     int main() {
     functionName();
     return 0;
     }
  functions must be DECLARED BEFORE they are called. But they have to
  be defined after the main function.

  Functions can have parameters that are variables within the function.
  They can be anythin. Just like python

     void myFunction(string fname) {
      cout << fname << " Refsnes\n";}

    int main() {
      myFunction("Liam"); //function will output "Liam"
      return 0;}

   -Default variable
   You can add a default variable using =. If the function has no argument
   when it's called it used the default variables.
        void myFunction(string country = "Norway") {
          cout << country << "\n";}

        int main() {
          myFunction("Sweden"); //outputs Sweden
          myFunction();    //outputs Norway
          return 0;}
  -Return values. If you want the function to return something you have
  to change the type of the function and enter what you want to return
      int myFunction (int x, int y){
      return y + x;}

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

-Classes and Objects
 A class is a blueprint of objects. Think class as car and object as Volvo
 You can create multiple objects
     class Car {
      public:   //access specifier. How methods can be accessed.
        string brand;
        string model;
        int year;    };
    int main() {
      // Create an object of Car

      //ClassName objName\\

      Car carObj1;
      carObj1.brand = "BMW";
      carObj1.model = "X5";
      carObj1.year = 1999;

      // Create another object of Car
      Car carObj2;
      carObj2.brand = "Ford";
      carObj2.model = "Mustang";
      carObj2.year = 1969;
      return 0;}
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

  -Constructor. Special method called when object of class is created.
    Use same name as class followed by (). **Think self in Python**
        class Car {        // The class
          public:          // Access specifier
            string brand;  // Attribute
            string model;  // Attribute
            int year;      // Attribute
            Car(string x, string y, int z) {  // Constructor with parameters
              brand = x;  //plug in stuff like a function into constructor.
              model = y;  //Each object will have all the same attributes
              year = z;}};  //but with what is entered as parameters.
        int main() {
          // Create Car objects and call the constructor with different values
          Car carObj1("BMW", "X5", 1999);
          Car carObj2("Ford", "Mustang", 1969);
          // Print values
          cout << carObj1.brand << " " << carObj1.model << " " << carObj1.year << "\n";
          cout << carObj2.brand << " " << carObj2.model << " " << carObj2.year << "\n";
          return 0;}
   You can also define constructor outside of class
    Car::Car(string x, string y, int z) {
      brand = x;
      model = y;
      year = z;}

-Access specifiers.
How member of a class can be accessed.
 -public    -members accessible from outside class
 -private   -members cannot be accessed from outside class.    Default.
 -protected -cannot be accessed outside class, but can be in inherited classes

    class MyClass {
      public:    // Public access specifier
        int x;   // Public attribute
      private:   // Private access specifier
        int y;   // Private attribute
    };

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

-Exceptions
These are errors. Uses three keywords:
    try    -define a block of code to be tested
    throw  -creates exception when problem is detected. goes to catch
    catch  -lets you define a new block of code if error is in try block.
  try and catch come in pairs. Like try and except in Python.
     try {    
         // Block of code to try
       throw exception;}  // Throw an exception when a problem arise
     catch () {
     // Block of code to handle errors
     } 
