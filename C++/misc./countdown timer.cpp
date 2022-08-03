//                         Option 1. 

#include <iostream>     // std::cout, std::endl
#include <thread>       // std::this_thread::sleep_for
#include <chrono>       // std::chrono::seconds

int main()
{
  std::cout << "countdown:\n";
  for (int i=10; i>0; --i) {
    std::cout << i << std::endl;
    std::this_thread::sleep_for (std::chrono::seconds(1)); //pauses for 1 second
  }
  return 0;}

//                         Option 2.

#include <iostream>
#include <Windows.h> // Need this for Sleep(milliseconds) function

int main() {
    for (int i = 10; i > 0; i-- ){
        std::cout << i << std::endl;
        Sleep(1000); 
        system("CLS");
    }}
