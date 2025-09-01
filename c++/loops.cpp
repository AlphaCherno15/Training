#include <iostream>
#include <list>
using namespace std;

int main() {
    // Example of a for loop

    // initialization, condition, increment or decrement
    for (int i = 0; i < 5; i++) {
        cout << "For Loop Iteration: " << i << endl;
        if (i == 3) {
            cout << "Continuing the loop at i = 3" << endl;
            continue; // continue example skip the rest of the loop when i is 3
        }
    }

    list<int> myList = {1, 2, 3, 4, 5};
    // range-based for loop or for each loop
    for (int value : myList) {
        cout << "Value from list: " << value << endl;
        if (value == 3) {
            cout << "Breaking the loop at value 3" << endl;
            break; // break example exit the loop when value is 3
        }

    }
    // Example of a while loop, first check condition, then execute
    int count = 0;
    while (count < 5) {
        cout << "While Loop Count: " << count << endl;
        count++;
    }

    // Example of a do-while loop executing at least once
    int num = 0;
    do {
        cout << "Do-While Loop Number: " << num << endl;
        num++;
    } while (num < 5);

    return 0;
}