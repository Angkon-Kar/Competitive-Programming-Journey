// Problem: A. Petya and Strings
// URL: https://codeforces.com/problemset/problem/112/A
// Tag: Implementation, Strings

#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    string s, t;
    getline(cin, s);
    getline(cin, t);

    // Convert both strings to lowercase
    for (char &c : s)
        c = tolower(c);
    for (char &c : t)
        c = tolower(c);

    // Compare strings
    if (s == t)
        cout << "0\n";
    else if (s > t)
        cout << "1\n";
    else
        cout << "-1\n";

    return 0;
}