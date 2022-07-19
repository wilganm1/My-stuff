#include <iostream>

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
                            std::cout << "Deposit complete" << "\n" << std::endl;
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
                            std::cout << "Deposit complete" << "\n" << std::endl;
                            break;}}
                    break;
                default:
                    std::cout << "Invalid. Try again." << std::endl;
                    goto pickAccount;
                    break;}}}

void loseMoney(){ //withdrawing money
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
                        std::cout << "Enter amount to withdraw: ";
                        int withdrawAmount{};
                        std::cin >> withdrawAmount;
                        if (withdrawAmount < 0){
                            std::cout << "Invalid. Please enter positive number" << std::endl;
                            std::cin.clear();
                            std::cin.ignore(10000, '\n');}
                        else if (withdrawAmount > checkingBalance) {
                            std::cout << "Requested withdrawal greater than current balance. Try again." << std::endl;
                            std::cin.clear();  //clears error flag
                            std::cin.ignore(10000, '\n');} // skips to next newline of cin
                        else {
                            checkingBalance -= withdrawAmount;
                            std::cout << "Withdrawal complete" << "\n" << std::endl;
                            break;}}
                        viewAccounts();
                    break;
                case 2:
                    while (true){
                        std::cout << "Enter amount to withdraw: ";
                        int withdrawAmount{};
                        std::cin >> withdrawAmount;
                        if (withdrawAmount < 0){
                            std::cout << "Invalid. Please enter positive number" << std::endl;
                            std::cin.clear();
                            std::cin.ignore(10000, '\n');}
                        else {
                            savingsBalance -= withdrawAmount;
                            std::cout << "Withdrawal complete." << "\n" << std::endl;
                            break;}}
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
                        std::cout << "Enter amount to transfer: ";
                        int transferAmount{};
                        std::cin >> transferAmount;
                        if (transferAmount < 0){
                            std::cout << "Invalid. Please enter positive number" << std::endl;
                            std::cin.clear();
                            std::cin.ignore(10000, '\n');}
                        else if (transferAmount > checkingBalance){
                            std::cout << "Invalid. Please enter positive number" << std::endl;
                            std::cin.clear();
                            std::cin.ignore(10000, '\n');}
                        else {
                            checkingBalance -= transferAmount;
                            savingsBalance += transferAmount;
                            std::cout << "Transfer complete." << "\n" << std::endl;
                            break;}}
                    break;
                case 2: //savings
                    while (true){
                        std::cout << "Enter amount to transfer: ";
                        int transferAmount{};
                        std::cin >> transferAmount;
                        if (transferAmount < 0){
                            std::cout << "Invalid. Please enter positive number." << std::endl;
                            std::cin.clear();
                            std::cin.ignore(10000, '\n');}
                        else if (transferAmount > savingsBalance){
                            std::cout << "Transfer greater than current balance. Try again." << std::endl;
                            std::cin.clear();
                            std::cin.ignore(10000, '\n');}
                        else {
                            savingsBalance -= transferAmount;
                            checkingBalance += transferAmount;
                            std::cout << "Transfer complete" << "\n" << std::endl;
                            break;}}
                    break;
                default:
                    std::cout << "Invalid. Try again." << std::endl;
                    goto pickTransfer;
                    break;}}}

void Menu(){
    std::cout << "Welcome to MEW Banking." << "\n" << std::endl;
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
                    Menu();  //This will constantly recall Menu function. Recursion.
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
