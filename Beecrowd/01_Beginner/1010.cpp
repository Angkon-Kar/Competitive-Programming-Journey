// Problem: Simple Calculate
// URL: https://judge.beecrowd.com/en/problems/view/1010

#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int a, b, c, d;
    double price1, price2;

    cin >> a >> b >> price1;
    cin >> c >> d >> price2;

    double total = (b * price1) + (d * price2);

    cout << fixed << setprecision(2) << "VALOR A PAGAR: R$ " << total << endl;

    return 0;
}