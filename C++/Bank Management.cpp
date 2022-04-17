#include <iostream>
#include <cstring>

int checkingBalance{0};
int savingsBalance{0};
int withdrawAmount{};
int depositAmount{};


void viewAccounts(){ //view accounts; Making accounts comes later.
    std::cout << "\n";
    std::cout << "Checkings:  " << checkingBalance << std::endl;
    std::cout << "Savings: " << savingsBalance << std::endl;
    std::cout << "\n";}

void addMoney(){  //depositing money into accounts
    system("CLS");
    std::cout << "Which account would you like to add to?" <<std::endl;
    std::cout << "1) Checkings" << std::endl;
    std::cout << "2) Savings" << std::endl;
    std::cout << "Enter number: " << std::endl;
    int accountChoice{};
    std::cin >> accountChoice;
    if (std::cin.fail()){  //will catch if goal is not an integer
            std::cout << "Not an number. Try again." << std::endl;
            std::cin.clear();  //will erase the cin input
            std::cin.ignore(10000, '\n');}
    else {
        switch (accountChoice) {
    //need a fail-safe is negative integer is entered.
            case 1:
                while (true){
                    std::cout << "Enter amount to deposit: ";
                    std::cin >> depositAmount;
                    if (depositAmount < 0){
                        std::cout << "Invalid. Please enter positive number" << std::endl;
                        std::cin.clear();
                        std::cin.ignore(10000, '\n');}
                    else {
                        checkingBalance += depositAmount;
                        std::cout << "Deposit complete" << std::endl;
                        break;}}
                    viewAccounts();
                break;
            case 2:
                while (true){
                    std::cout << "Enter amount to deposit: ";
                    std::cin >> depositAmount;
                    if (depositAmount < 0){
                        std::cout << "Invalid. Please enter positive number" << std::endl;
                        std::cin.clear();
                        std::cin.ignore(10000, '\n');}
                    else {
                        savingsBalance += depositAmount;
                        std::cout << "Deposit complete" << std::endl;
                        break;}}
                    viewAccounts();
                break;
            default:
                break;}}}

void loseMoney(){ //withdrawing money
    system("CLS");
    std::cout << "Which account would you like withdraw from?" <<std::endl;
    std::cout << "1) Checkings" << std::endl;
    std::cout << "2) Savings" << std::endl;
    std::cout << "Enter number: " << std::endl;
    int accountChoice{};
    std::cin >> accountChoice;
    if (std::cin.fail()){  //will catch if goal is not an integer
            std::cout << "Not an number. Try again." << std::endl;
            std::cin.clear();  //will erase the cin input
            std::cin.ignore(10000, '\n');}
    else {
        switch (accountChoice) {
            case 1:
                while (true) {
                    std::cout << "Enter amount to withdraw: ";
                    std::cin >> withdrawAmount; //checks to see you don't take out more than is possible.
                    if (withdrawAmount > checkingBalance) {
                        std::cout << "Request greater than current balance. Please try again." << std::endl;
                        std::cin.clear();  //will erase the cin input
                        std::cin.ignore(10000, '\n');}
                    else {
                        checkingBalance -= withdrawAmount;
                        std::cout << "Withdrawal complete";
                        viewAccounts();
                        break;}}
                checkingBalance -= withdrawAmount;
                std::cin.clear();
                break;
            case 2:
                std::cout << "Enter amount to withdraw: ";
                while (true) {
                    std::cin >> withdrawAmount;
                    if (withdrawAmount > savingsBalance) {
                        std::cout << "Request greater than current balance. Please try again." << std::endl;
                        std::cin.clear();  //will erase the cin input
                        std::cin.ignore(10000, '\n');}
                    else {
                        savingsBalance -= withdrawAmount;
                        std::cout << "Withdrawal complete" << std::endl;
                        viewAccounts();
                        break;}
                }
                savingsBalance -= withdrawAmount;
                std::cin.clear();
                break;
            default:
                break;}}}

void transferMoney(){   //taking money from one account and putting it into another.
    system("CLS");
    double transferAmount{};
    std::cout << "Checkings:  " << checkingBalance << std::endl;
    std::cout << "Savings: " << savingsBalance << std::endl;
    std::cout << "\n";
    std::cout << "Which account would you like to transfer from? " << std::endl;
    std::string transferChoice{};
    while (true) {
        std::cin >> transferChoice;
        if (transferChoice == "checkings"){
            std::cout << "Choose amount to transfer" << std::endl;
            std::cin >> transferAmount;
            if (transferAmount < checkingBalance) {
                checkingBalance -= transferAmount;
                savingsBalance += transferAmount;
                break;}

            else if (transferAmount > checkingBalance) {
                        std::cout << "Request greater than current balance. Please try again";
                        std::cin.clear();  //will erase the cin input
                        std::cin.ignore(10000, '\n');}
                        }

        else if (transferChoice == "savings"){
            std::cout << "Choose amount to transfer" << std::endl;
            double transferAmount{};
            std::cin >> transferAmount;
            if (transferAmount < savingsBalance) {
                savingsBalance -= transferAmount;
                checkingBalance += transferAmount;
                break;}

            else if (transferAmount > savingsBalance) {
                    std::cout << "Request greater than current balance. Please try again";
                    std::cin.clear();  //will erase the cin input
                    std::cin.ignore(10000, '\n');}
                    }}}

void Menu(){
    std::cout << "Welcome to MEW Banking." << std::endl;
    std::cout << "1) View your accounts" << std::endl;
    std::cout << "2) Deposit money" << std::endl;
    std::cout << "3) Withdraw money" << std::endl;
    std::cout << "4) Transfer money" << std::endl;
    std::cout << "\n";
    std::cout << "Please select an option: ";
    int pickit;
    while (true){
        std::cin >> pickit;
        if (std::cin.fail()){  //will catch if goal is not an integer
                std::cout << "Not a number. Try again." << std::endl;
                std::cin.clear();  //will erase the cin input
                std::cin.ignore(10000, '\n');}
        else {
        switch (pickit){
            case 1:
                viewAccounts();
                Menu();  //Need to have Menu() after every other function is called to restart it
                break;
            case 2:
                addMoney();
                Menu();
                break;
            case 3:
                loseMoney();
                Menu();
                break;
            case 4:
                transferMoney();
                Menu();
                break;
            default:
                std::cout << "Please enter valid option" << std::endl;}}}}

int main(){
    Menu();
return 0;}
