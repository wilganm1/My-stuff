#include <iostream>
#include <vector> //for vector
#include <algorithm> //for iterator algorithm. find(), begin(), 

int main() 
{
    std::vector<int> v = { }; //Add numbers
    int key = ;   // CHANGE THIS TO WHAT YOU WANT TO FIND

    std::vector<int>::iterator itr = std::find(v.begin(), v.end(), key); //iterates through vector
    int index = std::distance(v.begin(), itr); 
    
    std::cout << index << std::endl; //finds index of key
    std::cout << v[index] << std::endl;
    v.erase(v.begin() + index);


    return 0;
}
