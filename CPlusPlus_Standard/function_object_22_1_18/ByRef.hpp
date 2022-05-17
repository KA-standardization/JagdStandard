#pragma once
#include <iostream>
#include <list>
#include <algorithm>
#include <iterator>


/*
	by reference 方式传递 function object
	需要在调用算法时明白标示function object是个reference类型
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
	//需要在调用算法时明白标示function object是个reference类型
	std::generate_n<std::back_insert_iterator<std::list<int>>, int, IntSeq&>(back_inserter(coll3), 9, seq);
	for (auto item : coll3) {
		std::cout << "by ref-->" << item << std::endl;
	}
	//std::generate_n<std::back_insert_iterator<std::list<int>>, int, IntSeq&>(back_inserter(coll3), 9, seq);
	//for (auto item : coll3) {
	//	std::cout << "by ref-->" << item << std::endl;
	//}
}