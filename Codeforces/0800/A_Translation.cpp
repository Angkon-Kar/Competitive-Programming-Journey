// Problem: A. Translation
// URL: https://codeforces.com/contest/41/problem/A
// Tag: Implementation, Strings

#include <iostream>
using namespace std;

int main()
{
    string s, t;
    cin >> s >> t;
    reverse(s.begin(), s.end());
    if (s == t)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    return 0;
}