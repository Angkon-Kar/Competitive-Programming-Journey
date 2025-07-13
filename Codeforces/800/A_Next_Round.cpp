// Problem: A. Next Round
// Contest: VK Cup 2012 Qualification Round
// URL: https://codeforces.com/problemset/problem/158/A
// Tag: Special Problem, Implementation
// Memory Limit: 256 Megabytes
// Time Limit: 3 Second

#include <iostream>
using namespace std;

int main()
{

    int n, k, max, i, c = 0, a[50];
    cin >> n >> k;

    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        if ((i + 1) == k)
        {
            max = a[i];
        }
    }

    for (int i = 0; i < n; i++)
    {
        if (a[i] >= max && a[i] > 0)
        {
            c++;
        }
    }

    cout << c << endl;

    return 0;
}