// Problem: Sphere
// URL: https://judge.beecrowd.com/en/problems/view/1011

#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

int main()
{
    int r;
    cin >> r;

    double pi = 3.14159;

    double total = (4 / 3.0) * pi * (pow(r, 3));
    cout << fixed << setprecision(3) << "VOLUME = " << total << endl;

    return 0;
}