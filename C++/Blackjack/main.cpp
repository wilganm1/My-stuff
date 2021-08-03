#include <iostream>
#include "random.hpp"
using Random = effolkronium::random_static;     //this is to use Random::get to get a random number

int goal{};           //zero-initialize the goal
void ignoreLine(){
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');}  //this function erases and ignores cin input for invalid input

int main() {
    while(true){                  //loop that will restart if retry is yes down below.
        int player_cards{};       //the hand for the player
        int dealer_cards{};       //the hand for the dealer
        int player_score{};     
        int dealer_score{};
        while (true){
            std::cout << "Enter goal: ";   
            std::cin >> goal;
            if (std::cin.fail()){  //will catch if goal is not an integer
                std::cout << "Not an number. Try again." << "\n";
                std::cin.clear();  //will erase the cin input
                ignoreLine();}     //removes bad input. Loop restarts
            else if (goal < 1) {
                std::cout << "Please enter positive number" << "\n";
                std::cin.clear();  //will erase the cin input
                ignoreLine();}
            else {break;};}

        while(player_score < goal && dealer_score < goal){   //This loop will reset the hands after every point.
            player_cards = 0;
            dealer_cards = 0;
            player_cards += Random::get(1,11);
            player_cards += Random::get(1,11);          //adds two cards to hands
            dealer_cards += Random::get(1,11);
            dealer_cards += Random::get(1,11);
            std::cout << "Player: " << player_cards << "\n";
            std::cout << "Dealer: " << dealer_cards << "\n";

            while (player_cards < 21){
                std::cout << "Hit or stay? ";
                std::string choice{};
                std::cin >> choice;
                if(choice == "hit" || choice == "Hit"){
                    player_cards += Random::get(1,11);
                    std::cout << "Player: " << player_cards << "\n";
                    std::cout << "Dealer: " << dealer_cards << "\n\n";}
                else {break;}}

            while(dealer_cards < 17){
                    dealer_cards += Random::get(1,11);}
            std::cout << "Player: " << player_cards << "\n";
            std::cout << "Dealer: " << dealer_cards << "\n\n";
            
            if (player_cards < 22 && player_cards > dealer_cards) {
                player_score += 1;
                std::cout << "You score" << "\n";
                std::cout << "Player: " << player_score << "\n";
                std::cout << "Dealer: " << dealer_score << "\n\n";}
            else if (player_cards < 22 && dealer_cards > 22){
                player_score += 1;
                std::cout << "You score" << "\n";
                std::cout << "Player: " << player_score << "\n";
                std::cout << "Dealer: " << dealer_score << "\n\n";}
            else if (dealer_cards < 22 && player_cards > 22){
                dealer_score += 1;
                std::cout << "Dealer scores" << "\n";
                std::cout << "Player: " << player_score << "\n";
                std::cout << "Dealer: " << dealer_score << "\n\n";}
            else if (player_cards < 22 && dealer_cards < 22 && player_cards > dealer_cards){
                player_score += 1;
                std::cout << "You score" << "\n";
                std::cout << "Player: " << player_score << "\n";
                std::cout << "Dealer: " << dealer_score << "\n\n";}
            else if (dealer_cards < 22 && player_cards < 22 && dealer_cards > player_cards) {
                dealer_score +=1;
                std::cout << "Dealer scores" << "\n";
                std::cout << "Player: " << player_score << "\n";
                std::cout << "Dealer: " << dealer_score << "\n\n";}
            else if (player_cards == dealer_cards) {
                dealer_score += 1;
                std::cout << "Tie to dealer" << "\n";
                std::cout << "Player: " << player_score << "\n";
                std::cout << "Dealer: " << dealer_score << "\n\n";}
            else if (player_cards > 22 && dealer_cards > 22){
                std::cout << "Neither score" << "\n";
                std::cout << "Player: " << player_score << "\n";
                std::cout << "Dealer: " << dealer_score << "\n\n";}}
        if (player_score == goal){
            std::cout << "You win!" << "\n";}
        else if (dealer_score == goal){
            std::cout << "Dealer wins" << "\n";}
        std::cout << "Play again? (y/n): ";
        char retry{};
        std::cin >> retry;
        std::cout << "\n";
        if (retry == 'y'){
        } else {break;}}
    return 0;}