#include <iostream>
#include <string>
// Function prototype (declaration, and definition)
void prints(std::string msg) {
    std::cout << msg << std::endl;
}

// string functions
// function to convert a string to uppercase
std::string Upper(const std::string& str) {
    std::string result = str;
    for (char& c : result) {
        c = toupper(c);
    }
    return result;
}

// exemple of overloaded functions
int multiply(int a, int b) {
    return a * b;
}

double multiply(double a, double b) {
    return a * b;
}

void print(int msg){
    std::cout << msg << std::endl;
};

void print(double msg){
    std::cout << msg << std::endl;
};

void print(const std::string msg) {
    std::cout << msg << std::endl;
}

// Function declaration
int add(int a, int b);
void printi(int msg);


int main() {
    prints("Hello from functions.cpp!");

    int value;
    value = add(1, 2); 
    printi(value);

    // string functions
    std::string original = "hello world";
    std::string uppercased = Upper(original);
    prints("Original: " + original);
    prints("Uppercase: " + uppercased);

    // exemple of overloaded functions
    int intResult = multiply(3, 4); 
    double doubleResult = multiply(2.5, 4.0);
    prints("Integer multiplication: " + std::to_string(intResult));
    prints("Double multiplication: " + std::to_string(doubleResult));
    prints("Using overloaded print function:");
    print(42);
    print(3.14);
    print("Hello, World!");

    return 0;


}

//function definition
int add(int a, int b) {
    return a + b;
}
void printi(int msg) {
    std::cout << msg << std::endl;
}



