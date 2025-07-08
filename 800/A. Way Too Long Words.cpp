// Problem: A. Way Too Long Words
// Contest: Codeforces Round #65 (Div. 2)
// URL: https://codeforces.com/problemset/problem/71/A
// Tag: Strings
// Memory Limit: 256 Megabytes
// Time Limit: 1 Second

#include <iostream>
using namespace std;

int main()
{
    char s[123];
    int t;
    cin >> t;

    while (t--)
    {
        cin >> s;
        int len = 0;
        while (s[len] != 0)
        {
            len++;
        }
        if (len > 10)
        {
            cout << s[0] << len - 2 << s[len - 1] << endl;
        }
        else
        {
            cout << s << endl;
        }
    }
}