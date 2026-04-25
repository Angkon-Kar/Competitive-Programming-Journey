// Problem: System of Equations
// URL: https://codeforces.com/problemset/problem/214/A
// Tag: Brute Force

#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    int count = 0;

    for (int a = 0; a * a <= n; a++) {
        int b = n - a * a;
        if (b >= 0 && a + b * b == m) {
            count++;
        }
    }

    for (int b = 0; b * b <= m; b++) {
        int a = m - b * b;
        if (a >= 0 && a * a + b == n) {
            // Avoid double-counting the same pair
            if (a * a + b == n && a + b * b == m) {
                // This pair was already counted in the first loop
                // so we skip adding again
            }
        }
    }

    cout << count << "\n";
    return 0;
}