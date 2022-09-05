#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include "random.hpp"

using Random = effolkronium::random_static;

void print(std::vector<char> const &lts){  //prints out available positions. found online.
    std::cout << "\t\t  ";
    for (auto const &i: lts) {
        std::cout << i << ' ';}
}

void game(std::vector<char>& bp, std::vector<char>& the_letters){
    system("CLS");
    std::cout << "\t\t       _______" << std::endl;
    std::cout << "\t\t      |       |" << std::endl;
    std::cout << "\t\t      "<<bp[0]<<"       |" << std::endl;
    std::cout << "\t\t     "<<bp[2]<<bp[1]<<bp[3]<<"      |" << std::endl;
    std::cout << "\t\t     "<<bp[4]<< " "<<bp[5]<<"      |" << std::endl;
    std::cout << "\t\t            __|__\n" << std::endl;
}

bool match(std::vector<char>& word, char& guess, std::vector<char>& the_letters){
    int correct_guesses{};
    for (int i; i = 0; i++){
        if(i != word.size()){
            if (word[i] == guess){
                    word[i] = '*';
                    the_letters[i] = guess;
                    correct_guesses++;}
            else{
                break;}}}

    if (correct_guesses > 0){
        return true;}
    else {
        return false;}
}

void rules(std::vector<char>& word, std::vector<char>& body_parts, std::vector<char>& the_letters){
    int wrong_guesses{0};
    int letters_left = the_letters.size();
    while (wrong_guesses < 6 && letters_left > 0){  //Loop for the game. Guess wrong and a figure appear
        char guess{};
        print(the_letters);
        std::cout << "\n\t\t Guess a letter: ";
        std::cin >> guess;
        if (std::cin.fail()){ //will catch if goal is not an integer
            std::cout << "\nNot an number. Try again." << std::endl;
            std::cin.clear();  //will erase the cin input
            std::cin.ignore(10000, '\n');}
        else {
            if (!match(word,guess,the_letters)){//find a way to see if a character is in a string.
                switch (wrong_guesses){
                    case 0:
                        body_parts[wrong_guesses] = 'O';
                        wrong_guesses++;
                        game(body_parts,the_letters);
                        break;
                    case 1:
                        body_parts[wrong_guesses] = '|';
                        wrong_guesses++;
                        game(body_parts,the_letters);
                        break;
                    case 2:
                        body_parts[wrong_guesses] = '-';
                        wrong_guesses++;
                        game(body_parts,the_letters);
                        break;
                    case 3:
                        body_parts[wrong_guesses] = '-';
                        wrong_guesses++;
                        game(body_parts,the_letters);
                        break;
                    case 4:
                        body_parts[wrong_guesses] = '/';
                        wrong_guesses++;
                        game(body_parts,the_letters);
                        break;
                    case 5:
                        body_parts[wrong_guesses] = '\\';
                        wrong_guesses++;
                        game(body_parts,the_letters);
                        break;
                    default:
                        break;}}
            else {
                game(body_parts,the_letters);
                letters_left--;}}
    }
    if (wrong_guesses == 6){
        std::cout << "\n\n\t\t Out of guesses." << std::endl;}
    else if (letters_left == 0){
        std::cout << "\n\n\t\t You got it!" << std::endl;}
}

//The guessed letters still aren't printing. Try making the word a vector of characters instead of a string.

int main(){
    std::vector<char> word{};
    std::string random_word();
    std::vector<char> body_parts = {' ',' ',' ',' ',' ',' '};
    std::vector<char> the_letters = {};
    int word_length{};
    while (true){
        std::cout << "Choose word length from 3 to 7: ";
        std::cin >> word_length;
        if (std::cin.fail()){ //will catch if goal is not an integer
            std::cout << "\nNot an number. Try again." << std::endl;
            std::cin.clear();  //will erase the cin input
            std::cin.ignore(10000, '\n');}
        else if (word_length < 3 || word_length > 7){
            std::cout << "Out of range. Please try again." << std::endl;}
        else {
            for (int i = 0; i < word_length; i++){
                the_letters.push_back('_');} //Corresponds to word length
            break;}}
    switch (word_length){   //making different arrays
        case 3:{
            std::vector<std::string> three_letter_words = {"owl","ant","sky","ski","dog","cat","ham","hit","hot","ran","car","van","box","all","ice","zoo","sly","mix","man","ape","ken","bee","sin","gag",
            "gig","gym","fun","out","jew","few","fly","fat","pop","put","pin","pat","lye","sap","spy","cry","any","yam","bay","bar","dry","dab","ace","lol",
            "kip","kin","wet","see","sea","eye","elk","elm","oak","red","vat","que","lab","row"};
            int size_three_let = three_letter_words.size();
            std::string random_word = three_letter_words[Random::get(0, (size_three_let-1))];
            for (int i = 0; i < random_word.size(); i++){
                word.push_back(static_cast<char>(random_word[i]));}
            game(body_parts, the_letters);
            rules(word,body_parts,the_letters);
            break;}
        case 4:{
            std::vector<std::string> four_letter_words = {"bark","crib","part","swim","swam","kiln","milk","pull", "dull","bull","past","last","long","song","pain","tear","tier","pier",
            "made","blue","boon","boom","mask","scam","able","cope","dumb","yarn","yard","team","teal","beat","best","bets","bell","upon","lord","draw",
            "bats","baby","hell","hike","hill","hale","none","noon","noun","nine","name","nail","rate","ream","read","rare","rung","raze","gaze","toss","boss","spin","spun",
            "spur","joke","join","jest","only","over","once","pace","pies","ping","king","lawn","like","lame","dare","door","drip","vine","vain","barn","cats","crab",
            "grab","drab","slab","guts","fire","tire","wire","lyre","sire","mire","idea","talk","dove","bard","tree","hard","fair","hair","hero","zero"};
            int size_four_let = four_letter_words.size();
            std::string random_word = four_letter_words[Random::get(0, (size_four_let-1))];
            for (int i = 0; i < random_word.size(); i++){
                word.push_back(static_cast<char>(random_word[i]));}
            game(body_parts,the_letters);
            rules(word,body_parts,the_letters);
            break;}
        case 5:{
            std::vector<std::string> five_letter_words = {"skull","skill","train","crane","swarm","swine","swing","bring","alarm","aloof","aloft","fable","fling","found","hound","curse","verse","arson",
            "bread","breed","beard","joist","hoist","blast","crass","crude","drill","quill","value","olive","other","aroma","scent","sweet","piano","grant","lowly", "state","grate","great","wheel",
            "while","first","third","fifth","sixth","tenth","bound","going","doing","devour","sleep","sweep","chill","drown","crown","slice","alive","mince","mouse","douse","fight","might","light",
            "elder","elden","trust","crust","eight","ninth","square","money","hover","solve","digest","exodus","metal","blank","usual","rhyme","favor","awake","shout","coral"};

            int size_five_let = five_letter_words.size();
            std::string random_word = five_letter_words[Random::get(0, (size_five_let-1))];
            for (int i = 0; i < random_word.size(); i++){
                word.push_back(static_cast<char>(random_word[i]));}
            game(body_parts,the_letters);
            rules(word,body_parts,the_letters);
            break;}
        case 6:{
            std::vector<std::string> six_letter_words = {"thrust","climax","rotate","fourth","silent","strong","monkey","reflex","oppose","detect","accept","abroad","actual",
            "active","fusion","linear","breath","button","behind","caught","career","circle","effect","design","resign","export","little","nature","handed","people","strike","policy","prison","secret",
            "screen","saying","starve","struck","spirit","source","useful","unless","unique","wealth","yellow","mellow","winter","fellow","endure","refine","prayer"};

            int size_six_let = six_letter_words.size();
            std::string random_word = six_letter_words[Random::get(0, (size_six_let-1))];
            for (int i = 0; i < random_word.size(); i++){
                word.push_back(static_cast<char>(random_word[i]));}
            game(body_parts,the_letters);
            rules(word,body_parts,the_letters);
            break;}
        case 7:{
            std::vector<std::string> seven_letter_words = {"slander","propose","entitle","dispose","stealth","remorse","villain","suggest","believe","discard","prevail","unravel","entwine",
            "reverse","forsake","discard","requiem","request","survive","impress","genuine","jealous","revenge","conquer","execute","worship","enslave","prepare"};
            int size_seven_let = seven_letter_words.size();
            std::string random_word = seven_letter_words[Random::get(0, (size_seven_let-1))];
            for (int i = 0; i < random_word.size(); i++){
                word.push_back(static_cast<char>(random_word[i]));}
            game(body_parts,the_letters);
            rules(word,body_parts,the_letters);
            break;}
        break;}
    return 0;
}
