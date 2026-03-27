// Problem: A. Odd Divisor
// URL: https://codeforces.com/problemset/problem/1475/A
// Tag: Math, Number Theory

#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--)
    {
        long long n;
        cin >> n;

        if (n & (n - 1))
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
        {
            
        }
        
    }
    
}
/*
Explanation:
A number has an odd divisor greater than 1 if and only if it is not a power of 2. 
This is because powers of 2 only have divisors that are also powers of 2, which are all even except for 1.
Therefore, if n is a power of 2, it does not have any odd divisors greater than 1, and the answer is "NO". 
If n is not a power of 2, it has at least one odd divisor greater than 1, and the answer is "YES".
The check n & (n - 1) is a common bitwise operation to determine if n is a power of 2.

Input:
6
2
3
4
5
998244353
1099511627776

Output:
NO
YES
NO
YES
YES
NO

*/