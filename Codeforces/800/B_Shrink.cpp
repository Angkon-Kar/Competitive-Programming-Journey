// Problem: B. Shrink
// URL: https://codeforces.com/contest/2117/problem/B
// Tag: Constructive Algorithms

#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        for (int i = 2; i <= n; i++)
            cout << i << ' ';
        cout << 1 << endl;
    }
}