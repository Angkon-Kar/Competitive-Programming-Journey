// Problem: A. Summation
// Contest: Codeforces Round 4 (Div. 2)
// URL: https://codeforces.com/contest/4/problem/A
// Memory Limit: 64 Megabytes
// Time Limit: 1 Second

#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;

    if (n > 2 && n % 2 == 0)
    {
        cout << "Yes" << endl;
    }
    else
    {
        cout << "No" << endl;
    }
    return 0;
}