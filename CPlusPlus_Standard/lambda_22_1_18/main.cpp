#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

// 仿函数
// 可以将仿函数看做一般函数，只不过用的是一种更复杂的撰写手段：并非将所有语句放在函数体中

template <class InputIter,class T>
T acc(InputIter first, InputIter last, T init, T(*ptr)(T, T)) {
	cout << "first" << first << endl;
	cout << "++first" << ++first << endl;
	cout << "last" << last << endl;
	//while (first!=last){
	//	init = (*ptr)(init, *first);
	//	++first;
	//}

	//return init;
	return 0;
}

int func1(int x, int y) {

	return x + y;
}


int main() {

	int a[5] = { 1,2,3,4,5 };
	//int a_len = sizeof(a) / sizeof(a[0]);
	////cout <<  a_len << endl;
	////cout << sizeof(a) << endl;
	//for (int i = 0;i < a_len;++i) {
	//	cout << a[i] << endl;
	//}

	cout << a[0] << endl;
	auto a2 = ++a[0];
	cout << a2 << endl;


	int total = acc(&a[0], &a[5], 0, func1);
	//cout << "total:  " << total << endl;

	return 0;
}