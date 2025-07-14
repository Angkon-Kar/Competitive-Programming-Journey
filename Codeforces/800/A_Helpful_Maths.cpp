// Problem: A. Helpful Maths
// URL: https://codeforces.com/problemset/problem/339/A
// Tag: Greedy, Implementation, Sortings, Strings

#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
    string s;
    cin >> s;

    string digits = "";
    // Extract only the digits
    for (char c : s)
    {
        if (c != '+')
        {
            digits += c;
        }
    }

    // Sort the digits
    sort(digits.begin(), digits.end());

    // Reconstruct the output with plus signs
    for (size_t i = 0; i < digits.length(); ++i)
    {
        if (i > 0)
            cout << "+";
        cout << digits[i];
    }
    cout << endl;

    return 0;
}