#pragma once
#include <list>
#include <iostream>
#include <algorithm>
#include <iterator>

class IntSeq {
private:
	int value;
public:
	IntSeq(int val):value(val){}
	int operator()() {
		return ++value;
	}
};



void test() {
	std::list<int> coll;
	IntSeq seq(1);


	std::generate_n<std::back_insert_iterator<std::list<int>>, int, IntSeq&>(std::back_inserter(coll), 4, seq);
	//std::generate_n(std::back_inserter(coll), 4, IntSeq(1));
	for (auto item : coll) {
		std::cout << "ref val-A->"<< item <<std::endl;
	}
	std::generate_n<std::back_insert_iterator<std::list<int>>, int, IntSeq&>(std::back_inserter(coll), 4, seq);
	//std::generate_n(std::back_inserter(coll), 4, IntSeq(1));
	for (auto item : coll) {
		std::cout << "ref val-B->" << item << std::endl;
	}

	std::cout << coll.size() << std::endl;
}