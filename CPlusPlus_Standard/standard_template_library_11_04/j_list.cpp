#include <list>
#include <iostream>

void jagdList() {
	std::list<char> m_coll;

	for (char c = 'a';c <= 'z';++c) {
		m_coll.push_back(c);
	}

	for (auto element : m_coll) {
		std::cout << element << std::endl;
	}
}
