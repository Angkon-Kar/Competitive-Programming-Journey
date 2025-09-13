// Problem: Salary with Bonus
// URL: https://judge.beecrowd.com/en/problems/view/1009

#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int main()
{
    string name;
    cin >> name;
    
    double a, b;
    cin >> a >> b;

    double c = a + (b * 0.15);
    cout << fixed << setprecision(2) << "TOTAL = R$ " << c << endl;

    return 0;
}