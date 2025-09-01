#include <iostream>

int main() {
    using std::cout; 
    using std::endl; 
    using std::string; 

    // Example of if statement
    int age = 18;

    // example of greater than or equal to check
    if (age >= 18) {
        cout << "You are an adult." << endl;
    } 

    // example of 'or' statement -&&-
    else if (age <= 18 && age >= 13) {
        cout << "You are a teenager." << endl;
    }

    // example of less than check
    else if (age < 13) {
        cout << "You are a child." << endl;
    } 

    // example of 'or' statement 
    else if (age < 0 || age > 120) {
        cout << "Invalid age." << endl;
    }
    // else to fisish the if-else chain
    else {
        cout << "You are a minor." << endl;
    }

    // example of equality check
    if (age == 18) {
        cout << "You just became an adult!" << endl;
    }
    // example of does not equal check 
    else if(age != 18) {
        cout << "You are not 18 yet." << endl;
    }
    // example of Not operator
    else if (! (age)) {
        cout << "Age is not defined." << endl;
    }   
    
    // Example of switch statement
    int day = 3; // let's say 1 is Monday, 2 is Tuesday 
    switch (day) {
        case 1:
            cout << "Monday" << endl;
            break;
        case 2:
            cout << "Tuesday" << endl;
            break;
        case 3:
            cout << "Wednesday" << endl;
            break;
        case 4:
            cout << "Thursday" << endl;
            break;
        case 5:
            cout << "Friday" << endl;
            break;
        case 6:
            cout << "Saturday" << endl;
            break;
        case 7:
            cout << "Sunday" << endl;
            break;

        //  default case to handle unexpected values
        default:
            cout << "Invalid day!" << endl;
    }

    // Example of ternary operator
    int number = 10;

    // using ternary operator to check if number is even or odd
    string result = (number % 2 == 0) ? "Even" : "Odd";
    cout << "The number is: " << result << endl;

    bool hungry = true;

    hungry ? cout << "Let's eat!" << endl : cout << "Not hungry." << endl;
    return 0;
    }