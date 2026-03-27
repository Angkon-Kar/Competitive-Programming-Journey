// Problem: A. Codeforces Checking
// URL: https://codeforces.com/problemset/problem/1791/A
// Tag: Implementation, Strings

#include <iostream>
#include <string>

using namespace std;

void solve() {
    char c;
    cin >> c;

    string target = "codeforces";

    if (target.find(c) != string::npos) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
}

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--) {
        solve();
    }

    return 0;
}