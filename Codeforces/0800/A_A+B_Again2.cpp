// Problem: A. A+B Again?
// URL: https://codeforces.com/problemset/problem/1999/A
// Tag: Implementation, Math

#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    
    while (t--)
    {
        string s;
        cin >> s;

        int sum = 0;
        for (char c : s)
        {
            sum += c - '0';
        }
        cout << sum << endl;
        
    }
    
    return 0;
}