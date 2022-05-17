#include <iostream>
#include <vector>
#include <algorithm>
#include <list>

using namespace std;


void lambda_mutable() {
	list<int> l_i = { 1,2,3,4,5,6,7 };
	list<int>::iterator pos;
	int sum = 0;
	/*
		处理状态时,如果使用mutable,查找准则是个带状态的function object,其对应的lambda版本严格以by value方式传递内部计数器(用来表现状态)
		之所以by value是因为这个计数器在此次算法之外是不需要的
		remove_if算法在执行过程中会复制一份lambda,于是存在两个lambda对象都移除第三元素
	*/
	pos = remove_if(l_i.begin(), l_i.end(), [sum](int)mutable {return ++sum == 3;});
	l_i.erase(pos, l_i.end());
	for (int e : l_i) {
		cout << e << endl;
	}
}

void lambda_by_ref() {
	list<int> l_i = {1,2,3,4,5,6,7,8};
	list<int>::iterator pos;
	int sum = 0;
	pos = remove_if(l_i.begin(), l_i.end(), [&sum](int) {return ++sum == 3;});
	l_i.erase(pos, l_i.end());
	for (int i=0;i < size(l_i);++i) {
		cout << &l_i << endl;
	}
}

int main() {
	//vector<int> v_i = { 1,2,3,4,5,6 };
	//long sum = 0;
	//for_each(v_i.begin(), v_i.end(), 
	//	[&sum](int elem) // 不需要针对将被传入的function object 定义一个class,只要传入所需的机能.计算所得的状态被置于lambda之外的变量sum
	//	{
	//		sum += elem;
	//	});
	//cout << sum << endl;

	//lambda_mutable();
	lambda_by_ref();





	getchar();
	return 0;
}