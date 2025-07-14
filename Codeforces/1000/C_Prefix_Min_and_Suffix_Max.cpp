// Problem: C. Prefix Min and Suffix Max
// URL: https://codeforces.com/contest/2123/problem/C
// Tag: Brute Force, Data Structures

#include <iostream>
#include <vector>
#include <string>
#include <algorithm> // For std::min and std::max
 
void solve()
{
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for (int i = 0; i < n; ++i)
    {
        std::cin >> a[i];
    }
 
    // min_prefix[i] stores the minimum value in a[0...i]
    std::vector<int> min_prefix(n);
    min_prefix[0] = a[0];
    for (int i = 1; i < n; ++i)
    {
        min_prefix[i] = std::min(min_prefix[i - 1], a[i]);
    }
 
    // max_suffix[i] stores the maximum value in a[i...n-1]
    std::vector<int> max_suffix(n);
    max_suffix[n - 1] = a[n - 1];
    for (int i = n - 2; i >= 0; --i)
    {
        max_suffix[i] = std::max(max_suffix[i + 1], a[i]);
    }
 
    std::string ans(n, '0'); // Initialize answer string with '0's
 
    for (int i = 0; i < n; ++i)
    {
        // Condition 1: a[i] is smaller than all elements to its left.
        // This means a[i] is the minimum of the prefix a[0...i].
        // For i=0, there are no elements to the left, so this condition is true by default.
        bool possible_from_left_side = false;
        if (i == 0)
        {
            possible_from_left_side = true;
        }
        else
        {
            if (min_prefix[i - 1] > a[i])
            {
                possible_from_left_side = true;
            }
        }
 
        // Condition 2: a[i] is larger than all elements to its right.
        // This means a[i] is the maximum of the suffix a[i...n-1].
        // For i=n-1, there are no elements to the right, so this condition is true by default.
        bool possible_from_right_side = false;
        if (i == n - 1)
        {
            possible_from_right_side = true;
        }
        else
        {
            if (max_suffix[i + 1] < a[i])
            {
                possible_from_right_side = true;
            }
        }
 
        // If either condition is met, a[i] can be the final element.
        if (possible_from_left_side || possible_from_right_side)
        {
            ans[i] = '1';
        }
    }
    std::cout << ans << std::endl;
}
 
int main()
{
    // Optimize C++ standard streams for faster input/output.
    // This is common in competitive programming.
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
 
    int t;
    std::cin >> t; // Read the number of test cases
    while (t--)
    {
        solve(); // Solve each test case
    }
    return 0;
}