#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

int main() {
    while (1){
        system("CLS");
        srand(time(NULL));
        int player = 0;
        int computer = 0;
        int goal;
        char retry;
        char choices[3] = {'r','p','s'};
        char playerChoice;
        cout << "Rock Paper Scissors. You vs Computer." << "\n\n";
        while(1) {
            cout << "Enter goal: ";
            cin >> goal;
            if (goal < 1){
                cout << "Please enter a positive number." << endl;
            cin.clear();}
            else if (goal > 0) {
                break;}}
        while (player < goal && computer < goal){
                int randIndex = rand() % 3;  //range of 0 to 2.
                cout << "Choose rock, paper or, scissors (r/p/s): ";
                cin >> playerChoice;
                if (playerChoice == choices[randIndex]) {
                    cout << "\nTie." << endl;
                    cout << "Computer: " << computer << endl;
                    cout << "Player: " << player << "\n\n";}
                else if (playerChoice == 'r' && choices[randIndex] == 'p'){
                    cout << "\nComputer picked paper." << endl;
                    cout << "Computer scores a point." << endl;
                    computer++;
                    cout << "Computer: " << computer << endl;
                    cout << "Player: " << player << "\n\n";}
                else if (playerChoice == 'r' && choices[randIndex] == 's'){
                    cout << "\nComputer picked scissors." << endl;
                    cout << "You score a point." << endl;
                    player++;
                    cout << "Computer: " << computer << endl;
                    cout << "Player: " << player << "\n\n";}
                else if (playerChoice == 'p' && choices[randIndex] == 'r'){
                    cout << "\nComputer picked rock." << endl;
                    cout << "You score a point." << endl;
                    player++;
                    cout << "Computer: " << computer << endl;
                    cout << "Player: " << player << "\n\n";}
                else if (playerChoice == 'p' && choices[randIndex] == 's'){
                    cout << "\nComputer picked scissors." << endl;
                    cout << "Computer scores a point." << endl;
                    computer++;
                    cout << "Computer: " << computer << endl;
                    cout << "Player: " << player << "\n\n";}
                else if (playerChoice == 's' && choices[randIndex] == 'r'){
                    cout << "\nComputer picked rock."  << endl;
                    cout << "Computer scores a point." << endl;
                    computer++;
                    cout << "Computer: " << computer << endl;
                    cout << "Player: " << player << "\n\n";}
                else if (playerChoice == 's' && choices[randIndex] == 'p'){
                    cout << "\nComputer picked paper." << endl;
                    cout << "You score a point." << endl;
                    player++;
                    cout << "Computer: " << computer << endl;
                    cout << "Player: " << player << "\n\n";}
                else {
                    cout << "Invalid option. \n";}}
            if (computer == goal) {
                cout << "Computer wins!." << endl;}
            else if (player == goal) {
                cout << "You win!" << endl;}
            cout << "Retry? (y/n): ";
            cin >> retry;
            if (retry == 'y') {
                cout << "\n\n";}
            else {
                cout << "Goodbye" << endl;
                break;}}
    return 0;}
