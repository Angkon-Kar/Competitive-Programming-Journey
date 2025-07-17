// Problem: A. Only One Digit
// URL: https://codeforces.com/contest/2126/problem/A
// Tag: Implementation, Math

#include <iostream>
#include <string>
#include <algorithm>
#include <set>

// Function to check if two numbers share a common digit
bool sharesCommonDigit(int x, int y) {
    std::string s_x = std::to_string(x);
    std::string s_y = std::to_string(y);

    std::set<char> digits_x;
    for (char c : s_x) {
        digits_x.insert(c);
    }

    for (char c : s_y) {
        if (digits_x.count(c)) {
            return true;
        }
    }
    return false;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int t;
    std::cin >> t;
    while (t--) {
        int x;
        std::cin >> x;

        // Iterate from 0 upwards to find the smallest y
        for (int y = 0; ; ++y) {
            if (sharesCommonDigit(x, y)) {
                std::cout << y << std::endl;
                break;
            }
        }
    }
    return 0;
}