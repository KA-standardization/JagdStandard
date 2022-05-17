#include <iostream>

using namespace std;

struct MyClass {
private:
	int* elements;
	int numElems;
public:
	MyClass(int* ars, int num) :elements(ars), numElems(num) {}
	void swap(MyClass& m) {
		std::swap(elements, m.elements);
		std::swap(numElems, m.numElems);
	}
	void print() {
		cout << "num: " << numElems;
		cout << "first element: " << elements[0] << endl;
	}
	~MyClass() {
		cout << "~MyClass() " << endl;
	}
};

inline void swap(MyClass& m1, MyClass& m2) noexcept(noexcept(m1.swap(m2))) {
	m1.swap(m2);
}


int main() {
	int a[] = { 1,2,3 };
	int num_a = 3;

	int b[] = { 4,5 };
	int num_b = 2;
	MyClass my1 = MyClass(a, num_a);
	MyClass my2 = MyClass(b, num_b);
	my1.print();
	my2.print();

	swap(my1, my2);
	my1.print();
	my2.print();


	getchar();
	return 0;
}
