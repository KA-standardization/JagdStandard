#include <iostream>
#include "mypair1.cpp"
//#include "mypair2.cpp"


using namespace std;



void ka_pair_() {
	pair<int, double> pa(11, 11.1);
	pair<int, double> pa2;
	pair<int, double> pa3(22, 22.2);
	pa2 = pa;
	cout << pa.first << " <- pa ->  " << pa.second << endl;
	cout << get<0>(pa) << " <- pa ->  " << get<1>(pa) << endl;
	cout << (pa2 == pa) << endl;
	cout << (pa2 > pa) << endl;
	cout << get<0>(pa3) << " <- pa3 ->  " << get<1>(pa3) << endl;
	pa3.swap(pa);
	//swap(pa3, pa);
	cout << pa.first << " <- pa ->  " << pa.second << endl;
	cout << pa2.first << " <- pa2 ->  " << pa2.second << endl;

	int val_1 = 11;
	long val_2 = 100;
	pair<int, long> pa4 = make_pair(val_1, val_2);
	cout << &pa4 << endl;
}

template <class T1, class T2>
ostream& operator << (ostream& strm, const pair<T1, T2>& pa) {
	return strm << "[" << pa.first << "," << pa.second << "]";
}

void f(std::pair<int, const char*> pa) {
	cout << "std::pair<int,const char*>" << pa.first << "--" << pa.second << endl;
}

void b(std::pair<const int, std::string> pa) {
	cout << "std::pair<const int, std::string>" << pa.first << "--" << pa.second << endl;
}





int main() {
	//ka_pair_();
	//pair<int, double> p
	// a(11, 11.1);
	//operator<<(cout, pa);
	//typedef pair<int, float> IntFloatPair;
	//IntFloatPair pa_(123, 2.1);

	//cout << tuple_size<IntFloatPair>::value << endl;
	//pair<int, int> pa(21, 31);
	//tuple_element<0, IntFloatPair>::type;

	//tuple<int, float> t(1, 2.2);
	//pair<int, Foo> pa_1(32, t);
	////pair<int, Foo> pa_2(piecewise_construct, make_tuple(42), t);
	//pair<int, Foo> pa_3(piecewise_construct, tuple(42), t);
	//// 便捷函数 make_pair() 如果可能的话使用move语义,否则使用copy语义
	//make_pair(22, '@');

	//f(make_pair(22, "buch"));
	//b(make_pair(32, "Kaiser"));
	//int i = my_ref_pair();

	//cout << "i: " << i << endl;
	int i = 0;
	auto p = std::make_pair(std::ref(i), std::ref(i));
	++p.first;
	++p.second;

	std::cout << "i: " << i << std::endl;


	getchar();
	return 0;
}
