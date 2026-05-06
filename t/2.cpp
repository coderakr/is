// Write a c++ program to perform encryption and decryption using the method of Transposition technique.

#include <iostream>
using namespace std;

string encryption(string str, int key) {
  string cipher = "";

  for (int col = 0; col < key; col++) {
    for (int i = col; i < str.length(); i += key) {
      cipher += str[i];
    }
  }

  return cipher;
}

string decryption(string str, int key) {
  string text(str.length(), ' ');
  int index = 0;

  for (int col = 0; col < key; col++) {
    for (int i = col; i < str.length(); i += key) {
      text[i] = str[index++];
    }
  }

  return text;
}

int main(int argc, char* argv[]) {
  string str;
  cout << "Enter Your Text : ";
  getline(cin, str);

  int key;
  cout << "Enter Your Key Size : ";
  cin >> key;

  string encrypt = encryption(str, key);
  cout << "The Encrypted Cipher Is : " << encrypt << endl;

  string decrypt = decryption(encrypt, key);
  cout << "The Decrypted Text Is : " << decrypt;
  return 0;
}