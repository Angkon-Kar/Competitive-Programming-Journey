// Problem: A. Word
// URL: https://codeforces.com/problemset/problem/59/A
// Tag: Implementation, Strings

#include <iostream>
using namespace std;

int main()
{
    int n, i, u = 0, l = 0;
    string s;
    cin >> s;
    n = s.size();
    for (i = 0; i < n; i++)
    {
        if (isupper(s[i]))
        {
            u++;
        }
        else
        {
            l++;
        }
    }
    if (u > l)
    {
        for (i = 0; i < n; i++)
        {
            s[i] = toupper(s[i]);
        }
    }
    else
    {
        for (i = 0; i < n; i++)
        {
            s[i] = tolower(s[i]);
        }
    }
    cout << s;

    return 0;
}