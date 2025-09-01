#include <iostream>
using namespace std;
// using std::cout; 
// using std::endl;
// using std::string;


int main() {
    
    string name = "Robert";

    // Example of string concatenation
    string greeting = "Hello, " + name + "!";
    cout << greeting << endl;

    // Example of string length
    if (name.length() > 0) {
        cout << "The Name Length is: " << name.length() << endl;
    }

    // Example of accessing characters in a string
    cout << "The first character in the name is: " << name[0] << endl;
    // ot using at(index) method
    cout << "The second character in the name is: " << name.at(1) << endl;
    cout << "The last character in the name is: " << name[name.length() - 1] << endl;   

    // example of empty string check
    if (name.empty()) {
        cout << "The name string is empty." << endl;
    } else {
        cout << "The name string is not empty." << endl;
    }

    // clear the string
    name.clear();

    // append to the string
    name.append("Alice");
    // isert into the string .insert(index, string to insert)
    name.insert(0, "Ms. ");
    cout << "The new name is: " << name << endl;

    // Find method - returns the index of the first occurrence of the substring
    cout << "Index Number of 'i': "<< name.find("i") << endl;

    // erase method - erases part of the string from the specified index (from index, number of characters to erase)
    name.erase(0, 4); // Erase "Ms. "
    return 0;
}