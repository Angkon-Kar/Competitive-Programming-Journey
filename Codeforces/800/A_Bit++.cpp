// Problem: A. Bit++
// URL: https://codeforces.com/problemset/problem/282/A
// Tag: Implementation

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