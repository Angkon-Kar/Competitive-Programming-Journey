// Problem: Added A. Plus or Minus
// URL: https://codeforces.com/problemset/problem/1807/A
// Tag: Implementation

#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int n;
    cin >> n;
 
    for (int i = 1; i <= n; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        if(a + b == c){
            cout << "+" << endl;
        }
        else{
            cout << "-" << endl;
        }
    }
}