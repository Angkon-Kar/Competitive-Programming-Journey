// Problem: A. Blackboard Game
// URL: https://codeforces.com/contest/2123/problem/A
// Tag: Math

#include <iostream>
#include <string>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        if (n % 4 == 0)
        {
            cout << "Bob\n";
        }
        else
        {
            cout << "Alice\n";
        }
    }
    return 0;
}