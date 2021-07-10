#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

void rps() {
    while (1){
    srand(time(NULL));
    int player = 0;
    int computer = 0;
    int goal;
    string retry;
    cout << "Rock Paper Scissors. You vs Computer." << "\n\n";
    cout << "Enter goal: ";
    cin >> goal;
    string choices[3] = {"rock", "paper", "scissors"};
    string playerChoice;
    while (player < goal && computer < goal){
            int randIndex = rand() % 3;  //range of 0 to 2.
            string playerChoice = "";
            cout << "Choose rock paper or scissors: ";
            cin >> playerChoice;
            if (playerChoice == choices[randIndex]) {
                cout << "Tie." << endl;
                cout << "Computer: " << computer << endl;
                cout << "Player: " << player << "\n\n";}
            else if (playerChoice == "rock" && choices[randIndex] == "paper"){
                cout << "Computer picked " << choices[randIndex] << endl;
                cout << "Computer scores a point." << endl;
                computer++;
                cout << "Computer: " << computer << endl;
                cout << "Player: " << player << "\n\n";}
            else if (playerChoice == "rock" && choices[randIndex] == "scissors"){
                cout << "Computer picked " << choices[randIndex] << endl;
                cout << "You score a point." << endl;
                player++;
                cout << "Computer: " << computer << endl;
                cout << "Player: " << player << "\n\n";}
            else if (playerChoice == "paper" && choices[randIndex] == "rock"){
                cout << "Computer picked " << choices[randIndex] << endl;
                cout << "You score a point." << endl;
                player++;
                cout << "Computer: " << computer << endl;
                cout << "Player: " << player << "\n\n";}
            else if (playerChoice == "paper" && choices[randIndex] == "scissors"){
                cout << "Computer picked " << choices[randIndex] << endl;
                cout << "Computer scores a point." << endl;
                computer++;
                cout << "Computer: " << computer << endl;
                cout << "Player: " << player << "\n\n";}
            else if (playerChoice == "scissors" && choices[randIndex] == "rock"){
                cout << "Computer picked " << choices[randIndex] << endl;
                cout << "Computer scores a point." << endl;
                computer++;
                cout << "Computer: " << computer << endl;
                cout << "Player: " << player << "\n\n";}
            else if (playerChoice == "scissors" && choices[randIndex] == "paper"){
                cout << "Computer picked " << choices[randIndex] << endl;
                cout << "You score a point." << endl;
                player++;
                cout << "Computer: " << computer << endl;
                cout << "Player: " << player << "\n\n";}
            else {
                cout << "Enter valid option.";}}
        if (computer == goal) {
            cout << "Computer wins!." << endl;}
        else if (player == goal) {
            cout << "You win!" << endl;}
        cout << "Retry? (y/n): ";
        cin >> retry;
        if (retry == "y") {
            cout << "\n\n";}
        else if (retry == "n"){
            break;}}}

int main() {
    rps();
    return 0;}
