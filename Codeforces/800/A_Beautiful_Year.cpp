// Problem: A. Beautiful Year
// URL: https://codeforces.com/problemset/problem/271/A
// Tag: Implementation

#include <iostream>
using namespace std;

bool is_distinct(int year) {
    // Extract individual digits
    int a = year / 1000;       // Thousands place
    int b = (year / 100) % 10; // Hundreds place
    int c = (year / 10) % 10;  // Tens place
    int d = year % 10;         // Units place

    // Check if every digit is different from every other digit
    return (a != b && a != c && a != d && 
            b != c && b != d && 
            c != d);
}

int main() {
    int y;
    if (!(cin >> y)) return 0;

    // Increment and check until the condition is met
    while (true) {
        y++;
        if (is_distinct(y)) {
            cout << y << endl;
            break;
        }
    }

    return 0;
}