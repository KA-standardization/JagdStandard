#include <chrono>
#include <iostream>
#include <ratio>


using namespace std;

int main() {
	chrono::duration<int> t(20);
	cout << t.count() << endl;

	chrono::duration<double, ratio<1, 3>> d1(1);
	chrono::duration<double, ratio<1, 5>> d2(1);
	cout << d1.count() << endl;


	cout << (d1 > d2) << endl;
	//cout << dd << endl;
	chrono::milliseconds ms;
	chrono::seconds s(20);
	chrono::hours h(24);
	ms += s + h;
	ms *= 2;
	cout << ms.count() << "ms" << endl;
	cout << chrono::nanoseconds(ms).count() << "ns" << endl;

	chrono::seconds sec(155);
	// 隐式转换至一个较精准的单位类型永远可行 转换至较粗的单位类型不可行 要强制转换chrono::duration_cast
	//chrono::minutes m1 = sec; ERROR
	chrono::minutes m2 = chrono::duration_cast<std::chrono::minutes>(sec);
	cout << "m2.count()" << m2.count() << endl;

	cout << "##########################" << endl;

	chrono::milliseconds ms1(7777777);
	chrono::hours hh = chrono::duration_cast<chrono::hours>(ms1);
	chrono::minutes mm = chrono::duration_cast<chrono::minutes>(ms1 % chrono::hours(1));
	chrono::seconds ss = chrono::duration_cast<chrono::seconds>(ms1 % chrono::minutes(1));
	chrono::milliseconds mll = chrono::duration_cast<chrono::milliseconds>(ms1 % chrono::milliseconds(1));

	cout << hh.count() << endl;
	getchar();
	return 0;
}
