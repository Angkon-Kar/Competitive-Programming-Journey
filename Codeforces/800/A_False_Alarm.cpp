// Problem: A. False Alarm
// URL: https://codeforces.com/contest/2117/problem/A
// Tag: Greedy, Implementation

#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n, x;

        cin >> n >> x;

        int l = 1e5, r = -1;
        for (int i = 0; i < n; i++)
        {
            int door;
            cin >> door;

            if (door == 1)
            {
                l = min(l, i);
                r = max(r, i);
            }
        }
        if (x >= r - l + 1)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }

    return 0;
}