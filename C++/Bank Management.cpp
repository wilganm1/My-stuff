#include <iostream>
#include <cstring>

int checkingBalance{0};
int savingsBalance{0};
int withdrawAmount{};
int depositAmount{};
int transferAmount{};

void viewAccounts(){ //view accounts; Making accounts comes later.
    std::cout << "\n";
    std::cout << "Checkings:  " << checkingBalance << std::endl;
    std::cout << "Savings: " << savingsBalance << std::endl;
    std::cout << "\n";}

void addMoney(){  //depositing money into accounts
    system("CLS");
    std::cout << "Which account would you like to add to?" <<std::endl;
    std::cout << "1) Checkings: " << checkingBalance << std::endl;
    std::cout << "2) Savings: " << savingsBalance << std::endl;
    pickAccount:
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
                        int depositAmount{};
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
                        int depositAmount{};
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
                    std::cout << "Invalid. Try again." << std::endl;
                    goto pickAccount;
                    break;}}}

void loseMoney(){ //withdrawing money
    system("CLS");
    std::cout << "Which account would you like withdraw from?" <<std::endl;
    std::cout << "1) Checkings: " << checkingBalance << std::endl;
    std::cout << "2) Savings: " << savingsBalance << std::endl;
    pickAccount:
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
                        int withdrawAmount{};
                        std::cin >> withdrawAmount; //checks to see you don't take out more than is possible.
                        if (withdrawAmount >> checkingBalance) {
                            std::cout << "Request greater than current balance. Please try again." << std::endl;
                            std::cin.clear();  //will erase the cin input
                            std::cin.ignore(10000, '\n');}
                        else if (std::cin.fail()){  //will catch if goal is not an integer
                            std::cout << "Not an number. Try again." << std::endl;
                            std::cin.clear();  //will erase the cin input
                            std::cin.ignore(10000, '\n');}
                        else {
                            checkingBalance -= withdrawAmount;
                            std::cout << "Withdrawal complete";
                            viewAccounts();
                            break;}
                        }
                    checkingBalance -= withdrawAmount;
                    std::cin.clear();
                    break;
                case 2:
                    while (true) {
                        std::cout << "Enter amount to withdraw: ";
                        int withdrawAmount{};
                        std::cin >> withdrawAmount;
                        if (withdrawAmount > savingsBalance) {
                            std::cout << "Request greater than current balance. Please try again." << std::endl;
                            std::cin.clear();  //will erase the cin input
                            std::cin.ignore(10000, '\n');}
                        else if (std::cin.fail()){  //will catch if goal is not an integer
                            std::cout << "Not an number. Try again." << std::endl;
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
                    std::cout << "Invalid. Try again." << std::endl;
                    goto pickAccount;
                    break;}}}

void transferMoney(){   //taking money from one account and putting it into another.
    system("CLS");
    std::cout << "1) Checkings:  " << checkingBalance << std::endl;
    std::cout << "2) Savings: " << savingsBalance << std::endl;
    pickTransfer:
        std::cout << "Which account would you like to transfer from? " << std::endl;
        int transferChoice{};
        std::cin >> transferChoice;
        if (std::cin.fail()){  //will catch if goal is not an integer
                std::cout << "Not an number. Try again." << std::endl;
                std::cin.clear();  //will erase the cin input
                std::cin.ignore(10000, '\n');}
        else {
        switch (transferChoice){
            case 1: //choose checking
                while (true){
                    std::cout << "Choose amount to transfer." << std::endl;
                    int transferAmount{};
                    std::cin >> transferAmount;
                    if (std::cin.fail()){  //will catch if goal is not an integer
                        std::cout << "Not an number. Try again." << std::endl;
                        std::cin.clear();  //will erase the cin input
                        std::cin.ignore(10000, '\n');}
                    else if (transferAmount > checkingBalance) {
                        std::cout << "Request greater than current balance. Please try again.";
                        std::cin.clear();  //will erase the cin input
                        std::cin.ignore(10000, '\n');}
                    else {
                        checkingBalance -= transferAmount;
                        savingsBalance += transferAmount;
                        break;}
                    }
            case 2: //choose savings
                while (true ){
                    std::cout << "Choose amount to transfer." << std::endl;
                    int transferAmount{};
                    std::cin >> transferAmount;
                    if (std::cin.fail()){  //will catch if goal is not an integer
                        std::cout << "Not an number. Try again." << std::endl;
                        std::cin.clear();  //will erase the cin input
                        std::cin.ignore(10000, '\n');}
                    else if (transferAmount > savingsBalance) {
                        std::cout << "Request greater than current balance. Please try again.";
                        std::cin.clear();  //will erase the cin input
                        std::cin.ignore(10000, '\n');}
                    else {
                        savingsBalance -= transferAmount;
                        checkingBalance += transferAmount;
                        break;}
                    }
            default:
                goto pickTransfer;} //end of switch
                }}

void Menu(){
    std::cout << "Welcome to MEW Banking." << std::endl;
    std::cout << "1) View your accounts" << std::endl;
    std::cout << "2) Deposit money" << std::endl;
    std::cout << "3) Withdraw money" << std::endl;
    std::cout << "4) Transfer money" << std::endl;
    std::cout << "\n";
    pickOption:
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
                    std::cout << "Please enter valid option." << std::endl;
                    goto pickOption;
                    break;}}}}

int main(){
    Menu();
return 0;}
