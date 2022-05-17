#include <cstddef>
#include <typeinfo>
#include <cstring>

#include <iostream>

using namespace std;

int main() {
	int* p = NULL;
	if (typeid(*p) == typeid(NULL)) {
		cout << "* p is NULL" << endl;
	}

	string s1 = "abcd";
	string* p2 = &s1;
	cout << memchr(p2, 98, 4) << endl;
	cout << p2->c_str() << endl;
	cout << p2[0] << endl;

	getchar();
}
