// Problem: A. Watermelon
// URL: https://codeforces.com/contest/4/problem/A
// Tag: Brute Force, Math

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