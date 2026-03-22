// Problem: A. A+B Again?
// URL: https://codeforces.com/problemset/problem/1999/A
// Tag: Implementation, Math

#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    
    while (t--)
    {
        int n;
        cin >> n;
        cout << (n%10 + n/10) << endl;
    }
    
    return 0;
}