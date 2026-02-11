// Problem: A. A+B Again?
// URL: https://codeforces.com/problemset/problem/1999/A
// Tag: Implementation, Math

#include <iostream>
#include <vector>

using namespace std;

int main() { 
    
    vector<int> sums(100); 
    for(int i = 10; i < 100; i++) { 
        sums[i] = i / 10 + i % 10; 
    } 

    int t; cin >> t; 
    while(t--) { 
        int n; cin >> n; 
        cout << sums[n] << "\n"; 
    } 
    
    return 0; 
}