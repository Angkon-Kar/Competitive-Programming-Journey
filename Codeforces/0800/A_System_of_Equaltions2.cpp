// Problem: System of Equations
// URL: https://codeforces.com/problemset/problem/214/A
// Tag: Math

// Solved from second equations: a + b^2 = m
#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    int count = 0;
    for (int b = 0; b*b <= m; b++){
        int a = m - b*b;
        if ((a >= 0) && (a*a + b == n)){
            count++;
        }
    }

    cout << count << endl;
    return 0;
}