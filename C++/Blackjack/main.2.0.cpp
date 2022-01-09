#include <iostream>
#include "random.hpp"
#include <string>
using Random = effolkronium::random_static;   
/* this is to use Random::get to get a random number
Be sure to link it to the compiler */

int goal{};       //zero-initialize the goal

void showHands(int aa,int bb, int cc, int dd){ //function to show cards on screen.
    std::cout << "\tPlayer" << "\tDealer" << std::endl;
    std::cout << "\t  " << aa << "\t  " << bb << std::endl;
    std::cout << "\nPlayer score: " << cc << " / " << goal << std::endl;
    std::cout << "Dealer score: " << dd << " / " << goal << std::endl;}

int main() {
    while(true){              //loop that will restart if retry == yes down below.
        int player_cards{};   //need to zero initialize here so it's in proper scope
        int dealer_cards{};
        int player_score{};
        int dealer_score{};
        while (true){      //checks if goal entered is a whole positive number
            std::cout << "Enter goal: ";
            std::cin >> goal;
            if (std::cin.fail()){  //will catch if goal is not an integer
                std::cout << "Not an number. Try again." << std::endl;
                std::cin.clear();  //will erase the cin input
                std::cin.ignore(10000, '\n');}
            else if (goal < 1) {
                std::cout << "Please enter positive number" << std::endl;
                std::cin.clear();  //will erase the cin input
                std::cin.ignore(10000, '\n');}
            else {
                system("CLS");
                break;};}

        while(player_score < goal && dealer_score < goal){   //This loop will reset the hands after every point.
            player_cards = 0;
            dealer_cards = 0;
            player_cards += Random::get(1,11);
            player_cards += Random::get(1,11);    //adds two cards to hands
            dealer_cards += Random::get(1,11);
            dealer_cards += Random::get(1,11);
            showHands(player_cards, dealer_cards, player_score, dealer_score);

            while (player_cards < 21 && dealer_cards < 22){
                std::cout << "Hit or stay? (h/s)";
                std::string choice{};
                std::cin >> choice;
                if(choice == "h") {
                    player_cards += Random::get(1,11);
                    system("CLS");
                    showHands(player_cards, dealer_cards, player_score, dealer_score);}
                else {break;}}

            while(dealer_cards < 17){ //dealer must hit if cards < 17.
                    dealer_cards += Random::get(1,11);}
            system("CLS");
            showHands(player_cards, dealer_cards, player_score, dealer_score);

            if (player_cards < 22 && player_cards > dealer_cards) {
                player_score += 1;
                system("CLS");
                std::cout << "You score" << std::endl;}
            else if (player_cards < 22 && dealer_cards > 21){
                player_score += 1;
                system("CLS");
                std::cout << "You score." << std::endl;}
            else if (dealer_cards < 22 && player_cards > 21){
                dealer_score += 1;
                system("CLS");
                std::cout << "Dealer scores." << std::endl;}
            else if (dealer_cards < 22 && dealer_cards > player_cards) {
                dealer_score +=1;
                system("CLS");
                std::cout << "Dealer scores." << std::endl;}
            else if (player_cards == dealer_cards) {
                dealer_score += 1;
                system("CLS");
                std::cout << "Dealer scores." << std::endl;}
            else if (player_cards > 21 && dealer_cards > 21){
                system("CLS");
                std::cout << "Neither scores." << std::endl;}}
        if (player_score == goal){
            system("CLS");
            showHands(player_cards, dealer_cards, player_score, dealer_score);
            std::cout << "You win!" << "\n";}
        else if (dealer_score == goal){
            system("CLS");
            showHands(player_cards, dealer_cards, player_score, dealer_score);
            std::cout << "Dealer wins!" << std::endl;}
        std::cout << "Play again? (y/n): ";
        char retry{};
        std::cin >> retry;
        std::cout << "\n";
        if (retry == 'y'){ system("CLS");
        } else {break;}}
    return 0;}
