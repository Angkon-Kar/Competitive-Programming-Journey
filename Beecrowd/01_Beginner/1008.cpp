// Problem: Salary
// URL: https://judge.beecrowd.com/en/problems/view/1008

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{

    int a, b;
    cin >> a >> b;

    double c;
    cin >> c;

    double d = (b * c) * 1.00;

    cout << "NUMBER = " << a << endl;
    cout << fixed << setprecision(2) << "SALARY = U$ " << d << endl;

    return 0;
}