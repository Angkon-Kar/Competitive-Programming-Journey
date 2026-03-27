// Problem: A. Codeforces Checking
// URL: https://codeforces.com/problemset/problem/1791/A
// Tag: Implementation, Strings

#include <iostream>
#include <string>
using namespace std;

int main() {
    
    int t;
    cin >> t;

    while (t--)
    {
        string s;
        cin >> s;

        if (s == "codeforces")
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}