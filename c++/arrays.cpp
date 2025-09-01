#include <iostream>
#include <string>
// Function prototype (declaration, and definition)
void print(int msg){
    std::cout << msg << std::endl;
};

void print(double msg){
    std::cout << msg << std::endl;
};

void print(const std::string msg) {
    std::cout << msg << std::endl;
};

int getTotal(int arrayOfNum[], int size) {
    int total = 0;
    for (int i = 0; i < size; i++) {
        total += arrayOfNum[i];
    }
    return total;
}
// Bubble sort function
int bubblesort(){
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int size = sizeof(arr)/sizeof(arr[0]);

    for (int i = 0; i < size-1; i++) {
        for (int j = 0; j < size-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                // swap arr[j] and arr[j+1]
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    print("Sorted array: \n");
    for (int number: arr) {
        print(number);
    }

    return 0;
}
// Fill array with user input
int fill_function() {
    std::string foods[10];
    fill(foods, foods + 10, "Pizza");
    for (std:: string food: foods) {
        print(food);
    }
    return 0;
}
int main() {

    // arrays in C++
    int numbers[] = {1, 2, 3, 4, 5};
    print(numbers[0]);

    std::string  cars[] = {"Volvo", "BMW", "Ford", "Mazda"};
    print(cars[0]);

    // or define the size of the array
    int myNumbers[5] = {10, 20, 30, 40, 50};
    print(myNumbers[0]);

    // or define the size of the array and add values later
    int myNumbers2[5];
    myNumbers2[0] = 10;
    myNumbers2[1] = 20;
    print(myNumbers2[0]);

    // sizeof operator
    int myNumbers3[5] = {10, 20, 30, 40}; // last element will be 0
    std::cout << sizeof(myNumbers3) << " bytes" <<  std::endl; // total size in bytes

    // INTERATING OVER AN ARRAY
    for (int index = 0; index < 5; index++) {
        std::cout << myNumbers3[index] << std::endl;
    }
    //or for each loop
    for (int num : myNumbers3) {
        std::cout << num << std::endl;
    }
    // or calculating size of the array
    for (int index = 0; index < sizeof(myNumbers3)/sizeof(int); index++) {
        std::cout << myNumbers3[index] << std::endl;
    }
    
    // passibg array to a function, it musrt be passed with its size
    int array_size = sizeof(myNumbers3)/sizeof(int);
    getTotal(myNumbers3, array_size);
    print(getTotal(myNumbers3, array_size));

    bubblesort();
    fill_function();

    return 0;
}