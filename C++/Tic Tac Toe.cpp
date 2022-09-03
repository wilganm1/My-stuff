#include <iostream>
#include <vector>  //to create vectors
#include <algorithm> // for .begin() and .end() for vectors
#include <cstdlib> //rand() and srand().
#include "random.hpp"   //better at guessing random numbers

using Random = effolkronium::random_static;

bool checksSpaces(std::vector<int>ops, int choice){ //function to correct if the player enters a space that is not available. Otherwise stops the game.
    if (std::find(ops.begin(), ops.end(), choice) != ops.end()) {
        return true;}
    else {
        return false;}
}

void print(std::vector<int> const &ops){  //found online. prints out available positions
    for (auto const &i: ops) {
        std::cout << i << " ";}
}

void board(std::vector<char>& vec){
    system("CLS");
    std::cout << "\n\n";
    std::cout << "\t\t   7    8    9" <<std::endl;
    std::cout << "\t\t      |   |     " << std::endl;
    std::cout << "\t\t   " << vec[6]<<"  | " << vec[7] <<" |  " << vec[8] << std::endl;
    std::cout << "\t\t _____|___|_____" << std::endl;
    std::cout << "\t\t      |   |     " << std::endl;
    std::cout << "\t\t4  " << vec[3]<<"  | " << vec[4] <<" |  " << vec[5] << "  6 " << std::endl;
    std::cout << "\t\t _____|___|_____" << std::endl;
    std::cout << "\t\t      |   |     " << std::endl;
    std::cout << "\t\t   " << vec[0]<<"  | " << vec[1] <<" |  " << vec[2] << std::endl;
    std::cout << "\t\t      |   |     " << std::endl;
    std::cout << "\t\t   1    2    3";
}

void playerSelection(std::vector<int>& op, std::vector<char>& vec){ //Picking a spot
    p_select:
        std::cout << "\nPlease select an open space: ";
        print(op);
        std::cout << std::endl;
        int player_selection{};
        std::cin >> player_selection;
        if (checksSpaces(op, player_selection)) {
            vec[player_selection - 1] = 'X'; // -1 so the indices work out between 2 vectors
            std::vector<int>::iterator itr = std::find(op.begin(), op.end(), player_selection);
            int index = std::distance(op.begin(), itr);
            op.erase(op.begin() + index);}
        else if (!checksSpaces(op, player_selection)){
            std::cout << "Invalid. Try again." << std::endl;
            std::cin.clear();  //will erase the cin input
            std::cin.ignore(10000, '\n');
            goto p_select;}
}

void computerSelection(std::vector<int>& op, std::vector<char>& vec){
    srand(time(0));  // NEED THIS for random every time
    int comp_select = std::rand() % (op.size());
    int sel_elem = op[comp_select];
    vec[sel_elem - 1] = 'O'; // -1 so the indices work out between 2 vectors
    std::vector<int>::iterator itr = std::find(op.begin(), op.end(), sel_elem);
    int index = std::distance(op.begin(), itr);
    op.erase(op.begin() + index);
}

bool whoGoesFirst(){  // coin flip for who goes first
    return (Random::get<bool>()); // true with 50% probability by default
}

bool aWinner(std::vector<char>vec) { //determines a winner
    if (vec[0] == 'X' && vec[1] == 'X' && vec[2] == 'X' || vec[3] == 'X' && vec[4] == 'X' && vec[5] == 'X' || vec[6] == 'X' && vec[7] == 'X' && vec[8] == 'X') {
        std::cout << "\nYou win! Horizontal" << std::endl;
        return false;}
    else if (vec[0] == 'X' && vec[3] == 'X' && vec[6] == 'X' || vec[1] == 'X' && vec[4] == 'X' && vec[7] == 'X' || vec[2] == 'X' && vec[5] == 'X' && vec[8] == 'X') {
        std::cout << "\nYou win! Vertical" << std::endl;
        return false;}
    else if (vec[0] == 'X' && vec[4] == 'X' && vec[8] == 'X' || vec[2] == 'X' && vec[4] == 'X' && vec[6] == 'X') {
        std::cout << "\nYou win! Diagonal" << std::endl;
        return false;}
    else if (vec[0] == 'O' && vec[1] == 'O' && vec[2] == 'O' || vec[3] == 'O' && vec[4] == 'O' && vec[5] == 'O' || vec[6] == 'O' && vec[7] == 'O' && vec[8] == 'O') {
        std::cout << "\nComputer wins! Horizontal" << std::endl;
        return false;}
    else if (vec[0] == 'O' && vec[3] == 'O' && vec[6] == 'O' || vec[1] == 'O' && vec[4] == 'O' && vec[7] == 'O' || vec[2] == 'O' && vec[5] == 'O' && vec[8] == 'O') {
        std::cout << "\nComputer wins! Vertical" << std::endl;
        return false;}
    else if (vec[0] == 'O' && vec[4] == 'O' && vec[8] == 'O' || vec[2] == 'O' && vec[4] == 'O' && vec[6] == 'O') {
        std::cout << "\nComputer wins! Diagonal" << std::endl;
        return false;}
    else {
        return true;}
}

int main(){
    while(true){
        std::vector<int> open_positions = {1,2,3,4,5,6,7,8,9};  //I need to make these the ones that are used in functions
        std::vector<char> pst = {' ',' ',' ',' ',' ',' ',' ',' ',' '}; //Pass them by reference in other functions
        board(pst);
        switch (whoGoesFirst()){
            case 0: //false. Player first
                while (aWinner(pst) && open_positions.size() != 0){
                    board(pst);
                    std::cout << "\nYou go first" << std::endl;
                    playerSelection(open_positions, pst);
                    if (aWinner(pst) && open_positions.size() != 0){ //Need this so the game stops at the moment someone wins
                        computerSelection(open_positions, pst);}
                    else {
                        board(pst);
                        aWinner(pst);
                        break;}}
                break;
            case 1: //true. Computer first
                while (aWinner(pst) && open_positions.size() != 0){
                    computerSelection(open_positions, pst);
                    board(pst);
                    std::cout << "\nComputer goes first" << std::endl;
                    if (aWinner(pst) && open_positions.size() != 0){
                        playerSelection(open_positions, pst);}
                    else {
                        board(pst);
                        aWinner(pst);
                        break;}}
                break;}
        if (open_positions.size() == 0){
            std::cout << "No one wins.\n";
        }
        std::cout << "Play again? (y/n): ";
        char retry{};
        std::cin >> retry;
        if (retry == 'y'){}
        else {
            break;}}
    return 0;
}
