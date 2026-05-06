// Write a Java/C/C++/Python program that contains a string (char pointer) with a value \Hello
// World’. The program should AND or and XOR each character in this string with 127 and
// display the result

#include <iostream>
using namespace std;

int main() {
    // Define string using char array (safer than pointer for exam)
    char str[] = "Hello\nWorld";

    cout << "Original String:\n" << str << endl;

    // AND operation
    cout << "\nAfter AND with 127:\n";
    for (int i = 0; str[i] != '\0'; i++) {
        char ch = str[i] & 127;
        cout << ch;
    }
    cout << "\n_____AND_ASCII_OUTPUT_____: ";
    for(int i=0; str[i] !='\0'; i++){
        cout << (int)(str[i] & 127) << " ";
    }
    cout << endl;

    // XOR operation
    // cout << "\n\nAfter XOR with 127: ";
    // for (int i = 0; str[i] != '\0'; i++) {
    //     char ch = str[i] ^ 127;
    //     cout << ch;
    // }
    cout << endl;
    cout << "XOR ASCII OUTPUT: ";
    for(int i=0; str[i] !='\0'; i++){
        cout << (int)(str[i] & 127) << " ";
    }
    cout << endl;
    return 0;
}