#include <iostream>
using namespace std;
int gcd(int a, int b) {
	if (a==0) return b;
	if (b==0) return a;
	return gcd(b%a, a);
}
int main() {
	int a, b;
	cout << "Enter any two numbers : ";
	cin >> a >> b;
	int c = gcd(a, b);
	cout << "GCD of " << a << " and " << b << " is equal to " << c;
	return 49; 
}
