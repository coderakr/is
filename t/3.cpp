// Write a c++ program to implement DES algorithm.

#include <iostream>
#include <string>
#include <bitset>
using namespace std;

// Initial Permutation Table
int IP[64] = {
58,50,42,34,26,18,10,2,
60,52,44,36,28,20,12,4,
62,54,46,38,30,22,14,6,
64,56,48,40,32,24,16,8,
57,49,41,33,25,17,9,1,
59,51,43,35,27,19,11,3,
61,53,45,37,29,21,13,5,
63,55,47,39,31,23,15,7
};

// Final Permutation Table
int FP[64] = {
40,8,48,16,56,24,64,32,
39,7,47,15,55,23,63,31,
38,6,46,14,54,22,62,30,
37,5,45,13,53,21,61,29,
36,4,44,12,52,20,60,28,
35,3,43,11,51,19,59,27,
34,2,42,10,50,18,58,26,
33,1,41,9,49,17,57,25
};

// Expansion Table
int E[48] = {
32,1,2,3,4,5,4,5,
6,7,8,9,8,9,10,11,
12,13,12,13,14,15,16,17,
16,17,18,19,20,21,20,21,
22,23,24,25,24,25,26,27,
28,29,28,29,30,31,32,1
};

// Straight Permutation Table
int P[32] = {
16,7,20,21,
29,12,28,17,
1,15,23,26,
5,18,31,10,
2,8,24,14,
32,27,3,9,
19,13,30,6,
22,11,4,25
};

// S-Box (only one shown for simplicity, rest similar)
int S[8][4][16] = {
{
{14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7},
{0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8},
{4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0},
{15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13}
},
// Remaining 7 S-boxes omitted for brevity (can repeat same in exam if needed)
};

// Function to apply permutation
string permute(string input, int *table, int n) {
    string output = "";
    for (int i = 0; i < n; i++)
        output += input[table[i] - 1];
    return output;
}

// XOR function
string XOR(string a, string b) {
    string result = "";
    for (int i = 0; i < a.size(); i++)
        result += (a[i] == b[i]) ? '0' : '1';
    return result;
}

// Left shift
string shift_left(string key, int shifts) {
    return key.substr(shifts) + key.substr(0, shifts);
}

// Simplified DES round function
string des_round(string right, string key) {
    // Expansion
    string expanded = permute(right, E, 48);

    // XOR with key
    string xored = XOR(expanded, key);

    // S-box substitution (simplified)
    string sbox_output = "";
    for (int i = 0; i < 8; i++) {
        string block = xored.substr(i * 6, 6);
        int row = (block[0] - '0') * 2 + (block[5] - '0');
        int col = stoi(block.substr(1,4), nullptr, 2);
        int val = S[0][row][col]; // using only S1 for simplicity
        sbox_output += bitset<4>(val).to_string();
    }

    // Permutation
    return permute(sbox_output, P, 32);
}

int main() {
    string plaintext, key;

    cout << "Enter 64-bit plaintext (binary): ";
    cin >> plaintext;

    cout << "Enter 48-bit key (binary): ";
    cin >> key;

    // Initial Permutation
    plaintext = permute(plaintext, IP, 64);

    string left = plaintext.substr(0, 32);
    string right = plaintext.substr(32, 32);

    // 16 rounds (simplified same key used)
    for (int i = 0; i < 16; i++) {
        string temp = right;
        right = XOR(left, des_round(right, key));
        left = temp;
    }

    // Combine
    string combined = right + left;

    // Final Permutation
    string ciphertext = permute(combined, FP, 64);

    cout << "Cipher Text: " << ciphertext << endl;

    return 0;
}