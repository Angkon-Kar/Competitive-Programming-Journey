// Problem: A. Team
// URL: https://codeforces.com/problemset/problem/231/A
// Tag: Brute Force, Greedy

#include<iostream>
using namespace std;
 
#define optimize() ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define fraction() cout.unsetf(ios::floatfield);cout.precision(10);cout.setf(ios::fixed,ios::floatfield);
 
int main()
{
    int n, i, j, k = 0, c = 0, a[3];
    cin>>n;
 
    for (int i = 0; i < n; i++)
    {
        k = 0;
        for (int j = 0; j < 3; j++)
        {
            cin>>a[j];
        }
        for (int j = 0; j < 3; j++)
        {
            if(a[j] == 1) k++;
        }
        if(k > 1) c++;
    }
    
    cout << c << endl;
    
    return 0;
}