#include <iostream>
#include <forward_list>

void jagdForwordList() {
	std::forward_list<long> m_cool = { 2,3,4,5,6 };
	// resize改变元素个数, 要么指定新元素resize(9,100)否则默认为0
	m_cool.resize(9);
	for (auto elem : m_cool) {
		std::cout << elem << std::endl;
	}

}
