--------------------------------FUNCTIONS--------------------------------
Fucntions do things when they are called

        dataType myFunction(data type parameter 1, data type parameter 2) {
            // code to be executed
        }

To call them simply type their name.

                myFunction();

The data type of a function depends on it's return type. If it returns nothing
the data type is void.
  
 Variables can be defined within a function and belong only to it.

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
