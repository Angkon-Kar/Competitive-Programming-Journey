// Problem: A. Football
// Contest: Codeforces Round #77 (Div. 2)
// URL: https://codeforces.com/problemset/problem/96/A
// Tag: Implementation, Strings
// Memory Limit: 256 Megabytes
// Time Limit: 2 Second

#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s;
    cin >> s;

    if (s.find("0000000") != string::npos || s.find("1111111") != string::npos)
    {
        cout << "YES";
    }
    else
    {
        cout << "NO";
    }

    return 0;
}