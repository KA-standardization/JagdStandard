#include <iostream>

using namespace std;

class C {
public:
	void operator()(int x, int y) const;
	void memfunc(int x, int y) const;
};

void C::operator()(int x, int y) const {

}

void C::memfunc(int x, int y) const {
	cout << x + y << endl;
}
