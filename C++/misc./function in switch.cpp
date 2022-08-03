//You can use a bool function as an expression for a switch function

#include <iostream>
#include "random.hpp"
using Random = effolkronium::random_static; //used for random numbers

bool functionName(){
    return (Random::get<bool>()); // true with 50% probability by default
}

int main(){
    switch (functionName()){  //calling the function returns a 0 or 1.
        case 0: //false
            std::cout << "Got a zero" << std::endl;
            break;
        case 1: //true
            std::cout << "Got a one" << std::endl;
            break;}
    return 0;
}
