#include <iostream>
#include <vector> //for vector
#include <algorithm> //for iterator algorithm. find(), begin(), 

int main() 
{
    std::vector<int> VECTORNAME = {     }; //Add numbers
    int key = ;   // CHANGE THIS TO WHAT YOU WANT TO FIND

    std::vector<int>::iterator itr = std::find(VECTORNAME.begin(), VECTORNAME.end(), key); //iterates through vector
    int index = std::distance(VECTORNAME.begin(), itr); 
    
    std::cout << index << std::endl; //finds index of key
    std::cout << VECTORNAME[index] << std::endl;
    v.erase(VECTORNAME.begin() + index);


    return 0;
}
