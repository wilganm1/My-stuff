#include <iostream>
#include "random.hpp"
using Random = effolkronium::random_static;     //this is to use Random::get to get a random number

int goal{};           //zero-initialize the goal

int main() {
    while(true){              //loop that will restart if retry is yes down below.
        int player_cards{};   //the hand for the player
        int dealer_cards{};   //the hand for the dealer
        int player_score{};
        int dealer_score{};
        while (true){
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
            else {break;};}

        while(player_score < goal && dealer_score < goal){   //This loop will reset the hands after every point.
            player_cards = 0;
            dealer_cards = 0;
            player_cards += Random::get(1,11);
            player_cards += Random::get(1,11);          //adds two cards to hands
            dealer_cards += Random::get(1,11);
            dealer_cards += Random::get(1,11);
            std::cout << "Player: " << player_cards << std::endl;
            std::cout << "Dealer: " << dealer_cards << std::endl;

            while (player_cards < 21){
                std::cout << "Hit or stay? (h/s)";
                std::string choice{};
                std::cin >> choice;
                if(choice == "h") {
                    player_cards += Random::get(1,11);
                    std::cout << "Player: " << player_cards << std::endl;
                    std::cout << "Dealer: " << dealer_cards << "\n\n";}
                else {break;}}

            while(dealer_cards < 17){
                    dealer_cards += Random::get(1,11);}
            std::cout << "Player: " << player_cards << std::endl;
            std::cout << "Dealer: " << dealer_cards << "\n\n";

            if (player_cards < 22 && player_cards > dealer_cards) {
                player_score += 1;
                std::cout << "You score" << "\n";
                std::cout << "Player: " << player_score << "\n";
                std::cout << "Dealer: " << dealer_score << "\n\n";}
            else if (player_cards < 22 && dealer_cards > 21){
                player_score += 1;
                std::cout << "You score" << "\n";
                std::cout << "Player: " << player_score << "\n";
                std::cout << "Dealer: " << dealer_score << "\n\n";}
            else if (dealer_cards < 22 && player_cards > 21){
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
            else if (player_cards > 21 && dealer_cards > 21){
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
        if (retry == 'y'){ system("CLS");
        } else {break;}}
    return 0;}
