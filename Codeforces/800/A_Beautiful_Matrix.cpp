// Problem: A. Beautiful Matrix
// URL: https://codeforces.com/problemset/problem/263/A
// Tag: Implementation

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