// Problem: Area of a Circle
// URL: https://judge.beecrowd.com/en/problems/view/1002

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    double r, π = 3.14159;
    cin >> r;

    cout << fixed << setprecision(4) << "A=" << π * r * r << endl;
    return 0;
}