// Problem: System of Equations
// URL: https://codeforces.com/problemset/problem/214/A
// Tag: Brute Force

// Solved from first equations: a^2 + b = n
#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    int count = 0;
    for (int a = 0; a*a <= n; a++){
        int b = n - a*a;
        if ((b >= 0) && (a + b*b == m)){
            count++;
        }
    }

    cout << count << endl;
    return 0;
}