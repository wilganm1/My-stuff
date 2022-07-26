#include <iostream>
#include <chrono>
#include <vector>
#include <algorithm>
#include <cstdlib>

/* The player will be Xs and the computer will be Os.
There will be 9 positions. Each time the player or computer
makes a move that position will be used up

Have random number to decide who goes first. Binary choice
1 = player, 0 = computer.

Make an array of blank spaces that will be switched

Each time a position is picked I need to eliminate it from being picked again.
Can make a separate array that has values removed every time a position is picked.
*/

void print(std::vector<int> const &input){
    for (auto const &i: input) {
        std::cout << i << " ";
    }
}

std::vector<int> open_positions = {1,2,3,4,5,6,7,8,9};
std::vector<char> pst = {' ',' ',' ',' ',' ',' ',' ',' ',' '};

//Using this array will keep everything the same until it gets changed
//after each play.

//Make game board
void gameBoard(){   //need to pass entire array as argument. Use a pointer
    system("CLS");
    std::cout << "\n\n";
    std::cout << "\t\t   1    2    3" <<std::endl;
    std::cout << "\t\t      |   |     " << std::endl;
    std::cout << "\t\t   " << pst[0]<<"  | pst[1]|  p3  " << std::endl;
    std::cout << "\t\t _____|___|_____" << std::endl;
    std::cout << "\t\t      |   |     " << std::endl;
    std::cout << "\t\t4  p4 | p5| p6   6" << std::endl;
    std::cout << "\t\t _____|___|_____" << std::endl;
    std::cout << "\t\t      |   |     " << std::endl;
    std::cout << "\t\t   p7 | p8| p9  " << std::endl;
    std::cout << "\t\t      |   |     " << std::endl;
    std::cout << "\t\t   7    8    9";
}

//function to choose position

void playerSelection(){ //player
    p_select:
        std::cout << "\nPlease select an open space: ";
        int player_selection{};
        std::cin >> player_selection;
        if (std::cin.fail()){  //will catch if goal is not an integer
            std::cout << "Not an number. Try again." << std::endl;
            std::cin.clear();  //will erase the cin input
            std::cin.ignore(10000, '\n');
            goto p_select;}
        else {
            pst[player_selection - 1] = 'X'; // -1 so the indices work out between 2 vectors
            std::vector<int>::iterator itr = std::find(open_positions.begin(), open_positions.end(), player_selection - 1);
            int index = std::distance(open_positions.begin(), itr);
            std::cout << index << std::endl; //finds index of key
            std::cout << open_positions[index] << std::endl;
            open_positions.erase(open_positions.begin() + index);
        }
}

void computerSelection(){
    int comp_select = rand() % open_positions.size();
    int sel_elem = open_positions[comp_select];
    pst[sel_elem - 1] = 'O';
    std::vector<int>::iterator itr = std::find(open_positions.begin(), open_positions.end(), sel_elem -1);
    int index = std::distance(open_positions.begin(), itr);
    std::cout << index << std::endl; //finds index of key
    std::cout << open_positions[index] << std::endl;
    open_positions.erase(open_positions.begin() + index);
}


int main(){

    return 0;
}
