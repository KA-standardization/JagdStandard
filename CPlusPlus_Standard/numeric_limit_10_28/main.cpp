#include <climits>
#include <cfloat>
#include <limits.h>
#include <float.h>
#include <iostream>

using namespace std;

int main() {

	numeric_limits<float>::max();

	cout << numeric_limits<int>::is_specialized << endl;

	cout << numeric_limits<long int>::max() << endl;

	cout << numeric_limits<char>::is_signed << endl;
	getchar();
	return 0;
}
