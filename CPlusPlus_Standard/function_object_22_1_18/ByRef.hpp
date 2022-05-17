#pragma once
#include <iostream>
#include <list>
#include <algorithm>
#include <iterator>


/*
	by reference ��ʽ���� function object
	��Ҫ�ڵ����㷨ʱ���ױ�ʾfunction object�Ǹ�reference����
*/

class IntSeq {
private:
	int value;
public:
	IntSeq(int val):value(val){}
	int operator()() {
		return ++value;
	}
};

void FuncObjByRef() {
	std::list<int> coll3;
	IntSeq seq(1);
	//��Ҫ�ڵ����㷨ʱ���ױ�ʾfunction object�Ǹ�reference����
	std::generate_n<std::back_insert_iterator<std::list<int>>, int, IntSeq&>(back_inserter(coll3), 9, seq);
	for (auto item : coll3) {
		std::cout << "by ref-->" << item << std::endl;
	}
	//std::generate_n<std::back_insert_iterator<std::list<int>>, int, IntSeq&>(back_inserter(coll3), 9, seq);
	//for (auto item : coll3) {
	//	std::cout << "by ref-->" << item << std::endl;
	//}
}