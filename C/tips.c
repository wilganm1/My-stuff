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


--------------------------------------------------------------------------------

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
                
Enums

