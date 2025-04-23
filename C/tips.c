---------------------------------BASICS---------------------------------
Main function to run a program

#include <stdio.h>

int main() {

    return 0;
}

printf();    - prints to console
\n           - starts new line
\nn          - adds a line break
\t           - tab.

Loading libraries

#include <library>

-Basic syntax
;     - ends line of code
()    - used in functions. Sets parameters
{}    - Executable code within functions
""    - Used for plain text. Strings.
//    - single line comments/ Ignored by compiler
/* */ - multi line comments
+     - addition operator
-     - subtraction
*     - multiplication
/     - division
%     - modulus
++    - increment by 1
--    - decrement by 1
=     - assignment
+=    - adds to value
-=    - subtracts from value
*=    - multiplies value
/=    - divides value
%=    - modulus value
>     - greater than
<     - less than
==    - is equal to
!=    - not equal to
>=    - greater than or equal to
<=    - less than or equal to
&&    - logical AND operator
||    - logical OR operator
!     - logical NOT operator

- User input. Uses reference operator &

                scanf(format_specifier, &variable)

    String input

                fgets(stringVar, sizeof(stringVar), stdin);

------------------------------------VARIABLES----------------------------------------
Variables hold information to be used for stuff. Type must be defined.

Data types:

    int     - Whole numbers. (1,69,420)
    float   - decimal numbers. (14.88). 7 decimal points
    double  - decimal numbers. 15 decimal places.
    char    - single characters. ('a','z')
    bool    - true (1) or false (0)

To declare a variable, specify the type and assign it a value

        type variable_Name = value;

        int number = 15;

        int x = 5, y = 6, z = z;  //declare multiple variables
        int x,y,z;
        x = y = z = 50;           //Make multiple variables the same value
        float f1 = 35e3           //scientific notation

    use const keyword to make it immutable


To print out variables, you must use a FORMAT SPECIFIER inside printf().
    They must be inside double quotes "".

            printf("format specifier", variable)
-Specifiers
"%d","%i"  - int      printf("%d", number )
"%c"       - char
"%f"       - float
"%lf"      - double
"%s"       - string
"%p"       - pointer

To concatenate plain text and variables, separate them with a comma ,
        printf("My favorite number is: %d", myNum);

        int myNum = 15;
        char myLetter = 'D';
        printf("My number is %d and my letter is %c", myNum, myLetter);

You don't have to store variables if you use correct format specifier.
        printf("Number is: %d", 15);

Add variables together using + operator:
    int x = 5;
    int y = 6;
    int sum = x + y;
    printf("%d", sum);  // prints out 11

    Only show certain number of digits after decimal points

    printf("%f.nf")   - n is the number of digits

Type conversion
    - Manual conversion - use (type) to convert

        float sum = (float) 5/2;   // sum now equals 2.5

- Boolean variables
#include <stdbool.h>  //need to import this

 Variables are either true (1) or false (0). uses "%d" to printf()

            bool isSkyBlue = true;

Use == operator to determine if two values are same. will return integer 0 or 1.

- Arrays. Stores multiple values of same data type. Uses square brackets []

            data_type arrayName[] = {value1,value2,value3,...};

  -Indexing arrays. C language is zero-indexed. First value has index of 0.

                 arrayName[0] == value1;
                 arrayName[1] == value2;

  Can retroactively change an element's value in an aray using =

                 arrayName[2] = newValue;

  Array size manually set inside brackets -- [n]

        "%lu", sizeof(x);

-Multidimensional arrays

                int matrix[2][3] = {{1,4,2}, {3.6.8}};

    indexing works the same.

-Strings.
 #include <string.h>
  There is not string data type in C. So you make an array of chars. Uses ""

             char string[] = "Hello World!";

             printf("%s", string);

  Do use quotes inside strings use backslash \ before quotes.

 String methods using string.h

  strlen()   - length of string. returns int
  sizeof()   - size of string. returns int
  strcat()   - combine two strings
  strcpy()   - copies string
  strcmp()   - compares strings


Structures hold many different variables of any data type

        struct MyStructure {   // Structure declaration
          int myNum;           // Member (int variable)
          char myLetter;       // Member (char variable)
        }; // End the structure with a semicolon

To access a member of a struct use the period operator .

                // Create a structure called myStructure
                struct myStructure {
                  int myNum;
                  char myLetter;
                };

                int main() {
                  // Create a structure variable of myStructure called s1
                  struct myStructure s1;

                  // Assign values to members of s1
                  s1.myNum = 13;

                  // Print values
                  printf("My number: %d\n", s1.myNum);

                  return 0;
                }

 -Enums. A special type that represents a group of constants
    Like dictionarys in Python.

                enum enumName {
                  LOW = 25,
                  MEDIUM = 50,
                  HIGH = 75
                };
            These items can be set to any data type
    Items in an enum have a default value of what an index would be.
     So the 1st item in an enum has a value of 0, 2nd of 1, 3rd of 2.

    To access an item in an enum, call it then set a variable equal to one
    of its values

                enum enumName variable = MEDIUM;

------------------------------------CONDITIONALS------------------------------------
Conditionals carry out operations based on whether certain conditions are met.

C uses statements to handle conditions

        if (condition1) {
            //block of code executed if condition is true
        } else if (condition2){
            //block of code executed if condition1 is false and condition 2 is true
        } else {
            //block of code executed if all previous conditions false
        }

Switch statement. Basically a giant if else if statement

        switch (expression){
        case x:
            // code block
            break;
        case y:
            // code block
            break;
        default:
            // code block
        }


 The cases act as ifs. break stops the execution. default is optional and acts as final else.

 ------------------------------------LOOPS ------------------------------------
 Loops repeat code while a based on certain conditions

 While loop - alwyas runs while condition is true

        while (conditon) {
            // code to be executed
        }

 do/while loop - executes code block once before checking condition.

        do {
            // code to be execute
        }
        while (condition);

    ******WARNING. ALWAYS HAVE A WAY TO BREAK THE LOOP OR IT WILL BE INFINITE******

 For loop - used for a specific number of loops

         for (expression 1; expression 2; expression 3) {
            // code block to be executed
          }

Expression 1 is executed (one time) before the execution of the code block.
Expression 2 defines the condition for executing the code block.
Expression 3 is executed (every time) after the code block has been executed.

        -Example:
            int i;
            for (i = 0; i < 5; i++) {
              printf("%d\n", i);  // will print out 1 through 5, one per line.
            }
  -Nested loops - loops inside other loops

            int i, j;
            // Outer loop
            for (i = 1; i <= 2; ++i) {
              printf("Outer: %d\n", i);  // Executes 2 times

              // Inner loop
              for (j = 1; j <= 3; ++j) {
                printf(" Inner: %d\n", j);  // Executes 6 times (2 * 3)
              }
            }
   - break keyword. Used to stop a loop if condition is met

                    int i;

                    for (i = 0; i < 10; i++) {
                      if (i == 4) {
                        break; // ends at 4

    - continue. Skips current iteration in loop in condition met. Continues loop.

                    int i;

                    for (i = 0; i < 10; i++) {
                      if (i == 4) {
                        continue;  // skips 4


--------------------------------FUNCTIONS--------------------------------
Fucntions do things when they are called

        dataType myFunction(data type parameter 1, data type parameter 2) {
            // code to be executed
        }

To call them simply type their name.

                myFunction();

The data type of a function depends on it's return type. If it returns nothing
the data type is void.

 Variables can be defined within a function and belong only to it (local scope)

       void calculateSum() {
          int x = 5;
          int y = 10;
          int sum = x + y;
          printf("The sum of x + y is: %d", sum);
      }

Functions can hold parameters which are variables that are passed in from outside the function
Their type and name must be declared when the function is made;

      int CalculateSum(int x, int y){
        int sum = x + y;
        return sum;
      }

      calculateSum(400,20);

- Recursion
                int sum(int k);

                int main() {
                  int result = sum(10);
                  printf("%d", result);
                  return 0;
                }

                int sum(int k) {
                  if (k > 0) {
                    return k + sum(k - 1);
                  } else {
                    return 0;
                  }
                }
#include <math.h>

sqrt()        -square root
ceil()        -round up
floor()       -round down
pow(x,y)      -raises x to power of y
https://www.w3schools.com/c/c_ref_math.php

----------------------------------MEMORY----------------------------------
When variables are created a memory address is assinged to it and its location
is stored on the computer. Use reference operator & to access it.

                int myAge = 43;
                printf("%p", &myAge); // Outputs 0x7ffe5367e044

-Pointer variables*. Stores memory address of another variable as its value.

            int myAge = 43;
            int* ptr = &myAge;

  can also use * on a pointer to dereference it

2 types of memory: static and dynamic

    -Static memory is reserved for variables before runtime. These are hard
    coded variables that exist before the program runs.

     This memory cannot be changed once program runs.

    -Dynamic memory is memory allocated AFTER compilation. You have full
    control over how much memory is being used at any time.

    It can only be accessed with pointers. Use malloc() and calloc()

            int *ptr1 = malloc(size);
                 - size = memory to allocate in bytes
            int *ptr2 = calloc(amount, size);
                 - amount = number of items to allocate
                 - size = size of each item measured in bytes

     The best way to allocate memory for a dat type is to use sizeof

                    int *ptr1, *ptr2;
                    ptr1 = malloc(sizeof(*ptr1));
                    ptr2 = calloc(1, sizeof(*ptr2));


    Reallocate memory

                   int *ptr2 = realloc(ptr1, size)

     if realloc() can't reallocate memory it returns a NULL pointer

                   free(ptr1);  //frees allocated memory

----------------------------------FILES----------------------------------
In C, you can create, open, read, and write to files by declaring a
pointer of type FILE, and use the fopen() function:


        FILE *fptr;
        fptr = fopen(filename, mode);
                               -w    -creates a new file
                               -a    -appends new data to file
                               -r    -reads file
        fclose(fptr)     -closes file

If you want to create the file in a specific folder, just provide an absolute path (\)

        fptr = fopen("C:\\directoryname\\filename.txt", "w");
