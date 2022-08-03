#include <iostream>
#include <vector>
#include <algorithm> // Iterator for vector
#include <cstdlib> //rand() and srand().
#include "random.hpp"   //better at guessing random numbers

using Random = effolkronium::random_static;

/* The player will be Xs and the computer will be Os.
There will be 9 positions. Each time the player or computer
makes a move that position will be used up.
Have random number to decide who goes first. Binary choice
1 = player, 0 = computer.
Make a vector of blank spaces that will be switched
Each time a position is picked I need to eliminate it from being picked again.
Can make a separate vector that has values removed every time a position is picked.
*/

std::vector<int> open_positions = {1,2,3,4,5,6,7,8,9};
std::vector<char> pst = {' ',' ',' ',' ',' ',' ',' ',' ',' '};


void print(std::vector<int> const &open_positions){
    for (auto const &i: open_positions) {
        std::cout << i << " ";
    }
}

void board(){   //need to pass entire array as argument. Use a pointer
    system("CLS");
    std::cout << "\n\n";
    std::cout << "\t\t   1    2    3" <<std::endl;
    std::cout << "\t\t      |   |     " << std::endl;
    std::cout << "\t\t   " << pst[0]<<"  | " << pst[1] <<" |  " << pst[2] << std::endl;
    std::cout << "\t\t _____|___|_____" << std::endl;
    std::cout << "\t\t      |   |     " << std::endl;
    std::cout << "\t\t4  " << pst[3]<<"  | " << pst[4] <<" |  " << pst[5] << "  6 " << std::endl;
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
    print(open_positions);
    std::cout << std::endl;
    int player_selection{};
    std::cin >> player_selection;
    if (std::cin.fail()){  //will catch if goal is not an integer
        std::cout << "Not an number. Try again." << std::endl;
        std::cin.clear();  //will erase the cin input
        std::cin.ignore(10000, '\n');
        goto p_select;}
    else {
        pst[player_selection - 1] = 'X'; // -1 so the indices work out between 2 vectors
        std::vector<int>::iterator itr = std::find(open_positions.begin(), open_positions.end(), player_selection);
        int index = std::distance(open_positions.begin(), itr);
        open_positions.erase(open_positions.begin() + index);}
}

void computerSelection(){
    srand(time(0));  // NEED THIS
    int comp_select = std::rand() % (open_positions.size() + 1);
    int sel_elem = open_positions[comp_select - 1];
    pst[sel_elem - 1] = 'O';
    std::vector<int>::iterator itr = std::find(open_positions.begin(), open_positions.end(), sel_elem);
    int index = std::distance(open_positions.begin(), itr);
    open_positions.erase(open_positions.begin() + index);
    board();
}

//function who goes first
    bool whoGoesFirst(){
        return (Random::get<bool>()); // true with 50% probability by default
}

//need a function to determine who wins. Will stop the game if someone does
bool aWinner() {
    if (pst[0] == 'X' && pst[1] == 'X' && pst[2] == 'X' || pst[3] == 'X' && pst[4] == 'X' && pst[5] == 'X' || pst[6] == 'X' && pst[7] == 'X' && pst[8] == 'X') {
        board();
        std::cout << "\nYou win!. Horizontal" << std::endl;
        return true;}
    else if (pst[0] == 'X' && pst[3] == 'X' && pst[6] == 'X' || pst[1] == 'X' && pst[4] == 'X' && pst[7] == 'X' || pst[2] == 'X' && pst[5] == 'X' && pst[8] == 'X') {
        board();
        std::cout << "\nYou win!. Vertical" << std::endl;
        return true;}
    else if (pst[0] == 'X' && pst[4] == 'X' && pst[8] == 'X' || pst[2] == 'X' && pst[5] == 'X' && pst[6] == 'X') {
        board();
        std::cout << "\nYou win! Diagonal" << std::endl;
        return true;}
    else if (pst[0] == 'O' && pst[1] == 'O' && pst[2] == 'O' || pst[3] == 'O' && pst[4] == 'O' && pst[5] == 'O' || pst[6] == 'O' && pst[7] == 'O' && pst[8] == 'O') {
        board();
        std::cout << "\nComputer wins!. Horizontal" << std::endl;
        return true;}
    else if (pst[0] == 'O' && pst[3] == 'O' && pst[6] == 'O' || pst[1] == 'O' && pst[4] == 'O' && pst[7] == 'O' || pst[2] == 'O' && pst[5] == 'O' && pst[8] == 'O') {
        board();
        std::cout << "\nComputer wins!. Vertical" << std::endl;
        return true;}
    else if (pst[0] == 'O' && pst[4] == 'O' && pst[8] == 'O' || pst[2] == 'O' && pst[4] == 'O' && pst[6] == 'O') {
        board();
        std::cout << "\nComputer wins! Diagonal" << std::endl;
        return true;}
    else {
        return false;}
}

int main(){
    std::vector<int> open_positions = {1,2,3,4,5,6,7,8,9};
    std::vector<char> pst = {' ',' ',' ',' ',' ',' ',' ',' ',' '};
    switch (whoGoesFirst()){
        case 0: //false. Player first
            while (!aWinner()){
                board();
                playerSelection();
                computerSelection();}
            break;
        case 1: //true. Computer first
            while (!aWinner()){
                board();
                playerSelection();
                computerSelection();}
            break;
    }

    return 0;
}
