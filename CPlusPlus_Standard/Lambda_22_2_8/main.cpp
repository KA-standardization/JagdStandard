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
		����״̬ʱ,���ʹ��mutable,����׼���Ǹ���״̬��function object,���Ӧ��lambda�汾�ϸ���by value��ʽ�����ڲ�������(��������״̬)
		֮����by value����Ϊ����������ڴ˴��㷨֮���ǲ���Ҫ��
		remove_if�㷨��ִ�й����лḴ��һ��lambda,���Ǵ�������lambda�����Ƴ�����Ԫ��
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
	//	[&sum](int elem) // ����Ҫ��Խ��������function object ����һ��class,ֻҪ��������Ļ���.�������õ�״̬������lambda֮��ı���sum
	//	{
	//		sum += elem;
	//	});
	//cout << sum << endl;

	//lambda_mutable();
	lambda_by_ref();





	getchar();
	return 0;
}