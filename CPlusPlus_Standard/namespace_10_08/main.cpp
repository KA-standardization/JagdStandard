#include <iostream>
#include <functional>
#include "4_可被调用的对象(Callable_Object).cpp"


using namespace std;

//class P {
//public:
//	int m_a;
//	P(int a) :m_a(a) {}
//	~P() {
//		cout << "~P()" << endl;
//	}
//	void display() {
//		cout << m_a << endl;
//	}
//};
//
//struct Q {
//	int m_id;
//	virtual void run() = 0;
//};
//
//class Q1 :Q {
//public:
//	void run() {
//		cout << "Q1" << endl;
//	}
//};
//
//class Q2 :Q {
//public:
//	void run() {
//		cout << "Q2" << endl;
//	}
//};
//
//class P1 {
//public:
//	int m_a;
//	int m_b;
//	int m_l[3];
//	P1(int a, int b);
//	P1(initializer_list<int> list);
//
//	void display() {
//		for (int i = 0; i < 3; i++)
//		{
//			cout << m_l[i] << endl;
//		}
//	}
//};
//
//P1::P1(int a, int b) : m_a(a), m_b(b) {
//	cout << a + b << endl;
//}
//P1::P1(initializer_list<int> list) {
//	int i = 0;
//	for (int a : list) {
//		cout << a << endl;
//		m_l[i++] = a;
//	}
//}
//
//template <class T>
//void print(const T& elements) {
//	for (const auto& ele : elements) {
//		cout << ele << endl;
//	}
//	//for (auto _pos = elements.begin();_pos != elements.end();++_pos) {
//	//	const auto& ele = *_pos;
//	//	cout << ele << endl;
//	//}
//}

//void no_ex(int e) noexcept(true) {
//	try
//	{
//		int a = 5 / e;
//	}
//	catch (const std::exception&)
//	{
//		throw 0;
//	}
//
//}


//void lambda_test() {
//	// 直接调用
//	[] {
//		cout << "lambda simple" << endl;
//	}();
//
//	// 传递对象调用
//	auto lam = [] {
//		cout << "lambda simple2" << endl;
//	};
//
//	lam();
//	// 带参表达式
//	auto lam2 = [](const std::string& s) {
//		cout << s << endl;
//	};
//	lam2("lambda arg");
//	// 指明返回类型
//	auto lam3 = []()->double {
//		return 30;
//	};
//	cout << lam3() << endl;
//	// 访问外部作用域
//	int x = 0;
//	int y = 11;
//	// [=] by value 
//	// [&] by reference 
//	// [=,&y]
//	auto lam4 = [x, &y] {
//		cout << "x:" << x << endl;
//		cout << "y:" << y << endl;
//		y = 100;
//	};
//	lam4();
//	cout << y << endl;
//	// mutable by value by reference 限制lambda所定义的函数对象内
//	int id = 0;
//	auto lam5 = [id]() mutable {
//		cout << id << endl;
//		++id;
//	};
//	lam5();
//	lam5();
//	lam5();
//	cout << "id:" << id << endl;
//	// 明确指出函数返回类型为 lambda
//	//std::function<int(int, int)> reLam() {
//	//	return [](int x, int y)->int {
//	//		return x * y;
//	//	};
//	//}
//}
//
//// 函数生明语法
//template <class T1, class T2>
//auto add(T1 x, T2 y) -> decltype(x + y) {
//
//	return x * y;
//}
//
////模板默认参数
//template <class T, class con = vector<T>>
//class MyClass;
//// 如果只传一个实参,第二个实参会采用默认值
//// MyClass<int> x1;
//
//// 关键字 typename
//// 如果没有typename SubType被视为一个static成员
//template <typename T>
//class MyClass2 {
//	// 34
//	typename T::SubType* ptr;
//};
//// 类型Q作为此处的一个template实参的唯一可能是 类型Q有个内层类型SubType
//class Q {
//public:
//	typedef int SubType;
//};


//int main(int argc,char* argv[])
int main() {

	//P1 p(11, 12);
	//P1 p1{ 12,13,14 };
	//p1.display();

	//no_ex(0);
	//lambda_test();
	//cout << add(1, 2) << endl;
	//int* p = nullptr;

	//MyClass2<Q> x;


	// 非类型模板参数
	//bitset<32> flags32;
	//int i1 = int();
	//int i2{ 3 };
	//cout << i1 << ":" << i2 << endl;




	//int a[5] = { 1,2,3,4,5, };
	//print(a);

	//cout << a << endl;

	//cout << u8R"(\\n)" << endl;
	//cout << hex << 33 << endl;

	//int* p;
	//double* p2 = (double*)p;





	//P p(10);
	//p.display();

	//Q1 q1;
	//Q1* p1 = &q1;
	//p1->run();
	//sizeof(q1);

	//Q* p = (Q*)new Q2;
	//p->m_id = 10;

	//// 栈空间指针p地址
	//cout << &p << endl;

	//// 栈空间指针p指向堆空间地址
	//cout << p << endl;
	//delete p;
	//cout << "乘回风兮载云旗" << endl;

	C c;
	c.memfunc(1, 2);





	getchar();
	//return 0;
}
