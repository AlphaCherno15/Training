#include <iostream>
#include <vector>


namespace first{
    int a = 10; // global variable
}

namespace second{
    int a = 20; // another global variable
}

typedef std::string myString_t; // type alias for std::string
// or can be done using 'using'
using myString = std::string; // another way to create a type alias

int main() {
    // this is a coment
    /*
    multiline 
    comment
    */
    std::cout << "hello world" << std::endl;
    std::cout << "This project uses C++17 standard." << '\n';

    // Declaration and assignment example
    int x; // this is a declaration
    x = 5; // this is an assignment
    std::cout << "Value of x: " << x << std::endl;
    // or 
    int y = 10;
    std::cout << "Value of y: " << y << std::endl;

    // Using a constant
    const int z = 15; // constant declaration
    std::cout << "Value of z: " << z << std::endl;

    // single character
    char letter = 'A'; // character declaration
    std::cout << letter;

    // boolean value
    bool isTrue = true; // boolean declaration
    bool isFalse = false; // another boolean declaration

    std::cout <<isTrue << " " << isFalse << std::endl;

    // using a string
    std::string greeting = "Hello, C++!";
    std::cout << greeting << std::endl;

    int a = 5; // variable declaration

    std::cout << "Value of a: " << a << std::endl;
    // using namespaces
    std::cout << "Value from first namespace a: " << first::a << std::endl;
    std::cout << "Value from second namespace a: " << second::a << std::endl;

    using namespace first; // using the first namespace
    std::cout << "Value from first namespace a after using: " << a << std::endl;

    // using directives
    using std::cout; // using cout from std namespace
    using std::string; // using string from std namespace

    cout << "Using cout directly from std namespace." << std::endl; 
    string message = "This is a message using std::string.";
    cout << message << std::endl;

    // using type alias
    myString_t aliasMessage = "This is a message using type alias.";
    cout << aliasMessage << std::endl;
    
    // cin example
    int userInput; 
    std::cout << "Enter a number: ";
    std::cin >> userInput; // taking input from user
    cout << "You entered: " << userInput << std::endl;

    // get line example
    std::getline(std::cin >> std::ws, greeting); // taking a full line input
    cout << "You entered: " << greeting << std::endl;

    // const parameter example
    // turn a variable into a constant parameter, does not allow modification
    const int constantParam = 100;
    cout << "Constant parameter value: " << constantParam << std::endl;


    return 0;

}
