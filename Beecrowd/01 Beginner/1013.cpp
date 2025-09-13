// Problem: The Greatest
// URL: https://judge.beecrowd.com/en/problems/view/1013

#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int A, B, C;
    cin >> A >> B >> C;

    int greatestAB = (A + B + abs(A - B)) / 2;
    int greatest = (greatestAB + C + abs(greatestAB - C)) / 2;

    cout << greatest << " eh o maior" << endl;
    return 0;
}
