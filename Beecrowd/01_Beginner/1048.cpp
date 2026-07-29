// Problem: Salary Increase
// URL: https://www.beecrowd.com.br/judge/en/problems/view/1048
// Tag: Beginner, Math

#include <iostream>
using namespace std;

int main() {
    double salary, increase, new_salary;
    cin >> salary;

    if(salary <= 400.00){
        increase = salary * 0.15;
    } else if(salary <= 800.00){
        increase = salary * 0.12;
    } else if(salary <= 1200.00){
        increase = salary * 0.10;
    } else if(salary <= 2000.00){
        increase = salary * 0.07;
    } else {
        increase = salary * 0.04;
    }
    new_salary = salary + increase;

    cout.precision(2);
    cout << fixed << "Novo salario: " << new_salary << endl;
    cout << fixed << "Reajuste ganho: " << increase << endl;
    cout << fixed << "Em percentual: " << int((increase / salary) * 100) << " %" << endl;
    
    return 0;
}