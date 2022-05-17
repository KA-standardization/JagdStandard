#include <iostream>
#include <iterator>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	istream_iterator<string> cinPos(cin);
	ostream_iterator<string> coutPos(cout, " ");

	while (cinPos != istream_iterator<string>())
	{
		// cin指针加2
		advance(cinPos, 2);
		if (cinPos != istream_iterator<string>()) {
			*coutPos++ = *cinPos++;
		}
	}
	cout << endl;

	getchar();
	return 0;
}
