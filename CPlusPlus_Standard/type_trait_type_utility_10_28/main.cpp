#include <iostream>
#include <type_traits>
#include <functional>

using namespace std;

template <class T>
void foo(const T& val) {
	if (is_pointer<T>::value) {
		cout << "is_pointer" << endl;
	}
	else
	{
		cout << "no_pointer" << endl;
	}
}

template <typename T>
void bar_impl(const T& val, std::true_type) {
	cout << "is point val = " << *val << endl;
}

template <typename T>
void bar_impl(const T& val, std::false_type) {
	cout << "no point val = " << val << endl;
}

template <typename T>
void bar(const T& val) {
	// std::is_pointer<T>() 产生 true_type 否则false_type
	bar_impl(val, std::is_pointer<T>());
}

template <class T>
void foo_impl(T val, true_type) {
	cout << "int: " << val << endl;
}

template <class T>
void foo_impl(T val, false_type) {
	cout << "float: " << val << endl;
}

template <class T>
void foo1(T val) {
	foo_impl(val, std::is_integral<T>());
}

template <class T1, class T2>
typename std::common_type<T1, T2>::type test(const T1& x, const T2& y) {

	return x + y;
}

class C {
public:
	void myfunc(int x, int y) const {
		cout << x + y << endl;
	}
};

// 126 类型判断工具 type predicate
// 127 针对class 类型而设计 能够更加阐明class细节的 trait

int main() {
	int a = 10;
	float b = 11.1;
	int* p = &a;
	bar(a);

	foo1(a);
	foo1(b);

	cout << test(a, b) << endl;
	typedef int T;
	add_const<T>::type tp = 10;
	typedef const int T1;
	remove_const<T>::type tp2 = 11;
	typedef int& T3;
	T3 tp3 = a;

	cout << &tp << endl;
	cout << tp2 << endl;
	cout << tp3 << endl;

	// arary类型的维度
	cout << rank<int[][5][1]>::value << endl;
	// 维度2 的尺度
	cout << extent<int[][5][1], 1>::value << endl;

	int x;
	std::ref(x); //int&
	int y;
	std::cref(y); //const int&

	// wrapper
	std::function<void(const C&, int, int)> mf;
	mf = &C::myfunc;
	mf(C(), 42, 12);

	getchar();
	return 0;
}
