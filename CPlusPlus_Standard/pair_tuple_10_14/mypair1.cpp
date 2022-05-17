#include <iostream>
#include <utility>
#include <tuple>

using namespace std;

struct Foo {
	Foo(tuple<int, float>) {
		cout << "Foo(tuple<int, float>)" << endl;
	}

	template <typename... Args>
	Foo(Args... args) {
		cout << "Foo(Args... args)" << endl;
	}
	~Foo() {

	}
};
