// Problem: B. Drinks
// URL: https://codeforces.com/problemset/problem/200/B
// Tag: Implementation, Math

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cin >> n;
    double sum = 0;
    for (int i = 0; i < n; i++)
    {
        double p;
        cin >> p;
        sum += p;
    }

    cout << fixed << setprecision(12) << sum / n << endl;

    return 0;
}