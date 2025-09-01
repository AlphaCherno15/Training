#include <iostream>
#include <cmath>
#include <ctime>


int main() {
    using std::cout; // using cout from std namespace
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

    // sum of x, y, and z
    int sum = x + y + z; 
    std::cout << "Sum of x, y, and z: " << sum << std::endl;
    
    // double precision floating point
    double pi = 3.14159; 
    std::cout << "Value of pi: " << pi << std::endl;

    int a = 5; // variable declaration

    // arithmetic operations
    int num1 = 10;
    num1+=1;
    num1*=2;
    num1-=3;
    num1/=2;
    cout <<  num1 <<'\n';
    // to sum only once
    num1++;
    cout <<  num1 <<'\n';
    // to subtract only once
    num1--;
    cout <<  num1 <<'\n';
    // modulus operation
    int modResult = 10 % 3; // remainder of 10 divided by 3
    cout << "Modulus result of 10 % 3: " << modResult << std::endl;

    //type conversion
    double d = 5.5;
    int intValue = static_cast<int>(d); // converting double to int

    int correct = 8;
    int question = 10;
    double result = correct / question * 100 ;
    cout <<  result << "%" << '\n'; 

    double result2 = correct / (double)question * 100 ; // converting int to double for division
    cout <<  result2 << "%" << '\n'; 

    // max function
    int maxValue = std::max(x, y);
    cout << "Maximum value between x and y: " << maxValue<< std::endl;
    // min function
    int minValue = std::min(x, y);
    cout << "Minimum value between x and y: " << minValue << std::endl;

    double g;
    
    // square root function
    g = sqrt(4); // square root of 4
    cout << "Square root of 4: " << g << std::endl;

    // power function
    g = pow(2.0, 3.0); // 2 raised to the power of 3
    cout << "2 raised to the power of 3: " << g << std::endl; 

    // absolute value function
    g = abs(-5); // absolute value of -5
    cout << "Absolute value of -5: " << g << std::endl;

    // round function
    g = round(3.6); // rounding 3.6
    std::cout << "Rounded value of 3.6: " << g << std::endl; 

    // floor function
    g = floor(3.7); // rounding down 3.7    
    std::cout << "Floor value of 3.7: " << g << std::endl;

    // ceil function            
    g = ceil(3.2); // rounding up 3.2
    std::cout << "Ceil value of 3.2: " << g << std::endl;

    // sine function
    g = sin(3.14 / 2); // sine of 90 degrees (3.14/2 radians)
    std::cout << "Sine of 90 degrees: " << g << std::endl;

    // cosine function  
    g = cos(3.14); // cosine of 180 degrees (3.14 radians)
    std::cout << "Cosine of 180 degrees: " << g << std::endl;

    // tangent function
    g = tan(3.14 / 4); // tangent of 45 degrees (3.14/4 radians)
    std::cout << "Tangent of 45 degrees: " << g << std::endl;

    // random number generation
    srand(time(NULL)); // seed the random number generator
    int randomNum = rand(); // random number
    std::cout << "Random number: " << randomNum << std::endl;

    // random number in a specific range (0 to 99)
    int randomInRange = rand() % 100; // random number between 0 and 99 to get 100 just sum 1
    std::cout << "Random number between 0 and 99: " << randomInRange << std::endl;

    return 0;
}