#include <functional>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
// �����ظ���д�������ռ�
using namespace std::placeholders;

void incr(int& i) {
	++i;
}

/*
	���ó�Ա���� 492
		bind(&P::print,_1) 
			����һ��function obj,������Դ����P����paraml.print()
			Ҳ����˵,��һʵ���Ǹ���Ա����,��һ��ʵ�ν��������Ե��ó�Ա�����Ķ���
		bind(&P::print_2,_1,_2)
			_2��Ա�����Ĳ���
			P n("haha")
			bind(&P::print_2,_1,"abc")(n)
	���þ��иĶ������ĳ�Ա���� modifying member function

	���ڳ�Ա����,����mem_fn()adapter �Ͳ���Ҫռλ����ʾ������
		std::mem_fn(&P::print)
		std::mem_fn(&P::print)(n,"abc"); // calls n.print("abc");

	�������ݳ�Ա
		�����Ǹ�map, ��Ԫ����key/value pair, Ϊ�˵õ���Ԫ�ص�value�ķ���Ȩ����������&map
		std::bind(std::plus<int>(),_1,bind(&map<string, int>::value_type::second,_2))

	Adapter
		
*/



int main() {
	auto plus11 = std::bind(std::plus<int>(), std::placeholders::_1, 11);
	std::cout << "plus11  " << plus11(1) << std::endl;

	auto plus11multi = std::bind(std::multiplies<int>(), std::bind(std::plus<int>(), std::placeholders::_1, 10), 2);
	std::cout << "plus multiplies  " << plus11multi(2) << std::endl;

	// placeholders::_1 ָ��һ������
	auto pow3 = std::bind(std::multiplies<int>(), std::bind(std::multiplies<int>(), std::placeholders::_1, std::placeholders::_1), std::placeholders::_1);
	std::cout << "pow3  " << pow3(2) << std::endl;

	auto divide = std::bind(std::divides<double>(), std::placeholders::_2, std::placeholders::_1);
	std::cout << "divide  "<<divide(2,4) << std::endl;

	// �����binder��function object�����㷨,���߻������������������ÿһ��Ԫ�� 
	// �㷨 by reference
	

	vector<int> coll = { 1,2,3,4,5 };
	auto s = std::transform(coll.begin(), coll.end(), coll.begin(), std::bind(std::plus<int>(), _1, 100));
	for (int i = 0;i < size(coll);i++) {
		cout << "coll  " << coll[i] << endl;
	}
	
	// bind�ڲ��Ḵ�Ʊ������ʵ�� �������� ref()\cref()
	int i = 0;
	std::bind(incr, i)();
	cout << "i=" << i << endl;
	//std::bind(incr, std::ref(i))();
	//cout << "i=" << i << endl;

	string coll2 = "abcdef";
	auto index = std::find_if(coll2.begin(), coll2.end(), std::bind2nd(std::ptr_fun(std::strcmp), "c"));
	/*cout << "index-->" << index << endl;*/


	getchar();
	return 0;
}