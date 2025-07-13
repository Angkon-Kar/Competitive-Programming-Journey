// Problem: A. Beautiful Matrix
// Contest: Codeforces Round #161 (Div. 2)
// URL: https://codeforces.com/problemset/problem/263/A
// Tag: Implementation
// Memory Limit: 256 Megabytes
// Time Limit: 2 Second

#include <iostream>
using namespace std;

int main()
{
    int x, ii, jj, moves{0}, imoves{0}, jmoves{0};

    for (int i = 1; i <= 5; i++)
    {
        for (int j = 1; j <= 5; j++)
        {
            cin >> x;

            if (x == 1)
            {
                ii = i;
                jj = j;
            }
        }
    }

    jmoves = abs(jj - 3);
    imoves = abs(ii - 3);
    cout << imoves + jmoves;

    return 0;
}