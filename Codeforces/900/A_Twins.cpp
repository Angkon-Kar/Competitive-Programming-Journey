// Problem: A. Twins
// URL: https://codeforces.com/problemset/problem/160/A
// Tag: Greedy, Sorting

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> coins(n);

    for (int i = 0; i < n; i++)
    {
        cin >> coins[i];
    }

    sort(coins.rbegin(), coins.rend());

    int total = accumulate(coins.begin(), coins.end(), 0);
    int my_sum = 0;
    int count = 0;

    for (int i = 0; i < n; i++)
    {
        my_sum += coins[i];
        count++;
        if (my_sum > total - my_sum) {
            break;
        }
    }
    
    cout << count << "\n";

    return 0;
}