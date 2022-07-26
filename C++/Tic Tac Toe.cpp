#include <iostream>
#include <chrono>
#include <vector>
#include <algorithm>
#include <cstdlib>

/* The player will be Xs and the computer will be Os.
There will be 9 positions. Each time the player or computer
makes a move that position will be used up.
Have random number to decide who goes first. Binary choice
1 = player, 0 = computer.
Make a vector of blank spaces that will be switched
Each time a position is picked I need to eliminate it from being picked again.
Can make a separate vector that has values removed every time a position is picked.
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

void board(){   //need to pass entire array as argument. Use a pointer
    system("CLS");
    std::cout << "\n\n";
    std::cout << "\t\t   1    2    3" <<std::endl;
    std::cout << "\t\t      |   |     " << std::endl;
    std::cout << "\t\t   " << pst[0]<<"  | " << pst[1] <<" |  " << pst[2] << std::endl;
    std::cout << "\t\t _____|___|_____" << std::endl;
    std::cout << "\t\t      |   |     " << std::endl;
    std::cout << "\t\t4   " << pst[3]<<" | " << pst[4] <<" |  " << pst[5] << "  6 " << std::endl;
    std::cout << "\t\t _____|___|_____" << std::endl;
    std::cout << "\t\t      |   |     " << std::endl;
    std::cout << "\t\t   " << pst[6]<<"  | " << pst[7] <<" |  " << pst[8] << std::endl;
    std::cout << "\t\t      |   |     " << std::endl;
    std::cout << "\t\t   7    8    9";
}

//Make game board
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
        open_positions.erase(open_positions.begin() + index);}
}

void computerSelection(){
    std::srand(time(0));
    int comp_select = std::rand() % open_positions.size();
    int sel_elem = open_positions[comp_select];
    pst[sel_elem - 1] = 'O';
    std::vector<int>::iterator itr = std::find(open_positions.begin(), open_positions.end(), sel_elem -1);
    int index = std::distance(open_positions.begin(), itr);
    open_positions.erase(open_positions.begin() + index);
    board();
}

void playerScore(){
    //Player score first
    if (pst[0],pst[1],pst[2] == 'X','X','X' || pst[3],pst[4],pst[5] == 'X','X','X' || pst[6],pst[7],pst[8] = 'X','X','X'){ //Horizontal
        std::cout << "\nYou Win! Horizontal Run!" << std::endl;}
    else if (pst[0],pst[3],pst[6] == 'X','X','X' || pst[1],pst[4],pst[7] == 'X','X','X' || pst[2],pst[5],pst[8] = 'X','X','X'){  //Vertical
        std::cout << "\nYou Win! Vertical Run!" << std::endl;}
    else if (pst[0],pst[4],pst[8] == 'X','X','X' || pst[2],pst[4],pst[6] == 'X','X','X'){  //Diagonal
        std::cout << "\nYou Win! Diagonal Run!" << std::endl;}
    else {};
}

void computerScore(){
    if (pst[0],pst[1],pst[2] == 'O','O','O' || pst[3],pst[4],pst[5] == 'O','O','O' || pst[6],pst[7],pst[8] = 'O','O','O'){ //Horizontal
        std::cout << "\nYou Win! Horizontal Run!" << std::endl;}
    else if (pst[0],pst[3],pst[6] == 'O','O','O' || pst[1],pst[4],pst[7] == 'O','O','O' || pst[2],pst[5],pst[8] = 'O','O','O'){  //Vertical
        std::cout << "\nYou Win! Vertical Run!" << std::endl;}
    else if (pst[0],pst[4],pst[8] == 'O','O','O' || pst[2],pst[4],pst[6] == 'O','O','O'){  //Diagonal
        std::cout << "\nYou Win! Diagonal Run!" << std::endl;}
    else {};
}


//Function to get score. Needs to check every single combination. 8 in total

int main(){
    //Start a function that will determine who goes first
    std::vector<int> open_positions = {1,2,3,4,5,6,7,8,9};
    std::vector<char> pst = {' ',' ',' ',' ',' ',' ',' ',' ',' '};
    while (open_positions.size() > 0){
        board();
        playerSelection();
        playerScore();
        computerSelection();
        computerScore();
}

    return 0;
}
