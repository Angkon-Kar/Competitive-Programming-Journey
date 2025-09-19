// Problem: Area
// URL: https://judge.beecrowd.com/en/problems/view/1012

#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

int main()
{
    double a, b, c;
    cin >> a >> b >> c;

    double pi = 3.14159;

    cout << fixed << setprecision(3) << "TRIANGULO: " << 0.5 * a * c << endl;
    cout << fixed << setprecision(3) << "CIRCULO: " << pi * pow(c, 2) << endl;
    cout << fixed << setprecision(3) << "TRAPEZIO: " << 0.5 * (a + b) * c << endl;
    cout << fixed << setprecision(3) << "QUADRADO: " << pow(b, 2) << endl;
    cout << fixed << setprecision(3) << "RETANGULO: " << a * b << endl;

    return 0;
}