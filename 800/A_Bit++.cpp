// Problem: A. Bit++
// Contest: Codeforces Round #173 (Div. 2)
// URL: https://codeforces.com/problemset/problem/282/A
// Tag: Implementation
// Memory Limit: 256 Megabytes
// Time Limit: 1 Second

#include<iostream>
using namespace std;

int main() {
    int x, counter{0};
    string s;
    cin >> x;
 
    for (int i = 0; i < x; i++)
    {
        cin >> s;
        if (s[0] == '+' || s[s.length()-1] == '+')
        {
            counter++;
        }
        else
        {
            counter--;
        }
    }
    cout << counter;
    return 0;
}