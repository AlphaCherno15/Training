#include <iostream>

// Memory reference uses & to denote reference parameters

// the exemple below shows two functions to swap two strings and & works like global variables in python

// Function to swap two strings not using reference parameters- only swaps local copies
void swap(std::string x, std::string y) {
    std::string temp = x; // temporary variable to hold the value of x
    x = y; // assign the value of y to x
    y = temp; // assign the value of temp (original x) to y
    // This will NOT swap the original variables passed to the function, only the local copies
}

// Function to swap two strings using reference parameters
void swap2(std::string &x, std::string &y) {
    std::string temp = x; // temporary variable to hold the value of x
    x = y; // assign the value of y to x
    y = temp; // assign the value of temp (original x) to y
    // This will swap the original variables passed to the function
}

int main() {
    using std::cout; 
    using std::endl; 
    using std::string; 
    
    string x = "kool-Aid";
    string y = "Water";

    cout << "X: " << x << endl; // Outputs Kool-Aid
    cout << "Y: " << y << endl; // Outputs Water

    swap(x, y); // call the swap function

    cout << "After swap function" << endl;
    cout << "X: " << x << endl; // Outputs Water 
    cout << "Y: " << y << endl; // Outputs Kool-Aid
   
    swap2(x, y); // call the swap function

    cout << "After swap2 function" << endl;
    cout << "X: " << x << endl; // Outputs Water 
    cout << "Y: " << y << endl; // Outputs Kool-Aid
   
    
    return 0;
};