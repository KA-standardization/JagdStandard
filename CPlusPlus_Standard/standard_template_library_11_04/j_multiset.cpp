#include <set>
#include <string>
#include <iostream>

void jagdMultiset() {
	std::multiset<std::string> m_coll{ "buch","Kaiser","Kaiserin","jagd","madel" };
	for (const auto& elem : m_coll) {
		std::cout << "f: " << elem << std::endl;
	}
	m_coll.insert({ "buch","holle","jagd" });
	for (const auto& elem : m_coll) {
		std::cout << "e: " << elem << std::endl;
	}
}
