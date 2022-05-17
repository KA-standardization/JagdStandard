#include <ratio>
#include <iostream>

using namespace std;

int main() {
	typedef ratio<5, 3> F1;
	cout << F1::num << "/" << F1::den << endl;

	ratio<12, 12> one;
	cout << one.num << "/" << one.den << endl;



	getchar();
	return 0;
}
