#include <iostream>
#include <vector>  //to create vectors
#include <algorithm> // for .begin() and .end() for vectors
#include <cstdlib> //rand() and srand().
#include "random.hpp"   //better at guessing random numbers

using Random = effolkronium::random_static;

std::vector<int> open_positions = {1,2,3,4,5,6,7,8,9};
std::vector<char> pst = {' ',' ',' ',' ',' ',' ',' ',' ',' '};

//function to correct if the player enters a space that is not available. Otherwise stops the game
bool checksSpaces(std::vector<int> vec, int choice){
    if (std::find(vec.begin(), vec.end(), choice) != vec.end()) {
        return true;}
    else {
        return false;}
}

/*void print(std::vector<int> const &open_positions){  //found online. prints out available positions
    for (auto const &i: open_positions) {
        std::cout << i << " ";}
}*/

void board(){
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

void playerSelection(){ //Picking a spot
    p_select:
        std::cout << "\nPlease select an open space: ";
        std::cout << std::endl;
        int player_selection{};
        std::cin >> player_selection;
        if (checksSpaces(open_positions, player_selection)) {;}
        else {
            std::cout << "Space taken. Try again" << std::endl;
            std::cin.clear();  //will erase the cin input
            std::cin.ignore(10000, '\n');
            goto p_select;}
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
    srand(time(0));  // NEED THIS for random every time
    int comp_select = std::rand() % (open_positions.size() + 1);
    int sel_elem = open_positions[comp_select - 1];
    pst[sel_elem - 1] = 'O';
    std::vector<int>::iterator itr = std::find(open_positions.begin(), open_positions.end(), sel_elem);
    int index = std::distance(open_positions.begin(), itr);
    open_positions.erase(open_positions.begin() + index);
}

bool whoGoesFirst(){  // coin flip for who goes first
    return (Random::get<bool>()); // true with 50% probability by default
}

bool aWinner() { //determines a winner
    board();
    if (pst[0] == 'X' && pst[1] == 'X' && pst[2] == 'X' || pst[3] == 'X' && pst[4] == 'X' && pst[5] == 'X' || pst[6] == 'X' && pst[7] == 'X' && pst[8] == 'X') {
        std::cout << "\nYou win! Horizontal" << std::endl;
        return false;}
    else if (pst[0] == 'X' && pst[3] == 'X' && pst[6] == 'X' || pst[1] == 'X' && pst[4] == 'X' && pst[7] == 'X' || pst[2] == 'X' && pst[5] == 'X' && pst[8] == 'X') {
        std::cout << "\nYou win! Vertical" << std::endl;
        return false;}
    else if (pst[0] == 'X' && pst[4] == 'X' && pst[8] == 'X' || pst[2] == 'X' && pst[4] == 'X' && pst[6] == 'X') {
        std::cout << "\nYou win! Diagonal" << std::endl;
        return false;}
    else if (pst[0] == 'O' && pst[1] == 'O' && pst[2] == 'O' || pst[3] == 'O' && pst[4] == 'O' && pst[5] == 'O' || pst[6] == 'O' && pst[7] == 'O' && pst[8] == 'O') {
        std::cout << "\nComputer wins! Horizontal" << std::endl;
        return false;}
    else if (pst[0] == 'O' && pst[3] == 'O' && pst[6] == 'O' || pst[1] == 'O' && pst[4] == 'O' && pst[7] == 'O' || pst[2] == 'O' && pst[5] == 'O' && pst[8] == 'O') {
        std::cout << "\nComputer wins! Vertical" << std::endl;
        return false;}
    else if (pst[0] == 'O' && pst[4] == 'O' && pst[8] == 'O' || pst[2] == 'O' && pst[4] == 'O' && pst[6] == 'O') {
        std::cout << "\nComputer wins! Diagonal" << std::endl;
        return false;}
    else {
        return true;}
}

/*
BUG: Entering in a number randomly crashes the game. It's a Windows memory error. It's a memory access issue. I think it's because the computer
is trying to put in a number that doesn't exist in the vector.
*/

int main(){
    std::vector<int> open_positions = {1,2,3,4,5,6,7,8,9};
    std::vector<char> pst = {' ',' ',' ',' ',' ',' ',' ',' ',' '};
    switch (whoGoesFirst()){
        case 0: //false. Player first
            while (aWinner() && open_positions.size() != 0){
                board();
                std::cout << "\nYou go first" << std::endl;
                playerSelection();
                if (aWinner() && open_positions.size() != 0){ //Need this so the game stops at the moment someone wins
                    computerSelection();}
                else {break;}}
            break;
        case 1: //true. Computer first
            while (aWinner() && open_positions.size() != 0){
                board();
                computerSelection();
                if (aWinner() && open_positions.size() != 0){
                    std::cout << "\nComputer goes first" << std::endl;
                    playerSelection();}
                else {break;}}
            break;}
    std::cout << "Bug" << std::endl;
return 0;
}
